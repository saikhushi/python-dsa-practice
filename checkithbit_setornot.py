def check_ith_bit(n, i):
    if (n & (1 << i)) != 0:
        return True
    return False
n = int(input("Enter a number: "))
i = int(input("Enter bit position to check: "))
print(check_ith_bit(n, i))
