
def solve():
    start_pos = 50
    curr_pos = start_pos
    pwd = 0

    with open("1_input.txt") as f:
        for line in f:
            dr = line[0] #l / r
            am = int(line[1:]) # amount
            if dr == "R":
                am = am * -1
                
            curr_pos = (curr_pos + am)%100
            
            if curr_pos == 0:
                pwd += 1
            
            print(f"dr: {dr} am: {am} currpos: {curr_pos}")
    
    print(pwd)

solve()
