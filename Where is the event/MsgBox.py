from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry('200x200')
def alert():
    messagebox.showwarning('alert','Virus found.')
button = Button(text='Scan the Virus.',command=alert)
button.place(x=40,y=40)
window.mainloop()