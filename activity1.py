#importing the libraries
from tkinter import*
from tkinter.ttk import*

#create the tkinter window
root = Tk()
root.title("menubar")

#creating the menubar
menubar = Menu(root)

#adding file menu and the commands
file = Menu(menubar,tearoff = 0)
menubar.add_cascade(label = "File",menu = file)
file.add_command(label = "New File...",command = None)
file.add_command(label = "New Window",command = None)
file.add_command(label = "Open File",command = None)
file.add_separator()
file.add_command(label = "Exit",command = root.destroy)

#adding edit menu and the commands
edit = Menu(menubar,tearoff = 0)
menubar.add_cascade(label = "Edit",menu = edit)
edit.add_command(label = "Undo",command = None)
edit.add_command(label = "Redo",command = None)
edit.add_separator()
edit.add_command(label = "Copy",command = None)
edit.add_command(label = "Paste",command = None)
edit.add_separator()
edit.add_command(label = "Find",command = None)
edit.add_command(label = "Replace",command = None)

#adding help menu and the commands
help_opt = Menu(menubar,tearoff = 0)
menubar.add_cascade(label = "Help",menu = help_opt)
help_opt.add_command(label = "Welcome",command = None)
help_opt.add_command(label = "Documentation",command = None)
help_opt.add_separator()
help_opt.add_command(label = "Video Tutorials",command = None)

#displayment
root.config(menu = menubar)
root.mainloop()