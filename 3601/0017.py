from pkg_resources import get_default_cache


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    if a==1:
        return True

    else:
        return False
c=gcd(120,137)
print(c)