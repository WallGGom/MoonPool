def reverse_letter(word):
    bank = ""
    storage = ""
    for i in range(len(word) - 1, -1, -1):
        bank += word[i]
    for char in bank:
        if char.isalpha():
            storage += char

    return storage


print(reverse_letter('ultr53o?n'))