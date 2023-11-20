from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Menu_items
from .forms import Reservation

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def menu(request):
    menu_items=Menu_items.objects.all()
    menu_dict={'menu':menu_items}
    return render(request,'menu.html',menu_dict)

def display_menu_items(request,pk=None):
    if pk:
        menu_item=Menu_items.objects.get(pk=pk)
    else:
        menu_item=''
    return render(request,'menu_item.html',{'menu_item':menu_item})

def submission(request):
    return render(request,'destination.html')

def reservation(request):
    form=Reservation()
    if request.method=='POST':
        form=Reservation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submission') 
        else:
            messages.error(request, 'Invalid data! Check your informations again.')
    else:
        form = Reservation()
    context={'form':form}
    return render(request,'booking.html',context)

# Create your views here.
