#   ***********************  Sets   ***********************
"""
--Sets allow the storing of different Data Type values in order and Sets are changable in Runtime.
--Values are assigned to a variable in square brackets "{}"
  Ex :  name_set = {1, "python", 2.3, 2j}

"""


#   Create a Set
vm_set = {1, 2, 3, "Python", 1, 23}
print(vm_set)
print(type(vm_set))



#   Set values cannot be inserted once the set is created



#   Values can be added to a Set
vm_set.add("Moore")
print(vm_set)



#   Length of a Set
print(len(vm_set))



#   Remove values from Sets with remove(), discard(), pop()
#vm_set.remove("Moore")
print(vm_set)

vm_set.discard("Moore")
print(vm_set)

vm_set.pop()
print(vm_set)




#   Join two Sets
x={"Brackets", 2.3, 0, 3, "X"}
v={"Packets", 7.11, 11, 5, "V"}
w=v.union(x)
print(w)


#   Iterate Sets using Membership operator
for t in w:
    print(t)


#   Find a value present in a Set using Membership operator



#   Verify the presence of a value in a Set with MO



#   Clear data in Set using the clear() method




