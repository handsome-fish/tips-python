# 字典的合并
# 在python3中，提供了新的合并字典的方式，如方法1所示
# 此外python3还保留了python2的合并字典的方式，如方法2所示


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# 方法1
combined_dict = {**dict2, **dict1}
print(combined_dict)

print("==========================================")

# 方法2
dict1.update(dict2)
print(dict1)
