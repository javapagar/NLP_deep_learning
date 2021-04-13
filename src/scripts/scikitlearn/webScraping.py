import requests
from bs4 import BeautifulSoup as bs

class WebScraping():
      

    def __init__(self,url):
        self.page = requests.get(url)
        self.html = bs(self.page.content,'html.parser')

    def setUrl(self,url):
        self.page = requests.get(url)
        self.html = bs(self.page.content,'html.parser')

    def getRootUrl(self):
        url_split=self.page.url.split("/")
        return '/'.join(url_split[:-1])+"/"


    def getTitleLink(self):
        schema = self.html.find_all('li', class_='toctree-l1')
        titles = []

        for s in schema:
            a =s.find('a')
            titles .append((a.text.strip(),self.getRootUrl()+a['href']))
        
        return titles

    def scrapPage(self):
        level3_content =[]
        section = self.html.find('div', class_='section')
        paragraphs = section.find_all('p', recursive=False)
        content_global=self.getText(paragraphs)
        sections = section.find_all('div', class_='section', recursive=False)
        for sec in sections:
            level3=sec['id'].strip()
            paragraphs = sec.find_all('p', recursive=False)
            content=self.getText(paragraphs)
            level3_content.append((level3,content))

        return (content_global,level3_content)

    def getText(self,paragraphs):
        content_list=[]
        for p in paragraphs:
            content_list.append(p.text)
        
        return '\n'.join(content_list)
    
    def scrapPageAllChildren(self):
        level3_content =[]
        section = self.html.find('div', class_='section')
        elements = section.findChildren(recursive=False)
        
        for child in elements:
            print (child.name)

       