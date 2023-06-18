#loop manipulation and for with else (prints even and odd numbers till 16)
for i in range(1,20):
    if i==15:
        continue
    elif i==16:
        pass
    elif i==17:
        break
    if i%2==0:
        print("even",i)
    else:
        print("odd",i)
else:
    print("break used at 17") #this will not be printed as loop breaks at 17
print("*************************************") #to divide the for loop part and while loop part
#while with else (prints 10 to 1 descending numbers)
k=10
while k!=0:
    print(k)
    k-=1
else: 
    print("break statement not used")
