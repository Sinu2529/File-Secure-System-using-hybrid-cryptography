from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image, ImageTk,ImageDraw
from math import*
import time
from datetime import*
import mysql.connector as mysql
import pymysql 


class Login:
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

		title=Label(frame1,text="Login",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

		email=Label(frame1,text="Email ID",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=250,y=150)
		self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_email.place(x=250,y=180,width=350)

		password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=250,y=250)
		self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_password.place(x=250,y=280,width=350)

		btn_reg=Button(frame1,text="Register new Account?",command=self.register,font=("times new roman",12),bg="white",bd=0,fg="#B00857").place(x=250,y=320)

		btn_login=Button(frame1,text="Login",command=self.login,font=("times new roman",12),bg="#B00857",fg="white").place(x=250,y=360)
		
	def register(self):
		self.root.destroy()
		import reg
	


	def login(self):
		if self.txt_email.get()=="" or self.txt_password.get()=="":
			messagebox.showerror("Error","All Fields are required",parent=self.root)
		else:
			try:
				con=pymysql.connect(host="localhost",user="root",password="",database="fsecure")
				cur=con.cursor()
				cur.execute("select * from fsecure where email=%s and password=%s",(self.txt_email.get(),self.txt_password.get()))
				row=cur.fetchone()
				if row==None:
					messagebox.showerror("Error","Invalid ",parent=self.root)
				else:
					self.root.destroy()
					import main

			except Exception as es:
				messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)


root = Tk()

obj=Login(root)
root.mainloop()