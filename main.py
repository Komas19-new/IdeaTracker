import tkinter as tk
from tkinter import messagebox

def save_ideas():
    with open("ideas.txt", "w") as file:
        for idea in ideas:
            file.write(idea + "\n")

def save_done_ideas():
    with open("done_ideas.txt", "w") as file:
        for idea in done_ideas:
            file.write(idea + "\n")

def add_idea():
    idea_text = entry.get()
    if idea_text:
        ideas.append(idea_text)
        listbox.insert(tk.END, idea_text)
        entry.delete(0, tk.END)
        save_ideas()

def mark_done():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        listbox.itemconfig(index, bg="light gray")
        done_ideas.append(ideas[index])
        listbox_done.insert(tk.END, ideas[index])
        ideas.pop(index)
        listbox.delete(index)
        save_ideas()
        save_done_ideas()
    else:
        messagebox.showwarning("No Idea Selected", "Please select an idea to mark as done.")

def unmark_done():
    selected_index = listbox_done.curselection()
    if selected_index:
        index = selected_index[0]
        listbox_done.itemconfig(index, bg="white")
        ideas.append(done_ideas[index])
        listbox.insert(tk.END, done_ideas[index])
        done_ideas.pop(index)
        listbox_done.delete(index)
        save_ideas()
        save_done_ideas()
    else:
        messagebox.showwarning("No Idea Selected", "Please select a done idea to unmark.")

def reset():
    global ideas, done_ideas
    ideas = []
    done_ideas = []
    listbox.delete(0, tk.END)
    listbox_done.delete(0, tk.END)
    save_ideas()
    save_done_ideas()

# Load existing ideas from file
try:
    with open("ideas.txt", "r") as file:
        ideas = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    ideas = []

# Load existing done ideas from file
try:
    with open("done_ideas.txt", "r") as file:
        done_ideas = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    done_ideas = []

# Create the main application window
root = tk.Tk()
root.title("Idea Tracker")

# Create a label widget
label = tk.Label(root, text="Enter your ideas:")
label.pack(pady=10)

# Create a text entry widget
entry = tk.Entry(root, width=50)
entry.pack()

# Create a button to add ideas
add_button = tk.Button(root, text="Add Idea", command=add_idea)
add_button.pack(pady=5)

# Create a listbox to display ideas
listbox = tk.Listbox(root, width=50)
for idea in ideas:
    listbox.insert(tk.END, idea)
listbox.pack(pady=10)

# Create a button to mark ideas as done
done_button = tk.Button(root, text="Mark as Done", command=mark_done)
done_button.pack(pady=5)

# Create a listbox to display done ideas
listbox_done = tk.Listbox(root, width=50)
for idea in done_ideas:
    listbox_done.insert(tk.END, idea)
listbox_done.pack(pady=10)

# Create a button to unmark done ideas
unmark_done_button = tk.Button(root, text="Unmark Done", command=unmark_done)
unmark_done_button.pack(pady=5)

# Create a button to reset the application
reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
