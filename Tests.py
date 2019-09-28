from random import  shuffle
from os import system

board = [ '' for _ in range (9) ]

def draw():
    system("cls")

    print("\t", "----------------")
    print("\n\t","|             |")
    print("\n\t","|             |")
    print("\n\t","|             |")
    print("\n\t","|             |")
    print("\n\t","|             |")
    print("\n\t","|             |")
    print("\n\t","|             ",board[0])
    print("\n\t","|             ",board[1])
    print("\n\t","|             ",board[2])
    print("\n\t","|         ", board[3],board[7], board[4], )
    print("\n\t","|             ", board[8])
    print("\n\t","|           ", board[5], "", board[6])
    print("\n\t","|")
    print("\t","---------")


def head():
    board[0] = "O"

def chest():
    board[1] = "|"
    board[2] = "|"
    board[7] = "|"
    board[8] = "|"

def rhand():
    board[3] = "---"

def lhand():
    board[4] = "---"

def rleg():
    board[5] = "|"

def lleg():
    board[6] = "|"

def text_logic():
    ques_ans_dict = {   "5ENDKEYZHENERNSINWWIHUZFD(T)": "FLOOR",
                        " 2+2*2": "6",
                        "Причина смерти Пушкина(уф)": "Дантес",
                        "b64(G)R0xPUllH": "GLORY",
                        "Zn+CuCl2": "Cu+ZnCl2",
                        "Успех - это способность идти с одной неудачи на другую, не теряя энтузиазм. Кто был автором этой фразы": "Уинстон Черчилль",
                        "Cogito Ergo Sum": "Рене Декарт",
                        "Какое животное ходит на 4 лапах, потом на 2х и в конце жизни на 3х": "Человек"
                        }
    ques_seq = list(ques_ans_dict.keys())
    shuffle(ques_seq)

    body = [head, chest, rhand, lhand, rleg, lleg]
    shuffle(body)

    while len(body):
        draw()
        ques = ques_seq.pop()
        print(f"\n{ques}?")
        ans = input("Ответ: ")
        rightness = (ans == ques_ans_dict[ques])
        print(rightness)

        if not rightness:
            part = body.pop()
            part()

    draw()

text_logic()
