import requests

class StackoverflowApi():
    
    root = 'https://api.stackexchange.com/'
    site = '&site=stackoverflow'
    def __init__(self):
        pass


    def search(self, intitle:str, page:int =1,pagesize:int = 10,tagged:str=None,order:str = 'desc', sort:str='activity'):
        
        url =self.root+ 'search?page='+str(page)+'&pagesize='+str(pagesize)+'&order='+order+'&sort='+sort

        if tagged != None:
            url+='&tagged='+tagged
        if intitle!= None and len(intitle.strip())> 3:
            url+='&intitle='+intitle
        
        return requests.get(url + self.site)

    def advanceSearch(self, intitle:str=None, tagged:str=None, accepted:bool=False, page:int =1,pagesize:int = 10,order:str = 'desc', sort:str='relevance'):
        
        url =self.root+ 'search/advanced?page='+str(page)+'&pagesize='+str(pagesize)+'&order='+order+'&sort='+sort+ '&accepted='+str(accepted)

        if tagged != None:
            url+='&tagged='+tagged
        if intitle!= None and len(intitle.strip())> 3:
            url+='&intitle='+intitle
        
        return requests.get(url + self.site)
    
