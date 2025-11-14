#find the second largest number in a list
a = [13,56,78,5,89,7,8]
b = max(a)
a.remove(b)
c = max(a)
print(c)
