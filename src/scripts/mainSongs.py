
from hiphop.webScraping import WebScraping as ws



url_base = 'https://www.hhgroups.com/'
init='letras/o3d2p'
page = 1
song = 1
scrapper = ws(url_base)
lirycs = []
try:
    for p in range(0,190):
        scrapper.setUrl(url_base+init+str(page))
        list = scrapper.getUrlSongList()
        for l in list:
            scrapper.setUrl(url_base+l[0])
            liryc=scrapper.getLirycs()
            if liryc != '':
                lirycs.append(liryc)
                print('canci',song)
                song +=1
            
        
        print('pag',page)
        page+=1
        
    with open ('hiphop.txt','w',encoding='utf8') as f:
        f.write('\n'.join(lirycs))

    print('Canciones totales:',len(lirycs))
except:
    with open ('hiphop.txt','w',encoding='utf8') as f:
        f.write('\n'.join(lirycs))
    
    print('Canciones totales:',len(lirycs))