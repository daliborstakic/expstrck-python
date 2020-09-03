""" Importing Tkinter """
import tkinter as tk

# Main window
root = tk.Tk()

# First row
name_label = tk.Label(root, text="Name:")
name_field = tk.Entry(root)

# Placing elements on the grid
name_label.grid(row=0, column=0)
name_field.grid(row=0, column=1)

# Tkinter mainloop
tk.mainloop()
