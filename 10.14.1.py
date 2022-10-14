# 列表就像是数组
# 简单的python列表
movies = ['first', 'second', 'tired']
# 其中first就是第0项。
print(movies)
print(movies[1])
print(movies[0])
print(len(movies))  # 数据项个数

# 数据项增加与删除
listA = ['1', '2', '3']
print(listA)
listA.append('hello')  # 点记法调用方法
# append()方法：在列表末尾添加一个数据项
print(listA)
listA.pop()  # pop()方法删除末尾元素，listA.pop(2)
print(listA)
listA.pop(2)  # 删除列表第3个数据项
print(listA)

# 列表末尾增加一个数据项集合--extend()方法
listA.extend(['hhhh', "1254"])
print(listA)
#   列表中找到并删除一个特定的数据项--remove()方法
listA.remove('hhhh')
print(listA)
# 在某个特定位置前增加一个数据项--insert（）方法
listA.insert(0, 'number')
print(listA)




