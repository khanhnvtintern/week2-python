

def c_to_f() : 
    n = int(input("inp C : " ))
    return n*9/5 + 32 
def f_to_c(): 
    n = int(input("inp F : " ))
    return (n-32)*5/9
def kg_to_lb(): 
    n = int(input("inp kg : " ))
    return n*2.20462
def lb_to_kg():
    n = int(input("inp lb : " ))
    return n*0.453592
def met_to_feet():
    n = int(input("inp met : " ))
    return n*3.28084
def feet_to_meet():
    n = int(input("inp feet : " ))
    return n*0.3048
def out(n):
    return "out"

if __name__ == "__main__" : 
    server = print(""" 
                   1 : c to f
                   2 : f to c
                   3 : kg to lb
                   4 : lb to kg
                   5 : met to feet
                   6 : feet to meet
                   7 : out program
                   """)
    while True : 
        server = print(""" 
                   1 : c to f
                   2 : f to c
                   3 : kg to lb
                   4 : lb to kg
                   5 : met to feet
                   6 : feet to meet
                   7 : out program
                   """)
        user = int(input("input your's number : "))
        if user == 1 : 
            r = c_to_f()
            print("result :",r)
            continue
        elif user == 2 : 
            r = f_to_c()
            print("result :",r)
            continue
        if user == 3 : 
            r = kg_to_lb()
            print("result :",r)
            continue
        if user == 4 : 
            r = lb_to_kg()
            print("result :",r)
            continue
        if user == 5 : 
            r = met_to_feet()
            print("result :",r)
            continue
        if user == 6 : 
            r = feet_to_meet()
            print("result :",r)
            continue
        if user == 7 : 
            r = out(user)
            print(r)
            break
        
            