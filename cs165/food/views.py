from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import RegisteredUser
from django.contrib.auth.decorators import login_required

def foodHome(request):
    return render(request,'food/food-home.html')

def register(request):
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            newUser = User.objects.filter(username=username)[0]

            val = False
            if request.POST.get('is_owner', False):
                val = True

            newRegUser = RegisteredUser(user=newUser,is_owner=val)
            newRegUser.save()

            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'food/register.html')

@login_required
def profile(request):
    user = request.user
    user_is_owner = RegisteredUser.objects.filter(user=user)[0].is_owner

    return render(request,'food/profile.html',{'an_owner':user_is_owner})
