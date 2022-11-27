from functools import reduce
#even_list = [lambda arg=x: arg*2 for x in range(0,5)]

#for item in even_list:
   # print(item())

#Max = lambda a,b:a if (a>b) else b
#print(Max(0,2))
'''
List = [[1, 4, 16, 64],[2,3,4],[3, 6, 9, 12]]
 
# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)
print(list(sortList(List)))
# Get the second largest element
secondLargest = lambda x : [y[len(y)-2] for y in x]
res = secondLargest(List)
 
print(res)
'''
mutiply = [5,2,4,5,1]
#x = lambda x,y: True if x<y else False
print(any(mutiply[i]>mutiply[i+1]for i in range(len(mutiply)-1) ))
