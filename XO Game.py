from tkinter import *
from player import *
import random as r
from tkinter import messagebox
import numpy as np
user_1 = player()
user_2 = player()

user_1.name = "Player 1 - O"
user_2.name = "Player 2 - X"
user_1.symbole ="X"
user_2.symbole = "O"
user_1.enteries =[[0, 0, 0],[0,0, 0],[0,0, 0]]
user_2.enteries =[[0, 0, 0],[0,0, 0],[0,0, 0]]

#########

user_1.turn = r.choice([True , False])
user_2.turn = not(user_1.turn)


def turner(x,y):
    if user_1.turn:
        if not(user_1.enteries[x][y] or user_2.enteries[x][y]):
            user_1.enteries[x][y] = 1
            user_1.turn = user_2.turn
            user_2.turn = not(user_2.turn)
            disp.set("The Turn For:\n " +str(user_2.name))  
    else:
        if not(user_1.enteries[x][y] or user_2.enteries[x][y]):
            user_2.enteries[x][y] = 1
            user_1.turn = user_2.turn
            user_2.turn = not(user_2.turn)
            disp.set("The Turn For:\n " +str(user_1.name))
            
               
def clear_all():
    b1.set("")
    b2.set("")
    b3.set("")
    b4.set("")
    b5.set("")
    b6.set("")
    b7.set("")
    b8.set("")
    b9.set("")

def CHECK():
    if user_1.checker():
        msg = messagebox.showinfo("congratulations",user_1.name + " Won!")
        user_1.enteries =[[0, 0, 0],[0,0, 0],[0,0, 0]]
        user_2.enteries =[[0, 0, 0],[0,0, 0],[0,0, 0]]
        clear_all()
    if user_2.checker():
        msg = messagebox.showinfo("congratulations",user_2.name + " Won!")
        user_1.enteries =[[0, 0, 0],[0,0, 0],[0,0, 0]]
        user_2.enteries =[[0, 0, 0],[0,0, 0],[0,0, 0]]
        clear_all()
    if (np.array(user_1.enteries) + np.array(user_2.enteries)).sum() == 9:
        msg = messagebox.showinfo("Nobody won", "Nobody won !")
        user_1.enteries =[[0, 0, 0],[0,0, 0],[0,0, 0]]
        user_2.enteries =[[0, 0, 0],[0,0, 0],[0,0, 0]]
        clear_all()
def btt1():
    x =0
    y =0
    if not(user_1.turn):
        if not(user_1.enteries[x][y]==1 or user_2.enteries[x][y]==1):
            b1.set(user_1.symbole)
            
    if not(user_2.turn):
        if not(user_1.enteries[x][y] ==1 or user_2.enteries[x][y] ==1):
            b1.set(user_2.symbole)
    turner(x,y)
    CHECK()
def btt2():
    x = 0
    y =1
    if not(user_1.turn):
        if not(user_1.enteries[x][y] or user_2.enteries[x][y]):
            b2.set(user_1.symbole)
            
    if not(user_2.turn):
        if not(user_1.enteries[x][y] ==1 or user_2.enteries[x][y] ==1):
            b2.set(user_2.symbole)
    turner(x,y)
    CHECK()
def btt3():
    x = 0
    y =2
    if not(user_1.turn):
        if not(user_1.enteries[x][y] or user_2.enteries[x][y]):
            b3.set(user_1.symbole)
            
    if not(user_2.turn):
        if not(user_1.enteries[x][y] ==1 or user_2.enteries[x][y] ==1):
            b3.set(user_2.symbole)
    turner(x,y)
    CHECK()
def btt4():
    x = 1
    y = 0
    if not(user_1.turn):
        if not(user_1.enteries[x][y]==1 or user_2.enteries[x][y]==1):
            b4.set(user_1.symbole)
            
    if not(user_2.turn):
        if not(user_1.enteries[x][y] ==1 or user_2.enteries[x][y] ==1):
            b4.set(user_2.symbole)
    turner(x,y)
    CHECK()
                
def btt5():
    x = 1
    y =1
    if not(user_1.turn):
        if not(user_1.enteries[x][y] or user_2.enteries[x][y]):
            b5.set(user_1.symbole)
            
    if not(user_2.turn):
        if not(user_1.enteries[x][y] ==1 or user_2.enteries[x][y] ==1):
            b5.set(user_2.symbole)
    turner(x,y)
    CHECK()
def btt6():
    x = 1
    y = 2
    if not(user_1.turn):
        if not(user_1.enteries[x][y] or user_2.enteries[x][y]):
            b6.set(user_1.symbole)
            
    if not(user_2.turn):
        if not(user_1.enteries[x][y] ==1 or user_2.enteries[x][y] ==1):
            b6.set(user_2.symbole)
    turner(x,y)
    CHECK()
def btt7():
    x = 2
    y = 0
    if not(user_1.turn):
        if not(user_1.enteries[x][y] or user_2.enteries[x][y]):
            b7.set(user_1.symbole)
            
    if not(user_2.turn):
        if not(user_1.enteries[x][y] ==1 or user_2.enteries[x][y] ==1):
            b7.set(user_2.symbole)
    turner(x,y)
    CHECK()
def btt8():
    x = 2
    y = 1
    if not(user_1.turn):
        if not(user_1.enteries[x][y] or user_2.enteries[x][y]):
            b8.set(user_1.symbole)
            
    if not(user_2.turn):
        if not(user_1.enteries[x][y] ==1 or user_2.enteries[x][y] ==1):
            b8.set(user_2.symbole)
    turner(x,y)
    CHECK()
def btt9():
    x = 2
    y = 2
    if not(user_1.turn):
        if not(user_1.enteries[x][y] or user_2.enteries[x][y]):
            b9.set(user_1.symbole)
            
    if not(user_2.turn):
        if not(user_1.enteries[x][y] ==1 or user_2.enteries[x][y] ==1):
            b9.set(user_2.symbole)
    turner(x,y)
    CHECK()

last = Tk()

#last.state('withdrawn')
last.geometry("380x505")
last.maxsize(380,505)
last.minsize(380,505)
last.title("XO Game")
last.configure(bg = '#666666')

disp = StringVar()
b1 = StringVar()
b2 = StringVar()
b3 = StringVar()
b4 = StringVar()
b5 = StringVar()
b6 = StringVar()
b7 = StringVar()
b8 = StringVar()
b9 = StringVar()
lb1 = Label(last ,
            textvariable = disp ,  #T.set('bla bla')
            font = ('Arial',16 ),
            fg ='white',
            bg = '#036088',
            bd = 6,
            #relief = 'groove',
            #height = 1,
            height = 4,
            width = 32
           )
lb1.place(x = 0, y = 0)

if user_1.turn:
    disp.set("The Turn For:\n " +str(user_1.name))
else:
    disp.set("The Turn For:\n "  +str(user_2.name))
    
bt1 = Button(last,
             font = ('Arial',43 ),
             textvariable = b1,
             fg = '#036088',
             height = 1,
             command = btt1,
             width = 3)
bt1.place(x=12, y=120)

bt2 = Button(last,
             font = ('Arial',43 ),
             textvariable = b2,
             fg = '#036088',
             height = 1,
             command = btt2,
             width = 3)
bt2.place(x=142-6, y=120)

bt3 = Button(last,
             font = ('Arial',43 ),
             textvariable = b3,
             fg = '#036088',
             height = 1,
             command = btt3,
             width = 3)
bt3.place(x=12+130*2-2*6, y=120)

bt4 = Button(last,
             font = ('Arial',43 ),
             textvariable = b4,
             fg = '#036088',
             command = btt4,
             height = 1,
             width = 3)
bt4.place(x=12, y=120+130)

bt5 = Button(last,
             textvariable = b5,
             font = ('Arial',43 ),
             fg = '#036088',
             command = btt5,
             height = 1,
             width = 3)
bt5.place(x=12+130*1 -6, y=120+1*130)

bt6 = Button(last,
             textvariable = b6,
             font = ('Arial',43 ),
             height = 1,
             command = btt6,
             fg = '#036088',
             width = 3)
bt6.place(x=12+130*2 -2*6, y=120+1*130)

bt7 = Button(last,
             font = ('Arial',43 ),
             textvariable = b7,
             fg = '#036088',
             command = btt7,
             height = 1,
             width = 3)
bt7.place(x=12+130*0, y=120+2*130)

bt8 = Button(last,
             font = ('Arial',43 ),
             textvariable = b8,
             fg = '#036088',
             height = 1,
             command = btt8,
             width = 3)
bt8.place(x=12+130*1 -6, y=120+2*130)

bt9 = Button(last,
             font = ('Arial',43 ),
             textvariable = b9,
             command = btt9,
             fg = '#036088',
             height = 1,
             width = 3)
bt9.place(x=12+130*2 -2*6, y=120+2*130)




last.mainloop()
