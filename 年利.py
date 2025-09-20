print("年利(%) ")
per = int(input())/100 + 1
print("初期値、上限値 ")
startmax = input().split(",")
years = int(startmax[1]) / int(startmax[0]) / per
count = 1
while years >= 1:
    years = years /per
    count+=1
print("かかった年: " + str(count))