# GUI Hexadecimal Calculator
import tkinter as tk
from tkinter import messagebox

def calculate():
    """Perform calculation when = button is pressed"""
    try:
        expression = display.get()
        
        # Replace operators for evaluation
        expression = expression.replace('×', '*').replace('÷', '/')
        
        # Convert hex numbers to decimal for calculation
        import re
        
        def hex_to_dec(match):
            hex_num = match.group()
            return str(int(hex_num, 16))
        
        # Find all hex numbers and convert to decimal
        decimal_expression = re.sub(r'[0-9A-F]+', hex_to_dec, expression, flags=re.IGNORECASE)
        
        # Calculate result
        result = eval(decimal_expression)
        
        # Convert back to hex
        hex_result = hex(result).upper()[2:]
        display.set(hex_result)
        
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")
        display.set("0")
    except:
        messagebox.showerror("Error", "Invalid calculation!")
        display.set("0")

def button_click(value):
    """Handle button clicks"""
    current = display.get()
    if current == "0" or current == "Error":
        display.set(value)
    else:
        display.set(current + value)

def clear():
    """Clear the display"""
    display.set("0")

def backspace():
    """Remove last character"""
    current = display.get()
    if len(current) > 1:
        display.set(current[:-1])
    else:
        display.set("0")

# Create main window
root = tk.Tk()
root.title("Hexadecimal Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Display variable
display = tk.StringVar()
display.set("0")

# Create display
display_frame = tk.Frame(root)
display_frame.pack(pady=10)

display_entry = tk.Entry(display_frame, textvariable=display, font=('Arial', 16), 
                        justify='right', state='readonly', width=20)
display_entry.pack(padx=10, pady=10)

# Create buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'A', 'B', '+'],
    ['C', 'D', 'E', '='],
    ['F', 'Clear', '⌫', '']
]

# Create buttons
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == '=':
            btn = tk.Button(button_frame, text=text, font=('Arial', 12), 
                          command=calculate, width=5, height=2, bg='lightblue')
        elif text == 'Clear':
            btn = tk.Button(button_frame, text=text, font=('Arial', 12), 
                          command=clear, width=5, height=2, bg='orange')
        elif text == '⌫':
            btn = tk.Button(button_frame, text=text, font=('Arial', 12), 
                          command=backspace, width=5, height=2, bg='yellow')
        elif text == '':
            continue
        else:
            btn = tk.Button(button_frame, text=text, font=('Arial', 12), 
                          command=lambda t=text: button_click(t), width=5, height=2)
        
        btn.grid(row=i, column=j, padx=2, pady=2)

# Instructions
instructions = tk.Label(root, text="Enter hex numbers (0-9, A-F) and operations", 
                       font=('Arial', 10), fg='gray')
instructions.pack(pady=10)

# Run the application
root.mainloop()