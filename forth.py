
card_example = "Card   1: 58  6 71 93 96 38 25 29 17  8 | 79 33 93 58 53 96 71  8 67 90 17  6 46 85 64 25 73 32 18 52 77 16 63  2 38"


class Card:
    def __init__(self, card_str):
        colon_idx = card_str.find(":")
        self.id = int(card_str[4:colon_idx].strip())
        nums_str = card_str[colon_idx + 1:]
        winning_str = nums_str[:nums_str.find("|")]
        card_nums_str = nums_str[nums_str.find("|") + 1:]
        self.winning_nums = [int(st) for st in winning_str.split()]
        self.my_nums = [int(st) for st in card_nums_str.split()]
        self.num_of_copies = 1
        self._num_of_matches = -1

    def get_winning_val(self):
        val = self.num_of_matches()
        if val > 0:
            val = pow(2, val - 1)
        return val

    def add_number_of_copies(self, num):
        self.num_of_copies += num

    def num_of_matches(self):
        if self._num_of_matches > -1:
            return self._num_of_matches
        self._num_of_matches = 0
        for num in self.my_nums:
            if num in self.winning_nums:
                self._num_of_matches += 1
        return self._num_of_matches

    def print_me(self):
        print("id " + str(self.id) + "- copies: " + str(self.num_of_copies)
              + ", num of matches: " + str(self.num_of_matches()))
        # print("id " + str(self.id) + ": " + str(self.winning_nums) + " | " + str(self.my_nums))


def calculate_from_file(f_name):
    with open(f_name) as f:
        lines = f.readlines()
    sum_ids = 0
    sum_power = 0
    sum_val = 0
    prev_num_of_copies = 1
    sum_of_cards = 0
    all_cards = []
    for line in lines:
        cc = Card(line)
        sum_val += cc.get_winning_val()
        all_cards.append(cc)
    # print(sum_val)

    for i in range(0, len(all_cards)):
        cc = all_cards[i]
        sum_of_cards += cc.num_of_copies
        cc.print_me()
        for j in range(1, cc.num_of_matches() + 1):
            if i + j < len(all_cards):
                all_cards[i + j].add_number_of_copies(cc.num_of_copies)
            else:
                break
        print(sum_of_cards)
    print(sum_of_cards)


c = Card(card_example)
c.print_me()
print(c.get_winning_val())
print(c.num_of_matches())

calculate_from_file("forth_input.txt")
