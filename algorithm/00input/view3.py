import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(T):
    N = int(input())
    days = list(map(int, input().split()))
    b=0
    while days:
        m = max(days)
        i = days.index(m)
        if i == 0:
            b += 0
            days.remove(m)
        else:
            b+=m*i - sum(days[:i])
        days = days[i+1:]
    print(f'#{test_case+1} {b}')