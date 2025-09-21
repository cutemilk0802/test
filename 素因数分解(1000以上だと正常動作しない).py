print("素因数分解したい数字 ")
num = int(input())
count = 1
sosuu = 2
while num/sosuu >1:
    sosuu = 2
    count +=1
    for i in range(count-2):
        if count%(i+2) == 0:
            break
        else:
            sosuu +=1
    if sosuu == count :
        if num % sosuu ==0:
            num /= sosuu
            print(sosuu)  
            count -=1