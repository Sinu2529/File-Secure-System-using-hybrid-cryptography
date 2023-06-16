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


def encrypt_image():
	file1=filedialog.askopenfile(mode='r',filetype=[('mp4 file','*.mp4')])
	if file1 is not None:
		#print(file1)
		file_name=file1.name
		#print(file_name)
		key=entry1.get()
		print(file_name,key)
		fi=open(file_name,'rb')
		image=fi.read()
		fi.close()
		image=bytearray(image)
		for index,values in enumerate(image):
			image[index]=values^int(key)
		fi1=open(file_name,'wb')
		fi1.write(image)
		fi1.close()
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=200,padx=450, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text ="Videos Uploading", font=("Roboto", 32))
label.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame,text="Encrypt", command=encrypt_image)
button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame,text="Decrypt", command=encrypt_image)
button.pack(pady=12, padx=10)

entry1 =  customtkinter.CTkEntry(master=frame, placeholder_text="Key")
entry1.pack(pady=12, padx=10)

root.mainloop()