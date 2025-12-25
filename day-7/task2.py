#Exercises: Level 2
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Join A and B
A.union(B)
print(A.union(B))
#Find A intersection B
print(A.intersection(B))
#Is A subset of B
print(A.issubset(B))
#Are A and B disjoint sets
print(A.isdisjoint(B))
#Join A with B and B with A
AB = A.union(B)
BA = B.union(A)
print(AB,'\n', BA)
#What is the symmetric difference between A and B
#Delete the sets completely