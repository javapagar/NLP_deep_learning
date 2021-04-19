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

    def getUrlSongList(self):
        song_list= []
        songs = self.html.find_all('div',class_='tbl_oneline')
        for song in songs:
            song_element = song.find('a', class_='x')
            link = song_element['href']
            artists =song_element.find('span',class_='list_artist').text
            title = song_element.find('span',class_='list_title').text
            song_list.append((link,artists,title))
        return song_list
    
    def getLirycs(self):
        
        div = self.html.find('div',class_='letra_body l17 withEmbed')
        if not div:
            div = self.html.find('div',class_='letra_body l17')
        content=''
        try:
            
            content= div.text
        
        except:
            pass
        return content

    def scrapAllPage(self,levels):
        level_content=[]
        
        firstSection = self.html.find('div', class_='section')

        level_content.append(self.scrapFirstSection(levels,firstSection))

        sections = firstSection.find_all('div', class_='section', recursive=False)

        for sec in sections:

            level_content.extend(self.scrapSection(levels,sec))

        return level_content

    def scrapSection(self, levels, section):
        levels_aux=levels.copy()

        level_content =[]

        children = section.findChildren(recursive=False)
        
        content = []

        for child in children:

            if 'p' == child.name:
                 content.append(child.text)
            elif 'div' == child.name:
                type = child['class']
                if 'math' in type:
                    content.append('mathForm')
                elif 'figure' in type:
                    content.append('figure')
                elif 'highlight-default' in type:
                    content.append('code')
                elif 'topic' in type:
                    content.append('example')
                elif 'section' in type:
                    level_content.extend(self.scrapSection(levels_aux,child))
                else:
                    print(child['class'])
            elif 'h' in child.name:
                title= child.text.split('.')[-1].strip()
                level_int= len(child.text.split('.')[:-1])
                if level_int > len(levels):
                    levels_aux.append(title)
        
        level_content.append((levels_aux,"\n".join(content)))

        return level_content
                