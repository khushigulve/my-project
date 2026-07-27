import tkinter as tk

def greet():
    name = entry.get()
    label.config(text=f"Hello, {name}!")

root = tk.Tk()
root.title("User Form")
root.geometry("350x200")

tk.Label(root, text="Enter your name:").pack(pady=5)

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Submit", command=greet).pack(pady=10)

label = tk.Label(root, text="")
label.pack()

root.mainloop()