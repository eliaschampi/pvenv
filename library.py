import math
import datetime
import pytz
import locale
import os


def circleCals(p: float) -> None:

    #valor pi
    pi = math.pi

    #R=P2⋅π
    r = (p * 2) * pi

    #a=π*r^2
    a = pi  * (r ** 2)
    yield '{0:.7f}'.format(pi), '{0:.2f}'.format(r), '{0:.3f}'.format(a)


def questionOne():
    pi, r, a = next(circleCals(20.4))
    print(f" valor del pi: {pi}")
    print(f" valor de radio: {r}")
    print(f" valor de area: {a}")

def questionTwo():
    locale.setlocale(locale.LC_TIME, '')
    today = datetime.datetime.now(pytz.timezone("America/Lima"))
    one = today.strftime("%d-%m-%y")
    two = today.strftime("%d-%m-%Y")
    tree = today.strftime("Hoy dia es %A")
    four = today.strftime("%d~%m~%Y")
    five = today.strftime("%d-%m-%Y %H:%S:%M")
    print(one)
    print(two)
    print(tree)
    print(four)
    print(five)

def questionTree():
    dirs = os.listdir("./")
    for file in dirs:
        print(f"/{file}")

def run():
    #questionOne()
    #questionTwo()
    #questionTree()
    #questionFour()
    #questionSix()
    #questionSeven()
    #questionEight()
    print("hello world")


if __name__ == "__main__":
    run()