#!/usr/bin/python3.7
import serial
import time
import os
import RPi.GPIO as GPIO
from time import strftime, gmtime
from tkinter import *

runOnce = True
rootTitle = "SIM868 Full V1.1"
rootGeom = "800x480+5+5"
rootBgColor = "gray10"
rootFont = ("Helvetica","14")
fsMode = False

phonebookPerson1 = 0000000000
phonebookPerson2 = 0000000000
phonebookPerson3 = 0000000000

outgoingPhoneNumber = phonebookPerson1

msgBody="Message Sent from PiTrax at: "
msgEnding=", -PiTrax"
msg=(str(msgBody)+str(time.strftime('%r  %x'))+str(msgEnding))
######################################################################
#                            SIM868 Commands and Perams
######################################################################
##############################################
#            Start Serial Communucation
##############################################
def startSerialConnection():
    global ser
    ser=serial.Serial('/dev/ttyS0',115200,timeout=0.1)
    ser.close()
    try:
        ser=serial.Serial('/dev/ttyS0',115200,timeout=0.1)
        print("- - - - - - - - - - Serial Staring, Please Wait - - - - - - - - - -")
        time.sleep(3.0)
        print("- - - - - - - - - - Serial Started - - - - - - - - - -")
        time.sleep(1.0)
        #------------------------------------------------------------------------- Checking network status
        print("- - - - - - - - - - Checking Network States - - - - - - - - - -")
        #----------------------------------------------------- Check SIM Status
        sendData = bytes("AT+CPIN?\r", 'utf-8')
        ser.write(sendData)
        time.sleep(0.1)
        serResponse = ser.read(4096)
        print(str(serResponse.decode()))
        #----------------------------------------------------- Check Device Registration
        sendData = bytes("AT+CGREG=?\r", 'utf-8')
        ser.write(sendData)
        time.sleep(0.1)
        serResponse = ser.read(4096)
        print(str(serResponse.decode()))
        #----------------------------------------------------- Check Network
        sendData = bytes("AT+COPS?\r", 'utf-8')
        ser.write(sendData)
        time.sleep(0.1)
        serResponse = ser.read(4096)
        print(str(serResponse.decode()))
        #----------------------------------------------------- Check Signal
        sendData = bytes("AT+CSQ\r", 'utf-8')
        ser.write(sendData)
        time.sleep(0.1)
        serResponse = ser.read(4096)
        print(str(serResponse.decode()))
        #----------------------------------------------------- Check CNUM
        sendData = bytes("AT+CNUM\r", 'utf-8')
        ser.write(sendData)
        time.sleep(0.1)
        serResponse = ser.read(4096)
        print(str(serResponse.decode()))
        #------------------------------------------------------------------------- Set default configuration
        print("- - - - - - - - - - Set SMS Mode - - - - - - - - - -")
        #----------------------------------------------------- Set SMS Mode
        sendData = bytes("AT+CMGF=1\r", 'utf-8')
        ser.write(sendData)
        time.sleep(1.0)
        serResponse = ser.read(4096)
        print(str(serResponse.decode()))
        time.sleep(1.0)
        print("Setup Complete, Launching TK.")
        time.sleep(1.0)
    except Exception as e:
        print("Exception Thrown: ")
        print(e)
        time.sleep(2.0)
        exit()
    return
##############################################
#            Send SMS
##############################################
def sendSMS():
    global ser
    global msg
    global msgBody
    global msgEnding
    sendTextButton.configure(bg="orange",fg="gray1",activebackground="orange2",activeforeground="gray1")
    root.update()
    print("- - - - - - - - - - Sending Test Message - - - - - - - - - -")
    sendData = bytes("AT+CMGS=\"+1"+str(outgoingPhoneNumber)+"\"\r", 'utf-8')
    ser.write(sendData)
    time.sleep(1.0)
    ser.write(bytes(msg + chr(26),'utf-8'))
    time.sleep(5.0)
    serResponse = ser.read(4096)
    print(str(serResponse.decode()))
    sendTextButton.configure(bg="blue",fg="gray1",activebackground="blue2",activeforeground="gray1")
    root.update()
    time.sleep(1.0)
    return
##############################################
#            Place Call
##############################################
def placeCall():
    global ser
    print("Starting Call Process")
    sendDataString = ("ATD"+str(outgoingPhoneNumber)+";\r\n")
    sendData = bytes(str(sendDataString), 'utf-8')
    print(sendDataString)
    ser.write(sendData)
    time.sleep(2.0)
    serResponse = ser.read(4096)
    print(str(serResponse.decode()))
    print("Call Process Ended")
    time.sleep(1.0)
    return
##############################################
#            End Call
##############################################
def endCall():
    global ser
    print("Ending Call")
    sendData = bytes("ATH\r\n", 'utf-8')
    ser.write(sendData)
    time.sleep(2.0)
    serResponse = ser.read(4096)
    print(str(serResponse.decode()))
    print("Ending Call Done")
    time.sleep(1.0)
    return
######################################################################
#                            TK Commands and Perams
######################################################################
def programExit():
    global ser
    ser.close()
    print("Serial Closing")
    time.sleep(0.5)
    root.destroy()
    time.sleep(0.5)
    exit()
######################################################################
#                            Root TK Window
######################################################################
root=Tk()
root.title(rootTitle)
root.geometry(rootGeom)
root.configure(background=rootBgColor)
root.attributes('-fullscreen',fsMode)

programExitButton=Button(root,text="EXIT",font=(rootFont),bd=2,width=10,height=1,bg="red",fg="gray1",activebackground="red2",activeforeground="gray1",command=programExit)
programExitButton.place(x=655,y=405)

sendTextButton=Button(root,text="Send SMS",font=(rootFont),bd=2,command=sendSMS)
sendTextButton.place(x=5,y=5)

placeCallButton=Button(root,text="Send",font=(rootFont),bd=2,command=placeCall)
placeCallButton.place(x=5,y=55)

endCallButton=Button(root,text="End",font=(rootFont),bd=2,command=endCall)
endCallButton.place(x=5,y=105)





if (runOnce == True):
    
    sendTextButton.configure(width=10,height=1,bg="blue",fg="gray1",activebackground="blue2",activeforeground="gray1")
    placeCallButton.configure(width=10,height=1,bg="green",fg="gray1",activebackground="green2",activeforeground="gray1")
    endCallButton.configure(width=10,height=1,bg="red",fg="gray1",activebackground="red2",activeforeground="gray1")
    
    startSerialConnection()
    runOnce = False
    
root.mainloop()
