a = 'username=8613037253526,valid_type=1'

a = a.split(',')
print(len(a))
print(range(len(a)))
b = ""
for i in range(len(a)):
    b += '&' + a[i]
    print(a)
    if i == len(a)-1:
        continue
print(b)
