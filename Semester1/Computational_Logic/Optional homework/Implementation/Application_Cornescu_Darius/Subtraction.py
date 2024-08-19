from colorama import Fore
def get_representation(x, y):
    """
    This function converts two given strings x and y into strings of the same length by left-padding them with leading zeros.

    Parameters:
      x (str): A string representing the first value.
      y (str): A string representing the second value.

    Returns: tuple: A tuple of two strings, where both strings are left-padded with leading zeros to have the same
        length as the longer input string.
    """
    max_len = max(len(x), len(y)) + 1
    return x.zfill(max_len), y.zfill(max_len)


def compute_subtraction(base, number1, number2):
    """
    This function performs the subtraction of two numbers in a specified base.

    Parameters:
      base (int): The base in which the subtraction should be performed.
      number1 (str): The minuend.
      number2 (str): The subtrahend.

    Returns: str: The result of the subtraction as a string.
    """
    list_first, list_second = get_representation(number1, number2)
    list_borrows = [0 for _ in range(len(list_first))]
    list_answer = ['0' for _ in range(len(list_first))]

    converter = {str(i): i for i in range(10)}
    converter.update({chr(65 + i): 10 + i for i in range(6)})
    converter_inv = {v: k for k, v in converter.items()}

    for i in range(len(list_first) - 1, -1, -1):
        x = list_borrows[i] + converter[list_first[i]] - converter[list_second[i]]
        if x >= 0:
            list_answer[i] = converter_inv[x]
        else:
            list_borrows[i-1] = -1
            list_answer[i] = converter_inv[base + x]

    return ''.join(list_answer).lstrip('0')


def do_subtraction():
    """
    This function performs the subtraction of two numbers based on user inputs.
    Returns: None
    """
    try:
        base = int(input(Fore.LIGHTBLUE_EX+"Choose your base: "))
        number1 = input(Fore.LIGHTGREEN_EX+"First number:  ")
        number2 = input(Fore.LIGHTGREEN_EX+"Second number: ")
        print(Fore.LIGHTBLUE_EX+"The difference is: "+ Fore.LIGHTYELLOW_EX + compute_subtraction(base, number1, number2))
        print(Fore.RESET)
    except ValueError:
        print("Invalid base")