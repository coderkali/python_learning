marks = [54,23,45,56,78,98,67,89,90,34]

print(marks)

marks.append(100)

print(marks)

marks.insert(2, 200)

print(marks)

extraMarks = [300,400,500]

marks.extend(extraMarks)

print(marks)

marks.remove(45)

print(marks)

marks.pop(1)

print(marks)

marks.pop(2)

print(marks)


print(marks.count(100)) # counts the number of times 100 appears in the list
print(marks.index(78)) # returns the index of the first occurrence of 78 in the list
marks.sort()
print(marks) # returns the sorted list
marks.reverse()
print(marks) # returns the reversed list
marks.clear()
print(marks) # returns an empty list
print(len(marks)) # returns the number of items in the list
print(max(marks)) # returns the maximum value in the list
print(min(marks)) # returns the minimum value in the list
print(sum(marks)) # returns the sum of all items in the list