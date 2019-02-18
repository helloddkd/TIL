import sys
sys.stdin = open('input.txt','r')

T=int(input())
for t in range(1,T+1):
    N,M=list(map(int,input().split()))
    arr = list(map(int,input().split()))
    ss = [0]*(N-M+1)

    for i in range(N-M+1):
        s=0
        for j in range(M):
            s += arr[i+j]
        ss[i]=s
    print(f'#{t} {max(ss)-min(ss)}')