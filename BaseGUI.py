import BaseConverter as bc
import tkinter as tk

GUIVersion = "1.1"
val = "input values!"

def conv():
	if ent_i1.get() != "" and ent_b1.get() != "" and ent_b2.get() != "":
		val = bc.baseToBase(ent_i1.get(),ent_b1.get(),ent_b2.get())
	else:
		val = "input all values!"
	answer.config(text=val)
	root.after(100,conv)

#the window
root = tk.Tk()
root.title("Base Converter Version "+str(bc.version)+" | GUI V. "+str(GUIVersion))

label = tk.Label(root, text="Input's Base:", font=("Montserrat",16))
label.grid(row=0,column=0,padx=10,pady=10)

#entry for the input base
ent_b1 = tk.Entry(root, font=("Montserrat",14))
ent_b1.grid(row=1,column=0,padx=10,pady=10)

#entry for the number for conversion
label = tk.Label(root, text="Input Number:", font=("Montserrat",16))
label.grid(row=0,column=1,padx=10,pady=10)

ent_i1 = tk.Entry(root, font=("Montserrat",14))
ent_i1.grid(row=1,column=1,padx=10,pady=10)

label = tk.Label(root, text="Output's Base:", font=("Montserrat",16))
label.grid(row=2,column=0,padx=10,pady=10)

#entry for the output base
ent_b2 = tk.Entry(root, font=("Montserrat",14))
ent_b2.grid(row=3,column=0,padx=10,pady=10)

label = tk.Label(root, text="Output:", font=("Montserrat",16))
label.grid(row=2,column=1,padx=10,pady=10)

answer = tk.Label(root, text=str(val), font=("Montserrat",16))
answer.grid(row=3,column=1,padx=10,pady=10)

root.after(0,conv)
root.mainloop()