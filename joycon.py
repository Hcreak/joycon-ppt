import pygame
from pygame.locals import *
import time
import pyautogui

def left():
    pyautogui.keyDown('left')
def right():
    pyautogui.keyDown('right')
def up():
    pyautogui.keyDown('up')
def down():
    pyautogui.keyDown('down')
def enter():
    pyautogui.keyDown('enter')

switch={
'3': left,
'0': right,
'1': up,
'2': down,
'15': enter
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
