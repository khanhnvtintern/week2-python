#Viết một chương trình tìm ra số lớn nhất của một danh sách mà không sử dụng 
#hàm max()

def hw(): 
    lst =  [2, 5, 3, 10, 12]
    mx = 0; 
    for i in lst : 
        if i > mx : 
            mx = i
    return mx
if __name__ == "__main__":
    r = hw()
    print(r)