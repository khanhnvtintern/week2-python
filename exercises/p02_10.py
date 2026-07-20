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
if __name__ == "__main__":  
    r = hw()
    r2= hw2()
    print(r)
    print(r2)
        