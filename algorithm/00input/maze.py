import sys
sys.stdin = open('input.txt','r')

for i in range(10):
    N = int(input())
    arr=[]
    for i in range(16):
        arr.append(list(input()))
    print(N, arr)
    