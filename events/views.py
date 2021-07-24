from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from .models import Event, Ticket, Cathegorie, Order, OrderEvent, ShippinrAddress,AchatTicket,Publish, PublishEvent, TicketSale
from .forms import EventAddForm, TicketAddForm,AchatTicketForm
from django.utils.text import slugify
from django.conf import settings
from django.core.mail import send_mail
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.core import mail
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils.html import strip_tags
from django.http import JsonResponse
import json
import random
from django.contrib import messages

from django.contrib.auth.decorators import login_required




def event_home(request):
    allevents = PublishEvent.objects.all()
    promotor = request.user.promotor 

    context = {"allevents": allevents, "promotor": promotor}
    return render(request, 'events/event_index.html', context)

# permet d'afficher les details sur un evenement
@login_required(login_url='login')
def event_detail(request, id):
    event = PublishEvent.objects.get(id=id)
    print(event)
    a = request.GET['name']
    slu = slugify(a)
    myid = id
    promotor = request.user.promotor
    ev = Event.objects.get(slug=slu)
    tickets = TicketSale.objects.filter(name=ev)

    context = {
        "event": event,'myid': myid,'promotor': promotor, 'tickets': tickets
    }

    return render(request, 'events/event_detail.html', context)

# l'utilisateur remplis les informations pour le payement
def event_shipping(request, id):
    name = request.GET['name']
    promotor = request.user.promotor 
    id = id
    if request.method == 'POST':
        sp = request.POST['price']
        event = PublishEvent.objects.get(id=id)
        sp.split(";")
        prix = sp[0]
        cat = sp[1]
        idtick = sp[-1]
        val = TicketSale.objects.get(id=idtick)
        cont = {"name": name, "event": event, "val": val,"promotor": promotor, "id": id}
        return render(request, 'events/event_shipping.html', cont)

    event = PublishEvent.objects.get(id=id)

    context = {"name": name, "event": event,"id": id}
    return render(request, 'events/event_shipping.html', context)


@login_required(login_url='login')
def event_confirmation_pay(request, id):
    id = id
    promotor = request.user.promotor 
    if request.method == 'POST':
        code = request.POST.get("code")
        name = request.GET['name']
        amount = request.POST.get("useramount")
        totalpay = request.POST.get("totalamount")
        print(amount)
        print(totalpay)
        a= int(amount)
        b= int(totalpay)
        if b < a:
            print("je suis if")
            a = str(code)
            email = request.POST.get("us")
            subject = "Verification Code | Eventick"      
            message = "Copy This "+a+"  and Paste it in the site to confirm Transaction"
            to = [email]
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, message , from_email ,to )
            context = {
                "promotor" : promotor,
                "id": id
            }
            return render(request, 'events/event_confirmation_pay.html', context)
        else:
            print("je suis else")
            context = {
                "promotor" : promotor,
                "id": id
            }
            messages.success(request, 'Your balance is insuffisant')
            return redirect('events:event_shipping'+"/"+str(id)+'?name='+str(name))
        



# affiche la facture achete par le client et fait l'envois du mail 
@login_required(login_url='login')
def event_facture(request):
    promotor = request.user.promotor 
    if request.method == 'POST':
        cat = request.POST.get("categorie")
        nom = request.POST.get("name")
        total = request.POST.get("total")
        email = request.POST.get("email")
        qte = request.POST.get("qtee")
        verifcode = request.POST.get("validecode")
        code = request.POST.get("code")
        pr = request.POST.get("prix")
        phone = request.POST.get("phone")
        print(verifcode) 
        print(code)
        print(total)
        print(cat)
        print(nom)
        print(email)
        print(qte)
        print(phone)
        it = request.POST.get("idtick")
        if verifcode == code:
            print("bon code")
            categorie = Ticket.objects.get(ticket_cathegories=cat)
            sale_info = AchatTicket(Email_customer=email,Phone_number=phone,Ticket_quantity=qte,Total_amount=total)
            sale_info.Event_ticket = categorie
            sale_info.save()
            context = {
                "nom": nom,
                "categorie": categorie,
                "cat": cat,
                "total": total,
                "email": email,
                "pr": pr,
                "qte": qte,
                "phone": phone,
                "qrcode": sale_info.qr_code,
                "promotor": promotor
            }
            

            # html_message = render_to_string('events/event_facture.html', context)
            # plain_message = strip_tags(html_message)
            # mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
            # mail.send_mail(subject1, plain_message, from_email, [to], html_message=html_message)


            template_path = 'events/event_facture.html'
            return render(request, 'events/event_facture.html', context)
        else:
            messages.success(request, 'Code is Incorrect')
            return render(request, 'events/event_confirmation_pay.html')
    else:
        return redirect('events:event_confirmation_pay')


def home(request):
    allevents = Publish.objects.all()

    context = {
        "allevents": allevents
    }

    return render(request, 'events/index.html', context)


def about(request):
    return render(request, 'events/about.html')
    

def pdf(request):
    if request.method == 'POST':
        picture = request.POST['pic']
        date = request.POST['date']
        qte = request.POST['qte']
        total = request.POST['total']
        pri = request.POST['pka']
        z = AchatTicket.objects.filter(pk=pri)
        print(z)
        template_path = 'events/facture.html'

        context={
            'qr':picture,
            'total': total,
            'qt': qte,
            'date': date,
            'z': z,

        }
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="ticket.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response


def pdfnew(request, *args, **kwargs):
    pk = kwargs.get('pk')
    ticket = get_object_or_404(AchatTicket, pk=pk)
    template_path = 'events/recu.html'

    context={'ticket': ticket}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ticket.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response

def pdfview(request, *args, **kwargs):
    pk = kwargs.get('pk')
    ticket = get_object_or_404(AchatTicket, pk=pk)
    template_path = 'events/recu.html'

    context={'ticket': ticket}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="ticket.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response




def facture(request):
    vnm = AchatTicket.objects.all()
    context = {
        "vnm" : vnm
    }
    return render(request, 'events/facture.html', context)



def recieve(request, id):

    idr = AchatTicket.objects.get(id=id) 
    ids =idr.id  
    print(ids) 

    rvce = AchatTicket.objects.get(id=id)
    context = {
        "rvce":rvce
    }
    return render(request, 'events/facture.html', context)