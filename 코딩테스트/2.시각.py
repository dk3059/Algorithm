# 완전 탐색 : 모든 경우의 수를 주저 없이 다 계산하는 해결 방법

### 문제 : 시각

#Input
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count+=1
print(count)

