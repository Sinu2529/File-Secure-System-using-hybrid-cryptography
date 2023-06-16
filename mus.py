import customtkinter
from PIL import Image, ImageTk
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

from tkinter import *
from tkinter import filedialog

root = customtkinter.CTk()
root.geometry("1350x700+0+0")

root.bg=ImageTk.PhotoImage(file="images/fsecure1.jpg")
bg=Label(root,image=root.bg).place(x=0,y=0,relwidth=1,relheight=1)

def Decrypt():
	file1=filedialog.askopenfile(mode='r',filetype=[('mp3 file','*.mp3')])
	if file1 is not None:
		file_name=file1.name
		
		key=entry1.get()
		print(file_name,key)
		fi = open(file_name, "rb")
		file = fi.read()
		fi.close()

		file = bytearray(file)
		for index, value in enumerate(file):
			file[index] = value ^ int(key)

		fi1 = open(file_name, "wb")
		fi1.write(file)
		fi1.close()

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=200,padx=450, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text ="Music Uploading", font=("Roboto", 32))
label.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame,text="Encrypt", command=Decrypt)
button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame,text="Decrypt", command=Decrypt)
button.pack(pady=12, padx=10)

entry1 =  customtkinter.CTkEntry(master=frame, placeholder_text="Key")
entry1.pack(pady=12, padx=10)

root.mainloop()


