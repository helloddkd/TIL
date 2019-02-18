import sys
sys.stdin = open("input.txt", "r")

for i in range(10):
    D = int(input())
    arr = list(map(int,input().split()))
    while D>0:
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1
        D -= 1
    print(f'#{i+1} {max(arr)-min(arr))}')

