#DeJanae Faison

import sitka_highs as highs
import tkinter as tk

def highAction():
    f = open(highs.plt.show())
    print("Button pressed")

def lowAction():
    print("Low pressed")

def exitAction():
    root.quit()

root = tk.Tk()
root.title("Main Menu")

Label = tk.Label(root,text="High/Low Temperatures", font=('Verdana',15)).pack(side= "top", pady=10)

root.minsize(300,300)

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




