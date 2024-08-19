from colorama import Fore
def find_max_power_of_two(base):
    """
    Calculates the highest power of 2, k, such that base is divisible by 2.
    Continuously divides base by 2 until it is no longer divisible.
    Parameters:
      base (int): The base to be divided.

    Returns: int: The highest power of 2 which divides base.
    """
    power = 0
    while base % 2 == 0:
        base //= 2
        power += 1
    return power

def convert_to_binary(x, base):
    """
    Converts a number x from a given base to binary.
    Parameters:
      x (str): The number in the given base.
      base (int): The base of the number.

    Returns: str: The binary representation of the number.
    """
    number_list = list(x)
    base = int(base)
    binary_value = []
    base_digit_to_decimal = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                             '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                             'C': 12, 'D': 13, 'E': 14, 'F': 15}

    for digit in number_list:
        value = base_digit_to_decimal[digit]
        mini_group = []

        while value != 0:
            mini_group.append(str(value % 2))
            value //= 2

        while len(mini_group) < find_max_power_of_two(base):
            mini_group.append('0')

        binary_value.extend(mini_group[::-1])

    binary_representation = "".join(binary_value)
    return binary_representation.lstrip('0')

def convert_from_binary(x, base):
    """
    Converts a binary number to another base.
    Parameters:
      x (str): The binary number.
      base (int): The target base.

    Returns: str: The number in the target base.
    """
    number_list = list(x)
    base = int(base)
    base_integer = find_max_power_of_two(base)
    result = ""
    decimal_to_base_digit = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    while len(number_list) % base_integer != 0:
        number_list.insert(0, '0')

    for index in range(0, len(number_list), base_integer):
        value = 0
        power = 0
        for index2 in range(index + base_integer - 1, index - 1, -1):
            value += int(number_list[index2]) * (2**power)
            power += 1
        result += decimal_to_base_digit[value]

    return result.lstrip('0')

def rapid_conv(x, base1, base2):
    """
    Converts a number from a base to another base using the rapid conversion method.
    Parameters:
      x (str): The number in the given base.
      base1 (int): The base of the number.
      base2 (int): The target base.

    Returns: str: The number in the target base.
    """
    binary_representation = convert_to_binary(x, base1)
    return convert_from_binary(binary_representation, base2)
