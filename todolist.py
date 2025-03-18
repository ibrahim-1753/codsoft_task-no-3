import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        Listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    task = task_entry.get()
    if task:
        tasks = Listbox.get(0, tk.END)
        if task in tasks:
            index = tasks.index(task)
            Listbox.delete(index)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task not found in the list!")
    else:
        messagebox.showwarning("Warning", "Please enter a task to remove!")

#Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

#Button_frame
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

#Add task button
add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

#Remove task
remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task)
remove_button.pack(side=tk.LEFT, padx=5)

#Listbox
Listbox = tk.Listbox(root, width=40, height=15)
Listbox.pack(pady=10)

root.mainloop()