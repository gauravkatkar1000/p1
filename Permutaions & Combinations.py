from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

l=[1,2,3,4]
p1 = permutations(l,2)
for i in p1:
         print(i,end="")
c1 = combinations(l,2)
print()
for i in c1:
         print(i,end="")
c2 = combinations_with_replacement(l,2)
print()
for i in c2:
         print(i,end="")
