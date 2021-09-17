def prime_number(start,end):
    prime =[]
    for i in range(start,end+1):
        if i>1:
            for j in range (2,i):
                if i%j == 0:
                    break

            else:

                prime.append(i)

    return prime


print(prime_number(2,900))
