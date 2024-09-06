import math
import statistics as stats

trigonometric_functions_prompt = "(sin, cos, tan, cot, asin, acos, atan)"
statistical_functions_prompt = "(mean, mode, median, standard deviation, variance)"

menu_prompt = f"""1. Basic Operations(addition, subtraction, multiplication division)
2. Exponentiation
3. Roots
4. Trigonometric Functions {trigonometric_functions_prompt}
5. Statistical Functions {statistical_functions_prompt}
6. Unit Conversion (e.g., length, weight, temperature): """

menu_option = input(
    f"""Enter the index of the calculation option you want to do. Enter menu anytime you want to select option from
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
        solution = get_numerical_input(
            "Write the equation you want to solve: ")
        if solution != None:
            print(solution)
    elif menu_option == "2":
        base = get_numerical_input("Enter the base number: ")
        if base is None:
            continue
        exponent = get_numerical_input("Enter the exponent: ")
        if exponent is None:
            continue
        print(base**exponent)
    elif menu_option == "3":

        number = get_numerical_input(
            "Enter the number you'd like to find the root of: "
        )
        if number is None:
            continue

        root_degree = get_numerical_input(
            "Enter the degree of the root (e.g., 2 for square root, 3 for cube root): "
        )
        if root_degree is None:
            continue

        print(number ** (1/root_degree))
    elif menu_option == "4":

        selected_trigonometric_functions = input(
            f"Enter the trigonometric function you want to calculate {trigonometric_functions_prompt}"
            "Separate functions using commas if using more then one function(e.g., sin, cos, cot): ").split()

        if selected_trigonometric_functions == "menu":
            show_menu()

        angle_unit_choise = input(
            'Enter the angle unit (radians or degrees): ')
        if angle_unit_choise not in ('radians', 'degrees'):
            angle_unit_choise = input(
                'Invalid input: Enter either "radians" or "degrees": ')

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

        data = input(
            f"Provide values separated by comma (e.g., 10, 5, 8, 299): ")

        if data == "menu":
            show_menu()
            continue

        try:
            data = [float(value) for value in data.split(',') if value.strip()]
        except ValueError:
            print("Error: Please ensure you've entered valid numbers separated by commas. Empty input or non-numeric values are not allowed")
            continue

        selected_statistical_function = input(
            f"Enter statistical function you want to calculate {statistical_functions_prompt}. "
            "Separate functions using commas if using more then one function(e.g., mean, standard deviation): "
        )

        if selected_statistical_function == "menu":
            show_menu()
            continue

        for function in [value.strip() for value in selected_statistical_function.split(',') if value.strip()]:
            try:
                print(function, ' - ', getattr(stats, function)(data))
            except Exception as e:
                print(f'Invalid input: {e}. Please try again.')

    elif menu_option == "6":

        unit_conversion_option = input(
            "\nUnit Conversion Options:"
            "\n1. Length (e.g., meters to feet)"
            "\n2. Weight (e.g., kilograms to pounds)"
            "\n3. Volume (e.g., liters to gallons)"
            "\n4. Temperature (e.g., Celsius to Fahrenheit)"
            "\nPlease enter the number corresponding to your choice: "
        )

        if unit_conversion_option == "menu":
            show_menu()
            continue

        def get_valid_number(prompt, quantity_of_options=None):
            while True:
                try:
                    value = input(prompt)
                    if value == "menu":
                        show_menu()
                        break
                    else:
                        float(value)
                        if quantity_of_options and quantity_of_options > 4:
                            raise Exception('Enter valid option')

                        return value
                except:
                    print(
                        f'\nInvalid input: Make sure you entered valid number')

        def unit_conversion(conversion_option_prompt, conversion_factor):

            conversion_option = get_valid_number(conversion_option_prompt, 4)

            if conversion_option:

                value = get_valid_number(
                    "Enter the value you want to convert: ")

                def convert_unit(conversion_factor):
                    if float(conversion_option) % 2:
                        print(float(value) * conversion_factor)
                    else:
                        print(float(value) / conversion_factor)

                if conversion_option in ("1", "2"):
                    convert_unit(conversion_factor[0])
                elif conversion_option in ("3", "4"):
                    convert_unit(conversion_factor[1])
                elif conversion_option in ("5", "6"):
                    convert_unit(conversion_factor[2])

        if unit_conversion_option == '1':

            unit_conversion(
                "\nEnter the index of length conversion Options:"
                "\n1. Meters to Feet"
                "\n2. Feet to Meters"
                "\n3. Kilometers to Miles"
                "\n4. Miles to Kilometers"
                "\n5. Centimeters to Inches"
                "\n6. Inches to Centimeters"
                "\nPlease enter the number corresponding to your choice: ",
                [3.28084, 0.61371, 0.3937]
            )

        elif unit_conversion_option == '2':

            unit_conversion(
                "\nWeight Conversion Options:"
                "\n1. Kilograms to Pounds"
                "\n2. Pounds to Kilograms"
                "\n3. Grams to Ounces"
                "\n4. Ounces to Grams"
                "\n5. Stones to Kilograms"
                "\n6. Kilograms to Stones"
                "\nPlease enter the number corresponding to your choice: ",
                [2.2, 0.035274, 0.1575]
            )

        elif unit_conversion_option == '3':

            unit_conversion(
                "\nVolume Conversion Options:"
                "\n1. Liters to Gallons"
                "\n2. Gallons to Liters"
                "\n3. Milliliters to Fluid Ounces"
                "\n4. Fluid Ounces to Milliliters"
                "\n5. Cubic Meters to Liters"
                "\n6. Liters to Cubic Meters"
                "\nPlease enter the number corresponding to your choice: ",
                [0.264172, 0.033814, 1000]
            )

        elif unit_conversion_option == '4':

            temperature_convetion_option_prompt = (
                "\nTemperature Conversion Options:"
                "\n1. Celsius to Fahrenheit"
                "\n2. Fahrenheit to Celsius"
                "\n3. Kelvin to Celsius"
                "\n4. Celsius to Kelvin"
                "\n5. Kelvin to Fahrenheit"
                "\n6. Fahrenheit to Kelvin"
                "\nPlease enter the number corresponding to your choice: "
            )

            temperature_convetion_option = get_valid_number(temperature_convetion_option_prompt)

            if temperature_convetion_option == "1":
                value = get_valid_number("Enter the value you want to convert: ")
                print(float(value) * 1.8 + 32)
            elif temperature_convetion_option == "2":
                value = get_valid_number("Enter the value you want to convert: ")
                print((float(value) - 32) / 1.8)
            elif temperature_convetion_option == "3":
                value = get_valid_number("Enter the value you want to convert: ")
                print((float(value) - 273.15))
            elif temperature_convetion_option == "4":
                value = get_valid_number("Enter the value you want to convert: ")
                print((float(value) + 273.15))
            elif temperature_convetion_option == "5":
                value = get_valid_number("Enter the value you want to convert: ")
                print((float(value) - 273.15) * 1.8 + 32)
            elif temperature_convetion_option == "6":
                value = get_valid_number("Enter the value you want to convert: ")
                print((float(value) + 459.67) / 1.8)
            elif temperature_convetion_option == "menu":
                show_menu()
                continue

        else:
            print('\nEnter valid option to continue')
    else:
        print('\nEnter valid option to continue')
        show_menu()