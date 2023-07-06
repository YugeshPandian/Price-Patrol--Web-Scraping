import pandas as pd
import requests
import bs4
import lxml


def Flipkart_product(flipkart_url):
    Headers=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36','Accept-Language':'en-US,en;q=0.5'})
    res=requests.get(flipkart_url,headers=Headers)
    soup=bs4.BeautifulSoup(res.content,'html.parser')
    
    
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
        
    