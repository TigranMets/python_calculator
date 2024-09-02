import math
import statistics as stats

trigonometric_functions_prompt = "(sin, cos, tan, cot, asin, acos, atan)"
statistical_functions_prompt = "(mean, mode, median, standard deviation, variance)"

menu_prompt = f"""1. Basic Operations(addition, subtraction, multiplication division)
2. Exponentiation
3. Roots
4. Trigonometric Functions {trigonometric_functions_prompt}
5. Statistical Functions {statistical_functions_prompt}: """

menu_option = input(
    f"""Write the index of the calculation option you want to do. Enter menu anytime you want to select option from
the calculator menu. Enter ctrl + c anytime you want to exit. \n\n{menu_prompt}"""
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

        selected_trigonometric_functions = input(f"Enter the trigonometric function you want to calculate {trigonometric_functions_prompt}"
                    "Separate functions using commas if using more then one function(e.g., sin, cos, cot): ").split()
        
        if selected_trigonometric_functions == "menu":
            show_menu()
            continue

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
        
        for function in selected_trigonometric_functions:
            try:
                print(function, ' - ', getattr(math, function.strip())(angle))
            except Exception as e:
                print(f'Invalid input: {e}')        

    elif menu_option == "5":

        data = input(f"Provide values separated by comma (e.g., 10, 5, 8, 299): ")

        if data == "menu":
            show_menu()
            continue

        try:
            data = [float(value) for value in data.split(',') if value.strip()]
        except ValueError:
            print("Error: Please ensure you've entered valid numbers separated by commas. Empty input or non-numeric values are not allowed")
            continue

        selected_statistical_function = input(f"Enter statistical function you want to calculate {statistical_functions_prompt}. "
              "Separate functions using commas if using more then one function(e.g., mean, standard deviation): ")
        
        if selected_statistical_function == "menu":
            show_menu()
            continue

        for function in [value.strip() for value in selected_statistical_function.split(',') if value.strip()]:
            try:
                print(function, ' - ', getattr(stats, function)(data))
            except Exception as e:
                print(f'Invalid input: {e}. Please try again.')
                
    else: 
        print('\nEnter valid option to continue')