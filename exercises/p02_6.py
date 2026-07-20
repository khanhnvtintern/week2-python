#Viết chương trình in ra tất cả các số chẵn trong một danh sách
def hw():
    lst = [2, 5, 8, 10, 12] 
    fix_lst = []
    for i in lst : 
        if i % 2 == 0 : 
            fix_lst.append(i)
    return fix_lst

if __name__ == "__main__":
    r = hw()
    print(r)