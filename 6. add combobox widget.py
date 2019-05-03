from tkinter import *
from tkinter.ttk import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
combo = Combobox(window)
 
combo['values']= (1, 2, 3, 4, 5, "Text")
 
combo.current(3) #set the selected item index
 
combo.grid(column=0, row=0)
print(combo.get())# 获取选择的项

window.mainloop()