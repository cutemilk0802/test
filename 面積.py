print("図形の種類を指定してください。")
print("三角形、長方形、台形、平行四辺形、円、扇形")
zukei = input()
def sankaku():
    kousiki = input().split(",")
    print("面積: "+str(int(kousiki[0])*int(kousiki[1])/2))

def sikaku():
    kousiki = input().split(",")
    print("面積: "+str(int(kousiki[0])*int(kousiki[1])))
    
def daikei():
    kousiki = input().split(",")
    print("面積: "+str((int(kousiki[0])+int(kousiki[1]))*int(kousiki[2])/2))

def en():
    kousiki = input().split(",")
    print("面積: "+str(int(kousiki[0])**2)+"π")

def ougi():
    kousiki = input().split(",")
    print("面積: "+str(int(kousiki[0])**2*int(kousiki[1])/360)+"π")

if zukei == "三角形":
    print("底辺、高さを入力してください。")
    sankaku()
elif zukei == "長方形":
    print("縦、横を入力してください。")
    sikaku()
elif zukei == "台形":
    print("上底、下底、高さを入力してください。")
    daikei()
elif zukei == "平行四辺形":
    print("底辺、高さを入力してください。")
    sikaku()
elif zukei == "円":
    print("半径を入力してください。")
    en()
elif zukei == "扇形":
    print("半径、中心角を入力してください。")
    ougi()