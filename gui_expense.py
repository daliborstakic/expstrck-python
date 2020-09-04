""" Importing Tkinter """
import tkinter as tk
from tkinter import messagebox
import csv
from expense import Expense

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

def add_expense():
    """ Adding expenses to the .csv file and the ListBox """
    if name_field.get() == "" or cost_field.get() == "":
        error_message("You haven't entered any data!")

    try: # If the user tries to enter something else than a number
        cost = int(cost_field.get())
        name = name_field.get() # Storing the name value
        temp_exp = Expense(name, cost)
    except ValueError:
        cost_field.delete(0, tk.END) # Clearing the entry fields
        name_field.delete(0, tk.END)
        temp_exp = None
        error_message("You need to enter a number!")

    if temp_exp:
        """ If temp_exp is not None """
        with open("data.csv", "a", newline='') as csv_file:
            """ Writing to the .csv file """
            dict_writer = csv.DictWriter(csv_file, fieldnames=['name', 'cost'])
            dict_writer.writerow({'name': temp_exp.name, 'cost': temp_exp.cost})
            expense_list.insert(tk.END, f"{temp_exp.name} - {temp_exp.cost}")

        cost_field.delete(0, tk.END) # Clearing the entry fields
        name_field.delete(0, tk.END)
        exp.append(temp_exp) # Adding expense to expense list
        total_cost(exp) # Updating the total cost

def csv_to_list(exp):
    """ Fills the list on startup """
    with open("data.csv") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            expense_list.insert(tk.END, f"{row['name']} - {row['cost']}")
            exp.append(Expense(row['name'], int(row['cost'])))

def error_message(_message):
    """ Displays message """
    messagebox.showerror("Error", _message)

def total_cost(exp):
    """ Calculates the total cost and displays it """
    total_cost = sum(obj.cost for obj in exp)
    total_label = tk.Label(root, text=f"Total cost is: {total_cost}")
    total_label.grid(row=4, column=0, padx=5, pady=5)

# Expense list
exp = []
csv_to_list(exp)
total_cost(exp)

# Fourth row
button_add = tk.Button(root, text="Add", command=add_expense)
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
