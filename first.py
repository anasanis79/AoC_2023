# This is a sample Python script.
from string_digits import find_first_digit_alpha, find_last_digit_alpha, find_first_alpha_numeric_digit, find_last_alpha_numeric_digit


def find_calibration(stt):
    result = 10 * find_first_alpha_numeric_digit(stt) + find_last_alpha_numeric_digit(stt)
    return result


def calculate_from_file(f_name):
    with open(f_name) as f:
        lines = f.readlines()
    summ = 0
    for line in lines:
        summ += find_calibration(line)
    print(summ)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate_from_file("input.txt")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
