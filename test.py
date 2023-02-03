def list_sort(list,d):
    j=0
    for i in range(0,len(d)):
        if list[i][0] == list[0][0] or list[i][0] > list[j][0]:
            j = i
            continue
        if list[i][0] < list[j][0]:
            list[i],list[j] = list[j],list[i]
            list_sort(list,d)
def make_list(list,d1,d2):
    for i in range(0,len(d1)):
        list.append([d1[i],d2[i]])

d1 = [45,43,54]
d2 = [2,6,8]
data = []
make_list(data,d1,d2)
print(data)
list_sort(data,d1)
print(data)