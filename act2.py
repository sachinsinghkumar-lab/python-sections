setx = {"green","blue"}
sety = {"blue","yellow"}

#union
setUnion = setx.union(sety)
print(setUnion)

#Intnersection
setIntersection = setx.intersection(sety)
print(setIntersection)

#difference
setDifference = setx.difference(sety)
print(setDifference)

#symmetric differnce
setSymetric = setx.symmetric_difference(sety)
print(setSymetric)