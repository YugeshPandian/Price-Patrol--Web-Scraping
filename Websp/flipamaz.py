import pandas as pd
import requests
import bs4
import lxml
import time
import re
from django.core.cache import cache
from .models import ScrapedData
from .mail import mailsend



class flipamaz():
    def __init__(self,amazon_url,flipkart_url,buyprice,user,alertmail):
        self.amazon_url=amazon_url
        self.flipkart_url=flipkart_url
        self.buyprice=buyprice
        self.alertmail=alertmail
        self.user=user
        

    def Amazon_product(self,amazon_url):
        Headers=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36','Accept-Language':'en-US,en;q=0.5'})
        res=requests.get(self.amazon_url,headers=Headers)
        soup=bs4.BeautifulSoup(res.content,'lxml')
        
        
        #Product_Name
        time.sleep(5)
        try:
            name=soup.find(id='productTitle')
            Product=name.text.strip()
        except:
            Product='Not Available'
        time.sleep(5)
        
        #Product_Price
        try:
            price=soup.find_all("span",attrs={'class':'a-price-whole'})
            p=price[0].text.replace('.','').replace(',','')
            Product_Price=int(p)
        except:
            Product_Price='Not Available'
            
        #Product_Mrp
        time.sleep(5)
        try:
            #mrp=soup.find_all("span",attrs={'class':'a-offscreen'})
            #Mp=''
            #Mrp=''
            '''
            l=[]
            
            for i in mrp:
                if '₹' in i.text:
                    Mp=i.text.replace('₹','').replace(',','')
                    mr=int(float(Mp))
                    l.append(Mp)
                Mrp=max(l)
            '''
        # mr = soup.find_all('span', attrs={'class': 'a-price a-text-price'})
            mr = soup.find_all(class_=["a-price", "a-text-price"])
            Mrp=mr.text.split('₹')[1]
            
                #if mr > Product_Price:
                    #Mrp=mr
        except:
            Mrp='Not Available'
            
            
        #Product Ratings
        time.sleep(5)
        try:
            rate=soup.find(id='acrCustomerReviewText')
            Ratings=rate.text.replace(' ratings','')
        except:
            Ratings='No Reviews till now'
            
        #Product_Star
        time.sleep(5)
        try:
            star=soup.find_all("span",attrs={'class':'a-size-base a-color-base'})
            for i in star:
                pattern=r'\d+\.\d+'
                match=re.search(pattern,str(i))
                if match:
                    break
            Stars=match.group()+' Out of 5 Stars'
        except:
            Stars="No Ratings till now"
            
        #Product_Offer
        time.sleep(5)
        try:
            offer=soup.find_all("span",attrs={"class":"a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage"})
            off=offer[0].text.replace('-','')
        except:
            off='Not Available'
            
        #Product_Availability
        try:
            Avail=soup.find_all(id='buy-now-button')
            if Avail ==[]:
                Availability='Out of Stock'
            else:
                Availability='In Stock'
        except:
            Availability='Not Available'
        
        #Product_SpecialNote
        time.sleep(5)
        try:
            SP=soup.find_all("span",attrs={'class':'a-size-base dealBadgeSupportingText'})
            Special=SP[0].text
        except:
            Special='No Special Offer'
            
        #Product_InHand
        time.sleep(5)

        try:
            a=soup.find(id='availability')
            stock=a.text
        except:
            stock='Stocks High'
            
            
            
        amazon_dict={'Special_Note':Special,'Product_name':Product,'Selling_Price':Product_Price,'MRP':Mrp,'Offer':off,'Star':Stars,'Ratings':Ratings,'Availability':Availability,'InHand':stock}
        #amazon_df=pd.DataFrame(dict,index=[0])
        
        
    
        return amazon_dict 




    def Flipkart_product(self,flipkart_url):
        Headers=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36','Accept-Language':'en-US,en;q=0.5'})
        res=requests.get(self.flipkart_url,headers=Headers)
        soup=bs4.BeautifulSoup(res.content,'lxml')
        
        
        #Product_Name
        try:
            name=soup.find_all("span",attrs={'class':"B_NuCI"})
            Product_name=name[0].text
        except:
            try:
                name=soup.find(class_='B_NuCI')
                Product_name=name[0].text
            except:
                Product_name='Not Available'
        
    
        #Product_Price
        try:
            prices=soup.find_all("div",attrs={'class':"_30jeq3 _16Jk6d"})
            price=(prices[0].text)
        
        except:
            try:
                prices=soup.find(class_='_30jeq3 _16Jk6d')
                price=(prices[0].text)
            except:
                price='Not Available'
        
    

        #Product_Ratings
        Ratings=None
        try:
            r=soup.find_all("span",attrs={'class':"_2_R_DZ"})
            TR=r[0].text.strip().replace("\xa0&\xa0"," & ")
            if '&' in TR:
                Ratings=TR.split('&')[0]
            if 'and' in TR:
                Ratings=TR.split('and')[0]
        except:
            Ratings='NO Ratings till now'
                    
        #Product_Reviews
        try:
            Reviews_Count=TR.split('&')[1]
        except:
            try:
                Reviews_Count=TR.split('and')[1]
            except:
                Reviews_Count=0
                
        #Product_Star        
        try:
            Rate=soup.find_all("div",attrs={'class':"_3LWZlK"})
            Sr=Rate[0].text
            Star=Sr + ' Out of 5'
        except:
            Star='No Stars'
            
        #Product_MRP    
        try:
            mrp=soup.find_all("div",attrs={'class':"_3I9_wc _2p6lqe"})
            mrp=(mrp[0].text)
            
        except:
            mrp=price
            
            
        #Product_Offer    
        try:
            Off=soup.find_all("div",attrs={'class':"_3Ay6Sb _31Dcoz"})   
            Offer=Off[0].text.replace(' off','')
        except:
            try:
                Off=soup.find_all("div",attrs={'class':"_3Ay6Sb _31Dcoz pZkvcx"})
                Offer=Off[0].text.replace(' off','')
            except:
                try:
                    Mrp=int(mrp.replace('₹','').replace(',',''))
                    Price=int(price.replace('₹','').replace(',',''))
                    Off=((Mrp-Price)/Mrp) *100
                    off=round(Off,2)
                    Offer=str(off) + '%'
                except:
                    Offer=0
                
        #Availablity_Check
        try:
            stock=soup.find_all("button",attrs={"class":'_2KpZ6l _2U9uOA ihZ75k _3AWRsL'})
            stock=stock[0].text
            Availability_Status='In Stock'
        except:
            Availability_Status='Out of Stock'
            
        try:
            stock_c=soup.find_all("div",attrs={"class":'_2JC05C'})
            stock_count=stock_c[0].text    
        except:
            stock_count='Stocks High'
        
            
        flipkart_dict={'Product_Name':Product_name,'Selling Price':price,'MRP':mrp,'Offer':Offer,'Star':Star,'Rating':Ratings,'Availability':Availability_Status,'Stock In Hand':stock_count,'Reviews Count':Reviews_Count,}
        
        #flipkart_df=pd.DataFrame(Product_Data,index=[0])
        
        return flipkart_dict
        #first=soup.find_all("span",attrs={'class':'_2dMYsv'})
        #f=first[0].text


    def compare_prices(self):

            x=0
            y=0
            while x==0:
                
                stopflag=cache.get('stop_flag')
                if stopflag:
                    return
                else:
                    amazon_product = self.Amazon_product(self.amazon_url)
                    flipkart_product = self.Flipkart_product(self.flipkart_url)
                    user=self.user
                    buyprice=self.buyprice
                    buyprice=int(buyprice)

                    alertmail=self.alertmail

                    flipkart_name=flipkart_product['Product_Name']
                    amazon_name=amazon_product['Product_name']
                    
                    flipkart_mrp=flipkart_product['MRP']
                    amazon_mrp=amazon_product['MRP']
                    
                    flipkart_offer=flipkart_product['Offer']
                    amazon_offer=amazon_product['Offer']
                    
                    flipkart_star=flipkart_product['Star']
                    amazon_star=amazon_product['Star']

                    flipkart_rating=flipkart_product['Rating']
                    amazon_rating=amazon_product['Ratings']

                    flipkart_avail=flipkart_product['Availability']
                    amazon_avail=amazon_product['Availability']
                    
                    flipkart_stock=flipkart_product['Stock In Hand']
                    amazon_stock=amazon_product['InHand']
                    
                    #flipkart_note=flipkart_product['Availability']
                    amazon_note=amazon_product['Special_Note']
                    
                    amazon_price = amazon_product['Selling_Price']
                    flipkart_price = flipkart_product['Selling Price']
                    flipkart_price=flipkart_price.replace('₹','').replace(',','')
                    flipkart_price=int(flipkart_price)
                
                
                    scrapedata=ScrapedData(user=user,flipkart_name=flipkart_name,flipkart_price=flipkart_price,flipkart_mrp=flipkart_mrp,flipkart_offer=flipkart_offer,flipkart_star=flipkart_star,flipkart_rating=flipkart_rating,flipkart_avail=flipkart_avail,flipkart_stock=flipkart_stock,buyprice=buyprice,amazon_name=amazon_name,amazon_price=amazon_price,amazon_mrp=amazon_mrp,amazon_offer=amazon_offer,amazon_star=amazon_star,amazon_rating=amazon_rating,amazon_avail=amazon_avail,amazon_stock=amazon_stock,amazon_note=amazon_note)
                    scrapedata.save()
                    
                    while y==0:

                        if flipkart_stock=='Stocks High':
                            y=1
                        else:
                            subject=f'Price|Patrol Urgent! Low Stock Alert for {flipkart_name} on Flipkart!!!!'
                            message=f'Dear {user},\nWe wanted to inform you about the current stock status of the product you have been monitoring on Price|Patrol (Flipkart). It appears that the stock for {flipkart_name} is running low,\n And We recommend taking immediate action if you wish to purchase it.  \n Product Details:\nnProduct Name: {flipkart_name}\nCurrent_Stock:{flipkart_stock}\nCurrent Price: {flipkart_price}\nYou Defined Price: {buyprice}\nTo secure your purchase, please visit the Flipkart product page using the following link:\n{self.flipkart_url}\nPlease note that stock availability is subject to change, and there is a possibility of the product going out of stock soon.\n We encourage you to make a prompt decision to avoid missing out on this opportunity.\nThank you for using our services, and happy shopping!!!!!\n\n\n\nBest regards,\nPrice|Patrol'

                            mailsend(to_add=alertmail,subject=subject,message=message)
                            y=1
                        

                    
                
                    
                    if amazon_price == 'Not Available':
                        if flipkart_price > buyprice:
                            time.sleep(60)
                            print("Wait")
                            x=0
                            
                        else:
                            subject='Price|Patrol Price Drop!!!!'
                            message=f'Dear {user},\nWe are excited to inform you that the price of the product you have been monitoring on Price|Patrol (Flipkart) \n has dropped below your expectations! As per your request, we are sending you this email to notify you of the great news.\nProduct Name: {flipkart_name}\nCurrent Price: {flipkart_price}\nYou Defined Price: {buyprice}\nTo take advantage of this fantastic deal, simply click on the following link to visit the product page on Flipkart:\n{self.flipkart_url}\nPlease note that prices may fluctuate, and the current price mentioned in this email is accurate as of the time of sending.\nThank you for using our services, and happy shopping!!!!!\n\n\n\nBest regards,\nPrice|Patrol'
                            #stat=ScrapedData.objects.get(user=user)
                            #stat.status='Price Drop in Flipkart'
                            #stat.save()
                            return mailsend(to_add=alertmail,subject=subject,message=message)
                    else:
                        amazon_price=int(amazon_price)
                        if amazon_price <= flipkart_price:
                            if amazon_price <= buyprice:
                                subject='Price|Patrol Price Drop!!!!'
                                message=f'Dear {user},\nWe are excited to inform you that the price of the product you have been monitoring on Price|Patrol (Amazon)  \n has dropped below your expectations! As per your request, we are sending you this email to notify you of the great news.\nProduct Name: {amazon_name}\nCurrent Price: {amazon_price}\nYou Defined Price: {buyprice}\nTo take advantage of this fantastic deal, simply click on the following link to visit the product page on Flipkart:\n{self.amazon_url}\nPlease note that prices may fluctuate, and the current price mentioned in this email is accurate as of the time of sending.\nThank you for using our services, and happy shopping!!!!!\n\n\n\nBest regards,\nPrice|Patrol'
                                #stat=ScrapedData.objects.get(user=user)
                                #stat.status='Price Drop in Amazon'
                                #stat.save()
                                return mailsend(to_add=alertmail,subject=subject,message=message)
                            else:
                                time.sleep(60)
                                print('Wait1')
                                x=0
                        else:
                            if flipkart_price <= buyprice:
                                subject='Price|Patrol Price Drop!!!!'
                                message=f'Dear {user},\nWe are excited to inform you that the price of the product you have been monitoring on Price|Patrol (Flipkart) \n has dropped below your expectations! As per your request, we are sending you this email to notify you of the great news.\nProduct Name: {flipkart_name}\nCurrent Price: {flipkart_price}\nYou Defined Price: {buyprice}\nTo take advantage of this fantastic deal, simply click on the following link to visit the product page on Flipkart:\n{self.flipkart_url}\nPlease note that prices may fluctuate, and the current price mentioned in this email is accurate as of the time of sending.\nThank you for using our services, and happy shopping!!!!!\n\n\n\nBest regards,\nPrice|Patrol'
                                #stat=ScrapedData.objects.get(user=user)
                                #stat.status='Price Drop in Flipkart'
                                #stat.save()
                                return mailsend(to_add=alertmail,subject=subject,message=message)
                                
                            else:
                                time.sleep(60)
                                print('Wait2')
                                x=0
                


        
            

            