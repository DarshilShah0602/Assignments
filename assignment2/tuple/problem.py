# 1. Find maximum and minimum elements in a tuple
t = (10, 5, 20, 8)

print("Maximum:", max(t))
print("Minimum:", min(t))


# 2. Convert a list of tuples into a dictionary
list_of_tuples = [("a", 1), ("b", 2), ("c", 3)]
dictionary = dict(list_of_tuples)

print("Dictionary:", dictionary)


# 3. Count occurrence of an element in a tuple without using built-in methods
tup = (1, 2, 3, 2, 4, 2)
element = 2
count = 0

for item in tup:
    if item == element:
        count += 1

print("Count of", element, ":", count)


# 4. Create a tuple with mutable elements and modify the mutable data
tup = ([1, 2, 3], [4, 5])

tup[0][0] = 100   # modifying list inside tuple

print("Modified tuple:", tup)


# 5. Swap two tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)

t1, t2 = t2, t1

print("After swapping:")
print("t1:", t1)
print("t2:", t2)
