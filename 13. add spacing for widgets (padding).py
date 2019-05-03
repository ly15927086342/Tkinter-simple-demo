from tkinter import *
window = Tk()
window.title('welcome')
window.geometry('400x200')
lbl = Label(window, text="Hello",padx=20,pady=20,font=('Arial Bold',50))
lb2 = Label(window, text="World",font=('Arial Bold',50))
lbl.grid(column=0, row=0)
lb2.grid(column=1, row=0)
window.mainloop()