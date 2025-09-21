print("判定したい数字 ")
num = int(input())
if num == 1:
    print("素数ではありません")
sosuu = 2
for i in range(num-2):
    if num%(i+2) == 0:
        print("素数ではありません")
        break
    else:
        sosuu +=1
if sosuu == num :
    print("素数です")