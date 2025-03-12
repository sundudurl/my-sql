from tkinter import *

root = Tk()
Button1 = Button(root, text="혼공1")
Button2 = Button(root, text="혼공2")
Button3 = Button(root, text="혼공3")

Button1.pack(side=TOP, fill = X,padx = 10, pady = 10)
Button2.pack(side=TOP, fill = X,padx = 10, pady = 10)
Button3.pack(side=TOP, fill = X,padx = 10, pady = 10)

root.mainloop()