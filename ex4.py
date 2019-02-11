N, A, E = map(int, input().split())
#N Nombre de soldat
#A Nombre de relation amis
#E Nombre relations ennemis

Amis = []
Ennemis = []

for i in range(A):
    Amis.append(tuple(map(int, input().split())))

Amis += [(item[1],item[0]) for item in Amis]

for j in range(E):
    Ennemis.append(tuple(map(int, input().split())))

Ennemis += [(item[1],item[0]) for item in Ennemis]

def all_pairs(lst):
    if len(lst) < 2:
        yield []
        return
    if len(lst) % 2 == 1:
        # Handle odd length list
        for i in range(len(lst)):
            for result in all_pairs(lst[:i] + lst[i+1:]):
                yield result
    else:
        a = lst[0]
        for i in range(1,len(lst)):
            pair = (a,lst[i])
            for rest in all_pairs(lst[1:i]+lst[i+1:]):
                yield [pair] + rest

def computeScore(lst,amis,ennemis):
    score = 0
    for e in lst:
        if e in amis:
            score += 2
        elif e in ennemis:
            return -1
        else:
            score += 1
    return score

def forceBrute(amis,ennemis):
    all_res = []

    #paires = list(combinations((range(1,N+1)), 2))
    for x in all_pairs(list(range(1,N+1))):
        all_res.append(computeScore(x,amis,ennemis))
    return all_res

print(max(forceBrute(Amis,Ennemis)))