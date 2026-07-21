
#Bài 21.Làm game chọn nhóm. Có một danh sách gồm 8 người chơi, hãy lựa chọn ngẫu
#nhiên 4 người chơi không trùng nhau để cho vào nhóm A, còn lại cho vào nhóm
#B.
import random


def random_group():
    players = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    group_a = random.sample(players, 4)
    group_b = [player for player in players if player not in group_a]
    return group_a, group_b

#Bài 22. 
#Tìm vị trí của giá trị chẵn đầu tiên trong mảng 1 chiều các số nguyên. Nếu 
#mảng không có giá trị chẵn thì sẽ trả về -1

def find_lst(): 
    lst = [1,3,5,7,9]
    for n in lst: 
        if n%2 == 0: 
            return n
    return -1


"""
Given the year number. You need to check if this year is a leap year. If it is, print 
LEAP, otherwise print COMMON. 
The rules in Gregorian calendar are as follows: 
a year is a leap year if its number is exactly divisible by 4 and is not exactly 
divisible by 100 
a year is always a leap year if its number is exactly divisible by 400  
"""
def check_leap(n):
    if not isinstance(n, int) or n < 0:
        return "pls! check again your input"
    elif n%400 == 0:
        return "LEAP"
    elif n%4 == 0 and n%100 != 0: 
        return "LEAP"
    else:
        return "COMMON"

"""
Bài 24. 
Viết chương trình tính tổng S = 1 + 1/2 + 1/3 + …+ 1/n với n là số nguyên dương 
nhập từ bàn phím. 
"""
def cal_s(n):
    if not isinstance(n, int) or n <= 0:
        return "check again"
    s = 0
    for i in range(1, n + 1):
        s += 1 / i
    return s

    
    
"""
Phân tích một số thành tích các thừa số nguyên tố
"""

def bunkai(n):
    if not isinstance(n, int) or n <= 1:
        return "check again"
    lst = []
    while n % 2 == 0:
        lst.append(2)
        n //= 2
    p = 3
    while p <= n:   
        while n % p == 0:
            lst.append(p)
            n //= p
        p += 2  
    if n > 1:
        lst.append(n)
    return lst

"""Bài 27. 
Given a non-empty string and an int n, return a new string where the char at index 
n has been removed. The value of n will be a valid index of a char in the original 
string (i.e. n will be in the range 0..len(str)-1 inclusive)."""
def remove_ichar(char, n):
    if not isinstance(char, str) or not isinstance(n, int):
        return "error"
    if n < 0 or n >= len(char):
        return "error"
    new_str = char[:n] + char[n+1:]
    return new_str

"""Given a string, return a new string where the first and last chars have been 
exchanged. """
def ex_str(old_str):
    if not isinstance(old_str, str) or len(old_str) <= 1:
        return old_str

    new_str = old_str[-1] + old_str[1:-1] + old_str[0]
    return new_str

        
if __name__ == "__main__":
    #result = random_group()
    #result = find_lst()
    #result = check_leap("abc")
    #result = cal_s(12)
    #result = bunkai(97)
    #result = remove_ichar("kitten", 4)
    result = ex_str("code")
    print(result)