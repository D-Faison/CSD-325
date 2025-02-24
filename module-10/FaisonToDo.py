#DeJanae Faison Assignment 10.2 DATE
#Tkinter to do list

import tkinter as tk
import tkinter.messagebox as msg

class ToDo(tk.Tk):
    def __init__(self,tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks
        
        self.tasks_canvas = tk.Canvas(self)

        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.tasks_canvas,orient="vertical",command=self.tasks_canvas.yview)
        
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)
        #Window 
        self.title("Faison To Do List")
        self.geometry("300x400")

        self.task_create = tk.Text(self.text_frame, height=3, bg="white",fg="black")

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        
        self.canvas_frame = self.tasks_canvas.create_window((0,0),window=self.tasks_frame,anchor="n")

        self.task_create.pack(side=tk.BOTTOM,fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM,fill=tk.X)
        self.task_create.focus_set()

        todo = tk.Label(self,text="*** Add Items Here ***",bg="SteelBlue4",fg="black",pady=10,relief="raised",borderwidth=5)
        todo.bind("<Button-1>",self.remove_task)

        self.tasks.append(todo)

        for task in self.tasks:
            task.pack(side=tk.TOP,fill=tk.X)

        self.task_create = tk.Text(self, height=3, bg= "white",fg="black")
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>",self.mouse_scroll)
        self.bind_all("<Button-4>",self.mouse_scroll)
        self.bind_all("<Button-5>",self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        self.colour_schemes= [{"bg": "lightgrey", "fg": "black"},{"bg": "grey", "fg":"white"}]
    
    def add_task(self, event=None):
        task_text = self.task_create.get(1.0,tk.END).strip()

        if len(task_text)>0:
            new_task = tk.Label(self.text_frame,text=task_text,pady=10)

            self.set_task_color(len(self.tasks),new_task)

            new_task.bind("<Button-3>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)
        self.task_create.delete(1.0,tk.END)

    def remove_task(self,event):
        task = event.widget
if __name__ == "__main__":
    todo = ToDo()
    todo.mainloop()

#Resources:
#Dvlv. (2020). Tkinter-By-Example/Tkinter-By-Example.pdf at master · Dvlv/Tkinter-By-Example. GitHub. https://github.com/Dvlv/Tkinter-By-Example/blob/master/Tkinter-By-Example.pdf