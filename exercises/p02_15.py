

def cO(r) : 
    return "{:.2f}".format(2*3.14*r)
def sO(r) :
    return "{:.2f}".format(3.14*r*r)
def hw(r) : 
    return cO(r), sO(r)
if __name__ == "__main__":
    r = hw(5)
    print(r)