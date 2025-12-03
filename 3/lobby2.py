def calc_largest(s):
    s = s.strip()                    # strip newline/whitespace
    res = ""
    prev_pos = 0
    for _ in range(12):
        remaining_needed = 12 - len(res)
        found = False
        for d in range(9, -1, -1):   # try 9..0
            idx = s.find(str(d), prev_pos)
            if idx != -1 and len(s) - idx >= remaining_needed:
                res += str(d)
                prev_pos = idx + 1
                found = True
                break
        if not found:
            return None
    return res

def solve():
    jolts = []
    res = 0
    with open("3_input.txt") as f:
        for line in f:
            line = line.strip()
            val = calc_largest(line)
            print(f"line: {line} -> {val}")
            if val is not None:
                jolts.append(int(val))

    print(jolts)
    for num in jolts:
        res += num

    return res

print(solve())



# test = "818181911112111"


# print(calc_largest(test))