
import pickle
import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.tk_setPalette(background="white", foreground="white")
root.tk_setPalette(background="#C1C1C1")
root.title("To-Do List")

def add_task():
    task = entry.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task")

def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except FileNotFoundError:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat")

def save_task():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

def on_entry_click(event):
    if entry.get() == "Enter the task":
        entry.delete(0, "end")  # Clear the placeholder text

def on_entry_leave(event):
    if entry.get() == "":
        entry.insert(0, "Enter the task")

# Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50, bg="white", fg="#FF0000")
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks, command=listbox_tasks.yview)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry = tkinter.Entry(root, width=55, background="#E0E0E0", fg="black")
entry.insert(0, "Enter the task")
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_entry_leave)
entry.pack()

button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task, font=("Arial", 12, "bold"), fg="blue")
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task, font=("Arial", 12, "bold"), fg="red")
button_delete_task.pack()

button_load_task = tkinter.Button(root, text="Load task", width=48, command=load_tasks, font=("Arial", 12, "bold"), fg="green")
button_load_task.pack()

button_save_task = tkinter.Button(root, text="Save task", width=48, command=save_task, font=("Arial", 12, "bold"), fg="brown")
button_save_task.pack()

root.mainloop()
