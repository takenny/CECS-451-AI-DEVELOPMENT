list = ['one', 'two', 'three', 'four']
list.remove('two')
print(list)

list2 = [item for item in list]
list.clear()

print(list2)
