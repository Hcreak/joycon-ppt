# -*- coding: UTF-8 -*-
import Tkinter
import tkMessageBox
# import ScrolledText
import PIL.Image
import PIL.ImageTk
# import time

import pygame
# from pygame.locals import *
# import pyautogui
import joycon
import threading

run_statu = False
def change_statu():
    global run_statu
    run_statu = not(run_statu)
    global SW
    if run_statu == False:
        SW.config(image=jcimage_off)
    else:
        SW.config(image=jcimage_on)


def runscript():
    if run_statu == False:
        try:
            joycon.main()
        except pygame.error:
            tkMessageBox.showinfo( "joystick error", "joystick error")
            return
        t=threading.Thread(target=joycon.threadfun)
        t.start()
    else:
        joycon.postquit()
    change_statu()

root = Tkinter.Tk()
# root.geometry('200x200')
# root.geometry()

root.resizable(False, False)
root.title('JoyConPPT')
root.iconbitmap('joyconppt.ico')

im1 = PIL.Image.open('jc_right.png')
im1.thumbnail((200,200))
jcimage_off = PIL.ImageTk.PhotoImage(im1)
im2 = PIL.Image.open('jc_right_on.png')
im2.thumbnail((200,200))
jcimage_on = PIL.ImageTk.PhotoImage(im2)

SW = Tkinter.Button(root,image=jcimage_off,height=200,width=200,command=runscript)
# logs = ScrolledText.ScrolledText(root,height=15,width=20)

SW.grid(row=0)
# logs.grid(row=0,column=1)

# 进入消息循环
root.mainloop()
