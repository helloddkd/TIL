import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(T):
    N = int(input())
    days = list(map(int, input().split()))
    