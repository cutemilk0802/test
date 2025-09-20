print("数字を入力")
num = input().split(',')
num[0] = int(num[0])
num[1] = int(num[1])
print("演算子を入力")
keisan = input()
if keisan == "+":
    keisan = num[0] + num[1]
elif keisan == "-":
    keisan = num[0] - num[1]
elif keisan == "*":
    keisan = num[0] * num[1]
elif keisan == "/":
    keisan = num[0] / num[1]
elif keisan == "%":
    keisan = num[0] % num[1]
elif keisan == "**":
    keisan = num[0] ** num[1]
else:
    print("演算子を入力してください")
    exit()
print("演算結果:" + str(keisan))
