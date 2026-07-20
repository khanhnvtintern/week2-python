#Bài 9. 
#Viết một chương trình xóa tất cả phần tử lặp lại (trùng lặp) ra khỏi danh sách.
def hw(): 
    lst =  [1, 3, 5, 6, 3, 5, 6, 1]
    r = []
    for i in lst : 
        if i not in r : 
            r.append(i)
    return r
if __name__ == "__main__":
    r = hw()
    print(r)