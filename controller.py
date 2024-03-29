from sense_hat import SenseHat
from time import sleep
from random import randint

sense= SenseHat()
sense.set_rotation(270)

selection = 1
begin = False

def display():
    global selection
    if(selection == 1):
        return "[*]car []frog []pong []snake []TTT"
    if(selection == 2):
        return "[]car [*]frog []pong []snake []TTT"
    if(selection == 3):
        return "[]car []frog [*]pong []snake []TTT"
    if(selection == 4):
        return "[]car []frog []pong [*]snake []TTT"
    if(selection == 5):
        return "[]car []frog []pong []snake [*]TTT"

def start():
    global begin
    begin = True
    
def left(event):
    global selection
    if event.action=='pressed' and selection<5:
        selection+=1
        
def right(event):
    global selection
    if event.action=='pressed' and selection>1:
        selection-=1

sense.stick.direction_up = left
sense.stick.direction_down = right
sense.stick.direction_middle = start

while not begin:
    sense.show_message(display(),scroll_speed=0.05)
if(selection == 1):
    import car_race
if(selection == 2):
    import frog 
if(selection == 3):
    import pong
if(selection == 4):
    import snake
if(selection == 5):
    import TTT
