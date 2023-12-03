NSYM = '0123456789.'
NINE = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]




def parser(inp: str, pad: int=0) -> list[str]:
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
        str_len = len(grid[0])+pad*2
        grid2 = ['.'*str_len]
        for line in grid:
            grid2.append('.' + line + '.')
        grid2.append('.'*str_len)
        return grid2, sym_coord
    return grid, sym_coord


def nums_x(line, y_idx, x_idx, numdic):
    idxs = []
    nums = []
    num = []

    for i, let in enumerate(line):
        if let.isnumeric():
            num.append(let)
            idxs.append(i)
        else:
            if any(abs(x_idx-j)<=1 for j in idxs):
                numdic[str(idxs[0])+str(y_idx)] = int(''.join(num))
            num = []
            idxs = []

def find_nums_sym(grid, coords):
    # find nums given grid and symbol coordinates.
    nums = []
    for i in grid:
        print(i)
    print(' ')
    numdic = {}
    for coord in coords:
        idx, idy = coord[0], coord[1]
        top, center, bot = [], [], []

        nums_x(grid[idy-1], idy-1, idx, numdic)
        nums_x(grid[idy], idy, idx, numdic)
        nums_x(grid[idy+1], idy+1, idx, numdic)

        # if coord == '#':
        #     exit('a')

        # exit('ba')
        # print('bear', grid[idy-1])
        # print(idx, grid[idy-1].split('.'))
        # exit('ba')

        # for head in grid[idy-1][:idx-1][::-1]:
        #     if top.isnumeric():
        #         number.insert(0, head)
        #     else:
        #         break

        # print(grid[idy-1][:idx-1][::-1])
        # exit('ba')



        # for dx, dy in NINE:
        #     grid_el = grid[idy+dy][idx+dx]
        #     if grid_el.isnumeric():
        #         number = [grid_el]
        #         for head in grid[idy+dy][:idx+dx][::-1]:
        #             if head.isnumeric():
        #                 number.insert(0, head)
        #             else:
        #                 break
        #         for tail in grid[idy+dy][idx+dx+1:]:
        #             if tail.isnumeric():
        #                 number.append(tail)
        #             else:
        #                 break

        #         print('plum', grid[idy+dy])
        #         print('head', grid[idy+dy][:idx+dx][::-1])
        #         print('tail', grid[idy+dy][idx+dx+1:])
        #         print('numbs', number)
        #         # exit('a')
        #         # nums
        # exit('snow')
    print(numdic)
    print(sum(list(numdic.values())))

def part_a(inp: str, pad: int=0) -> int:
    grid, coords = parser(inp, pad)
    find_nums_sym(grid, coords)

    print('shark')


example1 = "./example1.txt"
part_a_txt = './part_a.txt'
# print(part_a(example1))
part_a(example1, 1)
part_a(part_a_txt, 1)
