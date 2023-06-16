from tkinter import*
import tkinter
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import mysql.connector as mysql
import pymysql


class Register:
	def __init__(self,root):
		self.root=root
		self.root.title("Registeration Window")
		self.root.geometry("1350x700+0+0")
		self.root.config(bg="white")

		self.bg=ImageTk.PhotoImage(file="images/fsecure1.jpg")
		bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)


		self.left=ImageTk.PhotoImage(file="images/log1.jpg")
		left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

		frame1=Frame(self.root,bg="white")
		frame1.place(x=480,y=100,width=700,height=500)

		title=Label(frame1,text="FSecure",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

	


		
		btn_register=Button(frame1,text="PhotoImage",font=("times new roman",15,"bold"),bg="green",fg="white", command=self.photo_window).place(x=50,y=130,width=250)
		btn_register=Button(frame1,text="Video",font=("times new roman",15,"bold"),bg="green",fg="white", command=self.videos_window).place(x=370,y=130,width=250)
		btn_register=Button(frame1,text="Document",font=("times new roman",15,"bold"),bg="green",fg="white", command=self.doc_window).place(x=50,y=200,width=250)
		btn_register=Button(frame1,text="Music",font=("times new roman",15,"bold"),bg="green",fg="white", command=self.audio_window).place(x=370,y=200,width=250)
		btn_register=Button(frame1,text="All Type Of File",font=("times new roman",15,"bold"),bg="green",fg="white", command=self.other_window).place(x=50,y=300,width=250)

	def photo_window(self):
		self.root.destroy()
		import en

	def videos_window(self):
		self.root.destroy()
		import cv1
		
	def doc_window(self):
		self.root.destroy()
		import doc

	def audio_window(self):
		self.root.destroy()
		import mus

	def other_window(self):
		self.root.destroy()
		import en	


root = Tk()
obj=Register(root)
root.mainloop()