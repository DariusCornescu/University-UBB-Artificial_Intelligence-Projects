def get_representation(x, y):
    max_len = max(len(x), len(y)) + 1
    return x.zfill(max_len), y.zfill(max_len)


def compute_sum(base, number1, number2):
    list_x, list_y = get_representation(number1, number2)
    list_answer = ['0' for _ in range(len(list_x))]

    converter = {str(i): i for i in range(10)}
    converter.update({chr(65 + i): 10 + i for i in range(6)})
    converter_inv = {v: k for k, v in converter.items()}

    for i in range(len(list_x) - 1, -1, -1):
        x = converter[list_answer[i]] + converter[list_x[i]] + converter[list_y[i]]
        list_answer[i] = converter_inv[x % base]
        if i > 0:
            list_answer[i - 1] = converter_inv[x // base]

    return ''.join(list_answer).lstrip('0')


def do_addition():
    try:
        base = int(input("Choose your base: "))
        number1 = input("First number:  ")
        number2 = input("Second number: ")
        print(compute_sum(base, number1, number2))
    except ValueError:
        print("Invalid base")
