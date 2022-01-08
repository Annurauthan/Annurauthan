import time

set_timer=int(input("Set timer for countdwon: "))
for i in range(set_timer ,0,-1):
    print(f"Left: {i} seconds")
    time.sleep(1)
    if i==1:
        print("Time up!!!")
