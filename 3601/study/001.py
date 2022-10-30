def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    if a==1:
        return True
    else:
        return False
