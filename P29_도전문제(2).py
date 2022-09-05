
# 3자리의 자연수 중 각 자리의 숫자의 합이 18인 경우의 수
mycount = 0

for i in range(100,1000):
    mysum =0
    for j in str(i):
        mysum += int(j)
    if mysum == 18:
        mycount += 1
        # print(i)

print(mycount)