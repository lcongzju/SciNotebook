from bs4 import BeautifulSoup
import requests
import urllib
import re
import unicodedata
import sys

URL='https://www.sigmaaldrich.com/catalog/product/sigma/s3147?lang=en&region=US'
r=requests.get(URL)
soup = BeautifulSoup(r.content,'html.parser')






# -------------------- Info in title: Product Name and Product Number ---------------------------
results=soup.find_all('meta',property="og:title")
a=str(results[0])
matches=re.search(r'".*\d"',a)
title=a[matches.start()+1:matches.end()-1].split()
ProductNum=title[-1]
ProductName=''.join(title[0:-1])

# --------------------- Info in subtitle: CAS Number...PubChem ID ------------------------------
results=soup.find_all(lambda tag: tag.name=='ul' and tag.get('class')==['clearfix'])
a=results[0].text

# CAS Number
matches=re.search(r'CAS Number.*\d\s',a)
CASNum=str(a[matches.start():matches.end()].split()[-1])

# Linear Formula  # unicode
matches=re.search(r'Linear Formula.*\s',a)
LinearFormula=a[matches.start():matches.end()].split()[-1]

# Molecular Weight
matches=re.search(r'Molecular Weight.*\d\s',a)
MWeight=str(a[matches.start():matches.end()].split()[-1])

# Beilstein Registry Number
matches=re.search(r'Beilstein Registry Number.*\d\s',a)
BRegistryNum=str(a[matches.start():matches.end()].split()[-1])

# EC Number
matches=re.search(r'EC Number.*\d\s',a)
ECNumb=str(a[matches.start():matches.end()].split()[-1])

# MDL Number
matches=re.search(r'MDL number.*\d\s',a)
MDLNum=str(a[matches.start():matches.end()].split()[-1])

# PubChem Substance ID
matches=re.search(r'PubChem Substance ID.*\d\s',a)
PubChemID=str(a[matches.start():matches.end()].split()[-1])