import re

p = re.compile('[a-z][a-z0-9]{4,}@[a-z]{2,}.[a-z]{2,5}')

while True:
    email = input("이메일 입력 : ")
    m = p.match(email)
    print(m)
