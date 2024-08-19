from colorama import Fore
def get_representation_for_operations(x):
    '''
    This function converts a given string x into a list of its individual characters, adding a '0' at the beginning.
    Parameters:
      x (str): A string representing the value.

    Returns: list: A list of characters from the input string, with a leading '0'.
    '''
    return ['0'] + list(x)


def char_to_int(char):
    '''
    This function converts a character into its corresponding integer value.
    Parameters:
      char (str): A single character.

    Returns: int: The integer value of the character.
    '''
    if char.isdigit():
        return int(char)
    else:
        return 10 + ord(char) - ord('A')


def int_to_char(int_value):
    '''
    This function converts an integer into its corresponding character value.
    Parameters:
      int_value (int): An integer.

    Returns:
    str: The character value of the integer.
    '''
    if int_value < 10:
        return str(int_value)
    else:
        return chr(ord('A') + int_value - 10)


def multiplication(base, number, multiplier):
    '''
    This function performs multiplication of two numbers represented in a given base.
    It uses lists for the representation of the numbers and the intermediate result.

    Parameters:
      base (int): The base of the number system used for computation.
      number (str): The first number to be multiplied.
      multiplier (str): The second number to be multiplied.

    Returns: str: The product of number and multiplier, represented in the specified base.
    '''
    list_number = get_representation_for_operations(number)
    list_carries = ['0' for _ in range(len(list_number))]
    list_answer = ['0' for _ in range(len(list_number))]

    for i in range(len(list_number) - 1, -1, -1):
        x = char_to_int(list_carries[i]) + char_to_int(list_number[i]) * char_to_int(multiplier)
        list_answer[i] = int_to_char(x % base)
        if i > 0:
            list_carries[i - 1] = int_to_char(x // base)

    answer = ''.join([digit for digit in list_answer if digit != '0'])

    return answer


def sum(base, number, number2):
    '''
    This function performs addition of two numbers represented in a given base.
    It uses lists for the representation of the numbers and the intermediate result.

    Parameters:
      base (int): The base of the number system used for computation.
      number (str): The first number to be added.
      number2 (str): The second number to be added.

    Returns: str: The sum of number and number2, represented in the specified base.
    '''
    list_number = get_representation_for_operations(number)
    list_second = get_representation_for_operations(number2)

    max_len = max(len(list_number), len(list_second))
    list_number = (['0'] * (max_len - len(list_number))) + list_number
    list_second = (['0'] * (max_len - len(list_second))) + list_second

    list_carries = ['0' for _ in range(len(list_number))]
    list_answer = ['0' for _ in range(len(list_number))]

    for i in range(max_len - 1, -1, -1):
        x = char_to_int(list_carries[i]) + char_to_int(list_number[i]) + char_to_int(list_second[i])
        list_answer[i] = int_to_char(x % base)
        list_carries[i - 1] = int_to_char(x // base)

    answer = ''.join([digit for digit in list_answer if digit != '0'])

    return answer


def substitution(x, base1, base2):
    '''
    This function performs substitution to convert a number from one base (base1) to another base (base2).
    It uses multiplication and addition operations to perform the conversion.

    Parameters:
      x (str): The number to be converted.
      base1 (int): The base of the number system in which the number is currently represented.
      base2 (int): The base of the number system to which the number is to be converted.

    Returns: str: The number represented in base2.
    '''
    if base1 != 10:
        list_number = get_representation_for_operations(x)
        power = '1'
        current_answer = ""

        for i, val in enumerate(list_number[::-1]):
            current_number = multiplication(base2, power, val)
            current_answer = sum(base2, current_answer, current_number)
            power = multiplication(base2, power, str(base1))

        copy_answer = current_answer.lstrip('0')
        return copy_answer if copy_answer else '0'

    else:
        hex_chars = "0123456789ABCDEF"
        answer = ""
        while x > 0:
            remainder = x % 16
            answer += hex_chars[remainder]
            x //= 16
        return (answer if answer else "0")[::-1]