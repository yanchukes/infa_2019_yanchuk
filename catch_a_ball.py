#!/usr/bin/env python3
# -*- coding: utf8 -*-
'''
    lesson 4
    Game:
    Catch a ball
    Сделать код читабельным и документированным.
    Реализовать подсчёт очков.
    Сделать шарики двигающимися со случайным отражением от стен.
    Реализовать одновременное присутствие нескольких шариков на экране.
    Добавить второй тип мишени со своей формой и своим специфическим харктером движения.
    Выдавать за эти мишени другое количество очков.
    Сделать таблицу лучших игроков, авматически сохраняющуюся в файл.
'''

import tkinter as tk
from random import randrange as rnd, choice
from math import sqrt
import time
root = tk.Tk()
root.geometry('800x600')

canv = tk.Canvas(root,bg='white')
canv.pack(fill=tk.BOTH,expand=1)

total = 0
number = 0
stag = "oval_" + str(number)
colors = ['red','orange','yellow','green','blue']

def new_ball():
    global x, y, r, number, stag
    canv.delete(tk.ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    number += 1
    print(stag)
    #print("Параметры круга:", x,y,r)
    ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0, tag=stag)
    root.after(1000,new_ball)


def click(event):
    global total
    coord = (event.x, event.y)
    #print(coord)
    distance = round(sqrt(abs(event.x - x)**2 + abs(event.y - y)**2))
    print("расстояние", distance)
    if sqrt(r**2) >= distance:
        total += 1
        print('Очков', total)
        canv.delete(stag)

if __name__ == '__main__':
    new_ball()
    canv.bind('<Button-1>', click)
    tk.mainloop()
