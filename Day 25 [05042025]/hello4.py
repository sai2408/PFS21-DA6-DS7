def palindrome(a):
    if a == a[::-1]:
        print("YES")
    else:
        print("NO")
def pangram(x):
    k1 = set(x)
    if len(k1) == 26:
        return True
    else:
        return False
