# HAM-Dash
HAM Dash (Amateur Radio Controller for vehicle 2 DIN Dash)

Project History (Newest at top):

February 2020: We plan to get the Plotting feature with Open Maps working as well as impliment all the modules together. We are still working on the DTMF encoding as well as getting the decoder chip to interface with the SIM868 chip as well as the radio speaker inputs at the same time. We are working on making isolation hardware to acomidate this issue.

January 2020: We have now uploaded the GPRS and GSM GUI applications for standalone use. The Open Maps for the GPRS GUI in not implimented in this build as we have been running into minor issues with it on the Raspberry Pi, which was to be expected. The current GPRS GUI is just the raw readings from the GPRS module on the SIM868 chip. It also has some unused buttons for power cycling that we have a better implimentation for at this time that is not in the current build but rather in the current beta build. It also features a changable Zulu / Local clock button, the Zulu clock pulls from the GPRS module when it reads that from a sattelite, having trouble using the RTC module on the board, possibly bad battery during testing. It also has multiple logs, one that is ALL details in human readable, a CPU temp log, a google maps plotter readable log, and a manual plot log that has an accompanying button on the GUI. The GSM GUI is very simple and currently allows for a pre configured text to be sent to a preconfigured number. It also will place and hang up a call to the same set phone number. We are still working on adding the listen for an incoming call function as well as adding a few text boxes to select the numbers as well as type out a message. The main purpose would be for the SOS menu where you can send out a mass text to your emergency contacts in case of emergency with your GPS coordinates, radio mode and frequency, last heading, and time send.

December 2019: We have also now started working on plotting the GPRS system to Open Maps, it is still not ready for upload.

November 2019: Started working on a GUI for the GPRS functionality of the SIM868 GSM/GPRS chip. We are testing it heavily before uploading.

October 2019: We now have the GUI base built enough to the point we feel we can upload it as a shell and let others add to it. V1.4 (MK-IV), will be considered the public Shell but will be updated along with the full system.

Pre Upload- from February 2019 - September 2019: We were learning and building the main base GUI with NO controls other than dummy buttons. It had base functionality and some system commands like an OS update script, and a shutdown or reboot function.
