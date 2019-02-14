import sys
sys.stdin = open("input5.txt","r")
sys.stdout = open('output5.txt', 'w')

T = int(input())

for test_case in range(T):
	N = int(input())
	arr = [[0 for _ in range(N)] for _ in range(N)]
	for i in range(N):
		tmp = input()
		for j in range(N):
			arr[i][j] = int(tmp[j])
		print(arr[i])


