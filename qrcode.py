import pyqrcode 
import png 
import pyzbar.pyzbar as pyzbar
from test import *

from PIL import Image
import cv2
import numpy as np


import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

import datetime  
def cam():
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_PLAIN

    while True:
        _, frame = cap.read()

        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            #print("Data", obj.data)
            cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                        (255, 0, 0), 3)

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break
def scan():
	try:
		a=pyzbar.decode(Image.open(filedialog.askopenfilename(title="Select Image Containing QRCode")))
		messagebox.showinfo("Data Stored in the QRCode",str(a[0].data))
		temp=tk.Tk()
		temp.withdraw()
		temp.clipboard_clear()
		temp.clipboard_append(str(a[0].data))
		temp.update()
		messagebox.showinfo("Access Data","Data is Copied To The ClipBoard")
		temp.destroy()
	except:
		messagebox.showinfo("Select","Select an Image Containing QRCode!")

def qrcodegen():
	url = pyqrcode.create(cont.get()) 
	print(len(nameentry.get()))
	if(len(str(nameentry.get()))!=0):
		mesg=str(nameentry.get())+".png"
		url.png(mesg, scale = 6)
	else:
		mesg="QRCode"+str(datetime.datetime.now())+".png"
		url.png(mesg, scale = 6)	
	messagebox.showinfo("Saved!","Your QRCode Has Been Created as {}".format(mesg))

	
def main():
	global root 
	root=tk.Tk()
	root.title("QRCODE Project")
	root.resizable(0,0)
	root.geometry("640x500")

	contlab=tk.Label(root,text="Enter The Content to Convert into QRCode:",font="8")
	contlab.place(relx=0.1,rely=0.05)
	global cont
	cont=tk.Entry(root,width=45)
	cont.place(relx=0.1,rely=0.1)

	namef=tk.Label(root,text="Name of QRCodeImage:",font=8)
	namef.place(relx=0.1,rely=0.155)
	
	global nameentry	
	nameentry=tk.Entry(root)
	nameentry.place(relx=0.41,rely=0.15)

	createb=tk.Button(root,width=10,text="Create",fg="#fff",bg="#000",command=qrcodegen)
	createb.place(relx=0.7,rely=0.12)

	scanbutton=tk.Button(root,text="Scan a QRCode Image",command=scan,fg="#fff",bg="#000")
	scanbutton.place(relx=0.1,rely=0.3)

	camerabutton=tk.Button(root,text="Scan a QRCode Through Camera",command=cam,fg="#fff",bg="#000")
	camerabutton.place(relx=0.1,rely=0.4)

	warncam=tk.Label(root,text="NOTE:-Press ESC Key and Wait For Few Seconds To Close the Camera",font="2")
	warncam.place(relx=0.1,rely=0.47)
	
	root.mainloop()
if __name__ == '__main__':
	main()