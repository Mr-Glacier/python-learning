# 在python中创建一个函数
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)


listB = [
    'the movies is great', 2022, 'i love it',
    [
        'ok', 'maybe you will love it',
        [
            'sure i will'
        ]
    ]
]
print_lol(listB)