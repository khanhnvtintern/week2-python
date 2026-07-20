def minv(lst) : 
    if len(lst) == 0 : 
        return None
    minn = lst[0]
    for i in lst : 
        if i < minn : 
            minn = i
    return minn
def maxv(lst) : 
    if len(lst) == 0 : 
        return None 
    maxn = lst[0]
    for i in lst : 
        if i > maxn : 
            maxn = i 
    return maxn 

def hw() : 
    #lst = [10, 3, 5, 6]
    lst = [7, 2, 10, 9]
    mv = minv(lst)
    mxv = maxv(lst)
    return mxv - mv 

if __name__ == "__main__":
    r = hw()
    print(r)