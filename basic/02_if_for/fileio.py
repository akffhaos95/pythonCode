# f = open("text.txt", 'w')
# f.write("txt파일 생성", encoding = 'UTF-8')
# f.close()
import json

# f = open("./basic/02_if_for/text.txt", 'r')
# line = "a"
# while line:
#     line = f.readline()
#     print(line)
# f.close()

customer = {
    'id' : 152352,
    'name' : '김진수',
    'history' : [
        {'date' : '2015-03-11', 'item' : 'iPhone'},
        {'date' : '2016-02-03', 'item' : 'Monitor'},
    ]
}
jsonString = json.dumps(customer)
with open('./basic/02_if_for/data.json', 'wt') as f:
    json.dump(customer, f, indent=4)

with open('./basic/02_if_for/data.json', 'rt') as f:
    json.dump(customer, f, indent=4)
