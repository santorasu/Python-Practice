lis = [3,5,6,4,6,9,7,11,22,"Santo",True]
print(lis)
print(type(lis))
print(lis[0])
print(lis[1])
print(lis[2])

print(lis[-3])
print(lis[len(lis)-3])
print(lis[5-3])
print(lis[2])

if 6 in lis:
    print("Yes")
else:
    print("No")

if "San" in "Santo":
    print("Yes")

print(lis)
print(lis[1:8])
print(lis[1:8:2])

lst = [i*i for i in range(11)]
print(lst)
lst = [i*i for i in range(11) if i%2==0]
print(lst)