from tkinter import *

root = Tk()

# body
root.config(bg = "lightblue")
root.geometry("600x600")
root.resizable(0, 0) 
root.title("Calculator")
# Function
def myClick():
	myLable2 = Label(root , text = int(e.get())+int(e2.get())) 
	myLable2.pack()
def myClick2():
	myLable2 = Label(root , text = int(e.get())-int(e2.get())) 
	myLable2.pack()
def myClick3():
	myLable2 = Label(root , text = int(e.get())*int(e2.get())) 
	myLable2.pack()
def myClick4():
	myLable2 = Label(root , text = int(e.get())/int(e2.get())) 
	myLable2.pack()


# lable
text = Label(root , text = "First Digit")
e = Entry(root)
text2 = Label(root , text = "Second digit")
e2 = Entry(root)
text692 = Label(root , text = " 									Result                                                                                                                                           " , bg = "purple")
text69 = Label(root , text = "   								    Function                                                                                                                                        " , bg = "purple")
myLable = Button(root , text = "Add" , command = myClick , padx = 500 )
myLable2 = Button(root , text = "subatract" , command = myClick2 , padx = 500 )
myLable3 = Button(root , text = "Multiply" , command = myClick3, padx = 500 )
myLable4 = Button(root , text = "Divide" , command = myClick4, padx = 500)

# Pack 
text.pack()
e.pack()
text2.pack()
e2.pack()
text69.pack()
myLable.pack()
myLable2.pack()
myLable3.pack()
myLable4.pack()

text692.pack()
# loop
root.mainloop()
