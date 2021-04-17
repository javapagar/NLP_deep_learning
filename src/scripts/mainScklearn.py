from scikitlearn.webScraping import WebScraping as ws
import pandas as pd
import pickle


user_guide = []
scrap = ws("https://scikit-learn.org/stable/user_guide.html")
i=0
titles = scrap.getTitleLink()
for t in titles:
    i+=1
    level1 = t[0].split('.')[-1].strip()
    print(i,level1)
    scrap.setUrl(t[1])
    subtitles = scrap.getTitleLink()
    j=0
    if len(subtitles) > 0:
    
        for subtit in subtitles:
            j+=1
            level2=subtit[0].split('.')[-1].strip()
            print(i,j,level2)
            scrap.setUrl(subtit[1])
            #scrap.scrapPageAllChildren()
            global_content,level3_content=scrap.scrapPage()
            user_guide.append({'level1':level1,'level2':level2,'level3':'','content' : global_content})
            for lev_content in level3_content:
                user_guide.append({'level1':level1,'level2':level2,'level3':lev_content[0],'content' : lev_content[1]})
    else:
       
        global_content,level3_content=scrap.scrapPage() 
        user_guide.append({'level1':level1,'level2':'','level3':'','content' : global_content})
        for lev_content in level3_content:
            j+=1
            print(i,j,lev_content[0])
            user_guide.append({'level1':level1,'level2':lev_content[0],'level3':'','content' : lev_content[1]})
        
df_sklearn = pd.DataFrame(user_guide)

with open('sklearn_guide.plk','wb') as rick:
    pickle.dump(df_sklearn,rick)
    
