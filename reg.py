from tkinter import*
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

		title=Label(frame1,text="Register here",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

		
		f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
		self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_fname.place(x=50,y=130,width=250)

		l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
		self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_lname.place(x=370,y=130,width=250)

		contact=Label(frame1,text="Contact",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
		self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_contact.place(x=50,y=200,width=250)

		email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
		self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_email.place(x=370,y=200,width=250)

		ques=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
		
		self.cmb_ques=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
		self.cmb_ques['values']=("Select","Your first pet name","Your Birth Place","Your Best Friend Name","Your Pet Name")
		self.cmb_ques.place(x=50,y=270,width=250)
		self.cmb_ques.current(0)

		ans=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
		self.txt_ans=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_ans.place(x=370,y=270,width=250)

		password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
		self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_password.place(x=50,y=340,width=250)

		cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
		self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_cpassword.place(x=370,y=340,width=250)


		self.var_chk=IntVar()
		chk=Checkbutton(frame1,text="I Agree The Terms And Condition",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)
		btn_register=Button(frame1,text="Sign-Up",font=("times new roman",15,"bold"),bg="green",fg="white", command=self.register_data).place(x=100,y=420,width=250)
		btn_login=Button(frame1,text="Already having account",command=self.login,font=("times new roman",12),bg="white",bd=0,fg="#B00857").place(x=150,y=460)

	def login(self):
		self.root.destroy()
		import log

	def clear(self):
		self.txt_fname.delete(0,END)
		self.txt_lname.delete(0,END)
		self.txt_contact.delete(0,END)
		self.txt_email.delete(0,END)
		self.txt_ans.delete(0,END)
		self.txt_password.delete(0,END)
		self.txt_cpassword.delete(0,END)
		self.cmb_ques.current(0)
	
	def register_data(self):
		if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_ques.get()=="" or self.txt_ans.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
			messagebox.showerror("Error","All Fields Are Required",parent=self.root)
		elif self.txt_password.get()!=self.txt_cpassword.get():
			messagebox.showerror("Error","Password And Confirm Password should be same",parent=self.root)
		elif self.var_chk.get()==0:
			messagebox.showerror("Error","Please aprrove our terms n Condition",parent=self.root)
		else:
			try:
				con=pymysql.connect(host="localhost",user="root",password="",database="fsecure")
				cur=con.cursor()
				cur.execute("select * from fsecure where email=%s",self.txt_email.get())
				row=cur.fetchone()
				#print(row)
				if row!=None:
					messagebox.showerror("Error","User Already Exist",parent=self.root)
				else:
					cur.execute("insert into fsecure(f_name,l_name,email,contact,ques,ans,password) values(%s,%s,%s,%s,%s,%s,%s)",
									(self.txt_fname.get(),
									self.txt_lname.get(),
									self.txt_email.get(),
									self.txt_contact.get(),
									self.cmb_ques.get(),
									self.txt_ans.get(),
									self.txt_password.get()
									))
					con.commit()
					con.close()
					messagebox.showinfo("success","RegisterSuccessfully",parent=self.root)
					self.clear()
			except Exception as e:
				messagebox.showerror("Error",f"Error due to: {str(e)}",parent=self.root)

			

root = Tk()
obj=Register(root)
root.mainloop()