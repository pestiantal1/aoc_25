import time

def fast_repeat_check(s):
    return s[0] != '0' and (s in (s + s)[1:-1])

def is_invalid(n): #n is string, half is even
    return fast_repeat_check(n)


def solve():
    txt = ""
    ranges = []
    sol = 0
    
    with open("2_input.txt") as f:
        txt = f.read()
        txt = txt.split(",")
        
        for i in range(len(txt)):
            ranges.append(txt[i].split("-"))
            
        #we have a ranges pairs here 
        
        for e in ranges: #for each entry in ranges
            for i in range(int(e[0]), int(e[1])+1): #go through the range
                if is_invalid(str(i)):
                    sol += i
                    print(i)
  
    print(sol)
    
solve()

# print(is_invalid("11"))
# print(is_invalid("12"))
# print(is_invalid("16"))
# print(is_invalid("123123"))
# print(is_invalid("99999999"))
# print(is_invalid("5566"))