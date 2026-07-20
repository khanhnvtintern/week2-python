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

if __name__ == "__main__":
    r = hw()
    print(r)