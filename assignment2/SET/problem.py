# 1. Find union, intersection, difference, and symmetric difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)


# 2. Remove common elements from two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1 = set1 - set2
set2 = set2 - {3, 4}

print("Set1 after removing common:", set1)
print("Set2 after removing common:", set2)


# 3. Check whether one set is a subset of another
a = {1, 2}
b = {1, 2, 3, 4}

print("Is subset:", a.issubset(b))


# 4. Print elements greater than a given number
s = {5, 10, 15, 20}
num = 10

for i in s:
    if i > num:
        print(i)


# 5. Convert list with duplicates into set and back to list
lst = [1, 2, 2, 3, 4, 4, 5]

unique_list = list(set(lst))
print("Unique list:", unique_list)
