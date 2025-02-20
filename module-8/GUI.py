#GUI for JSON practice

from tkinter import *
import Faison_JSONpractice as pythonFile

students = pythonFile.listofStudents
#Widget
root = Tk()

#Size
root.geometry("600x600")
#Title
root.title("Student Information")
w = Label(root, text='Original Student List')
w.pack()

studentList = Message(root,text = students)
studentList.pack()

root.mainloop()
