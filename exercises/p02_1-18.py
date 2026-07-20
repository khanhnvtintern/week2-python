#Cho một số nguyên, in " YES​" nếu chữ số cuối của nó là 7 và in " NO​" nếu không.
def hw_01(n): 
    if n % 10 == 7:
        return "YES"
    return "NO"

"""
Cho biết tọa độ của ba điểm A, B, C trên một đoạn thẳng. In khoảng cách từ điểm
A đến điểm gần nó nhất.
"""
def homework_01(a, b, c):
    try : 
        if a and b and c is None or a and b and c is not (int or float):
            return "error"
        else :  
            ab = abs(a - b)
            ac = abs(a - c)
            if ab < ac:
                return ab
            else:
                return ac
    except TypeError:
        return "type error"

#iết chương trình tính tổng các số trong một danh sách
def hw(n) :
    sum = 0
    for i in n:
        sum += i
    return sum


"""
    Viết game đoán số may mắn (guess the number)
Máy tính nghĩ một số random từ 1 cho đến 15 và hỏi bạn đoán. Máy tính sẽ nói
cho bạn khi bạn đoán sai là số may mắn là phải lớn hơn hoặc nhỏ hơn. Bạn sẽ
chiến thắng nếu bạn đoán đúng số đó trong 5 lượt chơi.
    """

import random


def guess():
    rd = random.randint(1, 15)
    for i in range(5):
        ip = input("guess 1-15 ")
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
        print("losethe answer is ", rd)


"""
Một cửa hàng sẽ giảm giá 10% nếu tổng chi phí mua hàng lớn hơn 10.000
Người dùng về số lượng từ bàn phím
Giả sử, một đơn vị mặt hàng sẽ có giá 100 đồng.
In tổng chi phí hóa đơn cho người dùng.
"""

def total(user_input,price):
    return user_input * price
def calculate_discount(user_input):
    price = 100
    discount = 10 / 100
    over_price = 10000
    total_price = total(user_input, price)
    if total_price > over_price:
        total_price = total_price - (total_price * discount)
    return total_price


#Viết chương trình in ra tất cả các số chẵn trong một danh sách
def hw():
    lst = [2, 5, 8, 10, 12]
    fix_lst = []
    for i in lst :
        if i % 2 == 0 :
            fix_lst.append(i)
    return fix_lst


#Viết một chương trình tìm ra số lớn nhất của một danh sách mà không sử dụng
#hàm max()

def hw():
    lst =  [2, 5, 3, 10, 12]
    mx = 0;
    for i in lst :
        if i > mx :
            mx = i
    return mx


#Cho một danh sách các số, hãy tìm và in tất cả các phần tử lớn hơn phần tử trước
def hw() :
    lst = [1,5,2,4,3]
    #lst = [5,5,5,5,5]
    fst = lst[0]
    r = []
    #print(len(lst)) #debug
    for i in range(1, len(lst)):
        #print(i,lst[i])#debug :3
        if lst[i] >= fst :
            r.append(lst[i])
        fst = lst[i]
    return r


#Bài 9.
#Viết một chương trình xóa tất cả phần tử lặp lại (trùng lặp) ra khỏi danh sách.
def hw():
    lst =  [1, 3, 5, 6, 3, 5, 6, 1]
    r = []
    for i in lst :
        if i not in r :
            r.append(i)
    return r


#Get first, second best scores from the list.
#List may contain duplicates

def hw2():
    lst = [86,86,85,85,85,83,23,45,84,1,2,0]
    fst = max(lst)
    while True :
        if lst.count(fst) > 0 :
            print(lst.count(fst))
            lst.remove(fst)
        else :
            break
    sec = max(lst)
    return fst,sec
def hw():
    lst =  [86,86,85,85,85,83,23,45,84,1,2,0]
    fst = 0
    sec = 0
    for i in lst :
        if i > fst :
            sec = fst
            fst = i
        elif i > sec and i != fst :
            sec = i
    return fst,sec


#Given an array length 1 or more of ints, return the difference between the largest
#and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2)
#functions return the smaller or larger of two values.

def minv(lst) :
    if len(lst) == 0 :
        return None
    minn = lst[0]
    for i in lst :
        if i < minn :
            minn = i
    return minn
def maxv(lst) :
    if len(lst) == 0 :
        return None
    maxn = lst[0]
    for i in lst :
        if i > maxn :
            maxn = i
    return maxn

def hw() :
    #lst = [10, 3, 5, 6]
    lst = [7, 2, 10, 9]
    mv = minv(lst)
    mxv = maxv(lst)
    return mxv - mv


#Viết một chương trình in ra các số chia hết cho 7 nhưng không chia hết cho 5
#nằm trong khoảng 100 cho đến 1000 (tính cả 100 và 1000).
#Kết quả: In trên một dòng và cách nhau bởi dấu phẩy.


def hw():
    mn = 100
    mx =1000
    divide = 7
    not_divide = 5
    lst = []
    for i in range(mn, mx + 1) :
        if i % divide == 0 and i % not_divide != 0 :
            lst.append(i)
    return lst


#Viết một chương trình in tất cả các số nguyên tố nhỏ hơn n. Với n là số nguyên
#dương nhập từ bàn phím.

def prime(n) :
    if n < 2 :
        return False
    if n == 2 :
        return True
    for i in range(2,n) :
        if n % i == 0 :
            return False
    return True
n = 12
for i in range(2,n): 
    if prime(i) : 
        print(i, end = " ")

#Cho một danh sách số nguyên: [5, 10, 15, 20, 25, 46]
#Tìm giá trị lớn nhất và nhỏ nhất của danh sách.

def mx(lst) :
    mx = 0
    for i in lst :
        if i > mx :
            mx = i
    return mx
def mn(lst) :
    mn = lst[0]
    for i in lst :
        if i < mn :
            mn = i
    return mn
def hw(lst) :
    return mx(lst),mn(lst)


#Viết chương trình nhập vào bán kính đường tròn, tính toán và in ra chu vi và diện
#tích hình tròn.

def cO(r) :
    return "{:.2f}".format(2*3.14*r)
def sO(r) :
    return "{:.2f}".format(3.14*r*r)
def hw(r) :
    return cO(r), sO(r)


"""
    Ask the user to enter a new password. Ask them to enter it again. If the two
passwords match, display “Thank you”. If the letters are correct but in the wrong
case, display the message “They must be in the same case”, otherwise display the
message “Incorrect”
    """

def create_pass():
    user = input("input your password: ")
    return user
def confirm_pass(user):
    user_confirm = input("confirm your password: ")
    if user == user_confirm :
        return "Thank you"
    else :
        return "they must be in the samecase "


#Viết một chương trình nhập số nguyên dương n và tính tổng của các chữ số của
#số n.
#
def fix(n):
    lst = []
    for i in str(n):
        lst.append(int(i))
    return lst
def sumn(lst):
    total = 0
    for i in lst :
         total = total + i
    return total


#Ứng dụng chuyển đổi nhiệt độ từ độ C sang F, chuyển đổi từ kg sang pao(lb),
#diện tích, thể tích, tốc độ, thời gian (Easy)
#
def c_to_f() :
    n = int(input("inp C : " ))
    return n*9/5 + 32
def f_to_c():
    n = int(input("inp F : " ))
    return (n-32)*5/9
def kg_to_lb():
    n = int(input("inp kg : " ))
    return n*2.20462
def lb_to_kg():
    n = int(input("inp lb : " ))
    return n*0.453592
def met_to_feet():
    n = int(input("inp met : " ))
    return n*3.28084
def feet_to_meet():
    n = int(input("inp feet : " ))
    return n*0.3048
def out(n):
    return "out"
server = print(""" 
                   1 : c to f
                   2 : f to c
                   3 : kg to lb
                   4 : lb to kg
                   5 : met to feet
                   6 : feet to meet
                   7 : out program
                   """)
while True : 
    server = print(""" 
                   1 : c to f
                   2 : f to c
                   3 : kg to lb
                   4 : lb to kg
                   5 : met to feet
                   6 : feet to meet
                   7 : out program
                   """)
    user = int(input("input your's number : "))
    if user == 1 : 
        r = c_to_f()
        print("result :",r)
        continue
    elif user == 2 : 
        r = f_to_c()
        print("result :",r)
        continue
    if user == 3 : 
        r = kg_to_lb()
        print("result :",r)
        continue
    if user == 4 : 
        r = lb_to_kg()
        print("result :",r)
        continue
    if user == 5 : 
        r = met_to_feet()
        print("result :",r)
        continue
    if user == 6 : 
        r = feet_to_meet()
        print("result :",r)
        continue
    if user == 7 : 
        r = out(user)
        print(r)
        break
if __name__ == "__main__":
    r = fix()
    print(r)