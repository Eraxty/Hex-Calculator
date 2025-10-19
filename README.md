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
```

#### 2. `HexCalculatorGUI` Class (Tkinter Version)
```python
# GUI Components
Display panel (hex and decimal)
Hex digit buttons (0-9, A-F)
Operation buttons (+, -, ×, ÷, AND, OR, XOR)
Function buttons (Clear, Backspace, Memory)
```

#### 3. `AdvancedHexCalculator` Class
```python
# Enhanced Features
Memory storage and recall
Operation history tracking
Advanced bitwise operations
Comprehensive error handling
```

---

## 📁 File Structure
```
hex_calculator/
│
├── hex_calculator.py          # CLI version
├── hex_calculator_gui.py      # GUI version
├── advanced_hex_calc.py       # Advanced features
└── README.md                  # Documentation
```

---

## 🚀 Installation & Usage

### Requirements
- Python 3.6 or higher  
- Tkinter (usually included with Python)

### Running the Applications
#### Command Line Version
```bash
python hex_calculator.py
```

#### GUI Version
```bash
python hex_calculator_gui.py
```

---

## 💡 Usage Examples

### Basic Operations
```
Input: A + 5
Output: F

Input: F - A
Output: 5

Input: A * 3
Output: 1E
```

### Bitwise Operations
```
Input: F AND A → A
Input: 5 OR A → F
Input: F XOR A → 5
```

### Complex Expressions
```
Input: (A + 5) * 2 → 1E
Input: F0 AND (A | 5) → A0
```

---

## 🔧 Technical Details

### Number Representation
- Positive numbers: Standard hexadecimal representation  
- Negative numbers: 32-bit two’s complement  
- Range: -2³¹ to 2³¹−1  

### Error Handling
- Division by zero detection  
- Invalid hexadecimal input  
- Expression parsing errors  
- Overflow/underflow handling  

### Memory Management
- 32-bit memory storage  
- Persistent during session  
- Support for memory addition and recall  

---

## 🎨 GUI Features

### Visual Elements
- Dual Display: Hex + Decimal  
- Color-coded buttons for digits, operations, and functions  
- Real-time updates between number systems  
- History panel for recent calculations  

### User Experience
- Intuitive layout  
- Keyboard support  
- Clear error messages  
- Responsive design  

---

## 📊 Use Cases

### Primary Applications
- **Programming & Debugging:** Memory address calculations, bitmasking  
- **Computer Science Education:** Teaching number systems and bitwise logic  
- **Embedded Systems:** Register calculations, hardware programming  
- **Professional Use:** Software dev, electronics, networking, security analysis  

---

## 🔄 Conversion Capabilities
- Hex → Decimal (real-time)  
- Decimal → Hex (on-demand)  
- Binary representation through bitwise operations  
- Two’s complement for negatives  

**Examples**
```
Hex: FFFF → Decimal: 65535
Decimal: -1 → Hex: FFFFFFFF
Hex: 7FFFFFFF → Decimal: 2147483647
```

---

## 🌟 Advanced Features
- History tracking (last 10 operations)  
- Memory register support  
- Customizable bit-size (8, 16, 32, 64-bit)  
- Theme customization for GUI  

---

## 📈 Potential Enhancements
- **Web Interface:** Flask/Django  
- **Mobile App:** Kivy / React Native  
- **Scientific Mode:** Floating-point hex  
- **API Integration:** REST API  
- **Plugin System:** Custom operation support  

---

## 🐛 Error Handling & Validation
- Validates hexadecimal input  
- Syntax and range checks  
- Graceful error recovery  
- State preservation after errors  

---

## 🧩 Summary
This **Hexadecimal Calculator** is a powerful tool for:
- Developers
- Students
- Embedded engineers  
- Security researchers  

Its **dual-interface** design makes it ideal for both **quick calculations** and **in-depth technical analysis**.

---

✨ *Created with Python, logic, and a bit of hex magic.*
