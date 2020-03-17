import sys
sys.stdin = open('쇠막대기 자르기.txt','r')

T = int(input())
for tc in range(T):
    steel = input()
    cnt = 0
    makdae = 0
    for i in range(len(steel)):
        if steel[i] == '(':
            makdae += 1
        elif steel[i] == ')' and steel[i-1] =='(':
            makdae -= 1
            cnt += makdae    
        elif steel[i] == ')' and steel[i-1] !='(':              
            cnt += 1        
            makdae -= 1      
    print(f'#{tc+1} {cnt}')


            


