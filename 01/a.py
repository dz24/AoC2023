import numpy as np

NUMS = "123456789"
NUMS_STRS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
DIC = {i: j for i, j in zip(NUMS_STRS, NUMS)}


def solver_a(inp: str) -> int:
    data = np.loadtxt(inp, dtype="str")
    nums_l = []
    for line in data:
        nums_l.append([i for i in line if i in NUMS])
    nums_int = [int(f"{i[0]}{i[-1]}") for i in nums_l]
    return sum(nums_int)


def str_to_num(line: str, num_l: list[int], rev: bool = False) -> None:
    for idx in range(len(line) - 2):
        word = line[-5 - idx :] if rev else line[: idx + 5]
        for num_str in NUMS_STRS:
            if num_str in word:
                num_l.insert(len(num_l) if rev else 0, DIC[num_str])
                return


def solver_b(inp: str) -> int:
    data = np.loadtxt(inp, dtype="str")
    nums_l = []
    for line in data:
        lnums = []
        idxes = []
        for idx, let in enumerate(line):
            if let in NUMS:
                lnums.append(let)
                idxes.append(idx)
        if len(line) < 3:
            pass
        elif idxes:
            str_to_num(line[: idxes[0]], lnums)
            str_to_num(line[idxes[-1] + 1 :], lnums, rev=True)
        else:
            str_to_num(line, lnums)
            str_to_num(line, lnums, rev=True)
        nums_l.append(int(f"{lnums[0]}{lnums[-1]}"))
    # return sum(nums_l)
    return sum(nums_l)


part_a = "./part_a.txt"
print(solver_a(part_a), solver_a(part_a) == 56108)
print(solver_b(part_a), solver_b(part_a) == 55652)
