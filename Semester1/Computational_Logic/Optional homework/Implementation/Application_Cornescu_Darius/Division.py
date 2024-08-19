from colorama import Fore
def get_representation(x):
    """
    This function converts a given string x into a list of characters.
    Parameters:
      x (str): A string representing the value.

    Returns: list: A list of characters from the input string.
    """
    return list(x)


def compute_division(base, number, divizor):
    """
    This function performs the division of two numbers in a specified base.
    Parameters:
      base (int): The base in which the division should be performed.
      number (str): The dividend.
      divizor (str): The divisor.

    Returns: tuple: The result of the division as a string (quotient, remainder).
    """
    list_number = get_representation(number)
    carrie = '0'
    list_answer = []

    converter = {str(i): i for i in range(10)}
    converter.update({chr(65 + i): 10 + i for i in range(6)})
    converter_inv = {v: k for k, v in converter.items()}

    for i in range(len(list_number)):
        x = converter[carrie]*base + converter[list_number[i]]
        list_answer.append(converter_inv[x // converter[divizor]])
        carrie = converter_inv[x % converter[divizor]]

    answer = ''.join(list_answer).lstrip('0')

    return (answer, carrie)


def do_division():
    """
    This function performs the division of two numbers based on user inputs.
    Returns: None
    """
    try:
        base = int(input(Fore.LIGHTBLUE_EX+"Choose your base: "))
        number = input(Fore.LIGHTGREEN_EX+"First number:  ")
        divizor = input(Fore.LIGHTGREEN_EX+"Second number: ")
        quotient, remainder = compute_division(base, number, divizor)
        print(Fore.LIGHTYELLOW_EX+"The quotient is ", quotient)
        print(Fore.LIGHTYELLOW_EX+"The reminder is ", remainder)
        print(Fore.RESET)
    except ValueError:
        print("Invalid base")

