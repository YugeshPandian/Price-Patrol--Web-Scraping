import pandas as pd
import requests
import bs4
import lxml
import time
import re




def Amazon_product(amazon_url):
    Headers=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36','Accept-Language':'en-US,en;q=0.5'})
    res=requests.get(amazon_url,headers=Headers)
    soup=bs4.BeautifulSoup(res.content,'html.parser')
    
    
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