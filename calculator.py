import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def power(x, y):
    return math.pow(x, y)

def main():
    print("--- ⚡ Aris Calc 2.0 ⚡ ---")
    print("Available operations: +, -, *, /, ^, exit")
    
    while True:
        try:
            user_input = input("\nEnter calculation (e.g., 5 + 3) or 'exit': ").strip()
            if user_input.lower() == 'exit':
                print("Bye! ⚡")
                break
            
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid format. Please use: <number> <operator> <number>")
                continue
            
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
            
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            elif operator == '^':
                result = power(num1, num2)
            else:
                print("Unknown operator! Use +, -, *, /, or ^")
                continue
            
            # Format result to remove .0 if it's an integer
            if result == int(result):
                result = int(result)
                
            print(f"Result: {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
