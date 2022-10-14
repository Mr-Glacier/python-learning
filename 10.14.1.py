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

#   处理列表数据
fav_movies = ['the happy dog', 'love is all']
print(fav_movies[0])
print(fav_movies[1])

for each_flick in fav_movies:
    print(each_flick)

count = 0
while count < len(fav_movies):
    print(fav_movies[count])
    count = count + 1

# 在列表中存储列表
listB = [
    'the movies is great', 2022, 'i love it',
    [
        'ok', 'maybe you will love it',
        [
            'sure i will'
        ]
    ]
]
print(listB[3][2][0])
print(listB)
for each_item in listB:
    print(each_item)

#   列表中查找列表
names = ['kobe', 'jams']
# isinstance(name,class)判断某数据，是否某类型数据，返回bool
isinstance(names, list)
print(isinstance(names, list))
num_names = len(names)
isinstance(num_names, list)
print(isinstance(num_names, list))

print(1111)
for each_itema in listB:
    if isinstance(each_itema, list):
        for nexted_item in each_itema:
            if isinstance(nexted_item,list):
                for tired_item in nexted_item:
                    print(tired_item)
            else:print(nexted_item)
    else:
        print(each_itema)
# 循环嵌套恶心，在后续编程中尽量避免使用循环嵌套
