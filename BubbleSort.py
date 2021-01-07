def BubbleSort(list1):
	n=len(list1)
	for i in range(n-1):
		for j in range(0,n-i-1):
			if list1[j]>list1[j+1]:
				list1[j],list1[j+1]=list1[j+1],list1[j]
	return list1

list2=[]
n=int(input("enter the number of elements in list: "))
for i in range(0,n):
	ele=int(input())
	list2.append(ele)
	

print(list2)
k=BubbleSort(list2)
print(k)