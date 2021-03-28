from StackOverFlowApi import StackoverflowApi as stoApi
from webScraping import WebScraping as ws
import json

api = stoApi()
thereMore = True
page = 1

wsElement= ws("https://stackoverflow.com/questions/48472277/housing-dataset-from-hands-on-machine-learning-with-sci-kit-learn-tensorflow-d")

print(wsElement.getHeaderQuestion())
print(wsElement.getQuestion())
print(wsElement.getAnswer())

"""while thereMore:
    print(page)
    response = api.search(page=page, intitle='machine learning', pagesize=100)
    respjson = json.loads(response.text)
    thereMore = bool(respjson['has_more'])
    questions = respjson['items']

    for question in questions:
        tags = question['tags']
        questionId = question['question_id']
        isAnswered = question['is_answered']
        print(questionId, isAnswered, tags)

    page += 1"""
