'''GUI Application
   Tkinter  (Tk Interface)
'''
from tkinter import Tk, ttk

#Tk - constructor
# ttk - object 

def sayHi():
    print("Hi to you!")
    ttk.Label(frame, text="From Say Hi.").grid(row=3,column=1)

root = Tk()

frame = ttk.Frame(root)
frame.grid()

lblHello = ttk.Label(frame, text="My Tkinter App").grid(row=0,column=0)
btnOk = ttk.Button(frame, text="OK", command=sayHi ).grid(row=1,column=0)
btnQuit = ttk.Button(frame, text="Quit", command=root.destroy ).grid(row=1,column=2)

root.mainloop()  #runs indefinitely
