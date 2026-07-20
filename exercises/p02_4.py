
import random


rd = random.randint(1, 15)
for i in range(5):
    ip = input("guess 1-15: ")
    if int(ip) == rd:
        print("correct")
        break
    if int(ip) < rd : 
        print("higher")
        continue
    else:
        print("lower")
        continue
else:
    print("lose, the answer is ", rd)
