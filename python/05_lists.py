# 1. Adding Elements
# append(item): Adds a single element to the end of the list. 
# extend(iterable): Adds all elements from an iterable (like another list) to the end of the list. 
# insert(index, item): Inserts an element at a specific index position. 
# 2. Removing Elements
# remove(item): Removes the first occurrence of a specified value (raises ValueError if not found). 
# pop(index): Removes and returns the element at a given index (defaults to the last item if no index is provided). 
# clear(): Removes all elements from the list, leaving it empty. 
# 3. Searching and Counting
# index(item): Returns the index of the first occurrence of a value (raises ValueError if not found). 
# count(item): Returns the number of times a value appears in the list. 
# 4. Sorting and Reversing
# sort(): Sorts the list in ascending order by default (can use reverse=True for descending). 
# reverse(): Reverses the order of elements in the list in place. 
# 5. Copying
# copy(): Returns a shallow copy of the list. 


# 6. Other Useful Methods
# len(list): Returns the number of elements in the list.
# max(list): Returns the largest element in the list.
# min(list): Returns the smallest element in the list.
# sum(list): Returns the sum of all elements in the list (works for numeric lists).
# sorted(list): Returns a new sorted list from the elements of the original list (does not modify the original list).
# list(iterable): Creates a new list from an iterable (like a string, tuple, or another list).
# Example usage of list methods
my_list = [3, 1, 4, 1, 5]
print("Original list:", my_list)
my_list.append(9)
print("After append:", my_list)
my_list.extend([2, 6])
print("After extend:", my_list)
my_list.insert(0, 0)
print("After insert:", my_list)
my_list.remove(1)
print("After remove:", my_list)
popped_item = my_list.pop()
print("After pop:", my_list, "Popped item:", popped_item)
my_list.clear()
print("After clear:", my_list)