nb = int(input())
f = 0
g = 0
for i in range(nb):
    tf, tg = input().split()
    f += int(tf)
    g += int(tg)

if f > g:
    print("Frodon plus rapide")
elif f < g:
    print("Gandalf plus rapide")
else:
    print("Pas de meilleur chemin")