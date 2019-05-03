from tkinter import *
from tkinter import ttk

# To create a tab control, there are 3 steps to do so.

# First, we create a tab control using Notebook class
# Create a tab using Frame class.
# Add that tab to the tab control.
# Pack the tab control so it becomes visible in the window.

window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
tab_control = ttk.Notebook(window)
 
tab1 = ttk.Frame(tab_control)
 
tab2 = ttk.Frame(tab_control)
 
tab_control.add(tab1, text='First')
 
tab_control.add(tab2, text='Second')
 
lbl1 = Label(tab1, text= 'label1')
 
lbl1.grid(column=0, row=0)
 
lbl2 = Label(tab2, text= 'label2')
 
lbl2.grid(column=0, row=0)
 
tab_control.pack(expand=1, fill='both')
 
window.mainloop()