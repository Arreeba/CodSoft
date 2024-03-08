import tkinter as tk
from tkinter import messagebox
def create_task():
    # get task details from input fields
    task_description = entry_description.get()
    task_due_date = entry_due_date.get()
    
    # Create a task object
    task = {"description": task_description, "due_date": task_due_date}
    
    # Add the task to the list of tasks
    tasks.append(task)
    
    # Clear the input fields
    entry_description.delete(0, tk.END)
    entry_due_date.delete(0, tk.END)
    
    # Refresh the tasks display
    refresh_tasks()
    
def delete_all_tasks():
     # Display a confirmation message
    result = messagebox.askquestion("Reset Frame", "Are you sure you want to reset the frame and clear all tasks?")
    if result == 'yes':
        # Clear the tasks list
        tasks.clear()
        # Refresh the tasks display
        refresh_tasks()
        
def delete_task(index):
    # Delete the task at the given index
    del tasks[index]
    # Refresh the tasks display
    refresh_tasks()
    
def refresh_tasks():
    # Clear the tasks frame
    for widget in frame_tasks.winfo_children():
        widget.destroy()
    
     # Display the tasks
    for i, task in enumerate(tasks):
        description = task["description"]
        due_date = task["due_date"]
        
        # Create the checkbox and label for each task
        checkbox = tk.Checkbutton(frame_tasks, bg="light gray", activebackground="light gray")
        checkbox.grid(row=i, column=0, sticky="w")
        task_label = tk.Label(frame_tasks, text=f"Task {i+1}: {description} (Due Date: {due_date})", fg="blue", bg="light gray")
        task_label.grid(row=i, column=1, sticky="w")
        delete_button = tk.Button(frame_tasks, text="Delete Task", command=lambda index=i: delete_task(index), bg="light gray", fg="red")
        delete_button.grid(row=i, column=2, padx=10)
        
def exit_application():
     result = messagebox.askquestion("Confirm Exit", "Are you sure you want to exit?")
     if result == 'yes':
        window.destroy()
# List to store tasks
tasks = []
# Create the main window
window = tk.Tk()
window.geometry("800x600")
window.title("To-Do List")

# Create labels and entry fields for task details
label_description = tk.Label(window, text="Task Description:")
label_description.pack()
entry_description = tk.Entry(window,bg="light gray",fg="blue")
entry_description.pack()

label_due_date = tk.Label(window, text="Due Date:")
label_due_date.pack()
entry_due_date = tk.Entry(window,bg="light gray",fg="blue")
entry_due_date.pack(pady=5)

# Create a button to create tasks
button_create=tk.Button(window,text="Create Task",command=create_task,bg="light gray",fg="blue")
button_create.pack(pady=5)

#Create a button to delete all tasks at once.
button_delete=tk.Button(window,text="Delete Tasks",command=delete_all_tasks,bg="light gray",fg="blue")
button_delete.pack(pady=5)

# Create the "Exit" button
button_exit = tk.Button(window, text="       Exit       ", command=exit_application,bg="light gray",fg="blue")
button_exit.pack(pady=5)

# Create a label for the title
label_title = tk.Label(window, text="To-Do List", font=("Helvetica", 16, "bold"), fg="blue")
label_title.pack()
# Create a frame to display tasks
frame_tasks = tk.Frame(window,bg="light gray", bd=2, relief="solid")
frame_tasks.pack(side="top", padx=50, pady=20)

# Run the GUI
window.mainloop()
