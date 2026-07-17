"""
    Bài 2. Viết một chương trình có thể tính giai thừa của một số cho trước. 
    Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy. 
    Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.
"""

def homework_02(n):
    result = 1 
    try : 
        for i in range(1,n+1): 
            result *= i
        return result
    except TypeError:
        print("Vui lòng nhập một số nguyên.")
        return {"error": "Vui lòng nhập một số nguyên."}

if __name__ == "__main__":
    r = homework_02(8)
    print(r)