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
#     for j in a.keys():
#         if j in b.keys():
#                 a[j] = b[j]
#     print(a)
# else:
#     print('b的数据类型为' + str(type(b)))


# import re
# a = 'b=1,c=2'


# def str_change_dic(data):
#     data = data.split(',')
#     c = {}
#     for i in data:
#         m = re.findall(r"(.+?)=", i)
#         n = re.findall(r"=(.+?)", i)
#         f = dict(zip(m, n))
#         c.update(f)
#     return c

# a = {'a': 1, 'b': 2}


# def dic_change_str(data):
#     d = ''
#     n = 1
#     for i in a:
#         if n < len(a):
#             d += str(i) + '=' + str(a[i]) + ','
#             n = n + 1
#         else:
#             d += str(i) + '=' + str(a[i])
#     return d
# a = 'abcdefg'
# if 'a' in a:
#     print("OK")
