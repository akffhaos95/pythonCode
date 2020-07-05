import json

data_file_path = './basic/02_if_for/data.json'
#단어 사전
word = {}

def loadQuiz():
    with open(data_file_path, 'rt') as f:
        word = json.load(f)
        return word

def saveQuiz():
    with open(data_file_path, 'wt') as f:
        json.dump(word, f, indent=4)

def insertQuiz(quiz):
    with open(data_file_path, "rt") as json_file:
        json_data = json.load(json_file)
    seq = len(json_data) + 1
    json_data[seq] = quiz
    with open(data_file_path, 'wt') as outfile:
        json.dump(json_data, outfile, indent=4)