import pygame
from pygame.locals import *
import time
import pyautogui

TaskSwitcher_statu = False

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
        TaskSwitcher_statu = not(TaskSwitcher_statu)
    else:
        pyautogui.keyUp('alt')
        TaskSwitcher_statu = not(TaskSwitcher_statu)



switch={
'3': left,
'0': right,
'1': up,
'2': down,
'15': enter,
'9': slideshow,
'12': Esc,
'14': TaskSwitcher        
}


def main() :
    pygame.joystick.init()
    joystick0 = pygame.joystick.Joystick(0)
    joystick0.init()

    print ("joystick start")

    pygame.init()

    while True:

        eventlist = pygame.event.get()

        for e in eventlist:
            if e.type == QUIT:
                return

            if e.type == pygame.locals.JOYBUTTONDOWN:
                input_button = str(e.button)
                print('button :{}'.format(input_button))

                switch[input_button]()

        time.sleep(0.1)

if __name__ == '__main__':
    try:
        main()
    except pygame.error:
        print ("joystick error")
