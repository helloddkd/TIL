import sys
sys.stdin = open('input.txt','r')

T=int(input())
for i in range(T):
    N=int(input())
    arr=list(map(int,input().split()))
    mx = arr[0]
    mn = arr[0]
    for num in arr:
        if mx<num:
            mx=num 
        if mn>num:
            mn=num 
    print(f'#{i+1} {mx-mn}')
