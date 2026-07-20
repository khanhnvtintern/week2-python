"""
    Ask the user to enter a new password. Ask them to enter it again. If the two 
passwords match, display “Thank you”. If the letters are correct but in the wrong 
case, display the message “They must be in the same case”, otherwise display the 
message “Incorrect” 
    """

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