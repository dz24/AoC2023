def parser(inp: str) -> list:
    games = {}
    with open(inp, "r") as read:
        for line in read:
            cnt = {"blue": 0, "red": 0, "green": 0}
            rip = line.rstrip().split()
            c_idx = line.find(":") + 1
            for aset in line[c_idx:].rstrip().split(";"):
                pairs = aset.split(",")
                for num, col in [i.split() for i in pairs]:
                    if cnt[col] < int(num):
                        cnt[col] = int(num)
            games[rip[1][:-1]] = cnt
    return games


def part_a(inp: str, req: dict) -> int:
    games = parser(inp)
    ids = 0
    for game, gdic in games.items():
        if all(gdic[key] <= item for key, item in req.items()):
            ids += int(game)
    return ids


def part_b(inp: str) -> int:
    games = parser(inp)
    powers = 0
    for game, gdic in games.items():
        powers += gdic["green"] * gdic["blue"] * gdic["red"]
    return powers


example1 = "./example1.txt"
part_a1 = "./part_a.txt"
req_a = {"blue": 14, "red": 12, "green": 13}
print(part_a(part_a1, req_a))
print(part_b(part_a1))
