

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
if __name__ == '__main__' : 
    n = 3124 
    lst = fix(n)
    r = sumn(lst)
    print(r)