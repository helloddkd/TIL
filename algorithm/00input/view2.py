import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for i in range(T):
    N=int(input())
    arr = list(map(int, input().split()))
    count = [0] * 101
    for num in arr:
        count[num] += 1
    m = 100-count[::-1].index(max(count))
    print(f'#{i} {m}')