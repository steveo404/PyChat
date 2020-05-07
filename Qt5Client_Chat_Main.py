# Script Name:  Chat_Messenger
# Author:       Steveo
# 
# Purpose:
# Client side of chat system.  Includes GUI for sending and receiving messages
# Dependent on server running
# Obtains user name from system login.  

# Latest code base = Chat6

import socket
import select
import os
import sys
import win10toast
from time import sleep
import threading
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtWidgets, uic

HEADER_LENGTH = 10

IP = "10.10.1.105"
PORT = 1235
firstSessionText = 0

# Storage list for new messages
new_message = []

# Pull the username from the system login ID
my_username = os.getlogin()

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a given ip and port
client_socket.connect((IP, PORT))

# Set connection to non-blocking state, so .recv() call won't block, just return some exception
# THIS HAD BEEN CAUSING ISSUES - CONSIDER COMMENTING OUT
#client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = "{:<{}}".format(len(username),HEADER_LENGTH).encode('utf-8')
client_socket.send(username_header + username)

# Textbox names in the UI
#txtRecvdMessage - received message UI box
#txtMessageOut

def SendUserNotification():
    # Send the user connection to the other client as a message
    userconnectmsg = (my_username + " has connected")
    userconnectmsg = userconnectmsg.upper()
    print(userconnectmsg)
 

def sendmessage(message):
	
    # Encode message to send and add header
    message = message.encode('utf-8')
    message_header = "{:<{}}".format(len(message),HEADER_LENGTH).encode('utf-8')
    client_socket.send(message_header + message)

def receivemessage():

    while True:
        # Receive our "header" containing username length, it's size is defined and constant
        username_header = client_socket.recv(HEADER_LENGTH)

        # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
        if not len(username_header):
            print('Connection closed by the server')
            sys.exit()

        # Convert header to int value
        username_length = int(username_header.decode('utf-8').strip())

        # Receive and decode username
        username = client_socket.recv(username_length).decode('utf-8')

        # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
        message_header = client_socket.recv(HEADER_LENGTH)
        message_length = int(message_header.decode('utf-8').strip())
        message = client_socket.recv(message_length).decode('utf-8')
        incomingmessage = username + ": " + message
            
        new_message.append(incomingmessage)

        sleep(.5)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
    #def __init__(self, *args, **kwargs):
        super().__init__()
        #super().__init__(*args, **kwargs)
        uic.loadUi("chat.ui", self)
        self.pbExit.clicked.connect(self.LeaveProgram)
        self.pbSendMessage.clicked.connect(self.SendChatMessage)
        self.setWindowTitle("Chat Messenger")

    def SendChatMessage(self):
        global firstSessionText

        message = self.txtMessageOut.toPlainText()

        messagebox = my_username + ": " + message

        if firstSessionText < 1:
            self.txtRecvdMessage.setText(messagebox)
            firstSessionText = 1
        else:
            # Subsequent messages
            self.txtRecvdMessage.append(messagebox)
        self.txtMessageOut.clear()

        sendmessage(message)

    def ReceiveTextMessage(self):
        global firstSessionText

        msgnotifier = win10toast.ToastNotifier()

        while new_message:

            #print(incomingmessage)
            if firstSessionText < 1:
                # If first entry
                self.txtRecvdMessage.setText(new_message.pop(0))
                firstSessionText = 1
            else:
                # If subsequent entry
                self.txtRecvdMessage.append(new_message.pop(0))  #HOW TO APPEND MORE TEXT
                msgnotifier.show_toast('Chat', 'New message', duration=2)

    def LeaveProgram(self):
        self.close()

app = QtWidgets.QApplication([])
app.setStyle('Fusion')
win = MainWindow()
win.show()

SendUserNotification()

msgthread = threading.Thread(target=receivemessage)
msgthread.daemon = True
msgthread.start()

timer = QTimer()
timer.timeout.connect(win.ReceiveTextMessage)
timer.start(1000)

app.exec_()


