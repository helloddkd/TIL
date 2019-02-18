import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for c in range(T):
    N = int(input())
    print(N)
    arr = [[0]*N]*N
    print(arr)
    arr[0] = [x for x in range(1,N+1)]
    for a in range(1,N):
        arr[a][-1] = [x for x in range(N+1, 2*N-1)]
