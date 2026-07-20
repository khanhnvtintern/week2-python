"""
Cho một số nguyên, in " YES​" nếu chữ số cuối của nó là 7 và in " NO​" nếu không.

    """

def hw_01(n): 
    if n % 10 == 7:
        return "YES"
    return "NO"
if __name__ == "__main__":
    r = hw_01(307)
    print(r)