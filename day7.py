from functools import cmp_to_key
FIVE_OF_KIND = 7
FOUR_OF_KIND = 6
FULL_HOUSE = 5
THREE_OF_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1
HAND_TYPES = [FIVE_OF_KIND, FOUR_OF_KIND, FULL_HOUSE, THREE_OF_KIND, TWO_PAIR, ONE_PAIR, HIGH_CARD]
CARD_TYPES = '23456789TJQKA'
NEW_CARD_TYPES = 'J23456789TQKA'
# CARD_TYPES = CARD_TYPES.__reversed__()

line_example = "Q4QKK 465"


def compare_two_letters(tup1, tup2):
    if tup1[0] > tup2[0]:
        return -1
    elif tup2[0] > tup1[0]:
        return 1
    elif NEW_CARD_TYPES.find(tup1[1]) > NEW_CARD_TYPES.find(tup2[1]):
        return -1
    elif NEW_CARD_TYPES.find(tup2[1]) > NEW_CARD_TYPES.find(tup1[1]):
        return 1
    return 0


def calc_hand_type2(hand_str):
    # print(hand_str)
    count_j = hand_str.count("J")
    if count_j == 0:
        return calc_hand_type(hand_str)

    counts = [(hand_str.count(ll), ll) for ll in hand_str]
    # print(counts)
    counts = sorted(counts, key=cmp_to_key(compare_two_letters))
    # print(counts)
    m = count_j
    m_c = "J"
    for c in counts:
        if c[1] != "J":
            m = c[0] + count_j
            m_c = c[1]
            break

    # print(m)
    # print(m_c)
    counts = [(c[0] if c[1] != "J" and c[1] != m_c else m, c[1] if c[1] != "J" and c[1] != m_c else m_c) for c in counts]
    # print(counts)
    # m = max(counts)

    if m == 5:
        return FIVE_OF_KIND
    elif m == 4:
        return FOUR_OF_KIND
    elif m == 3 and [c[0] for c in counts].__contains__(2):
        return FULL_HOUSE
    elif m == 3:
        return THREE_OF_KIND
    elif [c[0] for c in counts].count(2) == 4:
        return TWO_PAIR
    elif m == 2:
        return ONE_PAIR
    else:
        return HIGH_CARD


def calc_hand_type(hand_str):
    counts = [hand_str.count(ll) for ll in hand_str]
    m = max(counts)

    if m == 5:
        return FIVE_OF_KIND
    elif m == 4:
        return FOUR_OF_KIND
    elif counts.__contains__(3) and counts.__contains__(2):
        return FULL_HOUSE
    elif counts.__contains__(3):
        return THREE_OF_KIND
    elif counts.count(2) == 4:
        return TWO_PAIR
    elif m == 2:
        return ONE_PAIR
    else:
        return HIGH_CARD


def compare_hand_strs(hand_str1, hand_str2):
    ranks1 = [CARD_TYPES.find(c) for c in hand_str1]
    ranks2 = [CARD_TYPES.find(c) for c in hand_str2]
    for i in range(0, len(ranks1)):
        if ranks1[i] > ranks2[i]:
            return 1
        elif ranks2[i] > ranks1[i]:
            return -1
    return 0


def compare_hand_strs2(hand_str1, hand_str2):
    ranks1 = [NEW_CARD_TYPES.find(c) for c in hand_str1]
    ranks2 = [NEW_CARD_TYPES.find(c) for c in hand_str2]
    for i in range(0, len(ranks1)):
        if ranks1[i] > ranks2[i]:
            return 1
        elif ranks2[i] > ranks1[i]:
            return -1
    return 0


def compare_hands(hand1, hand2):
    if hand1.type > hand2.type:
        return 1
    elif hand2.type > hand1.type:
        return -1
    else:
        return compare_hand_strs(hand1.hand_str, hand2.hand_str)


def compare_hands2(hand1, hand2):
    if hand1.type > hand2.type:
        return 1
    elif hand2.type > hand1.type:
        return -1
    else:
        return compare_hand_strs2(hand1.hand_str, hand2.hand_str)


class MyHand:
    def __init__(self, hand_str, bid):
        self.hand_str = hand_str
        self.type = calc_hand_type(hand_str)
        self.bid = bid

    def print_me(self):
        print(self.hand_str + ", " + str(self.type) + ", " + str(self.bid))


class MyHand2:
    def __init__(self, hand_str, bid):
        self.hand_str = hand_str
        self.type = calc_hand_type2(hand_str)
        self.bid = bid

    def print_me(self):
        print(self.hand_str + ", " + str(self.type) + ", " + str(self.bid))



def calculate_from_file(f_name):
    with open(f_name) as f:
        lines = f.readlines()
    all_hands = []
    for line in lines:
        hand_and_bid = line.split()
        all_hands.append(MyHand(hand_and_bid[0], int(hand_and_bid[1])))
    # sorted(all_hands, cmp=compare_hands)

    all_hands = sorted(all_hands, key=cmp_to_key(compare_hands))
    # for h in all_hands:
    #     h.print_me()

    summ = 0
    i = 1
    for h in all_hands:
        summ += i * h.bid
        i += 1

    print("Part one: " + str(summ))

    all_hands2 = []
    for line in lines:
        hand_and_bid = line.split()
        all_hands2.append(MyHand2(hand_and_bid[0], int(hand_and_bid[1])))
    # sorted(all_hands, cmp=compare_hands)

    all_hands2 = sorted(all_hands2, key=cmp_to_key(compare_hands2))
    # for h in all_hands2:
    #     h.print_me()

    summ = 0
    i = 1
    for h in all_hands2:
        summ += i * h.bid
        i += 1

    print("Part two: " + str(summ))


calculate_from_file("input/day7.txt")

# print(calc_hand_type2("J2255"))
# print(calc_hand_type2("T55J5"))
# print(calc_hand_type2("KK677"))
# print(calc_hand_type2("KTJJT"))
# print(calc_hand_type2("QQQJA"))
# hand_and_bid = line_example.split()
#
# mh1 = MyHand(hand_and_bid[0], int(hand_and_bid[1]))
# mh1.print_me()