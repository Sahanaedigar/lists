def minmaxinArray(lst):
    return min(lst), max(lst)

n = int(input("Enter the number of elements: "))
lst = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    lst.append(num)

minimum, maximum = minmaxinArray(lst)
print("Minimum:", minimum)
print("Maximum:", maximum)
