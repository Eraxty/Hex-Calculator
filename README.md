# 🔢 Hexadecimal Calculator

## 📋 Project Overview
A comprehensive **hexadecimal calculator** implementation that performs **arithmetic** and **bitwise operations** on hexadecimal numbers.  
Available in both **Command-Line Interface (CLI)** and **Graphical User Interface (GUI)** versions.

---

## 🎯 Features

### ⚙️ Core Functionality
#### Hexadecimal Arithmetic
- Addition, Subtraction, Multiplication, Division  
- Power operations  
- Parentheses support for complex expressions  

#### Bitwise Operations
- AND, OR, XOR operations  
- Bitwise NOT (complement)  
- Left and Right shift operations  

#### Number System Conversion
- Real-time hex ↔ decimal conversion  
- Support for negative numbers (two’s complement)

---

## 💾 Advanced Features

### 🧠 Memory Operations
- Store, recall, and add to memory  
- Persistent memory during session  

### 🕓 Calculation History
- Track last 10 operations  
- View complete operation history  
- Error logging and handling  

### 🖥️ User Interface
- Clean, intuitive GUI with **Tkinter**  
- Command-line interface for quick operations  
- Real-time display updates  
- Error messages and validation  

---

## 🛠️ Technical Specifications

### Components

#### 1. `HexCalculator` Class (CLI Version)
```python
# Core methods
add(), subtract(), multiply(), divide()
bitwise_and(), bitwise_or(), bitwise_xor()
power(), left_shift(), right_shift()
hex_to_int(), int_to_hex()


# GUI Components
Display panel (hex and decimal)
Hex digit buttons (0-9, A-F)
Operation buttons (+, -, ×, ÷, AND, OR, XOR)
Function buttons (Clear, Backspace, Memory)
