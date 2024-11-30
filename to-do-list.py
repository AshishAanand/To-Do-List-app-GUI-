from tkinter import *
from PIL import Image, ImageTk
import json
import os

TASKS_FILE = 'tasks.json'

# Function to load data
def load_data():
    if os.path.exists(TASKS_FILE):  # Check if the file exists
        with open(TASKS_FILE, "r") as file:
            data = json.load(file)  # Load the JSON data into a Python object
            print("Data loaded successfully!")
            return data
    else:
        print("No existing data found. Starting fresh!")
        return []  # Return an empty list if no data is found

# Function to save data
def save_data(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

# Check Button was clicked or not
btn_clicked = False

def on_btn_click():
    global btn_clicked
    btn_clicked = True
    user_task = entry.get()

    if user_task == "":
        print("Please enter your task")
    else:
        # Load existing tasks
        tasks = load_data()

        # Add the new task to the list
        tasks.append(user_task)

        # Save the updated list to JSON
        save_data(tasks)

        # Create a frame for each task and its button
        task_frame = Frame(root, bg="white")
        task_frame.pack(pady=10, padx=20, fill="x")  # Adjust spacing between tasks

        # Added task label
        tasks_label = Label(task_frame, text=user_task, padx=10, pady=7, bg="lightgrey", anchor="w")
        tasks_label.pack(side="left", fill="x", expand=True)  # Align task to the left and stretch it

        # Delete button
        delete_btn = Button(task_frame, text="Done", command=lambda: delete_task(task_frame, user_task))
        delete_btn.pack(side="right", padx=10)  # Align delete button to the right

        # Clears entry when submitted
        entry.delete(0, END)

def delete_task(task_frame, task):
    """Delete the task and update the saved list."""
    task_frame.destroy()

    # Load existing tasks
    tasks = load_data()

    # Remove the deleted task
    tasks.remove(task)

    # Save the updated list back to the file
    save_data(tasks)

def resize_background(event):
    """Resize the background image when the window is resized."""
    new_width = event.width
    new_height = event.height

    resized_image = original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    updated_image = ImageTk.PhotoImage(resized_image)

    # Update the background label with the resized image
    background_label.config(image=updated_image)
    background_label.image = updated_image


root = Tk()

# Window size
root.geometry("750x655")
# Window title
root.title("To-do List app")

# Load the image
original_image = Image.open("images/Screenshot_20230802-143144_Instagram.jpg")
background_image = ImageTk.PhotoImage(original_image)

# Add the image to a Label
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Full window

# Bind the resize event to the function
root.bind("<Configure>", resize_background)

ashish = Label(root, text="Program your today or Next day to be better In future.", bg="lightblue", font=("Arial", 20))
ashish.pack(pady=30)

# Add a sample widget on top of the background
entry = Entry(root, width=100, font=("Arial", 16))
entry.pack(pady=50)

button = Button(root, text="Submit", command=on_btn_click)
button.pack(pady=10)

# Load existing tasks and display them
tasks = load_data()
for task in tasks:
    task_frame = Frame(root, bg="white")
    task_frame.pack(pady=10, padx=20, fill="x")

    tasks_label = Label(task_frame, text=task, padx=10, pady=7, bg="lightgrey", anchor="w")
    tasks_label.pack(side="left", fill="x", expand=True)

    delete_btn = Button(task_frame, text="Done", command=lambda tf=task_frame, t=task: delete_task(tf, t))
    delete_btn.pack(side="right", padx=10)

root.mainloop()
