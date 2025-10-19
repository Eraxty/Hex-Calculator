# Simple Hexadecimal Calculator
print("=== HEX CALCULATOR CLI ===")
print("Supports +, -, *, /, AND, OR, XOR")
print("Type 'quit' to exit\n")

def hex_to_int(h): return int(h, 16)
def int_to_hex(i): return hex(i).upper()[2:]

while True:
    expr = input("Enter expression (e.g., A + F): ").strip().upper()
    if expr == "QUIT": break

    try:
        parts = expr.split()
        if len(parts) != 3:
            print("❌ Format: A + F\n")
            continue

        a, op, b = parts
        n1, n2 = hex_to_int(a), hex_to_int(b)

        if op == '+': result = n1 + n2
        elif op == '-': result = n1 - n2
        elif op == '*': result = n1 * n2
        elif op == '/':
            if n2 == 0:
                print("❌ Cannot divide by zero!\n")
                continue
            result = n1 // n2
        elif op == 'AND': result = n1 & n2
        elif op == 'OR': result = n1 | n2
        elif op == 'XOR': result = n1 ^ n2
        else:
            print("❌ Unknown operator!\n")
            continue

        print(f"HEX Result: {int_to_hex(result)}")
        print(f"DEC Result: {result}\n" + "-" * 40)
    except Exception:
        print("❌ Invalid input (use hex digits 0–9, A–F)\n")

print("Goodbye 👋")
