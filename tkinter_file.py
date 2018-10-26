from tkinter import *
from tkinter import filedialog
import sys,os.path

root = Tk()
def load_file():
	global path,image_data
	
	filetypes = [("Images Files",(".bmp",".png")),
	("PNG",".png")]
				
	
	filename = filedialog.askopenfilename(filetypes = filetypes,initialdir = path)
	
	if filename != "":
		path = os.path.dirname(filename)
		image_data = PhotoImage(file=filename)
		label.configure(image=image_data)
	
path = ""
image_data = PhotoImage(width=64,height=64)

label = Label(root,image=image_data)
label.pack()

menu_root = Menu(root)
root.configure(menu=menu_root)

filemenu = Menu(menu_root,tearoff=0)
filemenu.add_command(label="Open",under=0,command=load_file)
filemenu.add_separator
filemenu.add_command(label="Exit",under=0,command=sys.exit)

menu_root.add_cascade(label="File",menu=filemenu)

root.mainloop()

