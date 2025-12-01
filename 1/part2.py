def solve():
    start_pos = 50 # starting position for dial
    curr_pos = start_pos # current position of dial
    pwd = 0 #actual counter for clicking 0

    with open("1_input.txt") as f:
        for line in f: #go through each input
            trc = 0 #tracker for each input
            
            dr = line[0] #l / r
            am = int(line[1:]) # amount
            if dr == "R":
                am = am * -1
                
            if dr == "L" and am%100 >= 100-curr_pos:
                #passed 0
                if (curr_pos + am) % 100 != 0:
                    pwd += 1
                    trc += 1
                pwd += (abs(am) // 100)
                trc += (abs(am) // 100)
            elif dr == "R" and curr_pos > 0 and abs(am)%100 >= curr_pos:
                if (curr_pos + am) % 100 != 0:
                    pwd += 1
                    trc += 1
                pwd += (abs(am) // 100)
                trc += (abs(am) // 100)
                
                
            elif dr == "R" and abs(am) >= 100:
                # For right movements >= 100 that don't meet the above condition
                pwd += (abs(am) // 100)
                trc += (abs(am) // 100)
            elif dr == "L" and abs(am) >= 100:
                # For left movements >= 100 that don't meet the above condition
                pwd += (abs(am) // 100)
                trc += (abs(am) // 100)
                
            curr_pos = (curr_pos + am)%100
            if curr_pos == 0:
                pwd += 1
                trc += 1
            
            print(f"0 clicked {trc} times")
            
            print(f"{dr}{am}: {curr_pos}")
    
    print(pwd)

solve()

# print(2//100)