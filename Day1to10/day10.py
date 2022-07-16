#functions with outputs


def print_operations():
    print("+")
    print("-")
    print("*")
    print("/")

def perform_operation(a, b):
    if operation_choice == "+":
        return a + b
    elif operation_choice == "-":
        return a - b
    elif operation_choice == "*":
        return a * b
    elif operation_choice == "/":
        return a / b
    else:
        return "Invalid operation selection"

num_first = int(input("What's the first number?: "))
print_operations()
operation_choice = input("Pick an operation: ")
num_second = int(input("What's the next number?: "))

continue_calculating = True

print(f"{num_first} {operation_choice} {num_second} = {perform_operation(num_first, num_second)}")
continue_choice = input(f"Type 'y' to continue calculating with {perform_operation(num_first, num_second)}, or type 'n' to start a new calculation:")
if continue_choice == "n":
    continue_calculating = False
    print("Thank you for using the calculator")


while continue_calculating == True:
    num_first = perform_operation(num_first, num_second)
    print_operations()
    operation_choice = input("Pick an operation: ")
    num_second = int(input("What's the next number?: "))
    perform_operation(num_first, num_second)
    print(f"{num_first} {operation_choice} {num_second} = {perform_operation(num_first, num_second)}")
    continue_choice = input(f"Type 'y' to continue calculating with {perform_operation(num_first, num_second)}, or type 'n' to start a new calculation:")
    if continue_choice == "n":
        continue_calculating = False
        print("Thank you for using the calculator")

