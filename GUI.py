import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        formatted_task = f"{task:<30} - {date.get():>40}"
        listbox.insert(tk.END, formatted_task)
        entry.delete(0, tk.END)
        date.delete(0, tk.END)

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except tk.TclError:
        pass

root = tk.Tk()
root.title("To-Do List")

# Listbox styles
listbox = tk.Listbox(root, fg="black", bg="pink")
listbox.pack(padx=50, pady=(25, 10), ipadx=600, ipady=700)

# Entry box styles
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(padx=10, pady=(0, 5))

# Date entry box styles
date = tk.Entry(root, font=("Arial", 12))
date.pack(padx=10, pady=(0, 5))

# Button styles
button_frame = tk.Frame(root)
button_frame.pack(pady=(0, 10))

add_button = tk.Button(button_frame, text="Add Task", command=add_task, font=("Arial", 12), fg="black", bg="light pink")
add_button.pack(side=tk.LEFT, padx=(0, 5))

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, font=("Arial", 12), fg="black", bg="light pink")
delete_button.pack(side=tk.LEFT, padx=(0, 5))

root.mainloop()