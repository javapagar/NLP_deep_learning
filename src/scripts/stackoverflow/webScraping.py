import requests
from bs4 import BeautifulSoup as bs

class WebScraping():
    
    

    def __init__(self,url):
        self.page = requests.get(url)
        self.html = bs(self.page.content,'html.parser')


    def getHeaderQuestion(self):
        hq=self.html.find(id='question-header')
        hq = hq.find('a',class_='question-hyperlink')
        return hq.text.capitalize()

    def getQuestion(self):

        q = self.html.find(id='question')
        q = q.find_all('div', class_='s-prose js-post-body')[0]
        paragraphs = q.find_all('p')

        questionString = ''
        for p in paragraphs:
            if p.text.strip() != '\n':
                questionString += p.text + " "
        
        return questionString.strip()

    def getAnswer(self):

        a = self.html.find_all('div', class_='answer accepted-answer')[0]
        a = a.find_all('div', class_='s-prose js-post-body')[0]
        paragraphs = a.find_all('p')

        answeredString = ''
        for p in paragraphs:
            if p.text.strip() != '\n':
                answeredString += p.text + " "
        
        return answeredString.strip()