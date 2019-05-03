from tkinter import *
from tkinter import filedialog
from os import path

window = Tk()
window.title("welcome liyu's first py GUI")
window.geometry('350x200')

# 鼠标点击button事件
def clicked():
	# file = filedialog.askopenfilename()
	# path.dirname(__file__):当前文件夹
	file = filedialog.askopenfilename(initialdir= path.dirname('C:/Users/'),filetypes = (("Text files","*.txt"),("all files","*.*")))
	print(file)

def clickedfiles():
	files = filedialog.askopenfilenames() # file是元组
	print(files)

def clickeddir():# 选文件夹
	dir = filedialog.askdirectory()
	print(dir)

btnfile = Button(window,text='choose file',command=clicked)
btnfiles = Button(window,text='choose files',command=clickedfiles)
btndir = Button(window,text='choose dirs',command=clickeddir)

btnfile.grid(column=0,row=0)
btnfiles.grid(column=0,row=1)
btndir.grid(column=0,row=2)
window.mainloop()