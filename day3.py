import re

prev_str = ".....487.599...........411...........................................574..679.136..........................30......255.......432............"
some_string1 = "....*......*............*..........&586..........................375...@..*....../.....835.............610*........./...............582....."
next_str = "...833........304...&.862...............203..........922.125...............819.............@....563.....................722..775............"

all_symbols = "[#%*/$@=&+-]"

one_symbol = "[*]"

numbers_reg = r"\d+"


class MyLine:
    def __init__(self, some_string):
        self.symbol_idx = get_symbol_idx(some_string, all_symbols)
        self.mul_idx = get_symbol_idx(some_string, one_symbol)
        self.numbers = [MyNumber(ret[0], ret[1]) for ret in get_idx_with_string(some_string, numbers_reg)]

    def print_me(self):
        print(self.symbol_idx)
        for num in self.numbers:
            num.print_me()

    def sum_adjacent(self, another_line):
        val = 0
        for num in self.numbers:
            for sym in another_line.symbol_idx:
                if num.is_adjacent(sym):
                    val += num.value
        return val

    def get_adjacent_num(self, idx):
        for num in self.numbers:
            if num.is_adjacent(idx):
                return num.value
        return 0

    def mul_adjacent_nums(self, prev_line, next_line):
        result = 0
        for m_idx in self.mul_idx:
            ar = []
            ar.extend(self.get_adj_nums(m_idx))
            ar.extend(prev_line.get_adj_nums(m_idx))
            ar.extend(next_line.get_adj_nums(m_idx))
            if len(ar) > 1:
                res = 1
                for a in ar:
                    res *= a
                result += res
        return result

        # final_result = 0
        # for m_idx in self.mul_idx:
        #     result = 1
        #     result *= self.mul_adj_nums(m_idx, self)
        #     result *= self.mul_adj_nums(m_idx, prev_line)
        #     result *= self.mul_adj_nums(m_idx, next_line)
        #     if result > 1:
        #         final_result += result
        #     print("mul_adjacent_nums: " + str(result))
        # return final_result



    def mul_adj_nums(self, idx, some_line):
        result = 1
        for num in some_line.numbers:
            if num.is_adjacent(idx):
                result *= num.value
        print("idx: " + str(idx) + ", mul_adj_nums: " + str(result))
        return result

    def get_adj_nums(self, idx):
        result = []
        for num in self.numbers:
            if num.is_adjacent(idx):
                result.append(num.value)
        return result

    def sum_internal_gear(self):
        summ = 0
        for m_idx in self.mul_idx:
            for i in range(0, len(self.numbers) - 1):
                if self.numbers[i].is_adjacent(m_idx) and self.numbers[i + 1].is_adjacent(m_idx):
                    summ += self.numbers[i].value * self.numbers[i + 1].value
        return summ

    def sum_gear(self, prev_line, next_line):
        summ = 0
        for m_idx in self.mul_idx:
            summ += prev_line.get_adjacent_num(m_idx) * next_line.get_adjacent_num(m_idx)
        return summ


class MyNumber:
    def __init__(self, num_string, idx):
        self.start = idx
        self.value = int(num_string)
        self.end = idx + len(num_string)

    def print_me(self):
        print(str(self.start) + ", " + str(self.value) + ", " + str(self.end))

    def is_adjacent(self, idx):
        return self.start - 1 <= idx <= self.end


def get_symbol_idx(stt, symbol):
    itr = re.finditer(symbol, stt)
    return [m.start(0) for m in itr]


def get_idx_with_string(stt, symbol):
    itr = re.finditer(symbol, stt)
    return [(m.group(), m.start(0)) for m in itr]


# print(get_symbol_idx(some_string1, all_symbols))
# print(get_idx_with_string(some_string1, numbers_reg))
ll = MyLine(some_string1)
# ll.print_me()
# print(ll.sum_adjacent(ll))
next_line1 = MyLine(next_str)
# next_line1.print_me()
# print(ll.sum_adjacent(next_line1))


def sum_important(my_line_prev, my_line, my_line_next):
    return 0


def calculate_from_file(f_name):
    with open(f_name) as f:
        lines = f.readlines()

    my_lines = []
    for line in lines:
        my_lines.append(MyLine(line))

    sum_all_adjacents(my_lines)

    sum_all_gears(my_lines)

def sum_all_adjacents(my_lines):
    summ = 0
    for i in range(1, len(my_lines) - 1):
        summ += my_lines[i].sum_adjacent(my_lines[i - 1])
        summ += my_lines[i].sum_adjacent(my_lines[i + 1])
        summ += my_lines[i].sum_adjacent(my_lines[i])
        # my_lines[i + 1].print_me()
    # print(summ)
    summ += my_lines[0].sum_adjacent(my_lines[1])
    # print(summ)
    summ += my_lines[len(my_lines) - 1].sum_adjacent(my_lines[len(my_lines) - 2])
    print(summ)


def sum_all_gears(my_lines):
    summ = 0
    for i in range(1, len(my_lines) - 1):
        s = my_lines[i].mul_adjacent_nums(my_lines[i - 1], my_lines[i + 1])
        if s > 1:
            print(s)
            summ += s
        # sum_gear = my_lines[i].sum_gear(my_lines[i - 1], my_lines[i + 1])
        # print("sum_gear: " + str(sum_gear))
        # summ += sum_gear
        # sum_gear = my_lines[i].sum_gear(my_lines[i - 1], my_lines[i])
        # print("sum_gear: " + str(sum_gear))
        # summ += sum_gear
        # sum_internal_gear = my_lines[i].sum_internal_gear()
        # print("sum_internal_gear: " + str(sum_internal_gear))
        # summ += sum_internal_gear

        # my_lines[i + 1].print_me()
    # print(summ)
    # summ += my_lines[0].sum_adjacent(my_lines[1])
    # print(summ)
    # summ += my_lines[len(my_lines) - 1].sum_adjacent(my_lines[len(my_lines) - 2])
    print(summ)


calculate_from_file("input/day3.txt")
