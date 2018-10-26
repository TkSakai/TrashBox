from tkinter import *


root = Tk()
root.option_add("*font",("FixedSys",14))

buf = StringVar()
buf.set("")

bool1 = BooleanVar()
bool1.set(True)

radioProp = IntVar().set(1)

chkbtn = Checkbutton(root,text="option1",variable=bool1)
chkbtn.pack()

rdbtn1 = Radiobutton(root,text="1",variable=radioProp,value=0)
rdbtn1.pack()

rdbtn2 = Radiobutton(root,text="2",variable=radioProp,value=1)
rdbtn2.pack()

rdbtn3 = Radiobutton(root,text="3",variable=radioProp,value=2)
rdbtn3.pack()

def calc(event):
	expr = buf.get()
	lb.insert("end",expr)
	lb.see("end")
	value = eval(expr)
	buf.set(str(value))

def get_expr(event):
	buf.set(lb.get("active"))
	
def delete_expr(event):
	lb.delete("active")
	
	
e = Entry(root,textvariable=buf)
e.bind("<Return>",calc)

lb = Listbox(root)
lb.bind("<Double-1>",get_expr)
lb.bind("<Button-3>",delete_expr)

sb1 = Scrollbar(root,orient="v",command=lb.yview)
sb2 = Scrollbar(root,orient="h",command=lb.xview)

lb.configure(yscrollcommand=sb1.set)
lb.configure(xscrollcommand=sb2.set)


"""

e.grid(row=0, columnspan=2,sticky="ew")
lb.grid(row=1,column=0,sticky="nsew")
sb1.grid(row=1,column=1,sticky="ns")
sb2.grid(row=2,column=0,sticky="ew")	
"""	
root.mainloop()