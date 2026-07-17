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

if __name__ == "__main__":
    r = homework_01(9, 5,6)
    print(r)    