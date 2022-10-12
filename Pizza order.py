from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

wn = tk.Tk()
wn.title('Pizza Order')
wn.geometry('1020x720')

pizza_size = ['Small', 'Medium', 'Large']
crusttype = ['Thin', 'Regular', 'Thick']
topping = ['Pepperoni', 'Sausage', 'Chicken', 'Bacon', 'Green pepper', 'Onion', 'Tomatoes', 'Jalapenos', 'Black olives']
extras = ['BreadSticks', 'Salad', 'Wings', 'Soda']


# functions ..........................................
def checkinfo():
    secondWn = Toplevel()
    secondWn.title('Confirm Order')
    secondWn.geometry('480x720')
    cslbl = tk.Label(secondWn, text=f'PIZZA ORDER FOR:    {customerEntry.get()} ').place(x=40, y=40)
    # csValue=customerEntry.get()
    sizelbl = tk.Label(secondWn, text=f'SIZE:  {radio_button.get()}').place(x=40, y=80)
    # rValue=radio_button.get()
    crustlbl = tk.Label(secondWn, text=f'CRUST TYPE:   {combo.get()} ').place(x=40, y=120)
    # crustValue=combo.get()
    toppingValue = ''
    for i in toppinglist.curselection():
        toppingValue = toppingValue + str(toppinglist.get(i)) + '\n'
    topping = tk.Label(secondWn, text=f'TOPPING:\n{toppingValue}').place(x=40, y=170)
    checkBoxValue1 = checkBoxVar1.get()
    checkBoxValue2 = checkBoxVar2.get()
    checkBoxValue3 = checkBoxVar3.get()
    checkboxlbl = tk.Label(secondWn, text=f'EXTRAS:\n {checkBoxValue1}  {checkBoxValue2}  {checkBoxValue3}').place(x=40,
                                                                                                                   y=290)
    # othercmValue=othercmEntry.get(1.0,END)
    othercm = tk.Label(secondWn, text=f'COMMENTS:\n{othercmEntry.get(1.0, END)}').place(x=40, y=350)
    Bbtn = tk.Button(secondWn, text='OK', command=lambda: secondWn.destroy()).place(x=200, y=400)

    frame = Frame(secondWn, width=100, height=50)
    frame.pack()
    frame.place(x=40, y=450, width=300, height=300,)
    myImage = ImageTk.PhotoImage(Image.open("/Users/muhammadhannan/Desktop/pythonProject Final project /pizza2.jpeg"))
    label = tk.Label(frame, image=myImage)
    label.pack()
    label = tk.Label(root, image=myImage)


def reset():
    csValue = customerEntry.delete(0, END)
    rValue = radio_button.set('medium')
    crustTypeCombo.current(0)
    toppingValue = ''
    # for i in toppinglist.curselection():
    # toppingValue=toppingValue+str(toppinglist(i))+'\n'
    ec1.deselect()
    ec2.deselect()
    ec3.deselect()
    othercmEntry.delete(1.0, END)


# costumer info .......................................
costumerlbl = tk.Label(wn, text='Customer Name:', font='Ariel 12 bold').place(x=40, y=20)
customerEntry = tk.Entry(wn, width=30)
customerEntry.place(x=150, y=20)

# pizza size ...........................................
pizzaSize_lbl = tk.Label(wn, text='Pizza Size:', font='Ariel 12 bold').place(x=100, y=60)
col = 1
xr = 150
# radiobutton pizza size ...............................
radio_button = tk.StringVar()
radio_button.set('medium')
tk.Radiobutton(wn, text='Small', variable=radio_button, value='Small').place(x=170, y=60)
tk.Radiobutton(wn, text='Medium', variable=radio_button, value='Medium').place(x=230, y=60)
tk.Radiobutton(wn, text='Large', variable=radio_button, value='Large').place(x=310, y=60)

# crust type ............................................
crustTypelbl = tk.Label(wn, text='Crust type:', font='Ariel 12 bold').place(x=100, y=100)
combo = tk.StringVar()
crustTypeCombo = ttk.Combobox(wn, textvariable=combo, values=crusttype, width=10)
crustTypeCombo.place(x=200, y=100)
crustTypeCombo.current(0)

# topping ...............................................
toppinglbl = tk.Label(wn, text='Topping:', font='Ariel 12 bold').place(x=100, y=145)
toppinglist = tk.Listbox(wn, selectmode=MULTIPLE)
toppinglist.place(x=200, y=140.)
for t in topping:
    toppinglist.insert(END, t)

# extras ................................................
extraslbl = tk.Label(wn, text='Extras:', font='Ariel 12 bold').place(x=40, y=320)
checkBoxVar1 = tk.StringVar()
checkBoxVar2 = tk.StringVar()
checkBoxVar3 = tk.StringVar()
checkBoxVar4 = tk.StringVar()
ec1 = tk.Checkbutton(wn, text='BreadSticks', variable=checkBoxVar1, onvalue='BreadSticks', offvalue='')
ec2 = tk.Checkbutton(wn, text='Salad', variable=checkBoxVar2, onvalue='Salad', offvalue='')
ec3 = tk.Checkbutton(wn, text='Wings', variable=checkBoxVar3, onvalue='Wings', offvalue='')
ec4 = tk.Checkbutton(wn, text='Soda', variable=checkBoxVar3, onvalue='Soda', offvalue='')
ec1.place(x=90, y=320)
ec2.place(x=190, y=320)
ec3.place(x=250, y=320)
ec4.place(x=315, y=320)
ec1.deselect()
ec2.deselect()
ec3.deselect()
ec4.deselect()

# other comments
tk.Label(wn, text='Other Comments:', font='Ariel 12 bold').place(x=40, y=360)
othercmEntry = tk.Text(wn, width=33, height=10)
othercmEntry.place(x=155, y=360)
# buttons
placeorderbutton = tk.Button(wn, text='Place Order', padx=6, pady=2, width=12, command=checkinfo).place(x=100, y=600)
resetbutton = tk.Button(wn, text='Reset', padx=6, pady=2, width=12, command=reset).place(x=270, y=600)
# Pizza Place name
tk.Label(wn, text=f'Pizza Barn', font='Ariel 20 bold italic').place(x=190, y=650)

frame = Frame(wn, width=100, height=50)
frame.pack()
frame.place(x=500, y=50, width=500, height=500,)
myImage1 = ImageTk.PhotoImage(Image.open("/Users/muhammadhannan/Desktop/pythonProject Final project /pizza1.webp"))
label = Label(frame, image=myImage1)
label.pack()

wn.mainloop()
