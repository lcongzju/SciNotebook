from bs4 import BeautifulSoup
import requests
import re
import mysql.connector



# connect to MYSQL Server
cnx = mysql.connector.connect(user='root', password='new_password',
                              host='127.0.0.1')


# iterate pages
page=1
products=True
while products:
    URL='https://www.sigmaaldrich.com/catalog/search?&interface=All&N=0+14577449&page='+str(page)+'&mode=partialmax&lang=en&region=US&focus=product'
    r=requests.get(URL)
    soup = BeautifulSoup(r.content,'html.parser')
    products=soup.find_all(lambda tag: tag.name=='li' and tag.get('class')==['productNumberValue'])
    page+=1
    for product in products:
        product_url='https://www.sigmaaldrich.com'+product.find(href=True)['href']
        a=Chemical(product_url)
        a.add_chemical_2db(cnx)
    cnx.commit()


