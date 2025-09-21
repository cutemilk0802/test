print("何番目まで実行する?")
count = int(input())-1
lastnum = 0
num = 1
print(num)
for i in range(count):
    print(num+lastnum)
    numcopy = num
    num += lastnum
    lastnum = numcopy