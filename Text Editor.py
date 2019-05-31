from tkinter import *
import tkinter.scrolledtext as ScrolledText
#Rood for main windw
root = Tk(className = " Text Editor")
textArea = ScrolledText.ScrolledText(root, width=200, height=80)
textArea.pack()

#Keep the window open
root.mainloop()
