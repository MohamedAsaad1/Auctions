
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import *
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages 

def index(request):
    return render(request, "auctions/index.html",{"active":Listings.objects.filter(active=True).all()

    })


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required(login_url='/login')
def create(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return render(request,"auctions/create.html",{
                "message":"You Must login"
            })
        cat = Categories.objects.get(pk=int(request.POST["categorie"]))
        op = Listings()
        op.title = request.POST["title"]
        op.description = request.POST["description"]
        op.url_image = request.POST["url_image"]
        op.categorie = cat
        op.starting_bid =request.POST["starting_bid"]
        op.name_user = request.user
        all = Listings.objects.filter(title=request.POST["title"])
        if all:
            return render(request,"auctions/create.html",{
                "taken":"This Title Already Taken Try Another Title"})
        op.save()
        return redirect("listing",list_id =op.id )
    return render(request,"auctions/create.html",{
        "categorie":Categories.objects.all(),
    })

def listing(request,list_id):
    listing = Listings.objects.get(pk=list_id)
    comment = Comments.objects.filter(item= list_id)
    user = request.user 
    if user.is_authenticated:
        exists = listing.watch_list(user)
    else:
        exists = False

    return render(request,"auctions/listing.html",{
        "listing":listing ,
        "comments":comment,
        "user":user,
        "number":comment.count(),
        "exists":exists
    })
    

def add_bid(request,list_id):
    listing = Listings.objects.get(pk=list_id)
    op = Bids()
    if request.user.is_authenticated:
        if request.method == "POST":
            bid = request.POST["bids"]
            if float(bid) > listing.max_bid:
                messages.success(request, 'Bid successfully.')
                op.amount = bid
                op.item = listing
                op.user = request.user
                op.save()
                return redirect('listing',list_id=list_id)
            messages.error(request, 'This number is less than the current number')
            return redirect('listing',list_id=list_id)
    messages.error(request, 'You Must login')
    return redirect('listing',list_id=list_id) 
        
        
@login_required(login_url='/login')          
def add_comment(request, list_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            listing = Listings.objects.get(pk=list_id)
            op = Comments()
            comment = request.POST["comment"]
            op.comment = comment
            op.user = request.user
            op.item = listing
            op.save()
        return redirect("listing",list_id=list_id)
    messages.error(request, 'You Must login')
    return redirect("listing",list_id=list_id)
    
@login_required(login_url='/login')
def watch_list(request):
    user = request.user
    return render (request, "auctions/watchlist.html",{
        "watchlist":user.watchlisting.all(),
        "name": user,

    })
@login_required(login_url='/login')
def watchlist_list(request,list_id):
    if request.method == "POST":
        listing = Listings.objects.get(pk=list_id)
        user = request.user
        listing.watchList.remove(user)
        messages.success(request, 'Listing removed from watchlist')
        return redirect("watchlist")

@login_required(login_url='/login')
def watchchange(request, list_id):
    if request.method == "POST":
        user = request.user
        listing = Listings.objects.get(pk=list_id)
        if listing.watch_list(user): listing.watchList.remove(user)
        else: user.watchlisting.add(listing)
        return redirect("listing",list_id=list_id)
@login_required(login_url='/login')
def categories(request):
    return render(request, "auctions/categories.html",{
        "categories":Categories.objects.all()
    })
@login_required(login_url='/login')
def category(request,cat_id):
    return render(request,"auctions/category.html",{
        "listing":Listings.objects.filter(active=True, categorie=cat_id ),
        "name":Categories.objects.get(pk=cat_id)
    })
    
@login_required(login_url='login')
def close(request, list_id):
    if request.method == "POST":
        listing =Listings.objects.get(pk=list_id)
        listing.active = False
        listing.save()
        messages.success(request, 'Auction successfully closed')
        return redirect('/')

@login_required(login_url='login')
def notify(request):
    return render(request,"auctions/notfiy.html",{
        "listing": Listings.objects.all(),
        "user":request.user
    })


       

 
        

            

        
        
