arr=[]
size=int(input("size "))
for i in range(size):
    ele=int(input("arr "))
    arr.append(ele)
k=int(input("k "))

even=[]
odd=[]
for i in arr:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
even.sort(reverse=True)
odd.sort(reverse=True)

lene=len(even)
leno=len(odd)


