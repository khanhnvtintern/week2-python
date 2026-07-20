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

if __name__ == "__main__":
    lst = [5, 10, 15, 20, 25, 46] 
    r = hw(lst)
    print(r)