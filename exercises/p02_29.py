"""29.
You are driving a little too fast, and a police officer stops you. Write code to 
compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big 
ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 
inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your 
birthday -- on that day, your speed can be 5 higher in all cases."""

def caught_speeding(speed, is_birth):
    if is_birth:
        speed -= 5
    if speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    else:
        return 2



"""Given 3 int values, a b c, return their sum. However, if one of the values is 13 
then it does not count towards the sum and values to its right do not count. So 
for example, if b is 13, then both b and c do not count. """   
def check_n(lst):
    for i in range(len(lst)):
        if lst[i] == 13:
            return i
    return -1
def lucky_num(a,b,c):
    lst = [a,b,c]
    r = check_n(lst)
    if r == -1:
        return sum(lst)
    else:
        lst = lst[:r]
        return sum(lst)
#- after optimizing 
def lucky_sum2(a, b, c):
    lst = [a, b, c]
    for i in range(3):
        if lst[i] == 13:
            return sum(lst[:i])
    return sum(lst)

"""33.Given a dictionary containing counts of both upvotes and downvotes, return what 
vote count should be displayed. This is calculated by subtracting the number of 
downvotes from upvotes. """
def get_vote_count(votes):
    return votes.get("upvotes", 0) - votes.get("downvotes", 0)

#Sắp xếp mảng 1 chiều tăng dần
def sort_1(arr):
    arr = arr[:]       
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

"""Viết một hàm có tên capital_indexes. Hàm nhận một tham số duy nhất là một 
chuỗi. Hàm của bạn sẽ trả về một danh sách tất cả các chỉ số (index) trong chuỗi 
có chữ in hoa."""
def capital_indexes(st):
    lst = []
    for i in range(len(st)):
        if st[i].isupper():
            lst.append(i)
    return lst

"""Kiểm tra đối xứng 
Một chuỗi gọi là đối xứng khi đọc từ trái qua phải hay phải qua trái thì kết quả 
giống nhau.  
Ví dụ: Chuỗi  "​bob​" và chuỗi " abba​" là đối xứng 
Chuỗi “ abcd​” không phải đối xứng vì  "abcd" != "dcba"​. 
Viết một hàm có tên  palindrome ​ kiểm"""
def palindrome(st):
    return st == st[::-1]

if __name__ == "__main__":
    #r = caught_speeding(65,True)
    #r =  lucky_num(3,1,13)
    #r = get_vote_count({ "upvotes": 13, "downvotes": 0 })
    #r = sort_1([3,5,2,8,10,7,12])
    #r = capital_indexes("HeLIO")
    r = palindrome('boba')
    print(r)