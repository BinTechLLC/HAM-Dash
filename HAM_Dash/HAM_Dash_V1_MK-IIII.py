#!/usr/bin/env python3.7
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Credits
# Programmed and debugged by Koltin Binford and Brian Fletcher
# This program is to be used on a custom built system for
# Brian Fletcher's vehicle amateur radio setup. This program
# can be used by others if they wish to recreate the hardware
# add ons required for this system, and make any personal
# modifications to functions, layout, schemes, etc.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Import Libraries
from tkinter import *
#import RPi.GPIO as GPIO
import time
from time import gmtime, strftime
import os
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Global Commands and Definitions Begin
#
#---------------------------------------------------------------------------------------------------- Integer Definition
currentTime=''
def restartMenuSystem():
    root.wm_state('normal')
    #time.sleep(0.5)
    menuSystem()
#---------------------------------------------------------------------------------------------------- Reboot System Command
def restartSystem():
    os.system('sudo shutdown -r now')
#---------------------------------------------------------------------------------------------------- Shutdown System Command
def shutdownSystem():
    os.system('sudo shutdown -s now')
#---------------------------------------------------------------------------------------------------------------- ! ! ! EXIT BUTTON - DO NOT REMOVE ! ! !
def programExit():
    root.destroy()
    #exit()
#---------------------------------------------------------------------------------------------------------------- ! ! ! EXIT BUTTON - DO NOT REMOVE ! ! !
#---------------------------------------------------------------------------------------------------- System Time Update
def systemTime():
    global currentTime
    currentTime = time.strftime('Z: %H:%M:%S',gmtime())
    clock.configure(text=currentTime)
    clock.after(200,systemTime)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Global Commands and Definitions End
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- DTMF Window Begins (5)
def menuDTMF():
    def menuDTMFExit():
        menuDTMF.destroy()
    menuDTMF = Toplevel(root)
    menuDTMF.geometry('800x480')
    menuDTMF.attributes('-fullscreen', True)       # Fullscreen True / False
    menuDTMF.configure(background="gray5")
    #------------------------------------------------------------------------------------------------------------------------------------------------------------- Page Background
    label5001 = Label(menuDTMF,image=background1)
    label5001.place(x=0,y=0)
    #----------------------------------------------------------------------------------------------------------------------------------------- Row 1
    #
    #---------------------------------------------------------------------------------------------------- 1 Button
    button5001=Button(menuDTMF,text='1',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button5001.place(x=15,y=15)
    #---------------------------------------------------------------------------------------------------- 2 Button
    button5002=Button(menuDTMF,text='2',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button5002.place(x=95,y=15)
    #---------------------------------------------------------------------------------------------------- 3 Button
    button5003=Button(menuDTMF,text='3',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button5003.place(x=175,y=15)
    #---------------------------------------------------------------------------------------------------- A Button
    button5004=Button(menuDTMF,text='A',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button5004.place(x=255,y=15)
    #----------------------------------------------------------------------------------------------------------------------------------------- Row 2
    #
    #---------------------------------------------------------------------------------------------------- 4 Button
    button5005=Button(menuDTMF,text='4',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button5005.place(x=15,y=95)
    #---------------------------------------------------------------------------------------------------- 5 Button
    button5006=Button(menuDTMF,text='5',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button5006.place(x=95,y=95)
    #---------------------------------------------------------------------------------------------------- 6 Button
    button5007=Button(menuDTMF,text='6',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button5007.place(x=175,y=95)
    #---------------------------------------------------------------------------------------------------- B Button
    button5008=Button(menuDTMF,text='B',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button5008.place(x=255,y=95)
    #----------------------------------------------------------------------------------------------------------------------------------------- Row 3
    #
    #---------------------------------------------------------------------------------------------------- 7 Button
    button5009=Button(menuDTMF,text='7',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button5009.place(x=15,y=175)
    #---------------------------------------------------------------------------------------------------- 8 Button
    button5010=Button(menuDTMF,text='8',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button5010.place(x=95,y=175)
    #---------------------------------------------------------------------------------------------------- 9 Button
    button5011=Button(menuDTMF,text='9',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button5011.place(x=175,y=175)
    #---------------------------------------------------------------------------------------------------- C Button
    button5012=Button(menuDTMF,text='C',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button5012.place(x=255,y=175)
    #----------------------------------------------------------------------------------------------------------------------------------------- Row 4
    #
    #---------------------------------------------------------------------------------------------------- * Button
    button5013=Button(menuDTMF,text='*',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button5013.place(x=15,y=255)
    #---------------------------------------------------------------------------------------------------- 0 Button
    button5014=Button(menuDTMF,text='0',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button5014.place(x=95,y=255)
    #---------------------------------------------------------------------------------------------------- # Button
    button5015=Button(menuDTMF,text='#',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button5015.place(x=175,y=255)
    #---------------------------------------------------------------------------------------------------- D Button
    button5016=Button(menuDTMF,text='D',font=('Helvetica','14'),width=5,height=3,bg="red2",fg="gray1")
    button5016.place(x=255,y=255)
    #----------------------------------------------------------------------------------------------------------------------------------------- Row 5
    #
    #---------------------------------------------------------------------------------------------------- Back Button
    button5099=Button(menuDTMF,text='BACK',font=('Helvetica','12'),width=18,height=2,bg="blue2",fg="gray1",command=menuDTMFExit)
    button5099.place(x=605,y=380)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- DTMF Window Ends (5)
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- System Menu Begin (9)
def menuSystem():
    def menuSystemExit():
        menuSystem.destroy()    
    def updateRaspbian():
        root.wm_state('iconic')
        menuSystem.wm_state('iconic')
        os.system('bash /home/pi/Projects/HAM_Dash/sh/call_system_update.sh')
        menuSystem.destroy()
        restartMenuSystem()
        
        
        
    menuSystem=Toplevel(root)
    menuSystem.attributes('-fullscreen', True)       # Fullscreen True / False
    menuSystem.title("System Settings")
    menuSystem.geometry('800x480')
    menuSystem.configure(background="gray5")
    #------------------------------------------------------------------------------------------------------------------------------------------------------------- Page Background
    label9001=Label(menuSystem, image=background1)
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
    #---------------------------------------------------------------------------------------------------- Credits Screen Button
    button9095=Button(menuSystem,text='App Credits',font=('Halvetica','12'),width=16,height=2,bg="green3",fg="gray1",command=creditsScreen)
    button9095.place(x=605,y=310)
    #----------------------------------------------------------------------------------------------------------------------------------------- Row 4
    #
    #---------------------------------------------------------------------------------------------------- Restart System Button
    button9096=Button(menuSystem,text='Restart System',font=('Halvetica','12'),width=16,height=2,bg="goldenrod1",fg="gray1",command=restartSystem)
    button9096.place(x=5,y=380)
    #---------------------------------------------------------------------------------------------------- Shutdown System Button
    button9097=Button(menuSystem,text='Shutdown System',font=('Halvetica','12'),width=16,height=2,bg="orange",fg="gray1",command=shutdownSystem)
    button9097.place(x=205,y=380)
    #---------------------------------------------------------------------------------------------------- Exit App Button
    button9098=Button(menuSystem,text='Exit App',font=('Halvetica','12'),width=16,height=2,bg="slate gray",fg="gray1",command=programExit)
    button9098.place(x=405,y=380)
    #---------------------------------------------------------------------------------------------------- Exit Settings Button
    button9099=Button(menuSystem,text='Exit Settings',font=('Halvetica','12'),width=16,height=2,bg="blue2",fg="gray1",command=menuSystemExit)
    button9099.place(x=605,y=380)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- System Menu End (9)
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Credits Menu Begin (9-1)
def creditsScreen():
    def creditsScreenExit():
        creditsScreen.destroy()
    creditsScreen=Toplevel(root)
    creditsScreen.attributes('-fullscreen', True)       # Fullscreen True / False
    creditsScreen.title("!!  S O S  !!")
    creditsScreen.geometry('800x480')
    creditsScreen.configure(background="gray5")
    #------------------------------------------------------------------------------------------------------------------------------------------------------------- Page Background
    label9101=Label(creditsScreen, image=photo10001)
    label9101.place(x=0,y=0)
    #------------------------------------------------------------------------------------------------------------------------------------------------------------- All Buttons
    #
    #---------------------------------------------------------------------------------------------------- Exit Credits Button
    button9101=Button(creditsScreen,text='Exit Credits',font=('Halvetica','12'),width=16,height=2,bg="blue2",fg="gray1",command=creditsScreenExit)
    button9101.place(x=605,y=380)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Credits Menu Ends (9-1)
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- SOS Menu Begin (0-1)
def menuSOS():
    def menuSOSExit():
        menuSOS.destroy()
    menuSOS=Toplevel(root)
    menuSOS.attributes('-fullscreen', True)       # Fullscreen True / False
    menuSOS.title("App Credits")
    menuSOS.geometry('800x480')
    menuSOS.configure(background="yellow")
    #------------------------------------------------------------------------------------------------------------------------------------------------------------- Page Background
    label0101=Label(menuSOS, image=background1)
    label0101.place(x=0,y=0)
    #------------------------------------------------------------------------------------------------------------------------------------------------------------- All Buttons
    #
    #----------------------------------------------------------------------------------------------------------------------------------------- Row 1
    #
    #---------------------------------------------------------------------------------------------------- Send CW SOS Button
    button0101=Button(menuSOS,text='CW Beacon',font=('Helvetica','12'),width=18,height=2,bg="red2",fg="gray1")
    button0101.place(x=5,y=5)
    #---------------------------------------------------------------------------------------------------- Send SOS and Location Button
    button0103=Button(menuSOS,text='Location Beacon',font=('Helvetica','12'),width=18,height=2,bg="red2",fg="gray1")
    button0103.place(x=205,y=5)
    #----------------------------------------------------------------------------------------------------------------------------------------- Row 4
    #
    #---------------------------------------------------------------------------------------------------- Exit SOS Menu Button
    button0199=Button(menuSOS,text='BACK',font=('Helvetica','14'),width=16,height=2,bg="blue2",fg="gray1",command=menuSOSExit)
    button0199.place(x=605,y=380)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- SOS Menu Ends (0-1)
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Root Window Begin (0)
root=Tk()
root.attributes('-fullscreen', True)       # Fullscreen True / False
root.title("HAM Dash V1")
root.geometry('800x480')
root.configure(background="gray5")
#------------------------------------------------------------------------------------------------------------------------------------------------------------- Background Image Imports
background1=PhotoImage(file="/home/pi/Projects/HAM_Dash/Backgrounds/Background-1.png")
background9=PhotoImage(file="/home/pi/Projects/HAM_Dash/Backgrounds/Background-2.png")
photo10001=PhotoImage(file="/home/pi/Projects/HAM_Dash/Backgrounds/Background-Credits.png")
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
#---------------------------------------------------------------------------------------------------- QSL Button
button0004=Button(root,text='QSL',font=('Halvetica','12'),width=16,height=2,bg="burlywood3",fg="gray1")
button0004.place(x=605,y=5)
#----------------------------------------------------------------------------------------------------------------------------------------- Row 2
#
#---------------------------------------------------------------------------------------------------- Clock Label
clock=Label(root,font=('Halvetica','15'),width=14,height=2,bg="gray1",fg="gray99")
clock.place(x=607,y=210)
#----------------------------------------------------------------------------------------------------------------------------------------- Row 3
#
#---------------------------------------------------------------------------------------------------- DTMF Button
button0091=Button(root,text='DTMF',font=('Halvetica','12'),width=16,height=2,bg="medium violet red",fg="gray1",command=menuDTMF)
button0091.place(x=605,y=75)
#---------------------------------------------------------------------------------------------------- DTMF Button
button0091=Button(root,text='SD 511',font=('Halvetica','12'),width=16,height=2,bg="medium violet red",fg="gray1")
button0091.place(x=605,y=145)
#----------------------------------------------------------------------------------------------------------------------------------------- Row 4
#
#---------------------------------------------------------------------------------------------------- SOS Button
button0095=Button(root,text='!!  S O S  !!',font=('Halvetica','12'),width=16,height=3,bg="red",fg="gray1",command=menuSOS)
button0095.place(x=605,y=275)
#----------------------------------------------------------------------------------------------------------------------------------------- Row 5
#





#---------------------------------------------------------------------------------------------------- Radio Readout Pannel
label0001=Label(root,text=' ',width=61,height=6,bg="gray35",fg="gray1")
label0001.place(x=1,y=375)



#---------------------------------------------------------------------------------------------------- Radio Readout Pannel
label0001=Label(root,text='Radio Readings',width=60,height=1,bg="ivory3",fg="gray1")
label0001.place(x=5,y=380)




#---------------------------------------------------------------------------------------------------- Radio 1 Label
label0002=Label(root,text='VHF - 2M',width=19,height=1,bg="seashell2",fg="gray1")
label0002.place(x=10,y=406)

#---------------------------------------------------------------------------------------------------- Radio 2 Label
label0003=Label(root,text='UHF - 440',width=19,height=1,bg="seashell3",fg="gray1")
label0003.place(x=190,y=406)

#---------------------------------------------------------------------------------------------------- Radio 3 Label
label0004=Label(root,text='Citizens Band',width=19,height=1,bg="AntiqueWhite3",fg="gray1")
label0004.place(x=370,y=406)






#---------------------------------------------------------------------------------------------------- Radio 1 Reading
label0002=Label(root,text='The "895"',width=19,height=2,bg="seashell2",fg="gray1")
label0002.place(x=10,y=436)

#---------------------------------------------------------------------------------------------------- Radio 2 Reading
label0003=Label(root,text='State Link - SF',width=19,height=2,bg="seashell3",fg="gray1")
label0003.place(x=190,y=436)

#---------------------------------------------------------------------------------------------------- Radio 3 Reading
label0004=Label(root,text='Channel 19',width=19,height=2,bg="AntiqueWhite3",fg="gray1")
label0004.place(x=370,y=436)





#---------------------------------------------------------------------------------------------------- System Settings Button
button0099=Button(root,text='System Settings',font=('Halvetica','12'),width=16,height=2,bg="blue",fg="gray1",command=menuSystem)
button0099.place(x=605,y=380)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Root Main Loops
systemTime()
root.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Root Window Ends (0)
