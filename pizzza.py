from tkinter import *
import tkinter as tk
from tkinter import ttk

wn = tk.Tk()
wn.title('pizza order')
wn.geometry('480x720')

pizza_size = ['small', 'medium', 'big']
crustypes = ['thin', 'normal', 'thick']
topping = ['pepperoni', 'sausage', 'green paper', 'onion', 'tomatos', 'anchovies']
extras = ['BreadSticks', 'salad', 'soda']


# functions ..........................................
def checkinfo():
    secondWn = Toplevel()
    secondWn.title('confirm page')
    secondWn.geometry('480x720')
    cslbl = tk.Label(secondWn, text=f'PIZZA ORDER FOR:    {cosutomerEntry.get()} ').place(x=40, y=40)
    # csValue=cosutomerEntry.get()
    sizelbl = tk.Label(secondWn, text=f'SIZE: \n  {radio_bottun.get()}').place(x=40, y=70)
    # rValue=radio_bottun.get()
    crustlbl = tk.Label(secondWn, text=f'CRUST TYPE \n  {combo.get()} ').place(x=40, y=120)
    # crustValue=combo.get()
    toppingValue = ''
    for i in toppinglist.curselection():
        toppingValue = toppingValue + str(toppinglist.get(i)) + '\n'
    topping = tk.Label(secondWn, text=f'TOPPING:\n{toppingValue}').place(x=40, y=170)
    checkBoxValue1 = checkBoxVar1.get()
    checkBoxValue2 = checkBoxVar2.get()
    checkBoxValue3 = checkBoxVar3.get()
    checkboxlbl = tk.Label(secondWn, text=f'EXTRAS:\n {checkBoxValue1}  {checkBoxValue2}  {checkBoxValue3}').place(x=40, y=300)
    # othercmValue=othercmEntry.get(1.0,END)
    othercm = tk.Label(secondWn, text=f'COMMENTS:\n{othercmEntry.get(1.0, END)}').place(x=40, y=350)
    Bbtn = tk.Button(secondWn, text='OK', command=lambda: secondWn.destroy()).place(x=200, y=400)


def reset():
    csValue = cosutomerEntry.delete(0, END)
    rValue = radio_bottun.set('medium')
    crustTypeCombo.current(0)
    toppingValue = ''
    # for i in toppinglist.curselection():
    #     toppingValue=toppingValue+str(toppinglist(i))+'\n'
    ec1.deselect()
    ec2.deselect()
    ec3.deselect()
    othercmEntry.delete(1.0, END)


# costumer info .......................................
costumerlbl = tk.Label(wn, text='customer name:').place(x=40, y=20)
cosutomerEntry = tk.Entry(wn, width=30)
cosutomerEntry.place(x=150, y=20)

# pizza size ...........................................
pizzaSize_lbl = tk.Label(wn, text='pizza size:').place(x=90, y=60)
col = 1
xr = 150
# radiobottun pizza size ...............................
radio_bottun = tk.StringVar()
radio_bottun.set('medium')
tk.Radiobutton(wn, text='small', variable=radio_bottun, value='small').place(x=160, y=60)
tk.Radiobutton(wn, text='medium', variable=radio_bottun, value='medium').place(x=220, y=60)
tk.Radiobutton(wn, text='big', variable=radio_bottun, value='big').place(x=290, y=60)

# cruss type ............................................
crusTypelbl = tk.Label(wn, text='crust type:').place(x=130, y=100)
combo = tk.StringVar()
crustTypeCombo = ttk.Combobox(wn, textvariable=combo, values=crustypes, width=10)
crustTypeCombo.place(x=200, y=100)
crustTypeCombo.current(0)

# topping ...............................................
toppinglbl = tk.Label(wn, text='topping:').place(x=130, y=220)
toppinglist = tk.Listbox(wn, selectmode=MULTIPLE)
toppinglist.place(x=200, y=140.)
for t in topping:
    toppinglist.insert(END, t)

# extras ................................................
extraslbl = tk.Label(wn, text='Extras:').place(x=130, y=320)
checkBoxVar1 = tk.StringVar()
checkBoxVar2 = tk.StringVar()
checkBoxVar3 = tk.StringVar()
ec1 = tk.Checkbutton(wn, text='BreadSticks', variable=checkBoxVar1, onvalue='BreadSticks', offvalue='')
ec2 = tk.Checkbutton(wn, text='salad', variable=checkBoxVar2, onvalue='salad', offvalue='')
ec3 = tk.Checkbutton(wn, text='soda', variable=checkBoxVar3, onvalue='soda', offvalue='')
ec1.place(x=190, y=320)
ec2.place(x=285, y=320)
ec3.place(x=350, y=320)
ec1.deselect()
ec2.deselect()
ec3.deselect()
# other cm
tk.Label(wn, text='other comments:').place(x=39, y=440)
othercmEntry = tk.Text(wn, width=33, height=10)
othercmEntry.place(x=150, y=360)
# buttons
placeorderbtn = tk.Button(wn, text='place order', padx=5, pady=2, width=12, command=checkinfo).place(x=100, y=600)
resetbtn = tk.Button(wn, text='reset', padx=5, pady=2, width=12, command=reset).place(x=270, y=600)

wn.mainloop()
