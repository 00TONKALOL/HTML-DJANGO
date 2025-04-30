from itertools import count

from django.shortcuts import render, redirect

from app_101.models import Person


# Create your views here.
def home(request):
    return render(request, 'home.html')


def submit(request):
    return render(request,  'home.html')

def submit(request):
    if request.method == "POST":
        names = request.POST.get('names')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        dob = request.POST.get('dob')
        weight= request.POST.get('weight')
        height= request.POST.get('height')
        print(names , email , phone ,dob,height,weight)
        Person.objects.create(names=names,email=email,phone=phone,dob=dob,weight=weight,height=height)
        count =Person.objects.count()
        print("You have{count} records")
    return redirect('home-page')


