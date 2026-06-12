setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
emptySet = set()  # Creating an empty set
print("Set A:", setA)
print("Set B:", setB)
print("Empty Set:", emptySet)
#operations on set
print("Union of setA and setB:", setA | setB)  # {1, 2, 3, 4, 5, 6, 7, 8}
print("Intersection of setA and setB:", setA & setB)  # {4, 5}
print("Difference of setA and setB:", setA - setB)  # {1, 2, 3}
print("Symmetric Difference of setA and setB:", setA ^ setB)  # {1, 2, 3, 6, 7, 8}  

#methods on sets
setA.add(6)
print("After adding 6 to setA:", setA)
setA.remove(2)
print("After removing 2 from setA:", setA)
setA.discard(10)  # No error if 10 is not in setA
print("After discarding 10 from setA:", setA)   
setA.pop()  # Removes and returns an arbitrary element
print("After popping an element from setA:", setA)
setA.clear()
print("After clearing setA:", setA)
setA.update({7, 8, 9})
print("After updating setA with {7, 8, 9}:", setA)
print("Is setA a subset of setB?", setA.issubset(setB))
print("Is setA a superset of setB?", setA.issuperset(setB))
disjoint_set = setA.isdisjoint(setB)
print("Is setA disjoint with setB?", disjoint_set)