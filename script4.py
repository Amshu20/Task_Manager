import tkinter as tk

root = tk.Tk()
root.title("My Routine Tracker")
root.geometry("300x250")

# Checkboxes
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

cb1 = tk.Checkbutton(root, text="Aloe", variable=var1)
cb2 = tk.Checkbutton(root, text="Curd", variable=var2)
cb3 = tk.Checkbutton(root, text="Exercise", variable=var3)

cb1.pack()
cb2.pack()
cb3.pack()

def save():
    print("Aloe:", var1.get())
    print("Curd:", var2.get())
    print("Exercise:", var3.get())

btn = tk.Button(root, text="Save Today", command=save)
btn.pack()

root.mainloop()