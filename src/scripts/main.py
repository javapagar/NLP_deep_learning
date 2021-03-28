from stackoverflow.StackOverFlowApi import StackoverflowApi as sofApi
from stackoverflow.webScraping import WebScraping as ws
from stackoverflow.QueriesStackoverFlow import INSERT_QUESTIONS, FIND_TAG, INSERT_TAG
from database.sqlite import SqliteDB
import json


#data base
db = SqliteDB('db/Stackoverflow.db')
db.connect()

#api
api = sofApi()
thereMore = True
page = 1

#while thereMore:
print(page)
response = api.advanceSearch(page=page, accepted=True,tagged='machine-learning', pagesize=5)
respjson = json.loads(response.text)
thereMore = bool(respjson['has_more'])
questions = respjson['items']

for question in questions:
    tags = question['tags']
    idTags =[]
    for t in tags:
        resp = db.executeQuery(FIND_TAG,(t,))
        rows = resp.fetchall()

        if len(rows)== 0:
            resp = db.executeQuery(INSERT_TAG,(t,))
            idTags.append(resp.lastrowid)
        else:
            for row in rows:
                idTags.append(row[0])
    print(idTags)
    if 'machine-learning' in tags and 'python' in tags:
        questionId = question['question_id']
        link = question['link']
        title  =question['title']
        wsElement= ws(link)
        content = wsElement.getQuestion()
        answer = wsElement.getAnswer()
        params = (questionId,title, content, link, answer)
        #db.executeQuery(INSERT_QUESTIONS, params)

        print(questionId, tags)
        

page += 1
db.close()