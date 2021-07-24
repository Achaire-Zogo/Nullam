from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.utils.text import slugify
# import db
from .models import Promotor
from events.models import Event, Ticket, Publish, AchatTicket, Cathegorie, PublishEvent, TicketSale
from events.forms import TicketAddForm, EventAddForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# fonction du dashboard
# affiche tous ce qui permet de faire des statistiques
@login_required(login_url='login')
def home(request):
    promotor = request.user.promotor
    eventss = promotor.eventss.all()
    eventdash = promotor.eventss.all()[0:5]
    total_event = eventss.count()
    email = request.user.email
    ik = request.user.pk
    print(id)
    rvce = AchatTicket.objects.all()
    ea = AchatTicket.objects.filter(Email_customer=email)
    a = promotor.tickets.all()
    print(eventss)
    b = promotor.tickets.all()[0:5]
    

    context = {'ea': ea, 'b': b, 'promotor': promotor, 'eventss': eventss, 'total_event': total_event, 'eventdash': eventdash}

    return render(request, 'accounts/home.html', context)

# voir tous les evenement cree et participe
@login_required(login_url='login')
def manage_event(request):
    promotor = request.user.promotor
    eventss = promotor.eventss.all()
    ctg = Cathegorie.objects.all()
    email = request.user.email
    ea = AchatTicket.objects.filter(Email_customer=email)

    context = {'ea': ea, 'promotor': promotor, 'eventss': eventss,'ctg': ctg}

    return render(request, 'accounts/manage_event.html', context)

# permet d'ajouter un evenement
@login_required(login_url='login')
def add_event(request):
    promotor = request.user.promotor
    eventss = promotor.eventss.all()
    ctg = Cathegorie.objects.all()
    if request.method == 'POST':
        c = request.POST['category']
        d = request.POST['desc']
        name = request.POST['name']
        tag = request.POST['tag']
        location = request.POST['location']
        sdate = request.POST['sdate']
        stime = request.POST['stime']
        edate = request.POST['edate']
        imgbaniere = request.FILES['imgbaniere']
        imganother = request.FILES['imganother']
        etime = request.POST['etime']
        pro = request.user.promotor
        slug = slugify(name)
        print(c)
        print(d)
        eve = Event(promotor=pro,name=name,slug=slug,tag=tag,description=d,location=location,event_start_date=sdate,event_start_time=stime,event_end_date=edate,event_end_time=etime,images_baniere=imgbaniere, images_2=imganother)
        eve.category = Cathegorie.objects.get(name=c)
        eve.save()
        return redirect('manage_event') 
    else:
        return redirect('manage_event')

    context = {'promotor': promotor, 'eventss': eventss, 'form': form,'ctg': ctg}
    return render(request, 'accounts/manage_event.html', context)

# affiche les details sur un evenement
# et d'ajouter un nouveau ticket sur un evenement
@login_required(login_url='login')
def details_of_event(request, slug):
    event = Event.objects.get(slug=slug)  # select * from event where id=id
    promotor = request.user.promotor   
    tickets = Ticket.objects.filter(event=event)
    public = PublishEvent.objects.filter(name=event)
    if request.method == 'POST':
        nameev = Event.objects.get(slug=slug)
        place = request.POST['nbrplace']
        price = request.POST['price']
        category = request.POST['category']
        sdate =request.POST['sdate']
        stime = request.POST['stime']
        edate = request.POST['edate']
        etime = request.POST['etime']
        mintick = request.POST['minticket']
        maxtick = request.POST['maxticket']
        pro = request.user.promotor
        slu = slugify(category)
        cont = {"event": event, 'promotor': promotor, 'tickets':tickets, 'public': public}
        if Ticket.objects.filter(event=event,ticket_cathegories=category).exists():
            messages.error(request, 'this Category already exist')
            render(request, 'accounts/event_detail.html', cont)
        else:
            if Ticket.objects.filter(event=event,price=price).exists():
                messages.error(request, 'this price Already Exist Try another')
                render(request, 'accounts/event_detail.html', cont)
            else:
                ticket = Ticket(event=nameev,promotor=pro,maximum_attende=maxtick,price=price,ticket_cathegories=category,slug=slu,ticket_start_date_sell=sdate,ticket_start_time_sell=stime,ticket_end_date_sell=edate,ticket_end_time_sell=etime,min_ticket=mintick,max_ticket=maxtick)
                ticket.save()
    else:
        render(request, 'accounts/event_detail.html')

    context = {
        "event": event, 'promotor': promotor, 'tickets':tickets, 'public': public
    }
    return render(request, 'accounts/event_detail.html', context)

# permet a un promoteur de publier son evenement
@login_required(login_url='login')
def publish(request, slug=None):
    if request.method == 'POST':
        name = request.POST['name']
        promotor = request.user.promotor
        pub = PublishEvent(promotor=promotor)
        pub.name = Event.objects.get(name=name)
        slu = slugify(name)
        pub.save()
        return redirect('details_of_event', slug=slu)


# permet a un promoteur de metre en vente un ticket
@login_required(login_url='login')
def onsale(request, slug=None):
    if request.method == 'POST':
        cat = request.POST['cat']
        name = request.POST['name']
        id = request.POST['id']
        newname = Event.objects.get(name=name)
        ticket = Ticket.objects.get(id=id)
        newtic = ticket.tick.all()
        print(newtic)
        promotor = request.user.promotor
        tick = TicketSale(promotor=promotor)
        tick.ticket = ticket
        tick.name = newname
        slu = slugify(name)
        tick.save()
        return redirect('details_of_event', slug=slu)


# permet d'ajouter un nouveau ticket pour un evenement 
@login_required(login_url='login')
def add_new_ticket(request, slug=None):
    event = Event.objects.get(slug=slug)  # select * from event where id=id
    promotor = request.user.promotor   
    tickets = Ticket.objects.filter(event=event)
    if request.method == 'POST':
        nameev = Event.objects.get(slug=slug)
        place = request.POST['nbrplace']
        price = request.POST['price']
        category = request.POST['category']
        sdate =request.POST['sdate']
        stime = request.POST['stime']
        edate = request.POST['edate']
        etime = request.POST['etime']
        mintick = request.POST['minticket']
        maxtick = request.POST['maxticket']
        pro = request.user.promotor
        slu = slugify(category)
        ticket = TICKET(event=nameev,promoto=pro,maximum_attende=maxtick,price=price,ticket_cathegories=category,slug=slu,ticket_start_date_sell=sdate,ticket_start_time_sell=stime,ticket_end_date_sell=edate,ticket_end_time_sell=etime,min_ticket=mintick,max_ticket=maxtick)
        ticket.save()
        return redirect('details_of_event', slug=slu)
    else:
        return redirect('details_of_event', slug=slu)

    context = {
        "event": event, 'promotor': promotor, 'tickets':tickets
    }
    return render(request, 'accounts/event_detail.html', context)


def loginpa(request):
    if request.user.is_authenticated:
        return redirect('events:event_home')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password =request.POST.get('password')
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('events:event_home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'accounts/login.html', context)
					
    
    
        

def logoutuser(request):

    logout(request)
    return redirect('events:event_home')

def register(request):
    if request.user.is_authenticated:
        return redirect('events:event_home')
    else:
        form = CreateUserForm() 
        if request.method== 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()

                login(request, user)
                amount = 0
                promotor = Promotor.objects.create(name=user.username, created_by=user, amount=amount)
                cool = form.cleaned_data.get('username')
                messages.success(request, 'account was created for ' + cool)
                return redirect('login')

        context = {'form':form}
        return render(request, 'accounts/register.html', context)



