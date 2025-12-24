# 1. Remove duplicate elements from a list without using set
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_list = []

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("Without duplicates:", unique_list)


# 2. Create a new list containing only even numbers using list comprehension
nums = [1, 2, 3, 4, 5, 6]
even_numbers = [n for n in nums if n % 2 == 0]

print("Even numbers:", even_numbers)


# 3. Find the second largest element in a list
values = [10, 20, 30, 40]
largest = max(values)
values.remove(largest)
second_largest = max(values)

print("Second largest:", second_largest)


# 4. Create a nested list and calculate the sum of each inner list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
for inner in nested_list:
    print("Sum:", sum(inner))


# 5. Demonstrate shallow copy and deep copy
import copy

original = [[1, 2], [3, 4]]

shallow = original.copy()
deep = copy.deepcopy(original)

original[0][0] = 100

print("Original:", original)
print("Shallow copy:", shallow)
print("Deep copy:", deep)
