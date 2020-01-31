#!/usr/bin/python3.7
import serial
import time
from time import gmtime, strftime
import os
from tkinter import *
import RPi.GPIO as GPIO
#####################################################
# Read Values
#####################################################
runOnce = 1
serialReadState = ''
fixReading=''
timeReading=''
latitudeReading=''
longitudeReading=''
altitudeReading=''
speedReading=''
cardinalReading=''
satConReading=''
satConCount=0
yearReturn=''
monthReturn=''
dayReturn=''
hourReturn=''
minuteReturn=''
secondReturn=''
secondFinal=''
lastSec=''
fullTime=''
#####################################################
# Error (Exception) Log File Begin
#####################################################
try:
    errorLog = open('/home/pi/Projects/SIM868/Logs/errorLog.txt','a+')
    startingString = "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # STARTING GPS LOG  "
    errorLog.write("\n\n"+str(startingString)+time.strftime('%c')+"\n\n")
    errorLog.close()
    time.sleep(0.5)
    os.system('sudo chmod 777 /home/pi/Projects/SIM868/Logs/errorLog.txt')
    print("\"Error Log\" File Permissions Set to 777")
except Exception as e:
    print(str(e))
    if (PermissionError):
        print("\"Error Log\" Permission Denied. Applying 777 and retrying.")
        try:
            os.system('sudo chmod 777 /home/pi/Projects/SIM868/Logs/errorLog.txt')
            time.sleep(0.5)
            errorLog = open('/home/pi/Projects/SIM868/Logs/errorLog.txt','a+')
            startingString = "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # STARTING GPS LOG  "
            errorLog.write("\n\n"+str(startingString)+time.strftime('%c')+"\n\n")
            errorLog.close()
        except Exception as e:
            print("Failed to write permissions to \"Error Log\". Does the Log dir exist?")
            print(str(e))
            time.sleep(5.0)
            exit()
    else:
        print("Looks like something else broke. Please debig in console.")
        print(str(e))
#####################################################
# GPS Log File Begin
#####################################################
try:
    gpsLog = open('/home/pi/Projects/SIM868/Logs/gpsLog.txt','a+')
    startingString = "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # STARTING GPS LOG  "
    gpsLog.write("\n\n"+str(startingString)+time.strftime('%c')+"\n\n")
    gpsLog.close()
    time.sleep(0.5)
    os.system('sudo chmod 777 /home/pi/Projects/SIM868/Logs/gpsLog.txt')
    print("\"GPS Log\"   File Permissions Set to 777")
except Exception as e:
    print(str(e))
    if (PermissionError):
        print("\"GPS Log\"   Permission Denied. Applying 777 and retrying.")
        try:
            os.system('sudo chmod 777 /home/pi/Projects/SIM868/Logs/gpsLog.txt')
            time.sleep(0.5)
            gpsLog = open('/home/pi/Projects/SIM868/Logs/gpsLog.txt','a+')
            startingString = "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # STARTING GPS LOG  "
            gpsLog.write("\n\n"+str(startingString)+time.strftime('%c')+"\n\n")
            gpsLog.close()
        except Exception as e:
            print("Failed to write permissions to \"GPS Log\". Does the Log dir exist?")
            print(str(e))
            time.sleep(5.0)
            exit()
    else:
        print("Looks like something else broke. Please debig in console.")
        print(Exception)
#####################################################
# Root TK Attributes
#####################################################
rootTitle="SIM868"
rootGeom="400x300+50+150"
rootFS=False
rootBackground="gray20"
#####################################################
# Serial Attributes
#####################################################
ser=serial.Serial('/dev/ttyS0',115200,timeout=0.2)
#####################################################
# GPIO Attributes
#####################################################
gsmPWR=4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(gsmPWR,GPIO.OUT)
GPIO.output(gsmPWR,GPIO.LOW)
time.sleep(2.0)
GPIO.output(gsmPWR,GPIO.HIGH)
time.sleep(2.0)
####################################################
# Program Exit
#####################################################
def programExit():
    clearDisplays()
    stopGPS()
    gpsLog.close()
    errorLog.close()
    programKill()
    return
#####################################################
# Program Kill
#####################################################
def programKill():
    GPIO.output(gsmPWR,GPIO.LOW)
    time.sleep(2.0)
    GPIO.output(gsmPWR,GPIO.HIGH)
    time.sleep(2.0)
    root.destroy()
    exit()
    return
#####################################################
# Clear Displays
#####################################################
def clearDisplays():
    fixDisplay.configure(text="Status:  DISCONNECTED",bg="red",fg="gray1")
    timeDisplay.configure(text="Zulu Time:  N/A",bg="gray30",fg="gray1")
    latitudeDisplay.configure(text="Latitude:  N/A",bg="gray30",fg="gray1")
    longitudeDisplay.configure(text="Longitude:  N/A",bg="gray30",fg="gray1")
    altitudeDisplay.configure(text="Altitude:  N/A",bg="gray30",fg="gray1")
    speedDisplay.configure(text="Speed:  N/A",bg="gray30",fg="gray1")
    cardinalDisplay.configure(text="Cardinal:  N/A",bg="gray30",fg="gray1")
    satConDisplay.configure(text="Sats:  N/A",bg="gray30",fg="gray1")
    return
#####################################################
# Set Displays
#####################################################
def setDisplays():
    global serialPrefix
    global serialCommand
    global serialSuffix
    global fixReading
    global timeReading
    global latitudeReading
    global longitudeReading
    global altitudeReading
    global speedReading
    global cardinalReading
    global satConReading
    global satConCount
    global fullTime
    if (str(fixReading) == "1"):
        fixDisplay.configure(text="Status:         CONNECTED",bg="green2",fg="gray1")
    timeDisplay.configure(text="MST Time:  "+str(fullTime),bg="RoyalBlue2",fg="gray1")
    latitudeDisplay.configure(text="Latitude:  "+str(latitudeReading),bg="orange3",fg="gray1")
    longitudeDisplay.configure(text="Longitude:  "+str(longitudeReading),bg="orange3",fg="gray1")
    altitudeDisplay.configure(text="Altitude:  "+str(altitudeReading),bg="LightGoldenrod2",fg="gray1")
    speedDisplay.configure(text="KPH Speed:  "+str(speedReading),bg="LightGoldenrod2",fg="gray1")
    cardinalDisplay.configure(text="Cardinal:  "+str(cardinalReading),bg="MediumOrchid2",fg="gray1")
    #print(satConReading)
    if (satConReading == "0"):
        satConCount = 0
    if (satConReading == "1"):
        satConCount = 1
    if (satConReading == "2"):
        satConCount = 2
    if (satConReading == "3"):
        satConCount = 3
    if (satConReading == "4"):
        satConCount = 4
    if (satConReading == "5"):
        satConCount = 5
    if (satConReading == "6"):
        satConCount = 6
    if (satConReading == "7"):
        satConCount = 7
    if (satConReading == "8"):
        satConCount = 8
    if (satConReading == "9"):
        satConCount = 9
    if (satConReading == "10"):
        satConCount = 10
    if (satConReading == "11"):
        satConCount = 11
    if (satConReading == "12"):
        satConCount = 12
    if (satConReading == "13"):
        satConCount = 13
    if (satConReading == "14"):
        satConCount = 14
    if (satConReading == "15"):
        satConCount = 15
    if (satConReading == "16"):
        satConCount = 16
    if (satConReading == "17"):
        satConCount = 17
    if (satConReading == "18"):
        satConCount = 18
    if (satConReading == "19"):
        satConCount = 19
    if (satConReading == "20"):
        satConCount = 20
    #####################################################
    if (satConCount <= 8):
        satConDisplay.configure(text="Sats:  "+str(satConReading),bg="red2",fg="gray1")
    elif (satConCount >= 9 and satConCount <= 12):
        satConDisplay.configure(text="Sats:  "+str(satConReading),bg="DarkOrange1",fg="gray1")
    elif (satConCount >= 13 and satConCount <= 15):
        satConDisplay.configure(text="Sats:  "+str(satConReading),bg="yellow3",fg="gray1")
    elif (satConCount <= 16):
        satConDisplay.configure(text="Sats:  "+str(satConReading),bg="green3",fg="gray1")
    #print(type(satConCount))
    #print(satConCount)
    fixDisplay.after(50, serialConnect)
    return
#####################################################
# Start GPS
#####################################################
def startGPS():
    global serialReadState
    serialReadState = 1
    ser.write(bytes("AT+CGNSPWR=1\r", 'utf-8'))
    time.sleep(1.0)
    ser.write(bytes("AT+CGNSPWR?\r", 'utf-8'))
    dataResponse = ser.read(1024)
    print(str(dataResponse))
    time.sleep(0.5)
    serialConnect()
    return
#####################################################
# Stop GPS
#####################################################
def stopGPS():
    global serialReadState
    serialReadState = 0
    ser.write(bytes("AT+CGNSPWR=0\r", 'utf-8'))
    time.sleep(1.0)
    ser.write(bytes("AT+CGNSPWR?\r", 'utf-8'))
    dataResponse = ser.read(1024)
    print(str(dataResponse))
    time.sleep(0.5)
    clearDisplays()
    return
#####################################################
# GPS Control
#####################################################
def gpsControl():
    global serialReadState
    if (serialReadState == 0):
        gpsControlButton.configure(text="GPS Off",bg="green",fg="gray1")
        startGPS()
    elif (serialReadState == 1):
        gpsControlButton.configure(text="GPS  On",bg="red",fg="gray1")
        stopGPS()
    return
#####################################################
# Physical Power Cycle
#####################################################
def powerCycle868():
    global serialReadState
    stopGPS()
    time.sleep(1.0)
    GPIO.output(gsmPWR,GPIO.LOW)
    print("BTN PR")
    time.sleep(2.0)
    GPIO.output(gsmPWR,GPIO.HIGH)
    print("BTN DPR")
    time.sleep(4.0)
    GPIO.output(gsmPWR,GPIO.LOW)
    print("BTN PR")
    time.sleep(2.0)
    GPIO.output(gsmPWR,GPIO.HIGH)
    print("BTN DPR")
    time.sleep(4.0)
    gpsControlButton.configure(text="GPS  On",bg="red",fg="gray1")
    serialConnect()
    return
#####################################################
# Serial Connect
#####################################################
def serialConnect():
    global runOnce
    global serialReadState
    global fixReading
    global timeReading
    global latitudeReading
    global longitudeReading
    global altitudeReading
    global speedReading
    global cardinalReading
    global satConReading
    global lastSec
    global fullTime
    if (serialReadState == 1):
        sendData = bytes("AT+CGNSINF\r", 'utf-8')
        ser.write(sendData)
        #time.sleep(0.1)
        serResponse = ser.read(1024)
        dataReturn =str(serResponse).split(',')
        #print(str(serResponse))
        fixReading=str(dataReturn[1])
        timeReading=str(dataReturn[2])
        latitudeReading=dataReturn[3]
        longitudeReading=dataReturn[4]
        altitudeReading=dataReturn[5]
        speedReading=dataReturn[6]
        cardinalReading=dataReturn[7]
        satConReading=dataReturn[14]
        #print(str(dataReturn))
        #print("Time Reading: "+str(timeReading))
        try:
            math = (list(timeReading)) # This turns it into a list and sorts it.
            yearTick = [math[shit] for shit in [0,1,2,3]]
            monthTick = [math[shit] for shit in (4,5)]
            dayTick = [math[shit] for shit in (6,7)]
            hourTick = [math[shit] for shit in (8,9)]
            minuteTick = [math[shit] for shit in (10,11)]
            secondTick = [math[shit] for shit in (12,13)]
            millisecondTick = [math[shit] for shit in (15,16,17)]
            yearFinal = ("".join(yearTick))
            monthFinal = ("".join(monthTick))
            dayFinal = ("".join(dayTick))
            hourFinal = ("".join(hourTick))
            if (hourFinal == "00"):
                hourFinal = "17"
            elif (hourFinal == "01"):
                hourFinal = "18"
            elif (hourFinal == "02"):
                hourFinal = "19"
            elif (hourFinal == "03"):
                hourFinal = "20"
            elif (hourFinal == "04"):
                hourFinal = "21"
            elif (hourFinal == "05"):
                hourFinal = "22"
            elif (hourFinal == "06"):
                hourFinal = "23"
            elif (hourFinal == "07"):
                hourFinal = "00"
            elif (hourFinal == "08"):
                hourFinal = "01"
            elif (hourFinal == "09"):
                hourFinal = "02"
            elif (hourFinal == "10"):
                hourFinal = "03"
            elif (hourFinal == "11"):
                hourFinal = "04"
            elif (hourFinal == "12"):
                hourFinal = "05"
            elif (hourFinal == "13"):
                hourFinal = "06"
            elif (hourFinal == "14"):
                hourFinal = "07"
            elif (hourFinal == "15"):
                hourFinal = "08"
            elif (hourFinal == "16"):
                hourFinal = "09"
            elif (hourFinal == "17"):
                hourFinal = "10"
            elif (hourFinal == "18"):
                hourFinal = "11"
            elif (hourFinal == "19"):
                hourFinal = "12"
            elif (hourFinal == "20"):
                hourFinal = "13"
            elif (hourFinal == "21"):
                hourFinal = "14"
            elif (hourFinal == "22"):
                hourFinal = "15"                
            elif (hourFinal == "23"):
                hourFinal = "16"
            minuteFinal = ("".join(minuteTick))
            secondFinal = ("".join(secondTick))
            millisecondFinal = ("".join(millisecondTick))
            fullTime = (str(hourFinal)+":"+str(minuteFinal)+":"+str(secondFinal)+"  "+str(monthFinal)+"/"+str(dayFinal)+"/"+str(yearFinal))
            if (str(lastSec) != str(secondFinal)):
                gpsLog = open('/home/pi/Projects/SIM868/Logs/gpsLog.txt','a+')
                gpsLog.write("Fix: "+str(fixReading)+"  Latitude: "+str(latitudeReading)+"  Longitude: "+str(longitudeReading)+"  Altitude: "+str(altitudeReading)+"  Speed: "+str(speedReading)+"  Cardinal: "+str(cardinalReading)+"  Sats: "+str(satConReading)+"  Zulu Time: "+str(fullTime)+"\n")
                gpsLog.close()
                lastSec = str(secondFinal)
            #print("Full Time: "+str(fullTime))
        except Exception as e:
            errorLog = open('/home/pi/Projects/SIM868/Logs/errorLog.txt','a+')
            errorLog.write(str(e)+time.strftime('  %c')+"\n")
            errorLog.close()
            print(str(e))
        
        setDisplays()
    if (serialReadState == 0):
        print("Read Mode Disabled.")
    return
#####################################################
# TK Root Main Screen
#####################################################
root=Tk()
root.title(rootTitle)
root.geometry(rootGeom)
root.attributes('-fullscreen', rootFS)
root.configure(background=rootBackground)
#####################################################
# Control Buttons
#####################################################
##################################################### Exit Button
exitButton=Button(root,
                  text="EXIT",font=("Helvetica","12"),
                  bd=2,width=10,height=1,
                  bg="red",fg="gray1",
                  command=programExit)
exitButton.place(x=275,y=255)
##################################################### Physical Power Button
powerButton=Button(root,
                  text="PWR",font=("Helvetica","12"),
                  bd=2,width=10,height=1,
                  bg="brown3",fg="gray1",
                  command=powerCycle868)
powerButton.place(x=140,y=255)

##################################################### GPS Enable / Disable Button
gpsControlButton=Button(root,
                  font=("Helvetica","12"),
                  bd=2,width=10,height=1,
                  command=gpsControl)
gpsControlButton.place(x=5,y=255)
#####################################################
# GPS Info Display
#####################################################
##################################################### GPS Fix Display
fixDisplay=Label(root,
                  font=("Helvetica","12"),
                  bd=2,width=42,height=1)
fixDisplay.place(x=5,y=5)
fixDisplay.after(100, serialConnect)
##################################################### GPS MST (Local) Time Display
timeDisplay=Label(root,
                  font=("Helvetica","12"),
                  bd=2,width=42,height=1)
timeDisplay.place(x=5,y=35)
##################################################### Latitude Display
latitudeDisplay=Label(root,
                  font=("Helvetica","12"),
                  bd=2,width=42,height=1)
latitudeDisplay.place(x=5,y=65)
##################################################### Longitude Display
longitudeDisplay=Label(root,
                  font=("Helvetica","12"),
                  bd=2,width=42,height=1)
longitudeDisplay.place(x=5,y=95)
##################################################### Altitude Display
altitudeDisplay=Label(root,
                  font=("Helvetica","12"),
                  bd=2,width=42,height=1)
altitudeDisplay.place(x=5,y=125)
##################################################### Speed Display
speedDisplay=Label(root,
                  font=("Helvetica","12"),
                  bd=2,width=42,height=1)
speedDisplay.place(x=5,y=155)
##################################################### Cardinal Direction Display
cardinalDisplay=Label(root,
                  font=("Helvetica","12"),
                  bd=2,width=42,height=1)
cardinalDisplay.place(x=5,y=185)
##################################################### Satellite Connections Display
satConDisplay=Label(root,
                  font=("Helvetica","12"),
                  bd=2,width=42,height=1)
satConDisplay.place(x=5,y=215)
##################################################### Run Once
if (runOnce == 1):
    clearDisplays()
    gpsControlButton.configure(text="GPS  On",
                               bg="red",fg="gray1")
    serialReadState = 0
    runOnce = 0
##################################################### Main loops
root.mainloop()
