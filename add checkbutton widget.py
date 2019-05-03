from tkinter import *
from tkinter.ttk import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
chk_state = BooleanVar()
# IntVar() 0:uncheck 1:check
 
chk_state.set(False) #set check state
print(chk_state.get())
 
chk = Checkbutton(window, text='Choose', var=chk_state)
 
chk.grid(column=0, row=0)
 
window.mainloop()