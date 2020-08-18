import json
import requests
import replit
import random

QuestionNumber = 0

def fetchData():
    request = requests.get("https://opentdb.com/api.php?amount=15&category=9&difficulty=medium&type=multiple")
    request_text = request.text
    data = json.loads(request_text)
    if data is None:
        print("Error, server connection failed")
    else:
        return data['results']
    
questions = fetchData()

def getQuestions():
    list = []

    for question in questions:
        list.append(question['question'])
        list.append(question['correct_answer'])
        for incorrectAnswer in question['incorrect_answers']:
            list.append(incorrectAnswer)

    return list
        

questionList = getQuestions()


def shuffleQuestions(questionList, questionNumber):
    list = []
    list.append(questionList[questionNumber*5+1])
    list.append(questionList[questionNumber*5+2])
    list.append(questionList[questionNumber*5+3])
    list.append(questionList[questionNumber*5+4])
    random.shuffle(list)
    return list


def displayQuestions():
    global QuestionNumber
    counter = 1
    while QuestionNumber >= 0 and QuestionNumber < 14:
        questionText = questionList[QuestionNumber*5]
        correctAnswer = questionList[QuestionNumber*5+1]
        possibleQuestions = shuffleQuestions(questionList, QuestionNumber)        
        print("\n" + questionText + "\n")        
        for question in possibleQuestions:
            
            print("    #"+ str(counter) + " " +question+"    ")
            counter = counter + 1
        counter = 1
        checkAnswer(correctAnswer.lower(), possibleQuestions)




def answerPrompt(possibleQuestions):
    ans = input("\nEnter an answer\n")

    for i in range (len(possibleQuestions)):
        possibleQuestions[i] = possibleQuestions[i].lower()

    
    if(ans.lower() not in possibleQuestions):
        print("Answer entered wrong")
        answerPrompt(possibleQuestions)

    else:
        return ans

def checkAnswer(correctAnswer, possibleQuestions):
    global QuestionNumber

    ans = answerPrompt(possibleQuestions)

    if ans.lower() == correctAnswer:
        print("\n****   Correct ***")
        QuestionNumber = QuestionNumber + 1
    else:
        print("\nGame Over")
        print("\nThe correct answer was, " + correctAnswer + "\n\n\n\n\n************")
        QuestionNumber = 100



displayQuestions()