def no_plus_sum(a,b):

    while b!=0:
        carry = a & b
        a = a^b
        b = carry << 1

    return a


print(no_plus_sum(8,7))