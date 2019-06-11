# coding=utf8

# def change_check_data(data):
#     n = []
#     for i in range(0, len(data)):
#         print(i)
#         b = data[i].split('~')
#         print(b)
#         n.append(b)
#         print(n)
#     return n


# a = 'driver~order~work,status~distance,destination~latitude'
# a = a.split(',')
# if len(a) > 1:
#     a = change_check_data(a)
#     print(a)

# a1 = a[0].split('~')
# a2 = a[1].split('~')
# a3 = a[2].split('~')
# print(a, a1, a2, a3)
# for i in a1:
#     print(i)


# a = {'test1': '', 'test2': ''}
# b = {'test1': '这是一个测试1', 'test2': '这是一个测试2'}
# print(b.keys())
# if isinstance(b, dict):
#     for i in a.keys():
#         print(i+'这是i的')
#         for j in b.keys():
#             print(j+'这是j的')
#             if i == j:
#                 a[i] = b[j]
#     print(a)
# else:
#     print('b的数据类型为' + str(type(b)))

