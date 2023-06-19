lis1=[]
print("Enter 5 numbers in the list:")
for i in range(0,5):
    e=int(input())
    lis1.append(e)
print("The sume of all elements in the list is:",sum(lis1))
print("The smallest number in the list is:",min(lis1))
print("The largest number in the list is:",max(lis1))
lis1.sort()
print("List in ascending order:",lis1)
lis1.reverse()
print("List in descending order:",lis1)
tup1=tuple(lis1)
print("List converted to tuple:",tup1)
del lis1 #list deleted