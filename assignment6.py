#defining funtion ds with arguments as roll_no and name
def ds(roll_no,name):
    lis1=[roll_no,name] #creating list with values roll_no,name
    tu1=(roll_no,name) #creating tuple with values roll_no,name
    set1={roll_no,name} #creating set with values roll_no,name
    dic1={"rollno":roll_no,"name":name} #creating dictionary with keys rollno, name and values roll_no, name respectively
    print("List before changing values:",lis1) 
    print("Tuple before changing values:",tu1)
    print("Set before changing values:",set1)
    print("Dicitionary before changing values:",dic1)
    lis1=[1,"kartik"] #changing values of list
    print("List after changing values:",lis1)
    tu1=(2,"aditya") #changing values of tuple
    print("Tuple after changing values:",tu1)
    set1={3,"chinmay"} #changing values of set
    print("Set after changing values:",set1)
    dic1.update({"rollno":4,"name":"mohit"}) #changing values of dictionary
    print("Dictionary after changing values:",dic1)
    #deleting all data structures
    del lis1
    del tu1
    del set1
    del dic1
ds(0,"karan") #passing values to the arguments of function ds
