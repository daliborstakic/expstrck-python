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
        clear_entry() # Clearing the entry fields
        temp_exp = None
        error_message("You need to enter a number!")

    if temp_exp:
        """ If temp_exp is not None """
        with open("data.csv", "a", newline='') as csv_file:
            """ Writing to the .csv file """
            dict_writer = csv.DictWriter(csv_file, fieldnames=['name', 'cost'])
            dict_writer.writerow({'name': temp_exp.name, 'cost': temp_exp.cost})
            expense_list.insert(tk.END, f"{temp_exp.name} - {temp_exp.cost}")

        clear_entry() # Clears entry fields
        exp.append(temp_exp) # Adding expense to expense list
        total_cost(exp) # Updating the total cost

def remove_expense():
    """ Removing the selected expense """
    del_item = expense_list.get(expense_list.curselection())
    name, cost = tuple(value.strip() for value in del_item.split('-'))
    expense_list.delete(expense_list.curselection()) # Deleting from the ListBox
    
    for obj in exp: # Deleting in the expense list
        if obj.name == name:
            exp.remove(obj)

    """ Only way to delete a line in a .csv file """
    lines = list() # Empty list

    with open('data.csv', 'r') as csv_file:
        dict_reader = csv.DictReader(csv_file, fieldnames=['name', 'cost'])
        for row in dict_reader:
            if row['name'] != name and row['cost'] != cost:
                lines.append(row) # Writing every row except the selected one

    with open('data.csv', 'w') as csv_file:
        dict_writer = csv.DictWriter(csv_file, fieldnames=['name', 'cost'])
        
        """ Filling the .csv file with new lines """
        for row in lines:
            dict_writer.writerow({'name': row['name'], 'cost': row['cost']}) # Rewriting the original list

    total_cost(exp) # Updating the total cost

def csv_to_list(exp):
    """ Fills the list on startup """
    with open("data.csv") as csv_file:
        reader = csv.DictReader(csv_file, fieldnames=['name', 'cost'])

        for row in reader:
            """ Fills both the ListBox and the expense list """
            expense_list.insert(tk.END, f"{row['name']} - {row['cost']}")
            exp.append(Expense(row['name'], int(row['cost'])))

def error_message(_message):
    """ Displays message """
    messagebox.showerror("Error", _message)

def total_cost(exp):
    """ Calculates the total cost and displays it """
    total_cost = sum(obj.cost for obj in exp)
    total_label = tk.Label(root, text=f"Total cost is: {total_cost} RSD")
    total_label.grid(row=4, column=0, padx=5, pady=5)

def clear_entry():
    """ Clears entry fields """
    cost_field.delete(0, tk.END) # Clearing the entry fields
    name_field.delete(0, tk.END)

# Expense list
exp = []
csv_to_list(exp)
total_cost(exp)

# Fourth row
button_add = tk.Button(root, text="Add", command=add_expense)
button_remove = tk.Button(root, text="Remove", command=remove_expense)

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
