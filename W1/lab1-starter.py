list1 = []
list2 = [1, 2, 3, 'Rapee']
list3 = [1,2,3,4,5,6]
list4 = ['a','e','i', 'o','u']
list5 = [list3,list4]
list6 = [[]]
# print(list2)


for cnt in range(10):
    print(cnt)
print()
for cnt in range(10, 1, -1):
    print(cnt)
for member in list4:
    print(member)
print()
txt = 'Programming'
i=1
# รับค่า value อย่างเดียว
for t in txt:
    if i%2 == 0:
        print(t)
    i+=1

# รับได้ index, value
for index, member in enumerate(['a','e','i','o','u']):
    print(index, member)