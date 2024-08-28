import math

menu_prompt = """1. Basic Operations(addition, subtraction, multiplication division)
2. Exponentiation
3. Roots
4. Trigonometric Functions (sin, cos, tan, cot, asin, acos, atan): """
menu_option = input(
    f"""Write the index of the calculation option you want to do. Enter menu anytime you want to select option from
the calculator menu. Enter quit() anytime you want to exit. \n\n{menu_prompt}"""
)

def show_menu():
    global menu_option
    menu_option = input(menu_prompt)

def get_numerical_input(prompt):
    user_input = input(prompt)

    if user_input == "menu":
        show_menu()
    else:
        try:
            return eval(user_input)
        except Exception as e:
            print(f"Invalid input: {e}. Please try again.")

while True:
    if menu_option == "1":
        get_numerical_input("Write the equation you want to solve: ")
    elif menu_option == "2":
        base = get_numerical_input("Enter the base number: ")
        if base is None:
            continue
        exponent = get_numerical_input("Enter the exponent: ")
        if exponent is None:
            continue
        print(base**exponent)
    elif menu_option == "3":
        number = get_numerical_input("Enter the number you'd like to find the root of: ")
        if number is None:
            continue
        root_degree = get_numerical_input("Enter the degree of the root (e.g., 2 for square root, 3 for cube root): ")
        if root_degree is None:
            continue

        print(number ** (1/root_degree))
    elif menu_option == "4":
        trigonometric_function_type = input("""Enter the trigonometric function you want to calculate (sin, cos, tan, cot, asin, acos, atan): """)
        if trigonometric_function_type == "menu":
            show_menu()
            continue
        elif trigonometric_function_type not in ("sin", "cos", "tan", "asin", "acos", "atan"):
            trigonometric_function_type = input('Invalid input: Enter either "sin", "cos", "tan", "asin", "acos", "atan": ')

        angle_unit_choise = input('Enter the angle unit (radians or degrees): ')
        if angle_unit_choise not in ('radians', 'degrees'):
            angle_unit_choise = input('Invalid input: Enter either "radians" or "degrees": ')

        angle = get_numerical_input('Enter the angle value: ')
        if angle == None:
            continue
        elif type(angle) not in (int, float):
            get_numerical_input('Enter valid angle value: ')

        if angle_unit_choise == 'degrees':
            angle = math.radians(angle)
        
        if trigonometric_function_type == 'sin':
            print(math.sin(angle))
        elif trigonometric_function_type == 'cos':
            print(math.cos(angle))
        elif trigonometric_function_type == 'tan':
            print(math.tan(angle))
        elif trigonometric_function_type == 'cot':
            print(1 / math.tan(angle))
        elif trigonometric_function_type == 'asin':
            if -1 <= angle <= 1:
                print(math.asin(angle))
            else:
                print('"Error: Input value is out of range for asin function."')
        elif trigonometric_function_type == 'acos':
            if -1 <= angle <= 1:
                print(math.asin(angle))
            else:
                print("Error: Input value is out of range for acos function.")
        elif trigonometric_function_type == 'atan':
            print(math.atan(angle))
    else: 
        print('\nEnter valid option to continue')
        show_menu()