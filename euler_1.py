#multiples 3 & 5
def sum_multiples_of_3_and_5(limit):
    total = 0

    for i in range(limit):
        if  i % 3 == 0 or i % 5 == 0:
            total += i
    return total

limit = 1000
result = sum_multiples_of_3_and_5(limit)

print(" The sum of the mulitples of 3 and 5 is :" , result)