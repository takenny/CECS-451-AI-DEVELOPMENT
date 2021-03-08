list = ['one', 'two', 'three', 'four']
list.remove('two')
print(list)

list2 = [item for item in list]
list3 = any(item in list for item in list2)
print("list3:", list3)
print(list2)
