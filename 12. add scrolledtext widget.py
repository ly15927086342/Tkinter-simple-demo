from tkinter import *
from tkinter import scrolledtext
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
 # 这里的width指字符个数，height指行数!
txt = scrolledtext.ScrolledText(window,width=40,height=10)
txt.insert(INSERT,'you text goes here')
txt.grid(column=0,row=0)
# txt.delete(1.0,END)

print(txt.get(1.0,END))# 获取从第一个字符到最后一个字符
 
window.mainloop()