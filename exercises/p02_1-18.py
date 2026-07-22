#https://github.com/khanhnvtintern/week2-python

import math
import random


#Cho một số nguyên, in " YES​" nếu chữ số cuối của nó là 7 và in " NO​" nếu không.
def hw_01(n):
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n phải là số nguyên")
    if abs(n) % 10 == 7:
        return "YES"
    return "NO"


"""
Cho biết tọa độ của ba điểm A, B, C trên một đoạn thẳng. In khoảng cách từ điểm
A đến điểm gần nó nhất.
"""
def homework_02(a, b, c):
    for v in (a, b, c):
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            raise TypeError("Tọa độ phải là số")
    return min(abs(a - b), abs(a - c))


#Viết chương trình tính tổng các số trong một danh sách
def hw3(lst):
    total = 0
    for i in lst:
        total += i
    return total


"""
    Viết game đoán số may mắn (guess the number)
Máy tính nghĩ một số random từ 1 cho đến 15 và hỏi bạn đoán. Máy tính sẽ nói
cho bạn khi bạn đoán sai là số may mắn là phải lớn hơn hoặc nhỏ hơn. Bạn sẽ
chiến thắng nếu bạn đoán đúng số đó trong 5 lượt chơi.
    """
def guess():
    rd = random.randint(1, 15)
    turns = 0
    while turns < 5:
        ip = input("guess 1-15: ").strip()
        if not ip.lstrip("-").isdigit():
            print("please enter a number")
            continue
        turns += 1
        n = int(ip)
        if n == rd:
            print("correct")
            return True
        if n < rd:
            print("higher")
        else:
            print("lower")
    print("lose, the answer is", rd)
    return False


"""
Một cửa hàng sẽ giảm giá 10% nếu tổng chi phí mua hàng lớn hơn 10.000
Người dùng về số lượng từ bàn phím
Giả sử, một đơn vị mặt hàng sẽ có giá 100 đồng.
In tổng chi phí hóa đơn cho người dùng.
"""
def total(quantity, price):
    return quantity * price

def calculate_discount(quantity):
    if isinstance(quantity, bool) or not isinstance(quantity, (int, float)):
        raise TypeError("Số lượng phải là số")
    if quantity < 0:
        raise ValueError("Số lượng không được âm")
    price = 100
    discount = 10 / 100
    over_price = 10000
    total_price = total(quantity, price)
    if total_price > over_price:
        total_price = total_price - (total_price * discount)
    return total_price


#Viết chương trình in ra tất cả các số chẵn trong một danh sách
def hw6(lst):
    r = []
    for i in lst:
        if i % 2 == 0:
            r.append(i)
    return r


#Viết một chương trình tìm ra số lớn nhất của một danh sách mà không sử dụng
#hàm max()
def hw7(lst):
    if len(lst) == 0:
        return None
    mx = lst[0]
    for i in lst:
        if i > mx:
            mx = i
    return mx


#Cho một danh sách các số, hãy tìm và in tất cả các phần tử lớn hơn phần tử trước
def hw8(lst):
    r = []
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            r.append(lst[i])
    return r


#Bài 9.
#Viết một chương trình xóa tất cả phần tử lặp lại (trùng lặp) ra khỏi danh sách.
def hw9(lst):
    r = []
    for i in lst:
        if i not in r:
            r.append(i)
    return r


#Get first, second best scores from the list.
#List may contain duplicates
def hw10(lst):
    fst = maxv(lst)
    if fst is None:
        return None, None
    rest = [i for i in lst if i != fst]
    return fst, maxv(rest)

def hw11(lst):
    fst = None
    sec = None
    for i in lst:
        if fst is None or i > fst:
            sec = fst
            fst = i
        elif i != fst and (sec is None or i > sec):
            sec = i
    return fst, sec


#Given an array length 1 or more of ints, return the difference between the largest
#and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2)
#functions return the smaller or larger of two values.
def minv(lst):
    if len(lst) == 0:
        return None
    minn = lst[0]
    for i in lst:
        if i < minn:
            minn = i
    return minn

def maxv(lst):
    if len(lst) == 0:
        return None
    maxn = lst[0]
    for i in lst:
        if i > maxn:
            maxn = i
    return maxn

def hw13(lst):
    if len(lst) == 0:
        return None
    return maxv(lst) - minv(lst)


#Viết một chương trình in ra các số chia hết cho 7 nhưng không chia hết cho 5
#nằm trong khoảng 100 cho đến 1000 (tính cả 100 và 1000).
#Kết quả: In trên một dòng và cách nhau bởi dấu phẩy.
def hw14():
    mn = 100
    mx = 1000
    divide = 7
    not_divide = 5
    lst = []
    for i in range(mn, mx + 1):
        if i % divide == 0 and i % not_divide != 0:
            lst.append(i)
    return lst


#Viết một chương trình in tất cả các số nguyên tố nhỏ hơn n. Với n là số nguyên
#dương nhập từ bàn phím.
def prime(n):
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n phải là số nguyên")
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def hw15(n):
    return [i for i in range(2, n) if prime(i)]


#Cho một danh sách số nguyên: [5, 10, 15, 20, 25, 46]
#Tìm giá trị lớn nhất và nhỏ nhất của danh sách.
def hw16(lst):
    return maxv(lst), minv(lst)


#Viết chương trình nhập vào bán kính đường tròn, tính toán và in ra chu vi và diện
#tích hình tròn.
def circumference(r):
    return 2 * math.pi * r

def area(r):
    return math.pi * r * r

def hw17(r):
    if isinstance(r, bool) or not isinstance(r, (int, float)):
        raise TypeError("Bán kính phải là số")
    if r < 0:
        raise ValueError("Bán kính không được âm")
    return circumference(r), area(r)


"""
    Ask the user to enter a new password. Ask them to enter it again. If the two
passwords match, display “Thank you”. If the letters are correct but in the wrong
case, display the message “They must be in the same case”, otherwise display the
message “Incorrect”
    """
def check_pass(password, confirm):
    if password == confirm:
        return "Thank you"
    if password.lower() == confirm.lower():
        return "They must be in the same case"
    return "Incorrect"

def create_pass():
    password = input("input your password: ")
    confirm = input("confirm your password: ")
    return check_pass(password, confirm)


#Viết một chương trình nhập số nguyên dương n và tính tổng của các chữ số của
#số n.
def fix(n):
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n phải là số nguyên")
    if n <= 0:
        raise ValueError("n phải là số nguyên dương")
    lst = []
    for i in str(n):
        lst.append(int(i))
    return lst

def sumn(lst):
    total = 0
    for i in lst:
        total = total + i
    return total

def sum_digits(n):
    return sumn(fix(n))


#Ứng dụng chuyển đổi nhiệt độ từ độ C sang F, chuyển đổi từ kg sang pao(lb),
#diện tích, thể tích, tốc độ, thời gian (Easy)
def c_to_f(n):
    return n * 9 / 5 + 32

def f_to_c(n):
    return (n - 32) * 5 / 9

def kg_to_lb(n):
    return n * 2.20462

def lb_to_kg(n):
    return n * 0.453592

def met_to_feet(n):
    return n * 3.28084

def feet_to_met(n):
    return n * 0.3048

MENU = {
    1: ("c to f", c_to_f),
    2: ("f to c", f_to_c),
    3: ("kg to lb", kg_to_lb),
    4: ("lb to kg", lb_to_kg),
    5: ("met to feet", met_to_feet),
    6: ("feet to met", feet_to_met),
}

def converter():
    while True:
        for key, (label, _) in MENU.items():
            print("   ", key, ":", label)
        print("   ", len(MENU) + 1, ": out program")

        choice = input("input your's number: ").strip()
        if not choice.isdigit():
            print("please enter a number")
            continue
        choice = int(choice)
        if choice == len(MENU) + 1:
            print("out")
            break
        if choice not in MENU:
            print("invalid choice")
            continue

        label, func = MENU[choice]
        value = input("input value: ").strip()
        try:
            value = float(value)
        except ValueError:
            print("please enter a number")
            continue
        print("result :", func(value))


if __name__ == "__main__":
    #r = hw_01(17)
    #r = homework_02(0, 5, -2)
    #r = hw3([1, 2, 3])
    #r = calculate_discount(200)
    #r = hw6([2, 5, 8, 10, 12])
    #r = hw7([2, 5, 3, 10, 12])
    #r = hw8([1, 5, 2, 4, 3])
    #r = hw9([1, 3, 5, 6, 3, 5, 6, 1])
    #r = hw10([86, 86, 85, 85, 85, 83, 23, 45, 84, 1, 2, 0])
    #r = hw11([86, 86, 85, 85, 85, 83, 23, 45, 84, 1, 2, 0])
    #r = hw13([7, 2, 10, 9])
    #r = hw14()
    #r = hw15(12)
    #r = hw16([5, 10, 15, 20, 25, 46])
    #r = hw17(2)
    #r = check_pass("Abc", "abc")
    #r = converter()
    r = sum_digits(1234)
    print(r)
