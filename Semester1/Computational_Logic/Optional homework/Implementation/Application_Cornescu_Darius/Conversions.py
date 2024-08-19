from Utils import *
from Substitusion_method import *
from Division_method import *
from Rapid_conversions import *
from colorama import Fore, Back, Style


def verify_power_of2(n):
    '''
    Checks if a number is a power of 2.
    Parameters:
      n (int): The number to be checked.

    Returns: bool: True if the number is a power of 2, False otherwise.
    '''
    while n % 2 == 0:
        n //= 2

    if n == 1:
        return True
    return False


def do_conversion():
    '''
    Converts a number from one base to another. The method of conversion is chosen based on the bases.
    If both bases are powers of 2, rapid conversion is used.
    If the original base is less than the target base, substitution method is used.
    Otherwise, successive divisions method is used.

    Returns:
    str: The converted number in the target base.

    Raises:
    ValueError: If the bases are not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 16].
    ValueError: If the number is not valid in the original base.
    '''
    flag = False
    while flag == False:
        try:
            number = input(Fore.LIGHTBLUE_EX+"What's the number you want to transform? ")
            base_of_number = int(input(Fore.LIGHTBLUE_EX+"What's the base the number is written in? "))
            base_to_convert = int(input(Fore.LIGHTBLUE_EX+"In what base would you like to convert it? "))


            if base_of_number not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 16] or base_to_convert not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 16]:
                raise ValueError(Fore.RED+"Incorrect bases")

            if verify_base(base_of_number, number):

                if verify_power_of2(base_of_number) and verify_power_of2(base_to_convert):
                    print(Fore.LIGHTYELLOW_EX+"The method used is rapid conversion ")
                    print(rapid_conv(number, base_of_number, base_to_convert))
                    flag = True

                elif base_of_number < base_to_convert:
                    print(Fore.LIGHTYELLOW_EX+"The method used is substitution method ")
                    print(substitution(number, base_of_number, base_to_convert))
                    flag = True

                else:
                    print(Fore.LIGHTYELLOW_EX+"The method used is succesive divisions ")
                    print(successive_divisions(number, base_of_number, base_to_convert))
                    flag = True
            else:
                print(Fore.RED+"The input is incorrect")
        except ValueError:
            print(Fore.RED+"Invalid basis")