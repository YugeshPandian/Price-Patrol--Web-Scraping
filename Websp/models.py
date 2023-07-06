from django.db import models
from django.contrib.auth.models import User
import datetime 
import os

def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)



class Trending(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    url=models.URLField(null=True,blank=True,max_length=750)
    status=models.BooleanField(default=False,help_text='0-Show,1-Hidden')
    trending=models.BooleanField(default=False,help_text='0-Normal,1-Trending')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class OfferBoth(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    flipkart_url = models.URLField(null=False,blank=False,max_length=750)
    amazon_url = models.URLField(null=False,blank=False,max_length=750)
    buyprice = models.IntegerField(null=False,blank=False)
    email = models.EmailField(null=False,blank=False)
    Target=models.TextField(max_length=50,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)


class Main(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    flipkart_url = models.URLField(null=False,blank=False,max_length=750)
    amazon_url = models.URLField(null=False,blank=False,max_length=750)
    buyprice = models.IntegerField(null=False,blank=False)
    email = models.EmailField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    

class ScrapedData(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    scraped_at=models.DateTimeField(auto_now_add=True)
    
    flipkart_name=models.TextField(max_length=500,null=False,blank=False)
    flipkart_price=models.TextField(null=False,blank=False)
    flipkart_mrp=models.TextField(null=False,blank=False)
    flipkart_offer=models.TextField(max_length=50,null=False,blank=False)
    flipkart_star=models.TextField(null=False,blank=False)
    flipkart_rating=models.TextField(max_length=50,null=False,blank=False)
    flipkart_avail=models.TextField(max_length=50,null=False,blank=False)
    flipkart_stock=models.TextField(max_length=50,null=False,blank=False)
    flipkart_note=models.TextField(max_length=50,null=True,blank=True)
    
    buyprice=models.IntegerField(null=True,blank=True)
    status=models.TextField(max_length=50,default='Not Yet')
    amazon_name=models.TextField(max_length=500,null=False,blank=False)
    amazon_price=models.TextField(null=False,blank=False)
    amazon_mrp=models.TextField(null=False,blank=False)
    amazon_offer=models.TextField(max_length=50,null=False,blank=False)
    amazon_star=models.TextField(null=False,blank=False)
    amazon_rating=models.TextField(max_length=50,null=False,blank=False)
    amazon_avail=models.TextField(max_length=50,null=False,blank=False)
    amazon_stock=models.TextField(max_length=50,null=False,blank=False)
    amazon_note=models.TextField(max_length=50,null=False,blank=False)
   




 