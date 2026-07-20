
"""
    Viết game đoán số may mắn (guess the number)  
Máy tính nghĩ một số random từ 1 cho đến 15 và hỏi bạn đoán. Máy tính sẽ nói 
cho bạn khi bạn đoán sai là số may mắn là phải lớn hơn hoặc nhỏ hơn. Bạn sẽ 
chiến thắng nếu bạn đoán đúng số đó trong 5 lượt chơi.
    """

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
