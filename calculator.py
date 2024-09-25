import math
import statistics as stats
from currencies_dictionary import currencies
import http.client
import json

INPUT_INSTRUCTION = "\nPlease enter the number corresponding to your choice: "
TRIGONOMETRIC_FUNCTIONS_PROMPT = "(sin, cos, tan, cot, asin, acos, atan, acot)"
STATISTICAL_FUNCTIONS_PROMPT = "(mean, mode, median, standard deviation, variance)"

menu_prompt = f"""1. Basic Operations(addition, subtraction, multiplication division)
2. Exponentiation
3. Roots
4. Trigonometric Functions {TRIGONOMETRIC_FUNCTIONS_PROMPT}
5. Statistical Functions {STATISTICAL_FUNCTIONS_PROMPT}
6. Conversions (e.g., length, weight, temperature, currency)
7. History
8. Settings: """

menu_option = input(
    f"""Enter the index of the calculation option you want to do. Enter menu anytime you want to select option from
the calculator menu. Enter ctrl + c anytime you want to exit. \n\n{menu_prompt}"""
)


def show_menu():
    global menu_option
    menu_option = input(menu_prompt)


def get_numerical_input(prompt):
    while True:
        try:
            user_input = input(prompt)

            if user_input == "menu":
                show_menu()
                break
            else:
                return eval(user_input)
        except Exception as e:
            print(f"Invalid input: {e}. Please try again.")


def get_input(prompt):
    while True:
        user_input = input(prompt)

        if user_input == "menu":
            show_menu()
            break
        else:
            return user_input


def commit_result(result, expression):
    with open('calculation_history.txt', 'a+') as file:
        file.seek(0)
        if file.readline().strip() == 'True' and float(file.readline()) >= sum(1 for line in file) + 2:
            file.write(f"\n{expression} {str(result)}")
        print(result)


while True:

    if menu_option == "1":
        while True:
            try:
                user_input = input('Write the equation you want to solve: ')

                if user_input == "menu":
                    show_menu()
                    break
                else:
                    commit_result(eval(user_input), user_input + ' =')
            except Exception as e:
                print(f"Invalid input: {e}. Please try again.")

    elif menu_option == "2":
        base = get_numerical_input("Enter the base number: ")
        if base is None:
            continue

        exponent = get_numerical_input("Enter the exponent: ")
        if exponent is None:
            continue

        commit_result(base**exponent, f'{base} to the power of {exponent} =')
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

        commit_result(number ** (1/root_degree),
                      f"The root of {number} with power {root_degree} ="
                      )
    elif menu_option == "4":
        print(menu_option)
        selected_trigonometric_functions = input(
            f"Enter the trigonometric function you want to calculate {TRIGONOMETRIC_FUNCTIONS_PROMPT}"
            " Separate functions using commas if using more then one function(e.g., sin, cos, cot): ").split(',')

        if 'menu' in selected_trigonometric_functions:
            show_menu()
            continue

        angle_unit_choise = input(
            'Enter the angle unit (radians or degrees): '
        )

        if angle_unit_choise == "menu":
            show_menu()
            continue
        elif angle_unit_choise not in ('radians', 'degrees'):
            angle_unit_choise = input(
                'Invalid input: Enter either "radians" or "degrees": '
            )

        angle = get_numerical_input('Enter the angle value: ')
        if angle is None:
            continue
        elif type(angle) not in (int, float):
            get_numerical_input('Enter valid angle value: ')

        if angle_unit_choise == 'degrees':
            angle = math.radians(angle)

        for function in selected_trigonometric_functions:
            try:
                stripped_function = function.strip()
                commit_result(
                    stripped_function + ' = ' + str(1/math.tan(angle) if stripped_function == 'cot'
                                                    else 1/math.tan(angle) if stripped_function == 'acot'
                                                    else getattr(math, stripped_function)(angle)),
                    f"{angle} {angle_unit_choise}"
                )
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
            f"Enter statistical function you want to calculate {STATISTICAL_FUNCTIONS_PROMPT}. "
            "Separate functions using commas if using more then one function(e.g., mean, standard deviation): "
        )

        if selected_statistical_function == "menu":
            show_menu()
            continue

        for function in [value.strip() for value in selected_statistical_function.split(',') if value.strip()]:
            try:
                commit_result(f"{function} - {getattr(stats, function)(data) if function != 'standard deviation' else stats.stdev(data)}",
                              f"Data Set - {data}")
            except Exception as e:
                print(f'Invalid input: {e}. Please try again.')

    elif menu_option == "6":

        conversion_option = input(
            "\nUnit Conversion Options:"
            "\n1. Length (e.g., meters to feet)"
            "\n2. Weight (e.g., kilograms to pounds)"
            "\n3. Volume (e.g., liters to gallons)"
            "\n4. Temperature (e.g., Celsius to Fahrenheit)"
            "\n5. Currency (e.g., USD to AMD)" +
            INPUT_INSTRUCTION
        )

        if conversion_option == "menu":
            show_menu()
            continue

        def unit_conversion(conversion_option_prompt, conversion_data):

            conversion_option = get_numerical_input(
                conversion_option_prompt + INPUT_INSTRUCTION
            )

            if conversion_option < 7:
                while True:
                    value = get_numerical_input(
                        "Enter the value you want to convert: ")

                    def convert_unit(conversion_data):
                        if conversion_option % 2:
                            commit_result(
                                value * conversion_data['conversionFactor'],
                                f"{value} {conversion_data['firstUnit']} converted to {conversion_data['secondUnit']} ="
                            )
                        else:
                            commit_result(
                                value / conversion_data['conversionFactor'],
                                f"{value} {conversion_data['secondUnit']} converted to {conversion_data['firstUnit']} ="
                            )

                    if conversion_option in (1, 2):
                        convert_unit(conversion_data[0])
                        break
                    elif conversion_option in (3, 4):
                        convert_unit(conversion_data[1])
                        break
                    elif conversion_option in (5, 6):
                        convert_unit(conversion_data[2])
                        break
            else:
                print('\nEnter valid option to continue')

        if conversion_option == '1':

            unit_conversion(
                "\nEnter the index of length conversion Options:"
                "\n1. Meters to Feet"
                "\n2. Feet to Meters"
                "\n3. Kilometers to Miles"
                "\n4. Miles to Kilometers"
                "\n5. Centimeters to Inches"
                "\n6. Inches to Centimeters",
                [
                    {'firstUnit': 'meters', 'secondUnit': 'feet',
                        'conversionFactor': 3.28084},
                    {'firstUnit': 'kilometers', 'secondUnit': 'miles',
                        'conversionFactor': 0.61371},
                    {'firstUnit': 'centimeters', 'secondUnit': 'inches',
                        'conversionFactor': 0.3937}
                ]
            )

        elif conversion_option == '2':

            unit_conversion(
                "\nWeight Conversion Options:"
                "\n1. Kilograms to Pounds"
                "\n2. Pounds to Kilograms"
                "\n3. Grams to Ounces"
                "\n4. Ounces to Grams"
                "\n5. Stones to Kilograms"
                "\n6. Kilograms to Stones",
                [
                    {'firstUnit': 'kilograms', 'secondUnit': 'pounds',
                        'conversionFactor': 2.2},
                    {'firstUnit': 'grams', 'secondUnit': 'ounces',
                        'conversionFactor': 0.035274},
                    {'firstUnit': 'stones', 'secondUnit': 'kilograms',
                        'conversionFactor': 0.1575}
                ]
            )

        elif conversion_option == '3':

            unit_conversion(
                "\nVolume Conversion Options:"
                "\n1. Liters to Gallons"
                "\n2. Gallons to Liters"
                "\n3. Milliliters to Fluid Ounces"
                "\n4. Fluid Ounces to Milliliters"
                "\n5. Cubic Meters to Liters"
                "\n6. Liters to Cubic Meters",
                [
                    {'firstUnit': 'liters', 'secondUnit': 'gallons',
                     'conversionFactor': 0.264172},
                    {'firstUnit': 'milliliters', 'secondUnit': 'fluid ounces',
                     'conversionFactor': 0.033814},
                    {'firstUnit': 'cubic meters', 'secondUnit': 'liters',
                     'conversionFactor': 1000}
                ]
            )

        elif conversion_option == '4':
            temperature_convetion_option = get_numerical_input(
                "\nTemperature Conversion Options:"
                "\n1. Celsius to Fahrenheit"
                "\n2. Fahrenheit to Celsius"
                "\n3. Kelvin to Celsius"
                "\n4. Celsius to Kelvin"
                "\n5. Kelvin to Fahrenheit"
                "\n6. Fahrenheit to Kelvin" +
                INPUT_INSTRUCTION
            )

            value = get_numerical_input(
                "Enter the value you want to convert: ")

            if temperature_convetion_option == 1:
                commit_result(value * 1.8 + 32,
                              f'{value} degrees Celsius to Fahrenheit =')
            elif temperature_convetion_option == 2:
                commit_result((value - 32) / 1.8,
                              f'{value} degrees Fahrenheit to Celsius =')
            elif temperature_convetion_option == 3:
                commit_result(value - 273.15,
                              f'{value} degrees Kelvin to Celsius =')
            elif temperature_convetion_option == 4:
                commit_result(value + 273.15,
                              f'{value} degrees Celsius to Kelvin =')
            elif temperature_convetion_option == 5:
                commit_result((value - 273.15) * 1.8 + 32,
                              f'{value} degrees Kelvin to Fahrenheit =')
            elif temperature_convetion_option == 6:
                commit_result((value + 459.67) / 1.8,
                              f'{value} degrees Fahrenheit to Kelvin =')
            elif temperature_convetion_option == "menu":
                show_menu()
                continue
            else:
                print('\nEnter valid option to continue')
        elif conversion_option == '5':
            base_currency = input(
            "\nWrite the currency name you want to convert (e.g., US Dollar): "
            ).lower()

            matched_base_currency = next(
                (key for key, value in currencies.items()
                 if any(base_currency.strip() in currency.lower() for country, currency in value.items())),
                'USD'
            )

            amount = get_numerical_input('\nEnter the amount: ')

            quote_currencies = input(
                '\nWrite the names of the currencies you want to convert to, separated by commas(e.g., dram, East Caribbean Dollar, Mexican Peso): '
            ).lower().split(',')

            matched_quote_currencies = ','.join([
                key for key, country_currency in currencies.items()
                if any(search_text.strip() in currency.lower() for search_text in quote_currencies
                       for country, currency in country_currency.items())
            ])

            if matched_quote_currencies:
                conn = http.client.HTTPSConnection("openexchangerates.org")

                conn.request(
                    "GET",
                    f"/api/latest.json?app_id=99c063e4313747869864128d6b993d43&base=USD&currencies={matched_quote_currencies + ',' + matched_base_currency}"
                )

                rates = json.loads(conn.getresponse().read().decode())['rates']

                for currency_code, value in rates.items():
                    currency_name = list(currencies[currency_code].values())[0]
                    commit_result(f"{value / rates[matched_base_currency] * amount} {currency_name}",
                                  f"{amount} {base_currency.title()} = ")

                conn.close()
            else: 
                print('No matching currencies found. Please try again.')
        else:
            print('\nEnter valid option to continue')

    elif menu_option == '7':
        with open('calculation_history.txt', "r") as file:
            line_number = 0
            for line in file.readlines()[2:]:
                line_number += 1
                print(f'\n{line_number}. {line}\n')
        show_menu()

    elif menu_option == "8":
        settings_option = input(
            "\n1. Enable history"
            "\n2. Disable history"
            "\n3. Set the limit of history items to keep(e.g., 10, 35, 100)"
            "\n4. Exit settings" +
            INPUT_INSTRUCTION
        )

        if settings_option in ("4", "menu"):
            show_menu()
        else:
            with open('calculation_history.txt', "r+") as file:
                lines = file.readlines()

                def file_reset_and_update(update_message):
                    file.seek(0)
                    print(lines)
                    file.truncate()
                    file.writelines(lines)
                    print(update_message)

                if settings_option == "1":
                    lines[0] = 'True\n'
                    file_reset_and_update('The history is enabled!')
                elif settings_option == "2":
                    lines[0] = 'False\n'
                    file_reset_and_update('The history is disabled!')
                elif settings_option == "3":
                    limit = str(get_numerical_input('Enter the limit: '))
                    lines[1] = limit
                    file_reset_and_update(f'Limit successfully set to {limit}')
                else:
                    print('\nEnter valid option to continue')
    else:
        print('\nEnter valid option to continue')
        show_menu()
