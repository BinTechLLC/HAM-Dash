#!/usr/bin/python3.7
import serial
import time
from time import strftime, gmtime
import os
from tkinter import *
import RPi.GPIO as GPIO
########################################################################################################
# Input Values
########################################################################################################
runOnce=True
printMainString = False
gpsPrintEnabled=False
gpsLogEnabled=True
tempC=''
tempF=''
serialReadState=0
timeState=0
timeReading=0
yearReading=0
monthReading=0
dayReading=0
dateReturn=''
hourReading=0
minuteReading=0
secondReading=0
timeReturn=''
lastSecA=0
lastSecB=0
fixReading=0.0
hdopReading=0.0
pdopReading=0.0
vdopReading=0.0
latitudeReading=0.0
longitudeReading=0.0
altitudeReading=0.0
speedReading=0.0
cardinalReading=0.0
satSeenReading=0.0
satUsedReading=0.0
hectopascalReading=0.0
########################################################################################################
# Log files and permissions
########################################################################################################
try:
    errorLog=open('/home/pi/Projects/SIM868/Logs/errorLog.txt','a+')
    gpsLog=open('/home/pi/Projects/SIM868/Logs/gpsLog.txt','a+')
    googlePlot=open('/home/pi/Projects/SIM868/Logs/googlePlot.txt','a+')
    manualPlot=open('/home/pi/Projects/SIM868/Logs/manualPlot.txt','a+')
    tempLog=open('/home/pi/Projects/SIM868/Logs/tempLog.txt','a+')
    
    errorLog.write("\n\n"+"  STARTING # # # # # # # # # # # # # # # # # # # # "+time.strftime('  %c')+"\n\n")
    gpsLog.write("\n\n"+"  STARTING # # # # # # # # # # # # # # # # # # # # "+time.strftime('  %c')+"\n\n")
    googlePlot.write("\n\n"+"  STARTING # # # # # # # # # # # # # # # # # # # # "+time.strftime('  %c')+"\n\n")
    manualPlot.write("\n\n"+"  STARTING # # # # # # # # # # # # # # # # # # # # "+time.strftime('  %c')+"\n\n")
    tempLog.write("\n\n"+"  STARTING # # # # # # # # # # # # # # # # # # # # "+time.strftime('  %c')+"\n\n")
    
    errorLog.close()
    gpsLog.close()
    googlePlot.close()
    manualPlot.close()
    tempLog.close()
except Exception as e:
    print("Error creating log files, trying as permission 777. Error: "+str(e))
    os.system('sudo chmod 777 /home/pi/Projects/SIM868/Logs/errorLog.txt')
    os.system('sudo chmod 777 /home/pi/Projects/SIM868/Logs/gpsLog.txt')
    os.system('sudo chmod 777 /home/pi/Projects/SIM868/Logs/googlePlot.txt')
    os.system('sudo chmod 777 /home/pi/Projects/SIM868/Logs/manualPlot.txt')
    os.system('sudo chmod 777 /home/pi/Projects/SIM868/Logs/tempLog.txt')
    try:
        errorLog=open('/home/pi/Projects/SIM868/Logs/errorLog.txt','a+')
        gpsLog=open('/home/pi/Projects/SIM868/Logs/gpsLog.txt','a+')
        googlePlot=open('/home/pi/Projects/SIM868/Logs/googlePlot.txt','a+')
        googlePlot=open('/home/pi/Projects/SIM868/Logs/manualPlot.txt','a+')
        tempLog=open('/home/pi/Projects/SIM868/Logs/tempLog.txt','a+')
        errorLog.write("\n\n"+"STARTING # # # # # # # # # # # # # # # # # # # # "+time.strftime('  %c')+"\n\n")
        gpsLog.write("\n\n"+"STARTING # # # # # # # # # # # # # # # # # # # # "+time.strftime('  %c')+"\n\n")
        googlePlot.write("\n\n"+"  STARTING # # # # # # # # # # # # # # # # # # # # "+time.strftime('  %c')+"\n\n")
        manualPlot.write("\n\n"+"  STARTING # # # # # # # # # # # # # # # # # # # # "+time.strftime('  %c')+"\n\n")
        tempLog.write("\n\n"+"STARTING # # # # # # # # # # # # # # # # # # # # "+time.strftime('  %c')+"\n\n")
        errorLog.close()
        gpsLog.close()
        googlePlot.close()
        manualPlot.close()
        tempLog.close()
    except Exception as e:
        print("Error creating log files. Error: "+str(e))
        time.sleep(3.0)
        exit()
########################################################################################################
# Root TK Attributes
########################################################################################################
rootTitle="SIM868 MK-II"
rootGeom="800x480+25+150" # Normal is "800x480+25+150"
rootFS=False
rootBackground="gray20"
########################################################################################################
# Serial Attributes
########################################################################################################
ser=serial.Serial('/dev/ttyS0',115200,timeout=0.1)
########################################################################################################
# GPIO Attributes
########################################################################################################
gsmPWR=4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(gsmPWR,GPIO.OUT)
GPIO.output(gsmPWR,GPIO.HIGH)
time.sleep(2.0)
######################################################
# Turn on GPS Chip
######################################################
GPIO.output(gsmPWR,GPIO.LOW)
time.sleep(2.0)
GPIO.output(gsmPWR,GPIO.HIGH)
time.sleep(2.0)
########################################################################################################
# CPU Temp Read
########################################################################################################
def cpuTemp():
    global tempC
    global tempF
    global secondReading
    global lastSecA
    tempLog=open('/home/pi/Projects/SIM868/Logs/tempLog.txt','a+')
    tFile = open('/sys/class/thermal/thermal_zone0/temp')
    temp = float(tFile.read())
    tempC = temp/1024
    tempC = "%.2f" % tempC
    tempF = float(tempC) # Do math line by line for accuracy, let it take up the memory.
    tempF = tempF*9
    tempF = tempF/5
    tempF = tempF+32
    tempF = "%.2f" % tempF
    #print("Temp C: "+str(tempC)+" - Temp F: "+str(tempF)+time.strftime(' -  %c'))
    tempLabel.configure(text="CPU: "+str(tempC)+" °C"+"  /  "+str(tempF)+" °F") # ,anchor="w" or "e"
    if (lastSecA != secondReading):
        #print("Last Sec A Changed: "+str(secondReading))
        lastSecA = secondReading
        tempLog=open('/home/pi/Projects/SIM868/Logs/tempLog.txt','a+')
        tempData = ("Temp C: "+str(tempC)+" - Temp F: "+str(tempF)+time.strftime(' -  %c')+"\n")
        tempLog.write(tempData)
        tempLog.close()
    tempLabel.after(100,cpuTemp)
    return
########################################################################################################
# Program Exit
########################################################################################################
def programExit():
    errorLog.close()
    gpsLog.close()
    googlePlot.close()
    manualPlot.close()
    tempLog.close()
    sendData = bytes("AT+CGNSPWR=0\r", 'utf-8')
    ser.write(sendData)
    time.sleep(2.0)
    GPIO.output(gsmPWR,GPIO.LOW)
    time.sleep(2.0)
    GPIO.output(gsmPWR,GPIO.HIGH)
    time.sleep(2.0)
    killPython()
    return
########################################################################################################
# Kill Python
########################################################################################################
def killPython():
    try:
        root.destroy()
    except Exception as e:
         print(str(e))
    exit()
    return

def resetSerial():
    ser=serial.Serial('/dev/ttyS0',115200,timeout=0.1)
    time.sleep(1.0)
    sendData = bytes("AT+CGNSPWR=1\r", 'utf-8')
    ser.write(sendData)
    serResponse = ser.read(1024)
    serialReadState = 1
    time.sleep(3.0)
    return
########################################################################################################
# Force GPS Power
########################################################################################################
def gpsPowerForce():
    serialReadState = 0
    sendData = bytes("AT+CGNSPWR=0\r", 'utf-8')
    ser.write(sendData)
    serResponse = ser.read(1024)
    print(serResponse)
    GPIO.output(gsmPWR,GPIO.LOW)
    time.sleep(4.0)
    GPIO.output(gsmPWR,GPIO.HIGH)
    time.sleep(4.0)
    resetSerial()
    return
########################################################################################################
# GPS Power Cycle
########################################################################################################
def gpsPowerCycle():
    serialReadState = 0
    sendData = bytes("AT+CGNSPWR=0\r", 'utf-8')
    ser.write(sendData)
    serResponse = ser.read(1024)
    GPIO.output(gsmPWR,GPIO.LOW)
    time.sleep(4.0)
    GPIO.output(gsmPWR,GPIO.HIGH)
    time.sleep(4.0)
    GPIO.output(gsmPWR,GPIO.LOW)
    time.sleep(4.0)
    GPIO.output(gsmPWR,GPIO.HIGH)
    time.sleep(6.0)
    resetSerial()
    return
########################################################################################################
# GPS Control
########################################################################################################
def gpsControl():
    global serialReadState
    if (serialReadState == 0):
        serialReadState = 1
        dataResponse = ser.read(1024)
        print(str(dataResponse))
    elif (serialReadState == 1):
        serialReadState = 0
        dataResponse = ser.read(1024)
        print(str(dataResponse))
    return
########################################################################################################
# Manual GPS Plot
########################################################################################################
def manualPlotFunction():
    global latitudeReading
    global longitudeReading
    manualPlotButon.configure(bg="yellow",activebackground="yellow")
    root.update()
    time.sleep(0.5)
    manualPlot=open('/home/pi/Projects/SIM868/Logs/manualPlot.txt','a+')
    manualPlot.write(str(latitudeReading)+", "+str(longitudeReading)+"\n")
    manualPlot.close()
    manualPlotButon.configure(bg="green4",activebackground="green2")
    root.update()
########################################################################################################
# Clock Control
########################################################################################################
def clockControl():
    global timeState
    if (timeState == 0):
        timeState = 1
        #print(timeState)
    elif (timeState == 1):
        timeState = 0
        #print(timeState)
    return
########################################################################################################
# Read Serial
########################################################################################################
def readSerial():
    global serialReadState
    global fixReading
    global hdopReading
    global pdopReading
    global vdopReading
    global timeReading
    global yearReading
    global monthReading
    global dayReading
    global dateReturn
    global hourReading
    global minuteReading
    global secondReading
    global timeReturn
    global lastSecB
    global latitudeReading
    global longitudeReading
    global altitudeReading
    global speedReading
    global cardinalReading
    global satSeenReading
    global satUsedReading
    global hectopascalReading
        
    if (serialReadState == 0):
        print("Serial Read Disabled")
        
    if (serialReadState == 1):
        #print("Serial Read Enabled")
        try:
            sendData = bytes("AT+CGNSINF\r", 'utf-8')
            ser.write(sendData)
            serResponse = ser.read(1024)
            if (printMainString == True):
                print(serResponse)
            time.sleep(0.1)
            byteReading = str(serResponse).split(',')
            fixReading = bytes(byteReading[1],'utf-8')
            fixReading = fixReading.decode('utf-8')
            fixReading = int(fixReading)
            timeReading = bytes(byteReading[2],'utf-8')
            timeReading = timeReading.decode('utf-8')
            seperate = (list(timeReading))
            yearReading = [seperate[i] for i in [0,1,2,3]]
            yearReading = ("".join(yearReading))
            yearReading = int(yearReading)
            monthReading = [seperate[i] for i in [4,5]]
            monthReading = ("".join(monthReading))
            monthReading = int(monthReading)
            dayReading = [seperate[i] for i in [6,7]]
            dayReading = ("".join(dayReading))
            dayReading = int(dayReading)
            if (dayReading <= 9):
                dayString = ("0"+str(dayReading))
                dayReading = int(dayString)
            if (dayReading >= 10):
                dayString = (dayReading)
                dayReading = int(dayString)
            if (monthReading <= 9):
                monthString = ("0"+str(monthReading))
                monthReading = int(monthString)
            if (monthReading >= 10):
                monthString = (monthReading)
                monthReading = int(monthString)
            dateReturn = (str(monthString)+"/"+str(dayString)+"/"+str(yearReading))
            hourReading = [seperate[i] for i in [8,9]]
            hourReading = ("".join(hourReading))
            hourReading = int(hourReading)
            minuteReading = [seperate[i] for i in [10,11]]
            minuteReading = ("".join(minuteReading))
            minuteReading = int(minuteReading)
            secondReading = [seperate[i] for i in [12,13]]
            secondReading = ("".join(secondReading))
            secondReading = int(secondReading)
            if (hourReading <= 9):
                hourString = ("0"+str(hourReading))
                hourReading = int(hourString) 
            if (hourReading >= 10):
                hourString = (hourReading)
                hourReading = int(hourString)
            if (minuteReading <= 9):
                minuteString = ("0"+str(minuteReading))
                minuteReading = int(minuteString)
            if (minuteReading >= 10):
                minuteString = (minuteReading)
                minuteReading = int(minuteString)
            if (secondReading <= 9):
                secondString = ("0"+str(secondReading))
                secondReading = int(secondString)
            if (secondReading >= 10):
                secondString = (secondReading)
                secondReading = int(secondString)
            timeReturn = (str(hourString)+":"+str(minuteString)+":"+str(secondString))
        except Exception as e:
            print(str(e))
        try:
            latitudeReading = bytes(byteReading[3],'utf-8')
            latitudeReading = float(latitudeReading.decode('utf-8'))
            #latitudeReading = float(latitudeReading)
        except Exception as e:
            print("LAT EXC: "+str(e))
        try:
            longitudeReading = bytes(byteReading[4],'utf-8')
            longitudeReading = float(longitudeReading.decode('utf-8'))
            #longitudeReading = float(longitudeReading)
        except Exception as e:
            print("LOT EXC: "+str(e))
        try:
            altitudeReading = bytes(byteReading[5],'utf-8')
            altitudeReading = float(altitudeReading.decode('utf-8'))
            altitudeReading = "%.2f" % altitudeReading
            altitudeReading = float(altitudeReading)
        except Exception as e:
            print("ALT EXC: "+str(e))
        try:
            speedReading = bytes(byteReading[6],'utf-8')
            speedReading = float(speedReading.decode('utf-8'))
            #speedReading = float(speedReading)
            speedReading = speedReading  * 0.6213711922
            speedReading = "%.2f" % speedReading
            speedReading = float(speedReading)
        except Exception as e:
            print("SP EXC: "+str(e))
        try:
            cardinalReading = bytes(byteReading[7],'utf-8')
            cardinalReading = cardinalReading.decode('utf-8')
            cardinalReading = float(cardinalReading)
            cardinalReading = "%.2f" % cardinalReading
            cardinalReading = float(cardinalReading)
        except Exception as e:
            print("CD EXC: "+str(e))
        try:
            hdopReading = bytes(byteReading[10],'utf-8')
            hdopReading = hdopReading.decode('utf-8')
            hdopReading = float(hdopReading)
        except Exception as e:
            print("HDOP EXC: "+str(e))
        try:
            pdopReading = bytes(byteReading[11],'utf-8')
            pdopReading = pdopReading.decode('utf-8')
            pdopReading = float(pdopReading)
        except Exception as e:
            print("PDOP EXC: "+str(e))
        try:
            vdopReading = bytes(byteReading[12],'utf-8')
            vdopReading = vdopReading.decode('utf-8')
            vdopReading = float(vdopReading)
        except Exception as e:
            print("VDOP EXC: "+str(e))
        try:
            satSeenReading = bytes(byteReading[14],'utf-8')
            satSeenReading = satSeenReading.decode('utf-8')
            satSeenReading = int(satSeenReading)
        except Exception as e:
            print("SS EXC: "+str(e))
        try:
            satUsedReading = bytes(byteReading[15],'utf-8')
            satUsedReading = satUsedReading.decode('utf-8')
            satUsedReading = int(satUsedReading)
        except Exception as e:
            print("SU EXC: "+str(e))
        try:
            hectopascalReading = bytes(byteReading[18],'utf-8')
            hectopascalReading = hectopascalReading.decode('utf-8')
            hectopascalReading = int(hectopascalReading)
        except Exception as e:
            print("PAS EXC: "+str(e))
        if (gpsPrintEnabled == True):
            #print("###################################################################################################################################")
            #print("Time: H: "+str(type(hourReading))+" M: "+str(type(minuteReading))+" S: "+str(type(secondReading)))
            #print("Date: M: "+str(type(monthReading))+" D: "+str(type(dayReading))+" Y: "+str(type(yearReading)))
            #print("GPS1: FIX: "+str(type(fixReading))+" LAT: "+str(type(latitudeReading))+" LON: "+str(type(longitudeReading)))
            #print("GPS2: DIR: "+str(type(cardinalReading))+" MPH: "+str(type(speedReading))+" ALT: "+str(type(altitudeReading)))
            #print("GPS3: SEEN: "+str(type(satSeenReading))+" USED: "+str(type(satUsedReading)))
            print("###################################################################################################################################")
            print("Time: "+str(timeReturn)+"  "+str(dateReturn))
            print("Fix: "+str(fixReading)+"  DIR: "+str(cardinalReading))
            print("Lat: "+str(latitudeReading)+"  Lon: "+str(longitudeReading))
            print("MPH: "+str(speedReading)+"  Alt: "+str(altitudeReading))
            print("SEEN: "+str(satSeenReading)+"  USED: "+str(satUsedReading))
            print("HDOP: "+str(hdopReading)+"  PDOP: "+str(pdopReading)+"  VDOP: "+str(vdopReading))
            print("Hectopascal: "+str(hectopascalReading))
            print("###################################################################################################################################")
        if (gpsLogEnabled == True):
            if (lastSecB != secondReading):
                #print("Last Sec B Changed: "+str(secondReading))
                lastSecB = secondReading
                gpsLog = open('/home/pi/Projects/SIM868/Logs/gpsLog.txt','a+')
                googlePlot = open('/home/pi/Projects/SIM868/Logs/googlePlot.txt','a+')
                gpsDataString1 = ("######################################################### "+time.strftime('%H:%M:%S')+time.strftime('   %m/%d/%Y')+"\n")
                gpsDataString2 = ("Time: "+str(dateReturn)+"  "+str(timeReturn)+"\n")
                gpsDataString3 = ("Fix: "+str(fixReading)+"  DIR: "+str(cardinalReading)+"\n")
                gpsDataString4 = ("Lat: "+str(latitudeReading)+"  Lon: "+str(longitudeReading)+"\n")
                gpsDataString5 = ("MPH: "+str(speedReading)+"  Alt: "+str(altitudeReading)+"\n")
                gpsDataString6 = ("SEEN: "+str(satSeenReading)+"  USED: "+str(satUsedReading)+"\n")
                gpsDataString7 = ("HDOP: "+str(hdopReading)+"  PDOP: "+str(pdopReading)+"  VDOP: "+str(vdopReading)+"\n")
                gpsDataString8 = ("Hectopascal: "+str(hectopascalReading)+"\n")
                gpsLog.write(gpsDataString1)
                gpsLog.write(gpsDataString2)
                gpsLog.write(gpsDataString3)
                gpsLog.write(gpsDataString4)
                gpsLog.write(gpsDataString5)
                gpsLog.write(gpsDataString6)
                gpsLog.write(gpsDataString7)
                gpsLog.write(gpsDataString8)
                if (str(latitudeReading) != "b''" and str(longitudeReading) != "b''"):
                    googlePlot.write(str(latitudeReading)+", "+str(longitudeReading)+"\n")
                gpsLog.close()
                googlePlot.close()
    exitButton.after(100,readSerial)
    return
########################################################################################################
# Live Display
########################################################################################################
def displayUpdates():
    global serialReadState
    global clockState
    global fixReading
    global hdopReading
    global pdopReading
    global vdopReading
    global timeReading
    global yearReading
    global monthReading
    global dayReading
    global dateReturn
    global hourReading
    global minuteReading
    global secondReading
    global timeReturn
    global lastSec
    global latitudeReading
    global longitudeReading
    global altitudeReading
    global speedReading
    global cardinalReading
    global satSeenReading
    global satUsedReading
    global hectopascalReading
    if (timeState == 0):
        timeDateLabel.configure(text=("Z: "+str(timeReturn)+"   "+str(dateReturn)))
    elif (timeState == 1):
        timeDateLabel.configure(text=("L: "+time.strftime('%H:%M:%S'))+time.strftime('   %m/%d/%Y'))
    timeDateLabel.after(100, displayUpdates)
    
    if (fixReading == 0):
        #print("State 0: "+str(fixReading))
        fixLabel.configure(text="DISCONNECTED",bg="red",fg="gray99",activebackground="red",activeforeground="gray99")
        cardinalLabel.configure(text=("Heading: "+str(cardinalReading)),bg="gray35",fg="gray99",activebackground="gray35",activeforeground="gray99")
        latitudeLabel.configure(text=("Latitude: "),bg="gray35",fg="gray99",activebackground="gray35",activeforeground="gray99")
        longitudeLabel.configure(text=("Longitude: "),bg="gray35",fg="gray99",activebackground="gray35",activeforeground="gray99")
        speedLabel.configure(text=("MPH: "+str(speedReading)),bg="gray35",fg="gray99",activebackground="gray35",activeforeground="gray99")
        satSeenLabel.configure(text=("GPS In View: "+str(satSeenReading)),bg="gray35",fg="gray99",activebackground="gray35",activeforeground="gray99")
        satUsedLabel.configure(text=("GNSS In Use: "+str(satUsedReading)),bg="gray35",fg="gray99",activebackground="gray35",activeforeground="gray99")
        altitudeLabel.configure(text=("Altitude: "),bg="gray35",fg="gray99",activebackground="gray35",activeforeground="gray99")
        
        hdopLabel.configure(text=("H DOP: "+str(hdopReading)),bg="gray35",fg="gray99",activebackground="gray35",activeforeground="gray99")
        pdopLabel.configure(text=("P DOP: "+str(pdopReading)),bg="gray35",fg="gray99",activebackground="gray35",activeforeground="gray99")
        vdopLabel.configure(text=("V DOP: "+str(vdopReading)),bg="gray35",fg="gray99",activebackground="gray35",activeforeground="gray99")
        
        hectopascalLabel.configure(text=("hPa: "+str(hectopascalReading)),bg="gray35",fg="gray99",activebackground="gray35",activeforeground="gray99")
        
        
        
    elif (fixReading == 1):
        #print("State 1: "+str(fixReading))
        fixLabel.configure(text="   CONNECTED",bg="green3",fg="gray99",activebackground="green3",activeforeground="gray99")
        cardinalLabel.configure(text=("Heading: "+str(cardinalReading)),bg="DeepSkyBlue3",fg="gray99",activebackground="DeepSkyBlue3",activeforeground="gray99")
        latitudeLabel.configure(text=("Latitude: "+str(latitudeReading)),bg="coral2",fg="gray99",activebackground="coral2",activeforeground="gray99")
        longitudeLabel.configure(text=("Longitude: "+str(longitudeReading)),bg="coral2",fg="gray99",activebackground="coral2",activeforeground="gray99")
        speedLabel.configure(text=("MPH: "+str(speedReading)),bg="DeepSkyBlue3",fg="gray99",activebackground="DeepSkyBlue3",activeforeground="gray99")
        satSeenLabel.configure(text=("GPS In View: "+str(satSeenReading)),bg="purple3",fg="gray99",activebackground="purple3",activeforeground="gray99")
        satUsedLabel.configure(text=("GNSS In Use: "+str(satUsedReading)),bg="purple3",fg="gray99",activebackground="purple3",activeforeground="gray99")
        altitudeLabel.configure(text=("Altitude: "+str(altitudeReading)),bg="DeepSkyBlue3",fg="gray99",activebackground="DeepSkyBlue3",activeforeground="gray99")
        
        hdopLabel.configure(text=("H DOP: "+str(hdopReading)),bg="cyan4",fg="gray99",activebackground="cyan4",activeforeground="gray99")
        pdopLabel.configure(text=("P DOP: "+str(pdopReading)),bg="cyan4",fg="gray99",activebackground="cyan4",activeforeground="gray99")
        vdopLabel.configure(text=("V DOP: "+str(vdopReading)),bg="cyan4",fg="gray99",activebackground="cyan4",activeforeground="gray99")
        
        hectopascalLabel.configure(text=("hPa: "+str(hectopascalReading)),bg="cyan4",fg="gray99",activebackground="cyan4",activeforeground="gray99")
    return
        
########################################################################################################
# Root Main Loop
########################################################################################################
root=Tk()
root.title(rootTitle)
root.geometry(rootGeom)
root.attributes('-fullscreen',rootFS)
root.configure(background=rootBackground)
################################################################################### Exit Button
exitButton=Button(root,text="EXIT",font=("Helvetica","14"),
                  bd=2,width=22,height=1,
                  bg="red2",fg="gray1",
                  command=programExit)
exitButton.place(x=525,y=435)

################################################################################### Temp Label
tempLabel=Button(root,font=("Helvetica","14"),
                 bd=2,width=22,height=1,
                 bg="red2",fg="gray1",
                 activebackground="red2",activeforeground="gray1")
tempLabel.place(x=5,y=395)
################################################################################### Power Once Button
powerOnceButton=Button(root,text="PWR  ONCE (10 SEC)",font=("Helvetica","14"),
                       bd=2,width=22,height=1,
                       bg="gray35",fg="gray1",
                       activebackground="gray35",activeforeground="gray1") # ,command=gpsPowerCycle
powerOnceButton.place(x=265,y=395)
################################################################################### Power Force Button
powerForceButon=Button(root,text="PWR FORCE (16 SEC)",font=("Helvetica","14"),
                       bd=2,width=22,height=1,
                       bg="gray35",fg="gray1",
                       activebackground="gray35",activeforeground="gray1") # ,command=gpsPowerForce
powerForceButon.place(x=525,y=395)

################################################################################### Manual Plot GPS Button
manualPlotButon=Button(root,text="Manual Plot",font=("Helvetica","14"),
                       bd=2,width=22,height=1,
                       fg="gray1",
                       activeforeground="gray1",
                       command=manualPlotFunction)
manualPlotButon.place(x=5,y=335)


################################################################################### Time and Date Label
timeDateLabel=Button(root,font=("Helvetica","14"),
                     bd=2,width=22,height=1,
                     bg="DodgerBlue3",fg="gray99",
                     activebackground="DodgerBlue1",activeforeground="gray99",
                     command=clockControl)
timeDateLabel.place(x=5,y=5)
################################################################################### Fix (CON/DISCON) Label
fixLabel=Button(root,font=("Helvetica","14"),
                bd=2,width=22,height=1)
fixLabel.place(x=265,y=5)
################################################################################### Cardinal Label
cardinalLabel=Button(root,font=("Helvetica","14"),
                     bd=2,width=22,height=1)
cardinalLabel.place(x=525,y=5)
################################################################################### Latitude Label
latitudeLabel=Button(root,font=("Helvetica","14"),
                     bd=2,width=22,height=1)
latitudeLabel.place(x=5,y=55)
################################################################################### Longitude Label
longitudeLabel=Button(root,font=("Helvetica","14"),
                      bd=2,width=22,height=1)
longitudeLabel.place(x=265,y=55)
################################################################################### Speed Label
speedLabel=Button(root,font=("Helvetica","14"),
                  bd=2,width=22,height=1)
speedLabel.place(x=525,y=55)
################################################################################### Satellite Seen Label
satSeenLabel=Button(root,font=("Helvetica","14"),
                    bd=2,width=22,height=1)
satSeenLabel.place(x=5,y=105)
################################################################################### Satellite Used Label
satUsedLabel=Button(root,font=("Helvetica","14"),
                    bd=2,width=22,height=1)
satUsedLabel.place(x=265,y=105)
################################################################################### Altitude Label
altitudeLabel=Button(root,font=("Helvetica","14"),
                     bd=2,width=22,height=1)
altitudeLabel.place(x=525,y=105)
################################################################################### HDOP Label
hdopLabel=Button(root,font=("Helvetica","14"),
                 bd=2,width=22,height=1)
hdopLabel.place(x=5,y=155)
################################################################################### PDOP Label
pdopLabel=Button(root,font=("Helvetica","14"),
                 bd=2,width=22,height=1)
pdopLabel.place(x=265,y=155)
################################################################################### VDOP Label
vdopLabel=Button(root,font=("Helvetica","14"),
                 bd=2,width=22,height=1)
vdopLabel.place(x=525,y=155)
################################################################################### Hectopascal Label
hectopascalLabel=Button(root,font=("Helvetica","14"),bd=2,width=22,height=1)
hectopascalLabel.place(x=5,y=205)  
if (runOnce):
    serialReadState = 1
    ser.write(bytes("AT+CGNSPWR=1\r", 'utf-8'))
    serResponse = ser.read(1024)
    print(serResponse)
    cpuTemp()
    readSerial()
    manualPlotButon.configure(bg="green4",activebackground="green2")
    displayUpdates()
    runOnce=False
    #time.sleep(2.0)
########################################################################################################
# Main Loops
########################################################################################################
root.mainloop()
