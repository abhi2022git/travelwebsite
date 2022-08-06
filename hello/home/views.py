from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Booking
from django.contrib import messages
# Create your views here.

def index(request):
    context = {
        "variable":"this is sent"



    }
    



    #return HttpResponse('this is homepage')
    return render(request, 'index.html', context)



def about(request):
    
    return render(request, 'about.html')


def services(request):
    
    return render(request, 'services.html')

def prices(request):
    
        
    
    return render(request, 'prices.html')

def search(request):
    if request.method =="POST":
        search=request.POST.get("search")
        search=Search(search=search)
        search.save()

        return render(request, 'search.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
       
        

    
    return render(request, 'contact.html')

def book(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        book=Booking(name=name,email=email,phone=phone, date=datetime.today())
        book.save()
        messages.success(request, 'Your booking has been done!')


    return render(request, 'book.html')


