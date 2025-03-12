from tkinter import *
from tkinter import messagebox

def clickButton():
    messagebox.showinfo("버튼", "버튼을 클릭했습니다.")

root = Tk()
root.geometry("200x200")

Button1 = Button(root, text="버튼을 클릭하세요",font= "고딕체", fg="blue", bg="white", command=clickButton)
Button1.pack(expand = 1)

root.mainloop()