#DeJanae Faison Assignment 10.2 DATE
#GUI to do list

import tkinter as tk
from tkinter import Menu

root = tk.Tk()
#Tkinter Window
root.title("Faison-To Do")
root.minsize(300,300)
root.configure(background="SteelBlue4",relief="raised",width=100,height=100,borderwidth=10)

#menu
menu_bar = Menu(root)
root.config(menu=menu_bar)
#Exit
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit",command=root.destroy)


#Root Loop
root.mainloop()

#Resources:
#Python Tkinter menu example - Create menu options. (2024, December 21). W3resource. https://www.w3resource.com/python-exercises/tkinter/python-tkinter-events-and-event-handling-exercise-11.php