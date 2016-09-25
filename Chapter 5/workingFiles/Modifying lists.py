list = [1,2,3,4,5,6,7,8,9,10,11]

list.append(12)

list2 = [12,13,14]
list.extend(list2)

list.insert(5,12)

list[5] = 12
list[5] = list[5]*2
del list[5:7]
list.remove(9)
list.reverse()
list.append(0)
list.reverse()

print(list)