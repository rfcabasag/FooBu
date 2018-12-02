from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import RegisteredUser, Establishment
from django.contrib.auth.decorators import login_required

@login_required
def foodHome(request):
    return render(request,'food/food-home.html')

def register_as_owner(request):
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            newUser = User.objects.filter(username=username)[0]

            newRegUser = RegisteredUser(user=newUser,is_owner=True)
            newRegUser.save()

            d1 = request.POST['est_name']
            d2 = request.POST['desc']
            d3 = request.POST['area']
            d4 = request.POST['street']

            newEstablishment = Establishment(owner=newRegUser, name=d1, desc=d2, area=d3, street=d4)
            newEstablishment.save()

            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'food/register-owner.html')

def register_as_customer(request):
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            newUser = User.objects.filter(username=username)[0]

            newRegUser = RegisteredUser(user=newUser,is_owner=False)
            newRegUser.save()

            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'food/register-customer.html')

def signup_as(request):
    return render(request,'food/signup-as.html')

@login_required
def profile(request):
    user = request.user
    user_is_owner = RegisteredUser.objects.filter(user=user)[0].is_owner

    return render(request,'food/profile.html',{'an_owner':user_is_owner})

@login_required
def establishment(request,est_id):
    x = Establishment.objects.filter(id=est_id)[0]
    location = x.street + " " + x.area
    return render(request,'food/establishment.html', {'est':x, 'loc':location})
