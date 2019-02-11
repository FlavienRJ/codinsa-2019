
#
# N, V, E = map(int, input().split())
# #N ennemi
# #V vie
# #E Energie
#
# Ennemis = []
#
# for i in range(N):
#     Ennemis.append(list(map(int, input().split())))
#
# i = 0
# res = []
#
# for com in itertools.permutations(Ennemis):
#     i += 1
#     Vtmp = V
#     Etmp = E
#     for enn in list(com):
#         en_con = 0
#         if Etmp > enn[0]:
#             en_con = enn[0]
#             Etmp = Etmp - en_con
#         else:
#             en_con = Etmp
#             Etmp = 0
#         Vtmp = Vtmp - degat(enn[0],en_con,enn[1])
#         if Vtmp < 1:
#             break
#     if Vtmp < 1:
#         continue
#     else:
#         res.append(Vtmp)
#
# if len(res) == 0:
#     print("GAME OVER")
# else:
#     print(str(max(res)))

import itertools
def degat(defe, nrj, att):
    return (defe-nrj)*att

N, V, E = list(map(int, input().split()))
#N ennemi
#V vie
#E Energie

Enemies = []
for i in range(N):
    Di, Ai = list(map(int, input().split()))
    Enemies.append([Di, Ai])
    Enemies = sorted(Enemies, key=lambda a: a[1])[::-1] #Classement de A mini a A maxi

for e in Enemies:
    Di = e[0]
    Ai = e[1]

    energy = 0
    if E > Di:
        E -= Di
        nrj = Di
    else:
        nrj = E
        E = 0

    V -= degat(Di, nrj, Ai)

if V > 0:
    print(V)
else:
    print("GAME OVER")