class Chemical:
    def __init__(self,URL):
        r=requests.get(URL)
        soup = BeautifulSoup(r.content,'html.parser')
        
        results=soup.find_all('meta',property="og:title")
        a=str(results[0])
        matches=re.search(r'".*\d"',a)
        title=a[matches.start()+1:matches.end()-1].split()
        self.ProductNum=title[-1]
        self.ProductName=''.join(title[0:-1])
                
        results=soup.find_all(lambda tag: tag.name=='ul' and tag.get('class')==['clearfix'])
        a=results[0].text
        
        try:
            matches=re.search(r'CAS Number.*\d\s',a)
            self.CASNum=str(a[matches.start():matches.end()].split()[-1])
        except:
            self.CASNum=None
        
        try:
            matches=re.search(r'Linear Formula.*\s',a)
            self.LinearFormula=a[matches.start():matches.end()].split()[-1]
        except:
            self.LinearFormula=None
        
        try:
            matches=re.search(r'Molecular Weight.*\d\s',a)
            self.MWeight=str(a[matches.start():matches.end()].split()[-1])
        except:
            self.MWeight=None
        
        # Beilstein Registry Number
        try:
            matches=re.search(r'Beilstein Registry Number.*\d\s',a)
            self.BRegistryNum=str(a[matches.start():matches.end()].split()[-1])
        except:
            self.BRegistryNum=None

        # EC Number
        try:
            matches=re.search(r'EC Number.*\d\s',a)
            self.ECNum=str(a[matches.start():matches.end()].split()[-1])
        except:
            self.ECNum=None

        # MDL Number
        try:
            matches=re.search(r'MDL number.*\d\s',a)
            self.MDLNum=str(a[matches.start():matches.end()].split()[-1])
        except:
            self.MDLNum=None

        # PubChem Substance ID
        try:
            matches=re.search(r'PubChem Substance ID.*\d\s',a)
            self.PubChemID=str(a[matches.start():matches.end()].split()[-1])
        except:
            self.PubChemID=None
        
    def add_chemical_2db(self,cnx):
        cursor=cnx.cursor(buffered=True)
        cursor.execute('USE ChemicalDB')
        add_chemical="""INSERT IGNORE INTO Chemicals (ProductName,ProductNum,CASNum,LinearFormula,MWeight,BRegistryNum,ECNum,MDLNum,PubChemID)
VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
        data_chemical=(self.ProductName,self.ProductNum,self.CASNum,self.LinearFormula,self.MWeight,self.BRegistryNum,self.ECNum,self.MDLNum,self.PubChemID)
        cursor.execute(add_chemical,data_chemical)
