def pattern(num):
    bank = ""
    for i in range(1, (num + 1), 2):
        bank += ((str(i) * i) + '\n')

    bank = bank[:len(bank)-1]
    return bank

print(pattern(9))

