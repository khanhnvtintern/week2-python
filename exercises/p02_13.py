

def prime(n) : 
    if n < 2 : 
        return False 
    if n == 2 : 
        return True 
    for i in range(2,n) :
        if n % i == 0 : 
            return False
    return True
if __name__ == "__main__":
    n = 12
    for i in range(2,n): 
        if prime(i) : 
            print(i, end = " ")