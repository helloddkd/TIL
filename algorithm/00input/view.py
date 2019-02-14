import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("view.txt", "w")

for test_case in range(10):
    N = int(input())
    case = list(map(int, input().split()))

    result = 0

    for i in range(2, len(case)-2):
        if case[i-1] < case[i] and case[i-2] < case[i]:
            if case[i+1] < case[i] and case[i+2] < case[i]:
                m = max(case[i-2], case[i-1], case[i+1], case[i+2])
                result += case[i] - m

    print('#{} {}'.format(test_case+1, result))