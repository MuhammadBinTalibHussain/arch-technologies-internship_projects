import tkinter as tk
from tkinter import ttk, messagebox

# Main Window
window = tk.Tk()
window.title("To-Do List App")
window.geometry("500x500")
window.config(bg="#1e1e2f")

tasks = []
completed_tasks = 0

# Add Task Function
def add_task():
    task = task_entry.get()

    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, "✔ " + task)
        task_entry.delete(0, tk.END)
        update_progress()
    else:
        messagebox.showwarning("Warning", "Please enter a task")

# Complete Task Function
def remove_task():
    global completed_tasks

    selected = listbox.curselection()

    if selected:
        listbox.delete(selected)
        completed_tasks += 1
        update_progress()
    else:
        messagebox.showwarning("Warning", "Please select a task")

# Progress Update Function
def update_progress():
    total = len(tasks)

    if total > 0:
        progress = (completed_tasks / total) * 100
        progress_bar["value"] = progress
        progress_label.config(text=f"Progress: {int(progress)}% Completed")
    else:
        progress_bar["value"] = 0
        progress_label.config(text="Progress: 0%")

# Title
title = tk.Label(
    window,
    text="📝 To-Do List Application",
    font=("Arial", 22, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=20)

# Task Entry
task_entry = tk.Entry(
    window,
    width=30,
    font=("Arial", 14),
    bd=3
)
task_entry.pack(pady=10)

# Button Frame
button_frame = tk.Frame(window, bg="#1e1e2f")
button_frame.pack(pady=10)

# Add Button
add_button = tk.Button(
    button_frame,
    text="Add Task",
    font=("Arial", 12, "bold"),
    bg="#00c853",
    fg="white",
    width=12,
    command=add_task,
    cursor="hand2"
)
add_button.grid(row=0, column=0, padx=10)

# Complete Button
remove_button = tk.Button(
    button_frame,
    text="Complete Task",
    font=("Arial", 12, "bold"),
    bg="#d50000",
    fg="white",
    width=15,
    command=remove_task,
    cursor="hand2"
)
remove_button.grid(row=0, column=1, padx=10)

# Listbox Frame
list_frame = tk.Frame(window)
list_frame.pack(pady=20)

# Scrollbar
scrollbar = tk.Scrollbar(list_frame)

# Task Listbox
listbox = tk.Listbox(
    list_frame,
    width=40,
    height=10,
    font=("Arial", 12),
    yscrollcommand=scrollbar.set,
    bd=3
)
listbox.pack(side=tk.LEFT)

scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Progress Label
progress_label = tk.Label(
    window,
    text="Progress: 0%",
    font=("Arial", 14, "bold"),
    bg="#1e1e2f",
    fg="#00ffcc"
)
progress_label.pack(pady=10)

# Progress Bar
progress_bar = ttk.Progressbar(
    window,
    length=300,
    mode='determinate'
)
progress_bar.pack(pady=10)

# Run Window
window.mainloop()