list1 = [(1, 1), (1, 1), (1, 2)]
print(list1)
if (1, 1) in list1:
    print("in")

list2 = list(set(list1))
print(list2)
