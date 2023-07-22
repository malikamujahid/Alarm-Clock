from tkinter .ttk import *   #import files
from tkinter import *
from pygame import mixer
from datetime import datetime
from time import sleep
# window
window= Tk()
window.title("")
window.geometry('350x150') 


def sound_alarm():
    mixer.music.load('Alarm Sound.mp3')
    mixer.music.play()


def alarm():
    while True:
        control = 1
        print (control)
        alarm_hour = '10'
        alarm_minutes = '25'
        alarm_seconds = '00'
        alarm_period = 'PM'.upper()

        now = datetime.now()
        hours = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        periods = now.strftime("%p")

        if control == 1:
            if alarm_period == periods:
                if alarm_hour == hours:
                    if alarm_minutes == minute:
                        if alarm_seconds == second:
                            print("Time to take a break")
                            sound_alarm()
        sleep(1)
mixer.init()
alarm()
window.mainloop()
