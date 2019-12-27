import pygame
from pygame.locals import *
# import time
import pyautogui
import sys

TaskSwitcher_statu = False
dragleft_statu = False

def left():
    pyautogui.press('left')
def right():
    pyautogui.press('right')
def up():
    pyautogui.press('up')
def down():
    pyautogui.press('down')
def enter():
    pyautogui.press('enter')
def slideshow():
    pyautogui.press('f5')
def Esc():
    pyautogui.press('esc')
def TaskSwitcher():
    global TaskSwitcher_statu
    if TaskSwitcher_statu == False:
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
    else:
        pyautogui.keyUp('alt')
    TaskSwitcher_statu = not(TaskSwitcher_statu)
def dragleft():
    global dragleft_statu
    if dragleft_statu == False:
        pyautogui.hotkey('ctrl', 'l')
    else:    
        pyautogui.press('esc')
    dragleft_statu = not(dragleft_statu)
    



switch={
'3': left,
'0': right,
'1': up,
'2': down,
'15': enter,
'9': slideshow,
'12': Esc,
'14': TaskSwitcher,
'11': dragleft        
}


def main():
    pygame.joystick.init()
    joystick0 = pygame.joystick.Joystick(0)
    joystick0.init()

    print ("joystick start")

    pygame.init()
    pygame.event.set_allowed([QUIT,JOYBUTTONDOWN,JOYHATMOTION])
   

def threadfun():
    y,x = 0,0
    
    while True:

        if x!=0 or y!=0:
            pyautogui.move(x*(-40),y*(-40))

        # time.sleep(5)
        # postquit()

        eventlist = pygame.event.get()
        for e in eventlist:
            if e.type == QUIT:
                return

            if e.type == JOYBUTTONDOWN:
                input_button = str(e.button)
                print('button :{}'.format(input_button))

                switch[input_button]()
            
            # if e.type == pygame.locals.JOYAXISMOTION:
            #     print('axis {} : {}'.format(e.axis,e.value))

            if e.type == JOYHATMOTION:
                position = e.value
                print('hat : {}'.format(position))
                y,x = position


def postquit():
    pygame.event.post(pygame.event.Event(QUIT))

if __name__ == '__main__':
    try:
        main()
    except pygame.error:
        print ("joystick error")
        sys.exit()
    threadfun()
    