The optimal value is : 5
The optimal value is : 3
MAX, MIN
=
1000
,
-
1000
def
minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta, branching, maxDepth):
if
depth
==
maxDepth:
return
values[nodeIndex]
if
maximizingPlayer:
best
=
MIN
for
i
in
range
(
0
, branching):
val
=
minimax(depth
+
1
, nodeIndex
*
branching
+
i,
False
, values, alpha, beta, branching, maxDepth)
best
=
max
(best, val)
alpha
=
max
(alpha, best)
if
alpha
>=
beta:
break
return
best
else
:
best
=
MAX
for
i
in
range
(
0
, branching):
val
=
minimax(depth
+
1
, nodeIndex
*
branching
+
i,
True
, values, alpha, beta, branching, maxDepth)
best
=
min
(best, val)
beta
=
min
(beta, best)
if
beta
<=
alpha:
break
return
best
b
=
2
maxDepth
=
3
values
=
[
3
,
5
,
6
,
9
,
1
,
2
,
0
,
-
1
]
print
(
"The optimal value is :"
, minimax(
0
,
0
,
True
, values, MIN, MAX, b, maxDepth))
b
=
4
maxDepth
=
2
values
=
[
3
,
5
,
6
,
9
,
1
,
2
,
0
,
-
1
,
-
3
,
-
5
,
-
6
,
-
9
,
-
1
,
-
2
,
0
,
1
]
print
(
"The optimal value is :"
, minimax(
0
,
0
,
True
, values, MIN, MAX, b, maxDepth))
#Homework:
#1. Read branching factor, max Depth, etc. from a file
#2. Find out the number of leaf nodes / internal nodes which are pruned.
#3. To do ideal ordering of the leaf nodes to maximize the pruning.
#4. Try to find the utility using the Knight's 10-digit T9-Mobile-Number game as well as the maximum number of nodes pruned.
