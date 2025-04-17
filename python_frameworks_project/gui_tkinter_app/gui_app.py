import tkinter as tk

root = tk.Tk()
root.title("Tkinter GUI Example")

label = tk.Label(root, text="Hello from Tkinter!")
label.pack(pady=20)

root.mainloop()