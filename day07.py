from collections import Counter

with open("day7.txt", "r") as of:
    data = of.read().strip()

values = {str(i): i for i in range(2, 10)} | {c: 10 + i for i, c in enumerate("TJQKA")}
hands = [([values.get(h) for h in hand], int(bid)) for hand, bid in [ln.split(" ") for ln in data.split("\n")]]
priority = {hand_type: i for i, hand_type in enumerate(["11111", "1112", "122", "113", "23", "14", "5"])}


def strength(h):
    s = "".join(map(str, sorted(Counter(h).values())))
    return priority.get(s), h


# Part one
hands_ranked = sorted(hands, key=lambda hand: strength(hand[0]))
print(sum([rank * bid for rank, (_, bid) in enumerate(hands_ranked, 1)]))
