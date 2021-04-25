# NLP_deep_learning: Generación automática de texto con RNR

## Librerias

### Librerias para hiphop_Generacion_texto_clean.ipynb:

* Pickle
* numpy
* re
* spacy (es_core_news_sm)
* tensorflow
* keras
* model_from_json

### librerias para webScraping.py:

* BeautifulSoup
* requests

### librerias para giveMeFlow:

* gtts
* os
* mutagen


## Resumen

El proyecto recopila, a través de web scrapping, las letras de casi 10.000 canciones de hip-hop. Con estas canciones se entrenará un red neuronal recurrente para que aprenda el estilo hip hop y genere canciones de forma automática.

## Estructura

* mainSongs.py -> se encarga de obtener la información
* hiphop_Generacion_texto_clean.ipynb -> En el se preprocesa el texto se crea, y entrena la red neuronal
* giveMeFlow.py -> un pequeño script que hace al ordenador recitar el texto
