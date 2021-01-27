from tkinter import *

root = Tk()
photo = PhotoImage(file = "abc.jpg")
label = Label(root,image = photo)
label.pack()

root.mainloop()