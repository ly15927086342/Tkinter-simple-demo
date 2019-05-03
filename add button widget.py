from tkinter import *
window = Tk()
window.title("welcome liyu's first py GUI")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

# 鼠标点击button事件
def clicked():
	lbl.configure(text='button was clicked')

btn = Button(window,text='click me',command=clicked,bg="orange",fg="red")
btn.grid(column=1,row=0)
window.mainloop()