from stackoverflow.StackOverFlowApi import StackoverflowApi as sofApi
from stackoverflow.webScraping import WebScraping as ws
from stackoverflow.QueriesStackoverFlow import INSERT_QUESTIONS, FIND_TAG, INSERT_TAG, INSERT_QUESTION_TAG, FIND_QUESTION
from database.sqlite import SqliteDB
import json


#data base
db = SqliteDB('db/Stackoverflow.db')
db.connect()

#api
api = sofApi()
thereMore = True
page = 51

while thereMore:
    print(page)
    response = api.advanceSearch(page=page, accepted=True,tagged='machine-learning', pagesize=100)
    respjson = json.loads(response.text)
    thereMore = bool(respjson['has_more'])
    questions = respjson['items']

    for question in questions:
        tags = question['tags']
        idTags =[]
        
        #insert tags
        for t in tags:
            resp = db.executeQuery(FIND_TAG,(t,))
            rows = resp.fetchall()

            if len(rows)== 0:
                resp = db.executeQuery(INSERT_TAG,(t,))
                idTags.append(resp.lastrowid)
            else:
                for row in rows:
                    idTags.append(row[0])
        
        script = []

        if 'machine-learning' in tags and 'python' in tags:
            questionId = question['question_id']
            resp = db.executeQuery(FIND_QUESTION,(questionId,))
            rows = resp.fetchall()

            if len(rows)== 0:
                link = question['link']
                title  =question['title']
                wsElement= ws(link)
                content = wsElement.getQuestion()
                answer = wsElement.getAnswer()
                params = (questionId,title, content, link, answer)
                
                script.append((INSERT_QUESTIONS, params))

                for t in idTags:
                    params=(questionId,t)

                    script.append((INSERT_QUESTION_TAG,params))
                
                db.executeTransaction(script)
                print("Insert question", questionId)
            #db.executeQuery(INSERT_QUESTIONS, params)

    page += 1
db.close()