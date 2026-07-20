"""
Một cửa hàng sẽ giảm giá 10% nếu tổng chi phí mua hàng lớn hơn 10.000 
Người dùng về số lượng từ bàn phím 
Giả sử, một đơn vị mặt hàng sẽ có giá 100 đồng. 
In tổng chi phí hóa đơn cho người dùng. 
"""

def total(user_input,price):
    return user_input * price
def calculate_discount(user_input):
    price = 100
    discount = 10 / 100
    over_price = 10000
    total_price = total(user_input, price)
    if total_price > over_price:
        total_price = total_price - (total_price * discount)
    return total_price

if __name__ == "__main__":
    user_input = int(input("input your mount of product: "))
    result = calculate_discount(user_input)
    print("total price: ", format(result, ".0f"))