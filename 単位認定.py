print("課題、中間、定期の評価割合")
wariai = input().split(",")
print("それぞれの満点の点数")
max = input().split(",")
print("それぞれの獲得した点数")
point = input().split(",")
print("A,B,C,Fの基準値")
kijun = input().split(",")
goukei = int(point[0]) / int(max[0]) * int(wariai[0]) + int(point[1]) / int(max[1]) * int(wariai[1]) + int(point[2]) / int(max[2]) * int(wariai[2]) 
if goukei >= int(kijun[0]):
    print("A")
elif goukei >= int(kijun[1]):
    print("B")
elif goukei >= int(kijun[2]):
    print("C")
else:
    print("F")