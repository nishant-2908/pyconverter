from quantity import *
import sys


def take_input_as_numeric(
    message: str = "Enter the number",
    error_message: str = "Please enter a valid number",
    negative_allowed: bool = False,
    decimal_allowed: bool = True,
    zero: bool = False,
):
    """
    Takes input from the user as integer
    Parameters:
    message (str) - The message to be displayed to the user
    error_message (str) - The error message to be displayed to the user
    negative_allowed (bool) - Whether negative numbers are allowed or not
    Returns:
    int - The integer entered by the user
    """

    # Running a while Loop
    while True:

        # Getting the input from the user while displaying the message
        userinput = input(message)

        # Try-except block
        try:

            # Try to convert to decimal
            decimal_value = float(userinput)

            # If zero is allowed and the decimal value is zero itself
            if zero and decimal_value == 0:

                # Return the decimal of the userinput
                return decimal_value

            # If the negative allowed is allowed
            if negative_allowed:

                # If the decimal is allowed
                if decimal_allowed:

                    # Return the decimal value
                    return decimal_value

                # If decimal value is not allowed
                else:

                    # If the decimal value is an integer
                    if decimal_value == int(decimal_value):

                        # Return the integer of the decimal value
                        return int(decimal_value)

                    # If the decimal value is an not integer
                    else:

                        # Print the error message
                        print(error_message)

            # If the negative allowed is not allowed
            else:

                # If decimal is allowed
                if decimal_allowed:

                    # Return the decimal value
                    return decimal_value

                # If decimal is not allowed
                else:

                    # If the decimal value is an integer
                    if decimal_value == int(decimal_value):

                        # Return an integral value of the decimal
                        return int(decimal_value)

                    # If decimal value is not an integer
                    else:

                        # Print an error message
                        print(error_message)

        # If the operation faces ValueError
        except ValueError:

            # Print the error message
            print(error_message)


def input_in_options(
    message: str,
    options: list,
    error_message: str = "Invalid option",
):
    """
    Asks for the input from a given option
    If the userinput is not in the given options, it asks for the input again
    """

    # Running a while loop
    while True:

        # Getting the input from the user
        userinput = input(message)

        # If the lower case of the userinput is not in the list generated by lowercasing all the options of the given list
        if userinput.lower().strip() in [str(option).lower() for option in options]:

            # Return the userinput
            return userinput

        # Else
        else:

            # Print the error message
            print(error_message)


# Defining a list to convert the quantities
converters = [
    "Length",
    "Weight",
    "Area",
    "Temperature",
    "Volume",
    "Time",
    "Power",
    "Speed",
    "Pressure",
]


def main():
    # Printing the welcome message
    print("Welcome to PyConverters! \n")

    # For i and k in enumeration of converters
    for i, k in enumerate(converters):

        # Printing the message
        print(f"{i+1}. {k}")

    # Getting the input
    quantity_input = input_in_options(
        "\nEnter the serial number of the quantity: ",
        options=[str(i + 1) for i in range(len(converters))],
    )

    # Getting the quantity
    quantity_user = converters[int(quantity_input) - 1]

    # Getting the list of the units for the selected quantity
    if quantity_user == "Length":
        quantity_selected = length
    elif quantity_user == "Weight":
        quantity_selected = weight
    elif quantity_user == "Area":
        quantity_selected = area
    elif quantity_user == "Temperature":
        quantity_selected = temperature
    elif quantity_user == "Volume":
        quantity_selected = volume
    elif quantity_user == "Time":
        quantity_selected = time
    elif quantity_user == "Power":
        quantity_selected = power
    elif quantity_user == "Speed":
        quantity_selected = speed
    elif quantity_user == "Pressure":
        quantity_selected = pressure

    # Printing the supported units for the selected quantity
    for i, k in enumerate(quantity_selected):
        print(f"{i+1}. {k.name.capitalize()} ({k.prefix})")

    # Getting the serial number for the unit
    unit_selected = input_in_options(
        "\nEnter the serial number of the first unit: ",
        options=[str(i + 1) for i in range(len(quantity_selected))],
    )

    # Getting the unit
    unit_user = quantity_selected[int(unit_selected) - 1]

    # Asking the user for the number to convert
    number = take_input_as_numeric(
        "Enter the number to convert: ",
        "Invalid number",
    )

    # Converting the number of the user's entered quantity to SI unit
    si_unit_converted = number * unit_user.conversion_to_si

    # Printing a blank line
    print()

    # Now, converting SI to each unit
    for i, k in enumerate(quantity_selected):

        # If the iterator is the unit selected by the user
        if k.name == unit_user.name:

            # Just, continue
            continue

        # Print the conversion along with the unit
        print(
            f"{k.name.capitalize()} ({k.prefix}) = {si_unit_converted * k.si_to_unit}"
        )

    print()


# If the main function is executed as a file
if __name__ == "__main__":

    # Try-except block
    try:

        # Running the main function
        main()

        # Exiting the program with a zero exit code
        sys.exit(0)

    # If the user exits the program using Keyboard (Ctrl C)
    except KeyboardInterrupt:

        # Printing an error message
        print("You exited the program \n")

        # Exiting the program with a non-zero exit code
        sys.exit(1)