from colorama import Fore
def get_representation(x):
    """
      This function converts a given string x into a list of characters, with a leading '0' added.
      Parameters:
        x (str): A string representing the value.
      Returns: list: A list of characters, where the first character is '0' and the rest are the characters of the input string.
      """
    return ['0'] + list(x)


def compute_multiplication(base, number, multiplier):
    """
      This function performs the multiplication of two numbers in a specified base.
      Parameters:
        base (int): The base in which the multiplication should be performed.
        number (str): The first number to be multiplied.
        multiplier (str): The second number to be multiplied.

      Returns:str: The result of the multiplication as a string.
      """
    list_number = get_representation(number)
    list_carries = ['0' for _ in range(len(list_number))]
    list_answer = ['0' for _ in range(len(list_number))]

    converter = {str(i): i for i in range(10)}
    converter.update({chr(65 + i): 10 + i for i in range(6)})
    converter_inv = {v: k for k, v in converter.items()}

    for i in range(len(list_number) - 1, -1, -1):
        x = converter[list_carries[i]] + converter[list_number[i]] * converter[multiplier]
        list_answer[i] = converter_inv[x % base]
        if i > 0:
            list_carries[i-1] = converter_inv[x // base]

    return ''.join(list_answer).lstrip('0')


def do_multiplication():
    """
      This function reads the input from the user and performs the multiplication of two numbers in a specified base.
      """
    try:
        base = int(input(Fore.LIGHTBLUE_EX+"Choose your base: "))
        number = input(Fore.LIGHTGREEN_EX+"First number:  ")
        multiplier = input(Fore.LIGHTGREEN_EX+"Second number: ")
        print(Fore.LIGHTBLUE_EX+"The product is: "+ Fore.LIGHTYELLOW_EX + compute_multiplication(base, number, multiplier))
        print(Fore.RESET)
    except ValueError:
        print("Invalid base")