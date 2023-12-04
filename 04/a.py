def parser(inp: str) -> list[str]:
    cards = {}
    with open(inp, "r") as read:
        for idx, line in enumerate(read):
            split = line.rstrip().split("|")
            head = split[0].split()
            game = int(head[1][:-1])
            cards[game] = {"win": head[2:], "num": split[1].split()}
    return cards


def part_ab(inp: str) -> list[int, int]:
    cards = parser(inp)
    counter = {i: 1 for i in cards.keys()}
    tot_cnt = 0
    for game, dic in cards.items():
        win = dic["win"]
        nums = dic["num"]
        wins = sum([num in win for num in nums])
        tot_cnt += 1 * 2 ** (wins - 1) if wins else 0
        for i in range(game + 1, game + 1 + wins):
            counter[i] += 1 * counter[game]
    return tot_cnt, sum(list(counter.values()))


taska = "./taska.txt"
vala, valb = part_ab(taska)
print(vala, valb, vala == 25231, valb == 9721255)
