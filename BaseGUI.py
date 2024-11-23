import BaseConverter as bc
import tkinter as tk
import pyperclip as ppc

GUIVersion = "1.2"
val = "input values!"

def conv():
	if ent_i1.get() != "" and ent_b1.get() != "" and ent_b2.get() != "":
		val = bc.baseToBase(ent_i1.get(),ent_b1.get(),ent_b2.get())
	else:
		val = "input all values!"
	answer.config(text=val)
	root.after(100,conv)
	return val

def swap_text():
	temp = ent_b1.get()
	num = conv()
	if num == "input all values!":
		num = ""
	ent_b1.delete(0, tk.END)
	ent_b1.insert(0, ent_b2.get())

	ent_b2.delete(0, tk.END)
	ent_b2.insert(0,temp)

	ent_i1.delete(0, tk.END)
	ent_i1.insert(0, str(num))

def doCopy():
	ppc.copy(conv())

#the window
root = tk.Tk()
root.title("Base Converter Version "+str(bc.version)+" | GUI V. "+str(GUIVersion))

label = tk.Label(root, text="Input's Base:", font=("Montserrat",16))
label.grid(row=0,column=0,padx=10,pady=10)

#entry for the input base
ent_b1 = tk.Entry(root, font=("Montserrat",14),width=8)
ent_b1.grid(row=0,column=1,padx=10,pady=10)

#entry for the number for conversion
label = tk.Label(root, text="Input Number:", font=("Montserrat",16))
label.grid(row=0,column=2,padx=10,pady=10)

ent_i1 = tk.Entry(root, font=("Montserrat",14),width=16)
ent_i1.grid(row=0,column=3,padx=10,pady=10)

label = tk.Label(root, text="Output's Base:", font=("Montserrat",16))
label.grid(row=2,column=0,padx=10,pady=10)

#entry for the output base
ent_b2 = tk.Entry(root, font=("Montserrat",14),width=8)
ent_b2.grid(row=2,column=1,padx=10,pady=10)

label = tk.Label(root, text="Output:", font=("Montserrat",16))
label.grid(row=2,column=2,padx=10,pady=10)

answer = tk.Label(root, text=str(val), font=("Montserrat",16))
answer.grid(row=2,column=3,padx=10,pady=10)

copy_button = tk.Button(root, text="copy", font=("Montserrat", 16), command=doCopy)
copy_button.grid(row=3,column=3,padx=10,pady=10)

swap_button = tk.Button(root, text="swap", font=("Montserrat", 16), command=swap_text)
swap_button.grid(row=3,column=1,padx=10,pady=10)

root.after(0,conv)
root.mainloop()