N, P, A, X = map(int, input().split())
#N taille de la carte
#P Puissance de depart
#A nb allie
#X puissance de sauron

L, C = map(int, input().split())
#case de depart
Ls, Cs = map(int, input().split())
#case de sauron

carte = []
allies = [(L, C, 0), (Ls, Cs, 0)]
obstacles = []

#Je met les allies sur la map
for i in range(A):
    Li, Ci, Pi = map(int, input().split())
    allies.append((Li, Ci, Pi))

#Je met les obstacles sur la map
for x in range(N):
    row = list(map(int, input().split()))
    for y in range(N):
        if row[y] == 1:
            obstacles.append((x + 1, y + 1))
    carte.append(row)

#Distance simple dans une grille
def get_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


#A star nul
def get_fpd(debut, end, Obstacles, N):

    if debut == end:
        return None, []
    openList = [debut]
    nodes = {debut: ['', 0]}
    closedList = []
    x1, y1 = debut
    while openList:
        current_node = openList[0]
        for tmp in openList[1:]:
            if nodes[tmp][1] + get_distance(tmp, end) < nodes[current_node][1] + get_distance(current_node, end):
                current_node = tmp
        x, y = current_node
        if current_node == end:
            break

        openList.remove(current_node)
        closedList.append(current_node)

        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            X = current_node[0] + i
            Y = current_node[1] + j
            new_node = (X, Y)
            if new_node in Obstacles or new_node in closedList or X < 1 or X > N or Y < 1 or Y > N:
                continue
            elif not new_node in openList:
                openList.append(new_node)
                nodes[new_node] = [current_node, nodes[current_node][1] + 1]
            elif not new_node in nodes or nodes[new_node][1] > nodes[current_node][1] + 1:
                nodes[new_node] = [current_node, nodes[current_node][1] + 1]

    if current_node != end:
        return None, closedList

    parent = nodes[end][0]
    path = [end]
    while parent != debut:
        path = [parent] + path
        parent = nodes[parent][0]
    return path, closedList


Route = dict()

for i in range(A + 2):
    for j in range(i + 1, A + 2):
        L1, C1, P1 = allies[i]
        L2, C2, P2 = allies[j]

        path, closed_list = get_fpd((L1, C1), (L2, C2), obstacles, N)

        if (L1, C1) != (Ls, Cs):
            Route[((L1, C1), (L2, C2))] = P2 - len(path)
        if (L1, C1) != (L, C):
            Route[((L2, C2), (L1, C1))] = P1 - len(path)

depart = (L, C)
end = (Ls, Cs)
Allies = [(Ls, Cs)]

for a in allies[1:]:
    Li, Ci, Pi = a
    Allies.append((Li, Ci))

#Recurrence de merde
def recursDeMerde(checkpoints, position, score, paths):
    if (not checkpoints) or position == end:
        return score
    tab = []

    for checkpoint in checkpoints:
        tmp_score = score
        tmp_score += paths[(position, checkpoint)]
        tmp_value = paths[(position, checkpoint)]
        del paths[(position, checkpoint)]
        tmp_checkpoints = checkpoints.copy()
        tmp_checkpoints.remove(checkpoint)

        tab.append(recursDeMerde(tmp_checkpoints, checkpoint, tmp_score, paths))

        paths[(position, checkpoint)] = tmp_value

    return max(tab)


result = recursDeMerde(Allies, depart, P, Route)
print(result)
if result > X:
    print("VICTOIRE")
else:
    print("DEFAITE")