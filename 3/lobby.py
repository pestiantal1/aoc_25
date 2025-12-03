def calc_largest(s):
    joltage = 0
    n1 = ""
    n2 = ""

    for i in reversed(range(1,10)):
        # print(i)
        for pos, char in enumerate(s):
            if char == str(i):
                n1 = char
                # print(f"n1: {n1}")
                for j in reversed(range(1,10)):
                    # print(pos)
                    for pos2, char in enumerate(s[pos+1:]):
                        # print(s[pos+1:])
                        # print(char, j)
                        if char == str(j):
                            n2 = j
                            # print(f"n2: {n2}")
                            # print(f"{type(n1)} {type(n2)}")
                            # print(f"RES: {n1 + str(n2)}")
                            return n1 + str(n2)
                            
        
    # print(n1 + n2)

    # return joltage

def solve():
    jolts = []
    res = 0
    with open("3_input.txt") as f:
        for line in f:
            print(f"line: {line}")
            print(calc_largest(line))
            jolts.append(int(calc_largest(line)))

    print(jolts)

    for num in jolts:
        res += num
    
    return res

print(solve())



# test = "818181911112111"


# print(calc_largest(test))