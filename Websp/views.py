from django.shortcuts import redirect, render
from .models import *
from Websp.form import CustomUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core.cache import cache
from .flipamaz import flipamaz


import json
import requests
import bs4
import pandas as pd
import lxml
from .flipkart import Flipkart_product
from .amazon import Amazon_product


def home(request):
    trending=Trending.objects.filter(status=0)
    return render (request,"Html/index.html",{"trending":trending})

def login_page(request):
    if request.user.is_authenticated:
     return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("/")
            else:
                 messages.error(request,"Invalid User Name or Password")
                 return redirect("/login")
    return render(request,"Html/login.html")

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged Out Done")
    return redirect("/")

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success Now Ready for Save Money!")
            return redirect('/login')
    return render (request,"Html/register.html",{"form":form})


def mainpage(request):
   return render (request,"Html/mainpage.html")
   
     

        




    

'''
def twitter(request):
    Headers=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36','Accept-Language':'en-US,en;q=0.5'})
    Url=''
    res=requests.get(Url,headers=Headers)
    soup=bs4.BeautifulSoup(res.content,'html.parser')
 
   '''

def adddash(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:

            data=json.loads(request.body)
            flipkart=(data['flipkart_url'])
            amazon=(data['amazon_url'])
            buyprice=(data['buyprice'])
           # print(request.user.id)
            aemail=(data['aemail'])
            if all(var is not None for var in (flipkart, amazon, buyprice, aemail)):
                if OfferBoth.objects.filter(user=request.user,amazon_url=amazon,flipkart_url=flipkart):
                    return JsonResponse({'status':'Already in your Master_List'},status=200) 
                else:
                    OfferBoth.objects.create(user=request.user,flipkart_url=flipkart,amazon_url=amazon,buyprice=buyprice,email=aemail)
                    return JsonResponse({'status':'Added to your Master_List : Check this on DashBoard'},status=200) 
            else:
                return JsonResponse({'status':'Fill all the Fields'},status=200) 
             

        else:
            return JsonResponse({'status':'Login to Access'},status=200) 

    else:
        return JsonResponse({'status':'Invalid Access'},status=200)


def dashboard(request):
    if request.user.is_authenticated:
        dash=OfferBoth.objects.filter(user=request.user)
        scraped_data = ScrapedData.objects.filter(user=request.user)
        main=Main.objects.filter(user=request.user)
        return render(request, "Html/dashboard.html", {"main":main,"dash": dash, "scraped_data": scraped_data})
    else:
        return redirect(" ")
    

def master(request):
    if request.user.is_authenticated:
        dash=OfferBoth.objects.filter(user=request.user)
        
        return render(request, "Html/master.html", {"dash": dash})
    else:
        return redirect(" ")
    

def remove_dash(request,id):
    dashitem=OfferBoth.objects.get(id=id)
    dashitem.delete()
    return redirect("/dashboard")

def transform(request,id):
    dashitem=OfferBoth.objects.get(id=id)
    existing_item = Main.objects.filter(user=dashitem.user).first()
    if existing_item:
        error_message = "Track_List Already has One Item for this user."
        messages.error(request,error_message)
        return JsonResponse({"error":error_message},status=200)
    main_item=Main()    
    main_item=Main()
    main_item.user = dashitem.user
    main_item.flipkart_url = dashitem.flipkart_url
    main_item.amazon_url = dashitem.amazon_url
    main_item.buyprice = dashitem.buyprice
    main_item.email = dashitem.email
    main_item.save()
    
    dashitem.delete()
    
    return redirect("/dashboard")

def wish(request,id):
    main=Main.objects.get(id=id)
    offer=OfferBoth()
    offer.user = main.user
    offer.flipkart_url = main.flipkart_url
    offer.amazon_url = main.amazon_url
    offer.buyprice = main.buyprice
    offer.email = main.email
    offer.save()
    
    main.delete()
    
    return redirect("/dashboard")

@csrf_exempt  # Add this decorator to disable CSRF protection for simplicity. Handle CSRF protection properly in production.
def scrape(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            if Main.objects.filter(user=request.user):
                scraping = Main.objects.get(user=request.user)
                flipkart_url = scraping.flipkart_url
                amazon_url = scraping.amazon_url
                buyprice=scraping.buyprice
                alertmail=scraping.email

                user=request.user
                #print(amazon_url)
                flipamaz_obj=flipamaz(amazon_url=amazon_url,flipkart_url=flipkart_url,buyprice=buyprice,user=user,alertmail=alertmail)
                cache.set('stop_flag',False)
                flipamaz_obj.compare_prices()
                
                return render(request,'Html/dashboard.html') 
        else:
            return JsonResponse({'status': 'Login to Access'}, status=200)
        

def stop_scrape(request):
    cache.set('stop_flag',True)
    return JsonResponse({'status': 'Scraping stopped'}, status=200)