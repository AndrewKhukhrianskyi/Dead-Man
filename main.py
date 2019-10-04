from random import  shuffle
from os import system
from time import sleep
import json


board = [ '' for _ in range (9) ]

def draw(rightness = None):
    system("cls")

    print("\t", "----------------")
    print("\n\t","|             |")
    print("\n\t","|             |")
    print("\n\t","|             |")
    print("\n\t","|            ",board[0])
    print("\n\t","|            ",board[1])
    print("\n\t","|         ", board[3],board[7], board[4], )
    print("\n\t","|            ", board[8])
    print("\n\t","|          ", board[5], "", board[6])
    print("\n\t","|")
    print("\t","---------")

    if rightness != None:
        print()
        print("Верно" if rightness else f"Неверно, осталось {len(body)} попыток")
        sleep(.4)


def head():
    board[0] = "O"

def chest():
    board[1] = "|"
    board[2] = "|"
    board[7] = "|"
    board[8] = "|"

def rhand():
    board[3] = "--"

def lhand():
    board[4] = "--"

def rleg():
    board[5] = "|"

def lleg():
    board[6] = "|"


with open("questions.json", "r", encoding='utf-8') as file:
    ques_ans_dict = json.load(file)

ques_seq = list(ques_ans_dict.keys())
shuffle(ques_seq)

body = [head, chest, rhand, lhand, rleg, lleg]
draw()
while len(body) and len(ques_seq):
    ques = ques_seq.pop()
    print(f"\n{ques}?")

    ans = input("Ответ: ")
    rightness = (ans == ques_ans_dict[ques])
    if not rightness:
        part = body.pop()
        part()

    draw(rightness)
    draw()
