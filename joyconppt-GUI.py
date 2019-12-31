# -*- coding: UTF-8 -*-
import Tkinter
import tkMessageBox
import ScrolledText
import PIL.Image
import PIL.ImageTk
import sys

root = Tkinter.Tk()
root.geometry('200x200')
root.resizable(False, False)
root.title('JoyConPPT')
root.iconbitmap('joyconppt.ico')

im1 = PIL.Image.open('jc_right.png')
im1.thumbnail((200,200))
jcimage_off = PIL.ImageTk.PhotoImage(im1)
im2 = PIL.Image.open('jc_right_on.png')
im2.thumbnail((200,200))
jcimage_on = PIL.ImageTk.PhotoImage(im2)

SW = Tkinter.Button(root,image=jcimage_off,height=200,width=200)
logs = ScrolledText.ScrolledText(root,height=15,width=20)

class IORedirector(object):
    '''A general class for redirecting I/O to this Text widget.'''
    def __init__(self,text_area):
        self.text_area = text_area
        self.text_area.tag_configure('STDOUT',foreground='black')
        self.text_area.tag_configure('STDERR',foreground='red')
        self.END = 'end'
class StdoutRedirector(IORedirector):
    '''A class for redirecting stdout to this Text widget.'''
    def write(self,str):
        self.text_area.insert(self.END,str,'STDOUT')
        self.text_area.see(self.END)
class StderrRedirector(IORedirector):
    '''A class for redirecting stderr to this Text widget.'''
    def write(self,str):
        self.text_area.insert(self.END,str,'STDERR')
        self.text_area.see(self.END)

sys.stdout = StdoutRedirector(logs)
sys.stderr = StderrRedirector(logs)

SW.grid(row=0)
logs.grid(row=0,column=1)

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
        except:
            tkMessageBox.showinfo( "joystick error", "joystick error")
            return
        t=threading.Thread(target=joycon.threadfun)
        t.start()
    else:
        joycon.postquit()
    change_statu()

debug_statu = False
def bind_debug(event):
    global debug_statu
    if debug_statu == False:
        root.geometry('')
    else:
        root.geometry('200x200')
    debug_statu = not(debug_statu)
def bind_off(event):
    if run_statu == True:
        joycon.postquit()
        change_statu()

root.bind('<F5>',bind_debug)
root.bind('<Escape>',bind_off)
SW.config(command=runscript)
# 进入消息循环
root.mainloop()
