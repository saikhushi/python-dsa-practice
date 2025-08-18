def binary_to_decimal(k):
    resNumber = 0 
    p2 = 1 
    for i in range(len(k) - 1, -1, -1): 
        if k[i] == '1':
            resNumber += p2
        p2 *= 2 
    return resNumber

k = input("Enter a binary number: ")   # no space before k
print("Decimal:", binary_to_decimal(k))
