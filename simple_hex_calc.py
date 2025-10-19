# Simple Hexadecimal Calculator - Beginner Version
print("=== SIMPLE HEX CALCULATOR ===")
print("Type 'quit' to exit")

def hex_to_int(hex_num):
    """Convert hexadecimal to integer"""
    return int(hex_num, 16)

def int_to_hex(num):
    """Convert integer to hexadecimal"""
    return hex(num).upper()[2:]

while True:
    try:
        # Get first number
        num1 = input("Enter first hex number: ").strip().upper()
        if num1.lower() == 'quit':
            break
            
        # Get operator
        operator = input("Enter operator (+, -, *, /): ").strip()
        if operator.lower() == 'quit':
            break
            
        # Get second number
        num2 = input("Enter second hex number: ").strip().upper()
        if num2.lower() == 'quit':
            break
        
        # Convert to integers
        n1 = hex_to_int(num1)
        n2 = hex_to_int(num2)
        
        # Perform calculation
        if operator == '+':
            result = n1 + n2
        elif operator == '-':
            result = n1 - n2
        elif operator == '*':
            result = n1 * n2
        elif operator == '/':
            if n2 == 0:
                print("Error: Cannot divide by zero!")
                continue
            result = n1 // n2  # Integer division
        else:
            print("Error: Invalid operator! Use +, -, *, or /")
            continue
        
        # Convert back to hex and display
        hex_result = int_to_hex(result)
        print(f"Result: {num1} {operator} {num2} = {hex_result}")
        print(f"Decimal: {n1} {operator} {n2} = {result}")
        print("-" * 40)
        
    except ValueError:
        print("Error: Please enter valid hexadecimal numbers (0-9, A-F)")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        break

print("Thank you for using the Hex Calculator!")