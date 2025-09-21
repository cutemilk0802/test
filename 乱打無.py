import random
random_num = random.randint(1,500)
num=0
count=0
while num != random_num:
    print("数を入力 ")
    num = int(input())
    if num > random_num:
        print("それより小さい")
    elif num < random_num:
        print("それより大きい")
    count+=1
print(str(count)+"回で正解しました!")