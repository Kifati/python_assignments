import webbrowser as wb
from tkinter import *
obj=Tk(className=" Amazon Search Navigator")
e=Entry(obj,font=("Times New Roman",30))
e.grid()
def display():
    query=e.get()
    url="https://www.amazon.in/s?k="+query
    print("Navigating to: "+url)
    wb.open(url)
b=Button(obj,text="Navigate",font=("Times New Roman",30),command=display,bg="orange",activebackground="blue")
b.grid()
obj.mainloop()