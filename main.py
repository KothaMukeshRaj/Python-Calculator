import tkinter as tk

# Function to perform calculations
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to handle button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry field
entry = tk.Entry(window, width=20, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

# Create the number buttons
for i in range(9):
    button = tk.Button(window, text=str(i+1), width=5, height=2, font=("Arial", 12),
                       command=lambda i=i: button_click(i+1))
    button.grid(row=(i//3)+1, column=i%3)

# Create the operator buttons
operators = ['+', '-', '*', '/']
for i in range(len(operators)):
    button = tk.Button(window, text=operators[i], width=5, height=2, font=("Arial", 12),
                       command=lambda i=i: button_click(operators[i]))
    button.grid(row=i+1, column=3)

# Create the special buttons
clear_button = tk.Button(window, text="C", width=5, height=2, font=("Arial", 12), command=clear)
clear_button.grid(row=4, column=0)

zero_button = tk.Button(window, text="0", width=5, height=2, font=("Arial", 12),
                        command=lambda: button_click(0))
zero_button.grid(row=4, column=1)

equal_button = tk.Button(window, text="=", width=5, height=2, font=("Arial", 12), command=calculate)
equal_button.grid(row=4, column=2)

decimal_button = tk.Button(window, text=".", width=5, height=2, font=("Arial", 12),
                           command=lambda: button_click('.'))
decimal_button.grid(row=4, column=3)

# Run the GUI
window.mainloop()
def print_hi(name):
    print(f'Hi, {name}') 

if __name__ == '__main__':
    print_hi('PyCharm')

