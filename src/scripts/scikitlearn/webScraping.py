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
    
    def scrapFirstSection(self,levels, firstSection):
        #levels_aux= levels.copy()
        if len(levels) ==2:
            levels.pop(1)
        children = firstSection.findChildren(recursive=False)
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
                    content.append('example')
                elif 'topic' in type:
                    content.append('example')
                elif 'section' in type:
                    break
                else:
                    print(child['class'])
            elif 'h' in child.name:
                levels.append(child.text.split('.')[-1].strip())
                #levels_aux.append(child.text)
        
        return (levels,"\n".join(content))

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
                