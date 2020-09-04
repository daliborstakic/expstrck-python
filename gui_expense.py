""" Importing Tkinter """
import tkinter as tk

# Main window
root = tk.Tk()

# First row
name_label = tk.Label(root, text="Name:")
name_field = tk.Entry(root)

# Second row
cost_label = tk.Label(root, text="Cost:")
cost_field = tk.Entry(root)

# Third row
expense_list = tk.Listbox(root)

# Fourth row
button_add = tk.Button(root, text="Add")
button_remove = tk.Button(root, text="Remove")

# Placing elements on the grid
name_label.grid(row=0, column=0, padx=5, pady=5)
name_field.grid(row=0, column=1, padx=5, pady=5)

cost_label.grid(row=1, column=0, padx=5, pady=5)
cost_field.grid(row=1, column=1, padx=5, pady=5)

expense_list.grid(row=2, columnspan=2, padx=5, pady=5)

button_add.grid(row=3, column=0, padx=5, pady=5)
button_remove.grid(row=3, column=1, padx=5, pady=5)

# Tkinter mainloop
tk.mainloop()
