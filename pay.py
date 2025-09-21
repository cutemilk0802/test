print("いくら? ")
money = int(input())
print("100円:"+str(money//100)+"枚")
money -= money//100*100
print("10円:"+str(money//10)+"枚")
money -= money//10*10
print("1円:"+str(money)+"枚")