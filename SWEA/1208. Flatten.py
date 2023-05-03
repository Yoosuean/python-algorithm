for i in range(10):
    dump=int(input())
    boxs=list(map(int,input().split()))
    for j in range(dump):
        max_box=boxs.index(max(boxs))
        min_box=boxs.index(min(boxs))
        boxs[max_box]-=1
        boxs[min_box]+=1
    print(f'#{i+1} {max(boxs)-min(boxs)}')
