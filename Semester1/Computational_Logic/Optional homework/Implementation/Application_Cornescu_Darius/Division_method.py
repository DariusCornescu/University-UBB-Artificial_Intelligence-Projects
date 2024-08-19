from colorama import Fore
from Utils import *

def division(base, number, divizor):
    '''
    This function performs the division of a number represented in a given base by another number.
    It utilizes a list to store the individual digits of the quotient and a variable for the remainder.
    Parameters:
      base (int): The base of the number system used for computation.
      number (str): The dividend.
      divizor (str): The divisor.

    Returns: tuple: The result of the division as a string (quotient, remainder).
    '''
    list_number = get_representation_as_list(number)
    carrie = '0'
    list_answer = []

    for i in range(len(list_number)):
        x = int(carrie) * base + int(list_number[i])
        list_answer.append(str(x // int(divizor)))
        carrie = str(x % int(divizor))

    answer = ''.join(list_answer).lstrip('0') or '0'
    return (answer, carrie)


def successive_divisions(x, base1, base_to_convert):
    '''
    This function performs successive divisions to convert a number from one base (base1) to another base (base_to_convert).
    Parameters:
      x (str): The number to be converted.
      base1 (int): The base of the number system in which the number is currently represented.
      base_to_convert (int): The base of the number system to which the number is to be converted.

    Returns: str: The number represented in base_to_convert.
    '''
    if base_to_convert != 10:
        carrie = quotient = ""
        list_answer = []
        base_to_convert = str(base_to_convert)

        while carrie != "0":
            carrie, quotient = division(base1, x, base_to_convert)
            x = carrie
            list_answer.append(quotient)

        answer = "".join(list_answer[::-1])
        return answer
    else:
        answer = 0
        hex_chars = "0123456789ABCDEF"

        for digit in x:
            answer = answer * 16 + hex_chars.index(digit)

        return str(answer)
