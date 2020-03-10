import sys
sys.stdin = open('최장 증가 부분 수열.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    input_data = list(map(int,input().split()))
    mx = 0
    result = list()
    for n in range(N):
        for i in range(n,N):
            sample = list()
            for j in range(i,N):
                if len(sample):s
                    if sample[-1] <= input_data[j]:
                        sample.append(input_data[j])
                    else:
                        continue
                else:
                    sample.append(input_data[n])
            if len(sample) > mx:
                mx = len(sample)
                result = sample
    print('#{} {}'.format(tc+1,mx))
    print(result)