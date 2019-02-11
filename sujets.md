## Le précieux

### Sujet
Vous avez mis la main sur l’Anneau Unique de Sauron, et vous avez pour mission de le jeter dans les flammes du Mordor ! Mais vous êtes un peu étourdi, et ne savez plus sur lequel de vos doigts vous l’avez mis... <br>
Retrouvez le doigt sur lequel est l’anneau ! <br>
### Entrées
5 lignes :
« X » pour un doigt sans anneau
« O » pour un doigt avec l’anneau <br>
### Sorties
S’il y a un anneau, i le numéro du doigt sur lequel il est posé (on compte à partir de 1 !)
Sinon « Tu n’es pas invisible ! » <br>
### Précisions
- les doigts sont numérotés de 1 à 5
- Attention a bien rendre exactement la phrase demandée quand il n'y a pas d'anneau !

### Exemples

#### 1
X
O
X
X
X

2

#### 2
X
X
X
X
X

Tu n'est pas invisible !


## La longue route

### Sujet
Selon les recommandations de Gandalf, Frodon se rend donc vers Rivendell. Gandalf fera aussi le trajet mais est convaincu de pouvoir arriver plus vite que lui. Chacun connaît ses raccourcis, mais ils doivent tous les deux s'arrêter aux mêmes étapes sur le chemin. Déterminez lequel de Gandalf ou Frodon arrivera en premier au point de rendez-vous !
### Entrées
- Sur une ligne 0<=N<=1000 le nombre d’étapes sur le chemin
- Sur les N lignes suivantes, deux entiers 0<= Fi <=100 et 0<= Gi <=100 qui correspondent au temps que chacun met pour aller à l’étape suivante<br>

Le temps total mis par un des voyageurs est donc la somme des temps mis pour atteindre chaque étape. 
### Sorties
«Frodon plus rapide» si Frodon arrive plus tôt<br>
«Gandalf plus rapide» si Gandalf arrive plus tôt<br>
«Pas de meilleur chemin» si les deux voyageurs mettent le même temps.<br>

### Exemples
#### 1
164
5 70
60 13
62 6
28 72
84 86
91 83
72 81
64 57
63 99
54 53
60 79
82 100
88 47
21 87
80 11
65 52
77 81
79 84
48 8
68 38
62 60
96 27
74 100
64 52
69 3
36 59
58 93
40 40
81 74
7 43
45 73
2 69
98 56
37 82
20 85
13 96
24 98
66 68
84 15
59 72
74 81
0 94
37 17
64 62
4 0
5 67
3 88
3 87
99 67
73 6
9 73
20 26
43 11
44 60
58 85
62 41
4 57
56 6
55 71
53 97
47 91
67 69
96 38
27 81
38 85
4 81
98 29
30 32
65 49
32 14
76 6
71 1
75 76
59 30
54 88
51 14
30 50
48 8
61 68
63 26
50 41
56 96
27 51
67 66
93 27
58 56
31 26
87 96
3 49
39 98
17 40
39 88
87 81
48 22
52 21
39 55
14 47
20 68
81 17
85 41
49 14
45 12
31 27
94 81
45 13
33 27
59 31
88 34
42 4
8 27
76 61
37 98
67 22
30 65
67 42
47 69
35 90
60 99
99 94
18 15
87 93
62 83
12 16
43 13
50 91
20 58
70 57
98 55
17 96
23 25
11 87
3 22
37 33
50 49
66 31
25 60
17 30
35 41
62 67
2 77
69 44
90 64
53 15
66 34
68 87
88 36
33 3
54 42
61 73
83 41
14 46
20 64
87 13
89 9
92 17
23 98
100 39
75 45
61 15
8 9
18 7
55 99
54 17
74 65

Gandalf plus rapide

#### 2

646
83 11
50 68
36 96
46 30
75 18
1 91
40 11
63 53
73 50
9 94
93 31
53 75
33 93
51 36
78 100
63 45
96 42
60 9
7 82
65 31
86 81
83 38
28 23
1 61
70 58
26 3
93 56
81 84
61 99
37 71
23 48
65 40
70 98
93 4
15 23
81 41
76 28
40 14
12 99
98 18
8 3
83 21
53 44
77 81
21 55
2 85
38 76
63 47
72 59
83 30
73 52
26 59
43 86
27 96
46 48
26 80
40 39
28 57
26 0
23 77
16 48
89 65
69 69
71 3
17 59
87 28
30 76
46 8
92 76
11 70
23 29
55 61
38 98
71 66
45 39
54 55
56 0
46 84
32 95
2 98
91 9
7 16
97 51
98 13
78 41
10 3
20 25
71 1
28 27
40 38
27 52
0 27
14 50
90 33
79 71
62 53
49 41
20 98
44 49
28 82
70 52
51 48
54 7
18 47
48 35
51 99
37 28
69 23
72 99
89 32
87 83
8 24
8 57
77 47
67 52
2 99
3 27
7 65
60 0
22 96
73 27
80 52
66 98
74 0
72 9
69 34
39 91
34 47
95 6
62 22
15 6
92 41
90 99
27 75
74 35
41 37
31 57
23 52
4 57
71 5
96 23
62 53
92 1
10 66
59 44
36 87
91 71
18 76
78 74
40 40
26 1
31 58
11 81
19 43
72 21
49 22
97 48
68 58
25 55
100 39
28 72
80 21
32 4
53 18
10 26
32 49
40 60
94 86
66 83
55 33
5 58
59 0
7 36
43 63
80 52
68 93
33 17
69 71
80 92
52 54
76 98
24 67
38 79
96 21
26 30
94 51
67 62
18 66
32 54
35 22
21 29
92 70
40 23
29 10
0 99
10 72
0 95
22 31
98 58
14 76
6 81
9 24
50 73
50 68
74 41
11 14
2 67
9 56
99 11
14 99
70 20
28 41
64 18
8 80
83 61
27 57
89 72
91 85
56 9
25 48
29 74
11 96
91 52
61 87
5 4
18 95
24 73
92 97
7 98
32 32
56 40
66 80
13 84
90 93
84 32
95 21
25 56
39 99
97 10
63 23
29 36
74 19
60 17
15 60
89 31
9 55
5 22
43 15
66 85
49 59
31 44
55 53
70 48
33 7
85 92
15 24
50 81
95 5
1 55
26 34
78 82
52 32
88 5
66 35
88 3
70 24
88 93
14 60
19 100
76 34
62 97
23 33
38 84
31 96
96 42
42 67
98 57
53 19
83 99
46 63
97 0
18 71
27 65
6 74
87 43
14 98
77 97
21 20
23 63
88 32
39 66
18 15
3 58
71 98
66 72
15 69
39 63
28 22
28 88
11 38
70 18
85 30
19 64
64 87
64 89
40 57
96 20
47 20
77 15
59 44
61 23
71 80
33 40
56 9
9 36
78 21
5 90
70 55
51 61
16 61
84 89
15 93
74 27
86 22
20 1
88 87
84 93
56 78
85 52
63 20
98 8
41 70
29 0
78 76
96 12
13 9
33 18
2 2
82 34
21 90
38 93
33 50
86 0
27 94
68 29
3 27
27 9
46 85
77 83
78 63
14 30
26 10
85 26
55 25
48 55
43 2
86 52
50 65
32 40
58 25
72 91
62 59
55 79
43 39
46 41
96 15
83 5
45 2
65 33
3 28
47 77
63 60
58 34
27 58
52 44
95 17
11 49
57 44
46 11
67 32
95 88
96 13
93 45
75 23
58 83
49 99
23 52
18 51
4 80
87 34
12 61
24 42
8 49
69 11
78 79
56 78
47 45
56 68
36 74
89 43
77 46
18 21
56 5
100 82
12 52
70 94
18 86
91 6
87 32
73 10
85 79
79 98
65 29
57 48
94 30
70 38
10 28
98 69
3 16
70 77
79 34
88 4
55 18
15 24
16 56
38 63
17 59
75 85
78 65
39 94
39 20
49 56
21 37
6 13
56 44
23 98
27 21
39 73
92 52
81 92
24 20
56 90
58 48
81 49
0 27
4 39
54 24
85 92
35 84
82 68
85 12
68 49
66 91
52 32
93 57
37 41
5 85
88 58
63 25
91 98
84 64
42 98
8 69
26 59
73 36
64 94
66 7
90 63
5 68
61 70
76 100
57 24
79 95
56 95
97 83
67 10
97 5
49 55
2 22
47 80
24 12
3 36
65 42
3 100
4 4
55 82
65 23
54 44
47 51
75 54
56 49
70 89
96 80
15 27
90 73
36 34
53 54
2 48
7 30
39 65
22 26
73 15
61 28
62 65
2 13
70 67
95 49
40 60
44 15
64 10
87 95
12 34
79 81
56 78
32 75
24 71
4 15
48 25
65 63
29 47
56 60
16 29
20 16
10 90
47 12
49 85
2 53
34 43
71 85
81 46
53 35
54 28
76 55
59 47
86 40
87 95
82 8
19 73
1 54
52 34
34 13
26 89
10 48
59 78
41 22
78 51
53 40
54 2
73 61
45 76
72 97
34 62
38 28
69 81
51 47
32 11
77 93
77 13
20 34
35 41
37 94
41 7
46 79
11 93
17 78
98 21
6 72
80 48
12 0
77 86
52 37
7 10
94 70
86 86
23 11
58 11
29 50
76 54
67 56
50 37
87 32
49 96
91 90
66 82
15 6
62 25
97 51
53 49
4 90
1 67
46 45
63 46
63 47
39 79
100 85
22 36
23 79
65 59
88 85
19 47
67 70
21 58
67 45
70 27
69 75
17 54
28 1
29 76
60 32
25 53
74 89
45 89
41 77
36 55
9 30
74 84
65 21
27 94
75 38
75 74
11 2
96 98
90 96
21 23
40 97
14 39
12 75
0 25
19 26
31 55
21 8
76 76
41 98
42 26
55 14
12 71
36 40
78 80
84 3
28 87
16 65
22 41
40 30
74 6
94 25
49 69

Gandalf plus rapide

## L'armée mixte

### Sujet
De son côté, Saroumane, à la solde de Sauron, inspecte son armée, et veut donner l’impression qu’elle est le plus mixte possible. Pour ça il faut que chaque Uruk soit entre deux autres strictement plus petits que lui ou deux autres strictement plus grands que lui. <br>
Les soldats ont reçu l’ordre, il faut maintenant inspecter les troupes. Si elles ne sont pas bien rangées on peut décider de tuer un unique soldat pour que l’armée devienne rangée. <br>
Est-ce possible d’avoir le rangement voulu en tuant au plus un soldat ? <br>

### Entrées
- 1ère ligne : N, le nombre de soldats, 0<N<10³
- Ligne suivante : N entiers Ti, Ti la taille du soldat à la position i, Ti<10⁵
### Sorties
“MIXTE” si on peut avoir l’ordre voulu en tuant au maximum un soldat <br>
“CARNAGE” sinon.<br>

### Precisions
- Les soldats ne sont pas nécessairement tous de taille différentes
- Une armée composée d’un seul soldat est considérée comme mixte

### Exemples
#### 1
8
6 35 12 35 5 25 18 15

MIXTE

#### 2
6
35 1 25 16 22 20

MIXTE

#### 3
848
55616 25055 99806 39325 52792 73663 98906 9069 36197 70700 9369 80924 12872 88139 66499 19694 68681 48057 34853 74331 19829 28619 2945 1659 47591 41798 17280 41422 55297 43511 67074 69509 32153 60049 21717 74352 80753 88161 64516 37701 93406 43311 79975 80234 12842 4467 9720 21151 95669 6386 230 29515 1334 5204 15330 81441 28128 44002 78071 76398 62720 98753 51798 95266 13826 88742 50031 91033 44115 12053 40541 33061 9025 61370 68536 59770 41662 35299 34830 45973 87684 23480 41771 35562 61202 28344 12244 50248 32788 49809 2964 10987 28130 68668 25582 35007 19615 85330 39537 46411 28065 81775 4329 77217 5936 20642 65746 4769 65703 65614 16360 64133 5464 37952 24378 67660 43340 73996 22172 7942 22856 20039 43132 77017 17067 51931 45900 37166 69588 64107 83454 74459 32736 69123 52846 2638 23344 91322 86809 38194 42250 34599 71307 71169 55734 53309 96630 2663 58473 2309 85374 18510 49118 36662 70098 555 68832 46900 23189 22821 21156 52450 39578 59389 30515 6309 8910 50238 96614 97430 60463 5539 53130 7427 52731 31615 27107 62724 26083 17709 77324 24213 90878 5044 25500 93684 11770 75191 25540 24633 11981 94615 58325 62893 81257 4165 32447 7848 30062 76679 62037 12811 45594 97510 46412 8567 61308 3666 90145 98504 64902 76979 71098 39537 5248 52301 420 37173 48600 80590 89212 14239 94680 85272 83306 11743 76656 76294 89192 80162 68786 62172 46592 71532 27933 58095 15411 87381 82065 83150 95862 60669 32929 91788 73782 1037 90919 75019 412 30860 48177 90055 56268 9658 92249 61724 64903 55021 94738 46932 13649 35557 4542 49297 82637 47726 44349 34291 36708 43378 73663 97927 25796 21176 92731 70701 87973 64413 45240 59236 36871 85357 12776 56052 47351 74302 63765 15991 83600 16234 19411 39973 41918 41095 92565 33274 93118 66180 36284 92966 61826 52930 30026 21586 87697 89004 60309 26634 30762 51669 51095 54891 66824 33069 61570 52041 43489 99839 85712 15453 4489 69834 8632 80107 97684 37242 33533 65004 48889 62242 32672 63036 16978 4697 45462 86625 46431 99950 27925 39382 74090 49513 29991 8724 20613 99423 93089 92284 37711 60945 52846 54339 12310 14626 30852 43322 27639 76947 96472 23801 80193 96381 43757 28424 25655 85578 37671 2474 86036 22001 574 9734 72328 84620 39438 28339 14401 34263 51531 24287 76645 27976 42450 31900 7035 965 24411 26504 7626 48966 7819 70199 64025 94152 33445 28095 70102 9963 86816 69216 86866 63401 13748 18062 4457 37716 89134 73980 78655 25098 87779 64647 48390 39127 14625 97212 94269 744 21697 37703 3474 74439 32089 13721 10951 26360 22702 57812 59282 32207 85318 83575 70367 98187 34043 25441 50641 48979 52396 77699 91589 35916 91566 60359 29559 46868 79743 22551 5374 80222 12603 87275 37138 67594 14919 84627 78734 34752 84043 97213 37616 2409 38301 20483 22462 96299 35384 79252 1635 96863 61804 59421 75734 13392 83759 75284 93051 43985 49104 27041 77827 31995 38156 97802 69167 22531 1370 33209 89202 59541 19905 87659 31028 56367 87337 92440 39282 34683 29166 75771 86243 938 69265 37693 15830 47594 81674 83842 25943 60132 36408 92399 96112 58868 72504 84053 75788 64134 20372 31167 49911 48937 64818 82581 19297 14227 86733 19051 96801 82161 2722 29129 78774 81801 4769 49911 92681 54798 75459 93636 9998 23519 77018 98131 47561 86045 22500 2691 24078 4934 57017 69722 99169 86867 4164 52365 27483 29674 88655 1390 26446 30689 93462 66451 11968 94064 32254 5599 69139 29265 22782 71535 8517 9463 79803 83427 34963 23336 77266 35526 37976 69881 74639 12636 88564 66212 67674 27144 10951 33352 95249 65047 85693 84030 73232 72748 740 16403 40653 29033 8408 82535 76608 567 35935 35840 82303 8370 6000 72043 28201 93459 33455 27057 93912 23963 54259 69554 70329 26841 75817 73985 35960 2329 47217 76476 82804 18602 55046 2118 11921 36809 48252 55458 78445 23919 97281 98222 18346 76436 72165 90 89898 55870 93590 98884 36217 34346 11332 57073 99076 47349 94884 6569 11847 17736 50320 63440 94820 1118 19915 79197 26128 53812 85507 13977 17383 68812 63215 82741 76416 58205 77207 94536 87739 79738 61842 66692 74966 55005 67690 29236 10463 64784 55229 60020 66980 23544 21853 13165 10534 49439 55543 67499 59884 13180 3921 52221 7444 73825 82220 36873 17636 74465 24232 31401 17470 91388 24295 23078 34834 90024 46569 33135 23150 97758 54103 50006 92241 20414 59420 33831 34045 81887 95501 59910 21834 31159 77706 46660 77879 81636 55420 99710 84507 47829 64926 90162 18618 69975 62936 11966 13427 65504 94022 56183 92406 55026 10135 25955 5267 80940 16785 50835 63981 72947 57586 35073 65134 96760 16530 84866 83668 98727 90692 24743 87497 62795 67547 3798 36240 42529 12361 38464 70971 24311 11331 32639 57466 88320 37312 59470 81038 30808 67904 72293 95387 22831 3849 21519 53339 85363 89997 25193 94384 6046 46440 80378 98737 96217 96101 84330 16646 72620 54815 66432 56911 86755 7013 88443 91006 83390 52503 17869 91301 2069 24109 53775 73642 22406 18679 5957 1399 23613 8031 2160 54189 20286 72907 4585 88985 3378 17342 256 20383 9644 53246 82066 20883 95095 41040 78752 5126 5278 13055 62770 94653 2263

CARNAGE

## Traversée du fleuve
### Sujet
L’armée de Saroumane est formée et en ordre, mais a encore beaucoup de chemin à faire. Devant elle coule un fleuve, qu’elle va devoir traverser. Problème : il n’y a à disposition que des barques à deux places, et certains des Uruk-hai vont s’entretuer s’ils sont sur la même barque. 
En effet certains ont un ou plusieurs ennemis jurés, vous devez donc les séparer. <br>
Tant qu’à arranger les soldats vous proposez aussi à ceux qui le veulent de prendre la barque avec leurs frères de sang. Une barque avec deux frères de sang ( relation ami ) rapporte 2 points, une barque sans relation ami n’en rapporte qu’un, et il est interdit de faire embarquer deux ennemis jurés ensemble. <br>
Combien de points au maximum pouvez-vous avoir en arrangeant au mieux les soldats? <br>

### Entrées
- 1ère ligne : N, A, E le nombre de soldats, le nombre de relations amis, et le nombre de relations ennemis 

- A lignes suivantes : Ai1, Ai2 les numéros de deux soldats en relation amis <br>
- E lignes suivantes : Ei1, Ei2 les numéros de deux soldats en relation ennemi

Limites : <br>
2<=N<=6 , 0<=A<=N² , 0<=E<=N²e

### Sorties
Le nombre maximal de points possible, s’il existe une configuration qui évite de mettre deux ennemis ensemble
-1 s’il n’existe aucune configuration possible

### Précisions 
- Une approche par force brute sera acceptée pour cet exercice
- N est pair, les soldats sont numérotés de 1 à n
- Il ne peut pas y avoir de relation amitié ET ennemi entre deux soldats

### Exemples
#### 1
4 2 3
1 2
3 2
4 2
3 1
1 4

3

#### 2
4 1 2
2 1
3 1
3 4

2


## Seul contre tous
### Sujet
Un groupe d’ennemis vous attaque, vous ne survivrez pas sans une bonne stratégie !
Vous ne pourrez pas vous jeter à corps perdus dans chaque combat et devez donc ménager vos forces en acceptant de prendre quelques coups. <br>
Vous savez que les N ennemis ne sont pas tous identiques : certains se défendent moins bien et sont faciles à éliminer, d’autres sont presque inoffensifs. Vous arrivez à les jauger et à évaluer deux caractéristiques : leur attaque et leur défense <br>
Pour chaque combat vous pouvez utiliser un nombre entier d’énergie compris entre 0 et le niveau de défense de votre opposant (compris) . Moins vous investirez d’énergie et plus vous serez blessé : les dégâts que vous subissez sont calculés par <br>
<center>```Dégâts = (défense – énergie utilisée) * attaque```</center><br>
Ces dégâts sont directement soustraits à vos points de vie, vous mourrez s’ils atteignent 0 et ce même si c’est après avoir vaincu le dernier ennemi.<br>
Pouvez-vous défaire tous vos ennemis, et si oui combien de points de vie au maximum pouvez-vous conserver ?<br>
### Entrées
1ere ligne : N, V,  et E 3 entiers positifs, le nombre d’ennemis, vos points de vie, et votre énergie <br>
N lignes suivantes : Di et Ai 2 entiers positifs, la défense et l’attaque de l’ennemi affronté. <br>
Limites : <br>
- 0<=N<=1000
- 0<=V<=1000
- 0<=E<=200
- 0<=Di<=100
- 0<=Ai<=100
### Sorties
Si la survie est possible : <br>
1 entier, le nombre maximum de points de vie possibles à la fin de tous les combats
Sinon : <br>
« GAME OVER »

### Exemples
#### 1
8 25 12
3 3
2 2
1 3
2 3
2 3
2 2
2 1
3 2

17

#### 2

6 12 11
3 2
2 1
1 2
3 2
1 1
2 1

11

#### 3

6 12 8
2 2
2 2
2 2
2 2
1 2
1 1

9

## L'affrontement final

### Sujet
Pour vous, c’est l’heure de la bataille finale. Le Mordor est à portée de vue, mais vous n’êtes pas assez puissant pour l’affronter maintenant, vous devez rassembler vos alliés. Ceux-ci sont éparpillés sur une carte carrée de taille N.  <br>
Chacun des alliés possède une certaine puissance Pi , qui viendra immédiatement s’ajouter à la vôtre si vous passez par sa position (un même allié ne peut évidemment être rallié qu’une fois). <br>
Vous vaincrez Sauron uniquement si vous avez une puissance supérieure à la sienne en arrivant à sa position, vous allez donc tenter de maximiser la vôtre.
Pour compliquer les choses, vous perdez 1 de puissance quand vous vous déplacez d’une case.
De plus, le terrain n’est pas totalement ouvert : il y a des montagnes sur certaines cases, vous ne pouvez pas les franchir.


Arriverez vous à défaire Sauron, puis jeter l’Anneau dans les Flammes du Mordor ?


### Entrées
1ère ligne : N, P, A, la taille de la carte, la puissance au départ et le nombre d’alliés <br>
2e ligne : L et C les coordonnées de départ <br>
3e ligne : Ls et Cs les coordonnées de Sauron <br>
A lignes suivantes : Li, Ci, Pi les coordonnées de l’allié i et sa puissance <br>
N lignes suivantes : N entiers séparés par des espaces ( la carte ), 0 si c’est un terrain plat, 1 si c’est une montagne <br>
Limites : 
<ul>
<li> 2<=N<=50
<li> 0<=P<=10 000 
<li> 0<=A<=15  
</ul>

### Sorties
Sur une ligne : 1 entier, la puissance maximale possible au moment où on est arrivé sur l’emplacement de Sauron <br>
Sur une seconde ligne “VICTOIRE” si notre puissance est strictement supérieure à la sienne, “DEFAITE” sinon

### Précisions
Vous ne pouvez pas passer par la position de Sauron sans démarrer l’affrontement<br>

On peut toujours se rendre à la position de Sauron depuis le départ<br>

Toutes les coordonnées sont numérotées à partir de 1 et correspondent au numéro de la ligne et au numéro de la colonne de la position. <br>

Votre puissance peut temporairement passer par une valeur négative sans causer la défaite.<br>
Les cases suivantes sont toujours franchissables et distinctes:<br> 
<ul>
<li> Votre case de départ 
<li> Les cases de vos alliés 
<li> La case de Sauron
</ul>

<center> ![Illustration et solution pour l’exemple 1 ](https://i.imgur.com/j1ltZed.png) </center>

### Exemples

#### 1
12 7 0
10 8
3 3
1 0 0 1 0 0 0 0 0 0 0 0
1 0 0 0 1 0 0 0 0 0 0 0
1 0 0 0 0 0 0 1 1 0 1 1
0 1 0 0 0 0 1 0 1 0 0 0
1 0 0 1 0 1 0 0 1 0 1 0
0 1 0 0 1 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 1 0 0 0
0 0 0 1 0 1 0 0 0 0 0 1
0 1 0 0 1 0 0 0 0 1 0 0
0 0 0 0 0 0 0 1 0 0 0 0
1 0 1 0 0 0 0 1 0 0 0 0

-7
DEFAITE

#### 2

18 30 12
1 6
11 7
8 5 8
14 14 12
10 2 4
13 4 2
17 12 9
5 4 15
16 17 11
9 7 3
10 5 7
10 15 3
16 7 0
4 7 11
1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 0 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 1 0
0 0 0 1 0 0 0 0 0 1 0 0 1 0 0 0 1 1
0 0 0 0 1 0 0 0 0 0 1 1 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 0 1 1 0 1 0 0 0 1
1 1 1 1 0 0 0 0 0 1 1 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 1
0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 1
0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 0 0
0 0 0 1 0 0 0 1 0 1 0 0 0 0 0 1 0 0
0 0 0 0 0 1 1 0 0 1 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0 0 1 1 0 1 0 0 0
0 0 1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0
0 1 1 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 1 1 0 0 0 1 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0

53
VICTOIRE

#### 3

20 3 11
16 2
12 5
7 12 12
6 8 23
4 1 24
3 20 26
20 16 6
18 16 1
19 16 9
2 10 27
1 5 7
6 4 27
10 14 24
0 0 0 0 0 1 1 0 0 0 1 0 0 1 0 1 1 0 0 0
0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 1
1 0 0 0 1 0 1 0 0 1 0 0 1 0 1 1 0 0 1 0
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 1 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 1 0 0 0
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 1 1 1 0 0 0 1 1 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 0 0 1 0 0 0 1 0 0 0 0 0 1 0 1 0 0 0
0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 1 1 0 1 0
1 0 0 0 0 0 0 0 1 1 0 0 0 0 1 1 0 0 0 0
0 0 1 0 1 1 0 1 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0
1 1 0 0 0 0 1 1 0 1 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0
1 1 0 0 0 0 1 0 1 1 0 0 0 0 0 0 0 0 1 0
0 1 0 1 1 0 0 1 1 0 0 0 0 0 0 0 0 0 1 0
1 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0
0 0 0 1 0 1 0 0 1 1 0 1 0 0 0 0 0 0 1 0

90
VICTOIRE