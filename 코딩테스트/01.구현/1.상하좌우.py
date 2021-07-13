# 시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행

### 문제 1. 상하좌우
#Input
n = int(input())
x,y = 1, 1
plans = input().split() 

#Solution
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
directions = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(directions)):
        if plan == directions[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
    print(plan, x, y)
print(x, y)

