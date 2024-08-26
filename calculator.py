menu_prompt = "1. Basic Operations(addition, subtraction, multiplication division) \n2. Exponentiation: "
menu_option = input(
    f"Write the index of the calculation option you want to do. Enter menu anytime you want to select option from the calculator menu. Enter quit() anytime you want to exit. \n{menu_prompt}"
)

def show_menu():
    global menu_option
    menu_option = input(menu_prompt)

def get_input(prompt):
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
        get_input("Write the equation you want to solve: ")
    elif menu_option == "2":
        base = get_input("Enter the base number: ")
        if base is None:
            continue
        exponent = get_input("Enter the exponent: ")
        if exponent is None:
            continue
        print(base**exponent)
    else: 
        print('\nEnter valid option to continue')
        show_menu()