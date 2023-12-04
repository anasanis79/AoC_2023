class Combination:
    def __init__(self, comb_strs):
        colors_str = comb_strs.split(', ')
        self.blue = self.green = self.red = 0
        for color_str in colors_str:
            if "blue" in color_str:
                self.blue = int(color_str[:color_str.find("blue")])
            elif "green" in color_str:
                self.green = int(color_str[:color_str.find("green")])
            elif "red" in color_str:
                self.red = int(color_str[:color_str.find("red")])

    def print_me(self):
        print(str(self.red) + ", " + str(self.green) + ", " + str(self.blue))

    def is_comb_possible(self, max_red, max_green, max_blue):
        return self.red <= max_red and self.green <= max_green and self.blue <= max_blue


class Game:
    def __init__(self, line):
        game_id_str = line[:line.find(":")]
        self.combinations_strs = [st.strip() for st in line[len(game_id_str)+1:].split(";")]
        self.combinations = [Combination(st) for st in self.combinations_strs]
        self.game_id = int(game_id_str[5:])

    def print_combinations(self):
        for comb in self.combinations:
            comb.print_me()

    def is_game_possible(self):
        for comb in self.combinations:
            if not comb.is_comb_possible(12, 13, 14):
                return False
        return True

    def required_red(self):
        return max(1, max([comb.red for comb in self.combinations]))

    def required_green(self):
        return max(1, max([comb.green for comb in self.combinations]))

    def required_blue(self):
        return max(1, max([comb.blue for comb in self.combinations]))

    def power(self):
        return self.required_red() * self.required_green() * self.required_blue()


def calculate_from_file(f_name):
    with open(f_name) as f:
        lines = f.readlines()
    sum_ids = 0
    sum_power = 0
    for line in lines:
        g = Game(line)
        # print(g.game_id)
        print(g.combinations_strs)
        # g.print_combinations()
        # print(str(g.is_game_possible()))
        if g.is_game_possible():
            sum_ids += g.game_id
        print(str(g.required_red()) + ", " + str(g.required_green()) + ", " + str(g.required_blue()))
        print(str(g.power()))
        sum_power += g.power()

    print(sum_ids)
    print(sum_power)

if __name__ == '__main__':
    calculate_from_file("second_input.txt")
