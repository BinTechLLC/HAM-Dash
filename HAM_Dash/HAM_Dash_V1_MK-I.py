#!/usr/bin/env python3.7
#Remember to open the terminal and use Exec=lxterminal /home/pi/DOC/CODE.py
#So it can run correctly when you make the desktop icon. You will also need
#The top line in order for the script to load the Python library correctly.
#---------------------------------------------------------------------------------------------- Import Libraries
from tkinter import *
#import RPi.GPIO as GPIO
import time
import os
#-------------------------------------------------------------- Update Raspbian
def updateOS():
    os.system('sudo apt-get update')
#-------------------------------------------------------------- Reboot Function
def rebootRPi():
    os.system('sudo shutdown -r now')
#-------------------------------------------------------------- !!!EXIT BUTTON - DO NOT REMOVE!!!
def fullExit():
    root.destroy()      #Kills the full screen window
    exit()              #Kills terminal
#-------------------------------------------------------------- !!!EXIT BUTTON - DO NOT REMOVE!!!
#-------------------------------------------------------------- Menu 1
def menuSOS():
    menuSOS = Toplevel(root)
    menuSOS.geometry('800x480')
    menuSOS.attributes('-fullscreen', True)
    menuSOS.configure(background="magenta3")
    #---------------------------------------------------------------------------------------------- Banner
    photo5 = PhotoImage(file="/home/pi/Projects/HAM_Dash/Backgrounds/Background-2.png")
    label000099 = Label(menuSOS, image=photo)
    label000099.place(x=0,y=0)
    def menuSOSExit():
        menuSOS.destroy()
    button001199=Button(menuSOS,text='BACK',font=('Helvetica','16'),width=12,height=2,bg="hot pink",fg="gray1",command=menuSOSExit)
    button001199.place(x=605,y=380)
#-------------------------------------------------------------- Menu 1
def menuOne():
    menu1 = Toplevel(root)
    menu1.geometry('800x480')
    menu1.attributes('-fullscreen', True)
    menu1.configure(background="magenta3")
    #---------------------------------------------------------------------------------------------- Banner
    photo1 = PhotoImage(file="/home/pi/Projects/HAM_Dash/Backgrounds/Background-2.png")
    label11099 = Label(menu1, image=photo)
    label11099.place(x=0,y=0)
    def menuOneExit():
        menu1.destroy()
    button1199=Button(menu1,text='BACK',font=('Helvetica','16'),width=12,height=2,bg="hot pink",fg="gray1",command=menuOneExit)
    button1199.place(x=605,y=380)
#-------------------------------------------------------------- Menu 2
def menuTwo():
    menu2 = Toplevel(root)
    menu2.geometry('800x480')
    menu2.attributes('-fullscreen', True)
    menu2.configure(background="sienna4")
    #---------------------------------------------------------------------------------------------- Banner
    photo2 = PhotoImage(file="/home/pi/Projects/HAM_Dash/Backgrounds/Background-2.png")
    label21099 = Label(menu2, image=photo)
    label21099.place(x=0,y=0)
    def menuTwoExit():
        menu2.destroy()
    button2199=Button(menu2,text='BACK',font=('Helvetica','16'),width=12,height=2,bg="hot pink",fg="gray1",command=menuTwoExit)
    button2199.place(x=605,y=380)
#-------------------------------------------------------------- Menu 3
def menuThree():
    menu3 = Toplevel(root)
    menu3.geometry('800x480')
    menu3.attributes('-fullscreen', True)
    menu3.configure(background="blue4")
    #---------------------------------------------------------------------------------------------- Banner
    photo3 = PhotoImage(file="/home/pi/Projects/HAM_Dash/Backgrounds/Background-2.png")
    label31099 = Label(menu3, image=photo)
    label31099.place(x=0,y=0)
    def menuThreeExit():
        menu3.destroy()

    #--------------------------------------------------------------------
    button3101=Button(menu3, text='1',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button3101.place(x=15,y=15)
    
    button3102=Button(menu3, text='2',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button3102.place(x=95,y=15)
    
    button3103=Button(menu3, text='3',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button3103.place(x=175,y=15)
    
    button3104=Button(menu3, text='A',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button3104.place(x=255,y=15)
    
    #--------------------------------------------------------------------
    button3105=Button(menu3, text='4',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button3105.place(x=15,y=95)
    
    button3106=Button(menu3, text='5',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button3106.place(x=95,y=95)
    
    button3107=Button(menu3, text='6',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button3107.place(x=175,y=95)
    
    button3108=Button(menu3, text='B',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button3108.place(x=255,y=95)
    #--------------------------------------------------------------------
    
    button3109=Button(menu3, text='7',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button3109.place(x=15,y=175)
    
    button3110=Button(menu3, text='8',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button3110.place(x=95,y=175)
    
    button3111=Button(menu3, text='9',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button3111.place(x=175,y=175)
    
    button3112=Button(menu3, text='C',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button3112.place(x=255,y=175)
    #--------------------------------------------------------------------
    
    button3113=Button(menu3, text='*',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button3113.place(x=15,y=255)
    
    button3114=Button(menu3, text='0',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button3114.place(x=95,y=255)
    
    button3115=Button(menu3, text='#',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button3115.place(x=175,y=255)
    
    button3116=Button(menu3, text='D',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button3116.place(x=255,y=255)
    
    
    
    
    
    button3199=Button(menu3,text='BACK',font=('Helvetica','16'),width=12,height=2,bg="hot pink",fg="gray1",command=menuThreeExit)
    button3199.place(x=605,y=380)
#-------------------------------------------------------------- Menu 4
def menuFour():
    menu4 = Toplevel(root)
    menu4.geometry('800x480')
    menu4.attributes('-fullscreen', True)
    menu4.configure(background="red4")
    #---------------------------------------------------------------------------------------------- Banner
    photo4 = PhotoImage(file="/home/pi/Projects/HAM_Dash/Backgrounds/Background-2.png")
    label41099 = Label(menu4, image=photo)
    label41099.place(x=0,y=0)
    def menuFourExit():
        menu4.destroy()
    #----------------------------------- Version Mark
    button4101=Button(menu4, text='MK-I',font=('Helvetica','16'),width=12,height=2,bg="red3",fg="gray1")
    button4101.place(x=5,y=5)
    #----------------------------------- Reboot System Button
    button4196=Button(menu4,text='Reboot System',font=('Helvetica','16'),width=12,height=2,bg="DarkOrange1",fg="gray1",command=rebootRPi)
    button4196.place(x=5,y=380)

    #----------------------------------- Update System Button
    button4197=Button(menu4, text='Update System',font=('Helvetica','16'),width=12,height=2,bg="purple2",fg="gray1",command=updateOS)
    button4197.place(x=205,y=380)
    #---------------------------------------------------------------------------------------------- #DO NOT REMOVE OR ALTER
    #----------------------------------- #BUTTON EXITS FULL SCREEN AND ENDS PYTHON.
    button4199=Button(menu4, text='Exit App',font=('Helvetica','16'),width=12,height=2,bg="LightYellow2",fg="gray1",command= fullExit)
    button4199.place(x=405,y=380)
    #---------------------------------------------------------------------------------------------- #DO NOT REMOVE OR ALTER
    button4198=Button(menu4,text='Exit Settings',font=('Helvetica','16'),width=12,height=2,bg="hot pink",fg="gray1",command=menuFourExit)
    button4198.place(x=605,y=380)

#---------------------------------------------------------------------------------------------- Touch Screen Begin
root=Tk()
root.attributes('-fullscreen', True)       #Fullscreen True / False
root.title("Menus V2 MK-I")
root.geometry('800x480')
root.configure(background="hot pink")
time.sleep(0.5)
#---------------------------------------------------------------------------------------------- Banner
photo = PhotoImage(file="/home/pi/Projects/HAM_Dash/Backgrounds/Background-2.png")
label0099 = Label(root, image=photo)
label0099.place(x=0,y=0)
#---------------------------------------------------------------------------------------------- Base Menu Buttons
#----------------------------------- Menu 1 Button
button0001=Button(root, text='Radio Routing',font=('Helvetica','16'),width=12,height=2,bg="red2",fg="gray1",command=menuOne)
button0001.place(x=5,y=5)
#----------------------------------- Menu 2 Button
button0002=Button(root, text='Antenna Routing',font=('Helvetica','16'),width=12,height=2,bg="orange",fg="gray1",command=menuTwo)
button0002.place(x=205,y=5)
#----------------------------------- Menu 3 Button
button0003=Button(root, text='DTMF Encoder',font=('Helvetica','16'),width=12,height=2,bg="maroon2",fg="gray1",command=menuThree)
button0003.place(x=405,y=5)
#----------------------------------- Menu 4 Button
button0004=Button(root, text='System Settings',font=('Helvetica','16'),width=12,height=2,bg="green2",fg="gray1",command=menuFour)
button0004.place(x=605,y=5)


button0005=Button(root,text='!!  S O S  !!',font=('Helvetica','16'),width=12,height=2,bg="red",fg="gray1",command=menuSOS)
button0005.place(x=5,y=380)


root.mainloop()