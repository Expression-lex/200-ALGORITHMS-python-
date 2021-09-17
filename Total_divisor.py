def num_divisors(num):
    divisors = [i for i in range(1, num+1) if num%i == 0]
    return (divisors, len(divisors))


print(num_divisors(900))