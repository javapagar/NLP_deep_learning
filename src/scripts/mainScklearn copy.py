from scikitlearn.webScraping import WebScraping as ws
import pandas as pd
import pickle


user_guide = []
scrap = ws("https://scikit-learn.org/stable/user_guide.html")
i=0
titles = scrap.getTitleLink()
for t in titles:
    i+=1
    level = []
    level1 = t[0].split('.')[-1].strip()
    level.append(level1)
    scrap.setUrl(t[1])
    subtitles = scrap.getTitleLink()
    j=0

    if len(subtitles) > 0:
    
        for subtit in subtitles:
            j+=1
            scrap.setUrl(subtit[1])
            user_guide.extend(scrap.scrapAllPage(level))


    else:
        user_guide.extend(scrap.scrapAllPage(level))

user_guide_format =[]
for lc in user_guide:
    diccionario ={}
    for i,level in enumerate(lc[0]):
        diccionario['level'+str(i)] = level
    diccionario['content']=lc[1]
    user_guide_format.append(diccionario)   

df_sklearn = pd.DataFrame(user_guide_format)

with open('sklearn_guide.plk','wb') as rick:
    pickle.dump(df_sklearn,rick)   
