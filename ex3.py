N = int(input()) #nombre de soldats
data = list(map(int, input().split()))

if N < 3:
    print("MIXTE")
else:
    #verifier le cas si 2 soldats ont la meme taille
    m = 0 # -1 sinon 1
    res = 0 # 0:mixte 1:carnage
    chance = 0
    for i in range(N - 2):
        if (data[i] > data[i+1]) and (m == 1):
            res = 0
            m = -1
            continue
        elif (data[i] < data[i+1]) and (m == 1):
            if chance == 0:
                chance = 1
                res = 0
            else:
                res = 1
                m = 1
                break
        elif (data[i] > data[i+1]) and (m == -1):
            if chance == 0:
                chance = 1
                res = 0
            else:
                res = 1
                m = -1
                break
        elif (data[i] < data[i+1]) and (m == -1):
            res = 0
            m = 1
            continue
        elif (data[i] > data[i+1]) and (m == 0):
            m = -1
            continue
        elif (data[i] < data[i+1]) and (m == 0):
            m = 1
            continue
        else:
            continue

    if res > 0:
        print("CARNAGE")
    else:
        print("MIXTE")