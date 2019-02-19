import sys
sys.stdin=open('input.txt', 'r')

for test_case in range(int(input())):
    arr = list(map(int, input().split()))
    s = 0
    for x in arr:
        if x%2:
            s += x
    print(f'#{test_case+1} {s}')