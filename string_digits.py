digits_alpha = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def find_first_digit_alpha(stt):
    index = len(stt)
    res = ()
    i = 0
    for digit_alpha in digits_alpha:
        i += 1
        digit_idx = stt.find(digit_alpha)
        if 0 <= digit_idx < index:
            index = digit_idx
            res = (index, str(i))
            # print(res)
    return res


def find_last_digit_alpha(stt):
    index = -1
    res = ()
    i = 0
    for digit_alpha in digits_alpha:
        i += 1
        digit_idx = stt.rfind(digit_alpha)
        if digit_idx > index:
            index = digit_idx
            res = (index, str(i))
            # print(res)
    return res


def find_first_alpha_numeric_digit(stt):
    digits = [(i, c) for i, c in enumerate(stt) if c.isdigit()]
    first_alpha_digit = find_first_digit_alpha(stt)
    if first_alpha_digit is () and len(digits) == 0:
        return 0
    elif first_alpha_digit is ():
        return int(digits[0][1])
    elif len(digits) == 0:
        return int(first_alpha_digit[1])
    elif first_alpha_digit[0] < digits[0][0]:
        return int(first_alpha_digit[1])
    else:
        return int(digits[0][1])


def find_last_alpha_numeric_digit(stt):
    digits = [(i, c) for i, c in enumerate(stt) if c.isdigit()]
    last_alpha_digit = find_last_digit_alpha(stt)
    if last_alpha_digit is () and len(digits) == 0:
        return 0
    elif last_alpha_digit is ():
        return int(digits[len(digits) - 1][1])
    elif len(digits) == 0:
        return int(last_alpha_digit[1])
    elif last_alpha_digit[0] > digits[len(digits) - 1][0]:
        return int(last_alpha_digit[1])
    else:
        return int(digits[len(digits) - 1][1])
