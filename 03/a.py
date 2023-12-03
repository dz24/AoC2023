NSYM = "0123456789."
NINE = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def parser(inp: str, pad: int = 1) -> list[str]:
    # parses and pads grid, and finds symbol coordinates.
    grid = []
    sym_coord = []
    with open(inp, "r") as read:
        for idx_y, line in enumerate(read):
            rip = line.rstrip()
            grid.append(rip)
            for idx_x, let in enumerate(rip):
                if let not in NSYM:
                    sym_coord.append([idx_x + pad, idx_y + pad])

    if pad:
        str_len = len(grid[0]) + pad * 2
        grid2 = ["." * str_len]
        for line in grid:
            grid2.append("." + line + ".")
        grid2.append("." * str_len)
        return grid2, sym_coord
    return grid, sym_coord


def nums_x(line, y_idx, x_idx, numdic):
    num, idxs = [], []
    for i, let in enumerate(line):
        if let.isnumeric():
            num.append(let)
            idxs.append(i)
        else:
            if any(abs(x_idx - j) <= 1 for j in idxs):
                numdic[f"{idxs[0]}-{y_idx}"] = int("".join(num))
            num, idxs = [], []


def part_ab(inp: str) -> int:
    grid, coords = parser(inp)
    # find nums given grid and symbol coordinates.
    summ, numdic = 0, {}
    for coord in coords:
        numdic2 = {}
        idx, idy = coord[0], coord[1]
        nums_x(grid[idy - 1], idy - 1, idx, numdic2)
        nums_x(grid[idy], idy, idx, numdic2)
        nums_x(grid[idy + 1], idy + 1, idx, numdic2)
        if len(numdic2) == 2:
            values = list(numdic2.values())
            summ += values[0] * values[1]
        numdic.update(numdic2)

    return sum(list(numdic.values())), summ


part_a_txt = "./part_a.txt"
print(part_ab(part_a_txt), (532445, 79842967))
