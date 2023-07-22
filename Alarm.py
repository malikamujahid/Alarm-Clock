from tkinter .ttk import *   #import files
from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer
from datetime import datetime
from time import sleep
from threading import Thread
#color
bg_color='#ffffff'           # white background color
c1="#566FC6"                 # Blue frame line
c2="#000000"                  # Black frame body
# window
window= Tk()
window.title("")
window.geometry('350x150') 
window.configure(bg=bg_color)
#frames
frame_line= Frame(window, width=400, height=5, bg=c1)
frame_line.grid(row=0, column=0)

frame_body= Frame(window, width=400, height=290, bg=bg_color)
frame_body.grid(row=1, column=0)
# configuring frame body
img=Image.open('icon.jpg')
resized_img= img.resize((100,100))
tk_img = ImageTk.PhotoImage(resized_img)
img=ImageTk.PhotoImage(img)
app_image= Label(frame_body,height=100, image=img, bg=bg_color)
app_image.place(x=10,y=10)


#Set the Alarm Name
name= Label(frame_body,text= "Alarm", height= 1, font=('Times New Roman', 18, 'bold'), bg=bg_color)
name.place(x=120,y=10)


#Set the Hour Label
hour= Label(frame_body,text= "Hour", height= 1, font=('Times New Roman', 10, 'bold'), bg=bg_color, fg=c1)
hour.place(x=120,y=40)
c_hour=Combobox(frame_body, width=2, font=('arial', 15))
c_hour['values']= ("00","01","02","03","04","05","06","07","08","09","10","11","12")
c_hour.current(0)
c_hour.place(x=110, y=58)

# Set the minutes label
minutes= Label(frame_body,text= "Minutes", height= 1, font=('Times New Roman', 10, 'bold'), bg=bg_color, fg=c1)
minutes.place(x=160,y=40)
c_minutes=Combobox(frame_body, width=2, font=('arial', 15))
c_minutes['values']= ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                                         "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                                         "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
                                         "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
                                         "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
                                         "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_minutes.current(0)
c_minutes.place(x=160, y=58)


# Set the seconds label
seconds= Label(frame_body,text= "Seconds", height= 1, font=('Times New Roman', 10, 'bold'), bg=bg_color, fg=c1)
seconds.place(x=210,y=40)
c_seconds=Combobox(frame_body, width=2, font=('arial', 15))
c_seconds['values']= ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                                         "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                                         "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
                                         "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
                                         "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
                                         "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_seconds.current(0)
c_seconds.place(x=210, y=58)

# Set the period AM/PM label
period= Label(frame_body,text= "Period", height= 1, font=('Times New Roman', 10, 'bold'), bg=bg_color, fg=c1)
period.place(x=260,y=40) 
c_period=Combobox(frame_body, width=3, font=('arial', 15))
c_period['values']= ("AM", "PM")
c_period.current(0)
c_period.place(x=260, y=58)



def activate_alarm():
    t =Thread(target= alarm)
    t.start()


def Deactive_alarm():
    print('Deactivated alarm: ', selected.get())
    mixer.music.stop()

selected=IntVar()
rad1=Radiobutton(frame_body,font=('arial 10 bold'), value=1, text= "Activate", bg=bg_color, command= activate_alarm, variable=selected)
rad1.place(x=125,y=95)



def sound_alarm():
    mixer.music.load('Alarm Sound.mp3')
    mixer.music.play()
    selected.set(0)

rad2=Radiobutton(frame_body,font=('arial 10 bold'), value=2, text= "Deactivate", bg=bg_color, command= Deactive_alarm, variable=selected)
rad2.place(x=210,y=95)

def alarm():
    while True:
        control = 1
        print (control)
        alarm_hour = c_hour.get()
        alarm_minutes = c_minutes.get()
        alarm_seconds = c_seconds.get()
        alarm_period = c_period.get()
        alarm_period=str(alarm_period).upper()

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
window.mainloop()
