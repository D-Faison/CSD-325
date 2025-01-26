#DeJanae Faison Assignment 4.2 1/26/25

import sitka_highs as highs
import sitka_lows as lows
import tkinter as tk
from tkinter import messagebox
#Button function if high is selected
def highAction():
    highs.plt.show()
    print("Button pressed")
    
#Button funtion if low is selected
def lowAction():
    lows.plt.show()
    print("Low pressed")
    
#Funtion to exit program but display message
def exitAction():
    
    messagebox.showinfo("Exit Program","Have a good day")
    root.quit()

root = tk.Tk()
root.title("Main Menu")
#Header
Label = tk.Label(root,text="High/Low Temperatures", font=('Verdana',15)).pack(side= "top", pady=10)
#Subheader
subLabel = tk.Label(root,text="Select to see record tempratures", font=('Verdana',10)).pack(side= "top", pady=10)
#Window size
root.minsize(300,300)
#Buttons
highButton = tk.Button(root, text = "High",width= 10,command= highAction)
highButton.pack(pady= 10)

lowButton = tk.Button(root, text = "Low",width= 10,command= lowAction)
lowButton.pack(pady= 10)

exitButton = tk.Button(root, text = "Exit",width= 10,command= exitAction)
exitButton.pack(pady= 10)




root.mainloop()
#Resources:
#OpenAI. (2025). ChatGPT (40 mimi). https://chat.openai.com/chat
#GeeksforGeeks. (2019, April 15). minsize() method in Tkinter | Python. GeeksforGeeks. https://www.geeksforgeeks.org/minsize-method-in-tkinter-python/
#Python Tkinter - MessageBox Widget. (2020, March 10). GeeksforGeeks. https://www.geeksforgeeks.org/python-tkinter-messagebox-widget/




