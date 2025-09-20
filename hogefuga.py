print("何番まで表示する?")
num = int(input())
for i in range(num):
    if (i+1)%3 ==0 and (i+1)%5 ==0:
        print("hogefuga")
    elif (i+1)%3 ==0:
        print("hoge")
    elif (i+1)%5 ==0:
        print("fuga")
    else:
        print(i+1)
