import sys
sys.stdin = open("input.txt", "r")

for r in range(int(input())):
    K, N, M = list(map(int, input().split()))
    stations = list(map(int, input().split()))
    charge=0
    status=0
    interval = [0]*(M)
    stations.append(N)
    for i in range(M):
        interval[i]=(stations[i+1]-stations[i])
    if max(interval)>K:
        charge = 0
    else:
        for i in range(len(stations)):
            if status+K >= N:
                    break
            for j in range(len(stations)-1,-1,-1):
                if status+K>=stations[j]:
                    status = stations[j]
                    break
            charge += 1
    print(f'#{r+1} {charge}')