#!/usr/bin/env python3.7
#Remember to change the execute permissions to Anyone
#or the program will fail to run. You will also have
#to change the execute permissions on the desktop
#icon, should you choose to create one.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Credits
# Programmed and debugged by Koltin Binford and Brian Fletcher
# This program is to be used on a custom built system for
# Brian Fletcher's vehicle amateur radi setup. This program
# can be used by others if they wish to recreate the hardware
# add ons required for this system, and make any personal
# modifications to functions, layout, schemes, etc.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Import Libraries
from tkinter import *
#import RPi.GPIO as GPIO
import time
import os
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Global Commands Begin
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Credits Menu Begin (10)
def creditsScreen():
    def creditsScreenExit():
        creditsScreen.destroy()
    creditsScreen=Toplevel(root)
    creditsScreen.attributes('-fullscreen', False)       # Fullscreen True / False
    creditsScreen.title("App Credits")
    creditsScreen.geometry('800x480')
    creditsScreen.configure(background="gray5")
    #------------------------------------------------------------------------------------------------------------------------------------------------------------- Page Background
    label9999=Label(creditsScreen, image=photo9999)
    label9999.place(x=0,y=0)
    #---------------------------------------------------------------------------------------------------- Exit Credits Button
    button10002=Button(creditsScreen,text='Exit Credits',font=('Halvetica','12'),width=16,height=2,bg="blue2",fg="gray1",command=creditsScreenExit)
    button10002.place(x=605,y=380)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Credits Menu Begin (10)
#---------------------------------------------------------------------------------------------------- Update Raspbian Command
def updateRaspbian():
    os.system('sudo apt-get update')
#---------------------------------------------------------------------------------------------------- Reboot System Command
def restartSystem():
    os.system('sudo shutdown -r now')
#---------------------------------------------------------------------------------------------------- Shutdown System Command
def shutdownSystem():
    os.system('sudo shutdown -s now')
#---------------------------------------------------------------------------------------------------------------- ! ! ! EXIT BUTTON - DO NOT REMOVE ! ! !
def programExit():
    root.destroy()
    exit()
#---------------------------------------------------------------------------------------------------------------- ! ! ! EXIT BUTTON - DO NOT REMOVE ! ! !
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Global Commands End
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- System Menu Begin (9)
def menuSystem():
    def menuSystemExit():
        menuSystem.destroy()
    menuSystem=Toplevel(root)
    menuSystem.attributes('-fullscreen', False)       # Fullscreen True / False
    menuSystem.title("System Settings")
    menuSystem.geometry('800x480')
    menuSystem.configure(background="gray5")
    #------------------------------------------------------------------------------------------------------------------------------------------------------------- Page Background
    label9001=Label(menuSystem, image=background9)
    label9001.place(x=0,y=0)
    #------------------------------------------------------------------------------------------------------------------------------------------------------------- All Buttons
    #
    #----------------------------------------------------------------------------------------------------------------------------------------- Row 3
    #
    #---------------------------------------------------------------------------------------------------- Update App Button
    button9092=Button(menuSystem,text='Update App',font=('Halvetica','12'),width=16,height=2,bg="RoyalBlue2",fg="gray1")
    button9092.place(x=5,y=310)
    #---------------------------------------------------------------------------------------------------- Update System Button
    button9093=Button(menuSystem,text='Update System',font=('Halvetica','12'),width=16,height=2,bg="RoyalBlue2",fg="gray1",command=updateRaspbian)
    button9093.place(x=205,y=310)
    #---------------------------------------------------------------------------------------------------- NA Button
    button9094=Button(menuSystem,text=' ',font=('Halvetica','12'),width=16,height=2,bg="gray20",fg="gray1")
    button9094.place(x=405,y=310)
    #---------------------------------------------------------------------------------------------------- NA Button
    button9095=Button(menuSystem,text='App Credits',font=('Halvetica','12'),width=16,height=2,bg="gray20",fg="gray1",command=creditsScreen)
    button9095.place(x=605,y=310)
    #----------------------------------------------------------------------------------------------------------------------------------------- Row 4
    #
    #---------------------------------------------------------------------------------------------------- Restart System Button
    button9096=Button(menuSystem,text='Restart System',font=('Halvetica','12'),width=16,height=2,bg="firebrick3",fg="gray1",command=restartSystem)
    button9096.place(x=5,y=380)
    #---------------------------------------------------------------------------------------------------- Shutdown System Button
    button9097=Button(menuSystem,text='Shutdown System',font=('Halvetica','12'),width=16,height=2,bg="red",fg="gray1",command=shutdownSystem)
    button9097.place(x=205,y=380)
    #---------------------------------------------------------------------------------------------------- Exit App Button
    button9098=Button(menuSystem,text='Exit App',font=('Halvetica','12'),width=16,height=2,bg="slate gray",fg="gray1",command=programExit)
    button9098.place(x=405,y=380)
    #---------------------------------------------------------------------------------------------------- Exit Settings Button
    button9099=Button(menuSystem,text='Exit Settings',font=('Halvetica','12'),width=16,height=2,bg="blue2",fg="gray1",command=menuSystemExit)
    button9099.place(x=605,y=380)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- System Menu End (9)
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Root Window Begin
root=Tk()
root.attributes('-fullscreen', False)       # Fullscreen True / False
root.title("HAM Dash V1")
root.geometry('800x480')
root.configure(background="gray5")
#------------------------------------------------------------------------------------------------------------------------------------------------------------- Background Image Imports
background1=PhotoImage(file="/home/pi/Projects/HAM_Dash/Backgrounds/Background-1.png")
background9=PhotoImage(file="/home/pi/Projects/HAM_Dash/Backgrounds/Background-2.png")
photo9999=PhotoImage(file="/home/pi/Projects/HAM_Dash/Backgrounds/Background-Credits.png")
#------------------------------------------------------------------------------------------------------------------------------------------------------------- Page Background
label0001=Label(root, image=background1)
label0001.place(x=0,y=0)
#------------------------------------------------------------------------------------------------------------------------------------------------------------- All Buttons
#
#----------------------------------------------------------------------------------------------------------------------------------------- Row 1
#
#---------------------------------------------------------------------------------------------------- Mic Routing Button
button0001=Button(root,text='Mic Routing',font=('Halvetica','12'),width=16,height=2,bg="goldenrod",fg="gray1")
button0001.place(x=5,y=5)
#---------------------------------------------------------------------------------------------------- Antenna Routing Button
button0002=Button(root,text='Antenna Routing',font=('Halvetica','12'),width=16,height=2,bg="sienna2",fg="gray1")
button0002.place(x=205,y=5)
#---------------------------------------------------------------------------------------------------- GPS Button
button0003=Button(root,text='GPS',font=('Halvetica','12'),width=16,height=2,bg="gold",fg="gray1")
button0003.place(x=405,y=5)
#---------------------------------------------------------------------------------------------------- NA Button
button0004=Button(root,text='QSL',font=('Halvetica','12'),width=16,height=2,bg="burlywood3",fg="gray1")
button0004.place(x=605,y=5)
#----------------------------------------------------------------------------------------------------------------------------------------- Row 4
#
#---------------------------------------------------------------------------------------------------- System Settings Button
button0099=Button(root,text='System Settings',font=('Halvetica','12'),width=16,height=2,bg="orange",fg="gray1",command=menuSystem)
button0099.place(x=605,y=380)
root.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Root Window Ends
