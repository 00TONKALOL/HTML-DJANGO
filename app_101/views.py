from itertools import count
from wsgiref import headers

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites import requests
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tempita import url

from app_101.models import Person
from app_101.my_serializers import PersonSerializer
from app_101.myforms import PersonForm, LoginForm


# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def submit(request):
    return render(request, 'home.html')


@login_required
def submit(request):
    if request.method == "POST":
        names = request.POST.get('names')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        gender = request.POST.get('gender')
        print(names, email, phone, dob, height, weight)
        Person.objects.create(name=names, gender=gender, email=email, phone=phone, dob=dob, weight=weight,
                              height=height)
        count = Person.objects.count()
        print(f"You have {count} records")
    return redirect('home-page')


@login_required
def people(request):
    data = Person.objects.all()
    return render(request, 'list.html', {'data': data})


@login_required
def details(request, id):
    person = Person.objects.get(id=id)
    return render(request, 'details.html', {'person': person})


def delete(request, id):
    user = Person.objects.get(id=id)
    user.delete()
    message = f"User {user.name} deleted successfully"
    return redirect('people-page', {'message': message})


@login_required
def add_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('people-page')
    else:
        form = PersonForm()

    return render(request, 'forms.html', {'form': form})


@login_required
def login_user(request):
    global form
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home-page')
            return render(request, 'login.html', {'form': form})
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required(login_url='login-page')
def signin(request):
    return None


@login_required(login_url='login-page')
def signout(request):
    logout(request)
    return redirect('login-page')


@api_view(['GET'])
def api_people(request):
    watu = Person.objects.all()
    serializer = PersonSerializer(watu, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def single_person(request, id):
    person = Person.objects.get(id=id)
    serializer = PersonSerializer(person)
    return Response(serializer.data)



@api_view(['POST'])
def api_add(request, id):
    data = request.data
    serializer = PersonSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Successfully Added'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_delete(request , id):
    person = Person.objects.get(id=id)
    person.delete()
    return Response({"message", "Successfully deleted"})

@api_view(['PUT'])
def api_update(request, update_data=None):
    response = requests.put(url, json=update_data, headers=headers)

    # Check response status
    if response.status_code == 200:
        print("Update successful:", response.json())
    else:
        print("Update failed:", response.status_code, response.text)
