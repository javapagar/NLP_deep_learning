#!pip install gtts
from gtts import gTTS
import os
import time
from mutagen.mp3 import MP3


#función para cuardar y reproducir mp3
def saySomething(somethingToSay):
    myobj = gTTS(text=somethingToSay, lang="es", slow=True)
    myobj.save("texto.mp3")
    os.system("texto.mp3")
    
def getLength():
    audio = MP3("texto.mp3")
    return audio.info.length

rap = ["rimando y en mi camino,",
"todo el ventira no estuviendo en mi mano,",
"todo esos bares,",
"la puerta, que te llevo a la tumba, ",
"que se han contrado en la cartera,",
"esta es la cara de mi "]


for i in range(2):
    for rima in rap:
        saySomething(rima)
        delta = getLength()
        time.sleep(delta+0.5)
        