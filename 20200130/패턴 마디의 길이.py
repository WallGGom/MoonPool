import sys
sys.stdin = open('패턴 마디의 길이.txt', 'r')

N = int(input())
for tc in range(N):
    word = input()
    count = 1
    storage = [0]*len(word)
    bank = [0] * len(storage)
    for k in range(1, len(word)+1):
        for j in range(len(word)//count):
            storage[j] = word[j*k:(j+1)*k]
        count += 1
        bank[k-1] = storage
        storage = [0] * (len(word)//count)
        if bank[k-1][0] == bank[k-1][1]:
            # ans = (len(word) // len(bank[k-1][0])) # 반복되는 마디 수
            ans = len(bank[k-1][0]) # 반복되는 마디 길이
            print('#{} {}'.format(tc+1, ans))
            break












