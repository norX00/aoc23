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

# Part two
values["J"] = 1
hands = [([values.get(h) for h in hand], int(bid)) for hand, bid in [ln.split(" ") for ln in data.split("\n")]]


def joker_strength(h):
    card_counts = Counter(h)
    if 1 in h:
        card_to_pretend = card_counts.most_common()[0][0]
        for card in Counter(filter(lambda x: x != 1, h)):
            if card_to_pretend == 1 or card_counts[card] > card_counts[card_to_pretend]:
                card_to_pretend = card
        if card_to_pretend != 1:
            card_counts[card_to_pretend] += h.count(1)
            del card_counts[1]
    s = "".join(map(str, sorted(card_counts.values())))
    return priority.get(s), h


hands_ranked = sorted(hands, key=lambda hand: joker_strength(hand[0]))
print(sum([rank * bid for rank, (_, bid) in enumerate(hands_ranked, 1)]))
