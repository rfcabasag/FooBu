from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import RegisteredUser, Establishment, FoodItem, Rates, Favorites
from django.contrib.auth.decorators import login_required

@login_required
def foodHome(request):
    x = Establishment.objects.all()
    return render(request,'food/food-home.html',{'est_list':x} )

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
    favorites_list = Favorites.objects.select_related('cus').filter(cus__user=user)
    rated_list = Favorites.objects.select_related('est', 'cus').filter(cus__user=user)
    rates_list = []

    owned = Establishment.objects.filter(owner__user=user)

    for r in rated_list:
        raters = len(Rates.objects.filter(est=r.est))
        rate = 0
        if raters !=0:
            for i in Rates.objects.filter(est=r.est):
                rate = rate + i.rating
            rate = rate/raters
        rates_list.append(rate)

    return render(request,'food/profile.html',{'an_owner':user_is_owner, 'favorites_list':favorites_list, 'rates_list':rates_list, 'user':user, 'rated_list':rated_list, 'owned':owned})

@login_required
def establishment(request,est_id):
    x = Establishment.objects.filter(id=est_id)[0]
    location = x.street + " " + x.area

    user = request.user
    is_owner = RegisteredUser.objects.filter(user=user)[0].is_owner
    owns = (user == x.owner.user)
    

    raters = len(Rates.objects.filter(est=x))
    rate = 0
    if raters !=0:
        for i in Rates.objects.filter(est=x):
            rate = rate + i.rating
        rate = rate/raters
        
    favs = len(Favorites.objects.filter(est=x))
    fooditems = FoodItem.objects.filter(est=x)

    return render(request,'food/establishment.html', {'est':x, 'loc':location, 'owner':is_owner, 'favorite':favs, 'rate':rate, 'fooditems':fooditems, 'owns':owns})

@login_required
def favorite(request,est_id):
    user = request.user
    curr_owner = RegisteredUser.objects.filter(user=user)[0]
    is_owner = curr_owner.is_owner


    if is_owner:
        return redirect('food-home')

    est = Establishment.objects.filter(id=est_id)[0]    
    fav = len(Favorites.objects.filter(cus=curr_owner,est=est))
    if fav==0:
        newFav = Favorites(cus=curr_owner,est=est)
        newFav.save()
    else:
        Favorites.objects.filter(cus=curr_owner,est=est)[0].delete()
    
    return redirect('establishment',est_id=est_id)
    

@login_required
def addfooditem(request,est_id):
    x = Establishment.objects.filter(id=est_id)[0]
    if(request.method == 'POST'):
        d1 = request.POST['name']
        d2 = request.POST['price']

        newFoodItem = FoodItem(name=d1, price=d2, est = x)
        newFoodItem.save()

        return redirect('establishment', est_id = est_id)
    else:
       form = None

    return render(request,'food/addfooditem.html')

@login_required
def addestablishment(request):
    user = request.user
    est_owner = RegisteredUser.objects.filter(user=user)[0]

    if(request.method == 'POST'):
        d1 = request.POST['est_name']
        d2 = request.POST['desc']
        d3 = request.POST['area']
        d4 = request.POST['street']

        newEstablishment = Establishment(owner=est_owner, name=d1, desc=d2, area=d3, street=d4)
        newEstablishment.save() 
        
        return redirect('profile')       
    else:
        form = None

    return render(request, 'food/addestablishment.html')