from Addition import *
from Multiplication import *
from Subtraction import *
from Division import *
from Conversions import *
from colorama import Fore

def show_menue():
    """
    Displays the menu and all the possible operations the user can choose.

    Returns:
    None
    """
    print(Fore.LIGHTMAGENTA_EX)
    print("What operation do you want to perform? ")
    print("Addition - type 1")
    print("Subtraction  - type 2")
    print("Multiplication - type 3")
    print("Division - type 4")
    print("Conversion - type 5")
    print("If you want to end the program - type 6")


def main():
    """
    Displays the menu and performs the operation chosen by the user.
    If the user chooses an invalid operation, it raises a ValueError.

    Returns:None

    Raises:
    ValueError: If the user chooses an invalid operation.
    """
    flag = True
    while flag == True:
        try:
            show_menue()
            x = int(input(Fore.GREEN+ "Type your operation: "))

            if x == 1:
                do_addition()
            elif x == 2:
                do_subtraction()
            elif x == 3:
                do_multiplication()
            elif x == 4:
                do_division()
            elif x == 5:
                do_conversion()
            elif x == 6:
                flag = False
        except ValueError:
            print(Fore.RED+"Invalid operation")

if __name__ == "__main__":
    print(Fore.BLUE+ "Author: Cornescu Darius Constantin")
    main()