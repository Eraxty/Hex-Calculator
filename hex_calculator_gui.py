
import tkinter as tk
from tkinter import messagebox


def hex_to_int(hex_str):
    return int(hex_str, 16)

def int_to_hex(num):
    if num < 0:
        num = (1 << 32) + num  
    return hex(num).upper()[2:]


def calculate():
    try:
        expr = display.get().strip().upper()
        expr = expr.replace('×', '*').replace('÷', '/')
        tokens = expr.split()

        if len(tokens) != 3:
            messagebox.showerror("Error", "Use format: A + B")
            return

        a, op, b = tokens
        n1, n2 = hex_to_int(a), hex_to_int(b)

        if op == '+':
            result = n1 + n2
        elif op == '-':
            result = n1 - n2
        elif op == '*':
            result = n1 * n2
        elif op == '/':
            if n2 == 0:
                raise ZeroDivisionError
            result = n1 // n2
        elif op.upper() == 'AND':
            result = n1 & n2
        elif op.upper() == 'OR':
            result = n1 | n2
        elif op.upper() == 'XOR':
            result = n1 ^ n2
        else:
            messagebox.showerror("Error", "Invalid operator!")
            return

        display.set(int_to_hex(result))

    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")
        display.set("0")
    except Exception:
        messagebox.showerror("Error", "Invalid input!")
        display.set("0")

def insert(value):
    current = display.get()
    if current == "0":
        display.set(value)
    else:
        display.set(current + value)

def clear():
    display.set("0")

def backspace():
    current = display.get()
    display.set(current[:-1] if len(current) > 1 else "0")


root = tk.Tk()
root.title("Hexadecimal Calculator")
root.geometry("340x480")
root.resizable(False, False)

display = tk.StringVar(value="0")

entry = tk.Entry(root, textvariable=display, font=('Consolas', 18),
                 justify='right', bd=10, relief='sunken')
entry.pack(fill='x', padx=10, pady=15)

frame = tk.Frame(root)
frame.pack()

buttons = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', '7', '8'],
    ['9', '4', '5', '6'],
    ['1', '2', '3', '0'],
    ['+', '-', '×', '÷'],
    ['AND', 'OR', 'XOR', '='],
    ['⌫', 'Clear']
]

for r, row in enumerate(buttons):
    for c, val in enumerate(row):
        cmd = None
        if val == '=':
            cmd = calculate
        elif val == 'Clear':
            cmd = clear
        elif val == '⌫':
            cmd = backspace
        else:
            cmd = lambda v=val: insert(f" {v} " if v in ['+', '-', '×', '÷', 'AND', 'OR', 'XOR'] else v)
        
        tk.Button(frame, text=val, width=6, height=2, font=('Arial', 12),
                  bg='#e0e0e0' if val not in ['Clear', '='] else '#6cf' if val == '=' else '#f96',
                  command=cmd).grid(row=r, column=c, padx=3, pady=3)

tk.Label(root, text="Supports +, -, ×, ÷, AND, OR, XOR", fg='gray').pack(pady=5)
root.mainloop()
