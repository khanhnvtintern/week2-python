

def create_pass(): 
    user = input("input your password: ")
    return user
def confirm_pass(user): 
    user_confirm = input("confirm your password: ")
    if user == user_confirm :
        return "Thank you"
    else :
        return "they must be in the samecase "

if __name__ == "__main__":
    user = create_pass()
    n = confirm_pass(user)
    print(n)