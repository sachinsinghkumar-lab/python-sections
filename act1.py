my_set = {1,2,3}
print(my_set)

my_set2 = {1.0,"hello",(1,2,3)}
print(my_set2)

my_set3 = {1,2,3,3,4,4,5,6,7,7}
print(my_set3)

#set from list
my_set4 = set([1,2,3,4,5,6,6])
print(my_set4)

#remove from set
num_set = set([1,2,3,4,5,6])
print(f"Original set:{num_set}")

num_set.remove(1)
print(f"set after removing 1 is:{num_set}")
num_set.pop()
print(f"set after removing 6 is:{num_set}")