import math
from collections import deque
def dijkstra(n,carte,posNoeuds, num):
    dist = [[math.inf for i in range(n)] for j in range(n)]
    dist[posNoeuds[num][0]][posNoeuds[num][1]] = 0 #noeud de départ
    file = deque()
    file.append([posNoeuds[num][0],posNoeuds[num][1]])
    while(len( file ) != 0):
        pos = file.popleft()
        if( pos[0] == posNoeuds[1][0] and pos[1] == posNoeuds[1][1]):
            continue

        if( pos[0] > 0 and not carte[pos[0]-1][pos[1]] and dist[pos[0]-1][pos[1]] == math.inf):
            dist[pos[0]-1][pos[1]] = dist[pos[0]][pos[1]]+1
            file.append([pos[0]-1,pos[1]])
        if( pos[0] < n-1 and not carte[pos[0]+1][pos[1]] and dist[pos[0]+1][pos[1]] == math.inf ):
            dist[pos[0]+1][pos[1]] = dist[pos[0]][pos[1]]+1
            file.append([pos[0]+1,pos[1]])

        if( pos[1] > 0 and not carte[pos[0]][pos[1]-1] and dist[pos[0]][pos[1]-1] == math.inf):
            dist[pos[0]][pos[1]-1] = dist[pos[0]][pos[1]]+1
            file.append([pos[0],pos[1]-1])

        if( pos[1] < n-1 and not carte[pos[0]][pos[1]+1] and dist[pos[0]][pos[1]+1] == math.inf):
            dist[pos[0]][pos[1]+1] = dist[pos[0]][pos[1]]+1
            file.append([pos[0],pos[1]+1])
    #recompose le vecteur des distances
    #print(" ")
    #print("dist pour le noeud ", num)
    #for k in range( n):
    #	print(dist[k])
    distNoeuds  = [math.inf for k in range( a+2 )]
    for k in range( a+2 ):
        distNoeuds[k] = min( distNoeuds[k], dist[posNoeuds[k][0]][posNoeuds[k][1]])
    return distNoeuds

def longueChaine (num, bitmap):
    key = str( num ) +"".join( map ( str , bitmap ) )
    if( num == 1): 
        return 0
    if( key in mem):
        return mem[key]
    else:
        maxi = - math.inf
        for i in range( a+2 ):
            if( bitmap[i]!=1 and distMain[num][i] != -math.inf): #si on a pas encore visité le noeud i et qu'il est atteignable depuis le noeud courant
                bitmap[i] = 1 #on le choisit pour continuer
                maxi = max(maxi, distMain[num][i] + longueChaine(i,bitmap)) # on évalue la plus longue chaine en ayant ajouté ce noeud
                bitmap[i] = 0
        mem[key] = maxi
        return maxi

n,p,a = map(int,input().split())
posNoeuds = [[0 for i in range(2)] for j in range( a+2 )]
posNoeuds[0] = list(map(lambda x :int(x)-1,input().split()))
posNoeuds[1] = list(map(lambda x :int(x)-1,input().split()))
allie = [0] * (a+2)
for i in range( a ):
    l,c,f = map(int,input().split())
    posNoeuds[ i+2 ] = [l-1,c-1]
    allie[i+2] = f
carte = [[False for i in range(n)] for j in range(n)]
for i in range ( n ):
    carte [ i ] = list(map(int,input().split()))
distMain = [[0 for i in range(a+2)] for j in range(a+2)]
#print(carte)
#print(posNoeuds)
#print("fin pos noeuds")
#print("")
for i in range(a+2):
    distMain[i] = dijkstra(n,carte,posNoeuds,i)
#print("")
#print("dist finales : ")
#for k in range( a+2 ):
    #print(dist[k])
#appliquer le poids à tous les noeuds alliés
#for i in range(a+2):
#	print(distMain[i])
#print("")
#print("sans opti, ",a)
#print(-distMain[0][1]+p)
for i in range( a+2 ):
    for j in range( a+2):
        distMain[i][j] = - distMain[i][j] + allie[j]
#for i in range(a+2):
#	print(distMain[i])
mem = {}
use = [0] * (a+2)
use[0] = 1
maxi = longueChaine(0,use)
print( maxi + p )
if(maxi+p>a):
    print("VICTOIRE")
else:
    print("DEFAITE")
