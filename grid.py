from tkinter import *

root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text="Hello!")
myLabel2 = Label(root, text="I'm Redisp!")
# Putting it on the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

root.mainloop()
