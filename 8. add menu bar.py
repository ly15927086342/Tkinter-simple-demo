from tkinter import *
# from tkinter import Menu
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
menu = Menu(window)

# tearoff=0:取消虚线
new_item = Menu(menu,tearoff=0)

def clicked():
	print(1)
 
new_item.add_command(label='New',command=clicked)
new_item.add_separator()
new_item.add_command(label='Edit')
 
menu.add_cascade(label='File', menu=new_item)
menu.add_command(label='File2')
 
window.config(menu=menu)
 
window.mainloop()