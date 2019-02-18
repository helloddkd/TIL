import sys
sys.stdin = open("card.txt", "r")

T=int(input())
for i in range(T):
    N=int(input())
    arr = list(map(int,list(input())))
    count = [0]*10
    for num in arr:
        count[num] += 1
    mx = max(count)
    mxi=0
    for j in range(len(count)):
        if count[j] == mx:
            mxi = j
    print(f'#{i+1} {mxi} {mx}')