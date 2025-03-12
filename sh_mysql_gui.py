from tkinter import *

root = Tk()

root.title("GUI 기반 MySQL 데이터베이스 관리")
root.geometry("400x200")

Label1 = Label(root, text="혼자 공부하면 재밌어요")
Label2 = Label(root, text="한번 시작하면 끝장을 봅시다", font=("궁서체", 20), fg="blue")

Label1.pack()
Label2.pack()

root.mainloop()