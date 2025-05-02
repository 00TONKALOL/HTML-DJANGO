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
        gender= request.POST.get('gender')
        print(names , email , phone ,dob,height,weight)
        Person.objects.create(name=names,gender=gender,email=email,phone=phone,dob=dob,weight=weight,height=height)
        count =Person.objects.count()
        print(f"You have {count} records")
    return redirect('home-page')


def people(request):
    data=Person.objects.all()
    return render(request, 'list.html', {'data': data})


def details(request ,id):
    person = Person.objects.get(id=id)
    return render(request, 'details.html')


def delete(request ,id):
    user = Person.objects.get(id=id)
    user.delete()
    message=f"User {user.name} deleted successfully"
    return redirect('people-page' , {'message':message})
