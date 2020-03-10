T = int(input())

for tc in range(T):
    gallery = list(str(input()))
    # print(gallery)

    clap = 0
    helper = 0
    for need, human in enumerate(gallery):
        # print(need, human)
        if need <= clap:
            clap += int(human)
        elif human == 0:
            continue
        elif need > clap:
            helper += (need - clap)
            clap += (need - clap) + int(human)
    print('#{} {}'.format(tc+1,helper))