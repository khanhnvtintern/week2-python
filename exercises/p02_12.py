


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