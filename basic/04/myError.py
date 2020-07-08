class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명"

def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)

try:
    say_nick("안녕")
    say_nick("바보")
except MyError as e:
    print(e)