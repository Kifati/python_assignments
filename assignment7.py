def flfunc(fl1="karankif.txt"):
    try:
        fl1=open(fl1,"+a")
        fl1.writelines("Rollno: 59\nName: Karan\nClass: SYIF")
        fl1.seek(0)
        print(fl1.readlines())
        fl1.close
    except IOError:
        print("IO error")
    except FileNotFoundError:
        print("File not found")
flfunc()
