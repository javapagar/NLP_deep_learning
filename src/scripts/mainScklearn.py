from scikitlearn.webScraping import WebScraping as ws
import pandas as pd
import pickle

user_guide = []
scrap = ws("https://scikit-learn.org/stable/user_guide.html")

titles = scrap.getTitleLink()
for t in titles:
    level1 = t[0].split('.')[-1].strip()
    print(level1)
    scrap.setUrl(t[1])
    subtitles = scrap.getTitleLink()
    for subtit in subtitles:
        level2=subtit[0].split('.')[-1].strip()
        print(level2)
        scrap.setUrl(subtit[1])
        global_content,level3_content=scrap.scrapPage()
        user_guide.append({'level1':level1,'level2':level2,'level3':'','content' : global_content})
        for lev_content in level3_content:
            user_guide.append({'level1':level1,'level2':level2,'level3':lev_content[0],'content' : lev_content[1]})

df_sklearn = pd.DataFrame(user_guide)

with open('sklearn_guide.plk','wb') as rick:
    pickle.dump(df_sklearn,rick)
    
