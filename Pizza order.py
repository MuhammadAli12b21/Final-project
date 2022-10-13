from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

wn = tk.Tk()
wn.title('Pizza Order')  # Declaring window title
wn.geometry('1020x720')  # Configuring window size

# Declaring Variables
pizza_size = ['Small', 'Medium', 'Large']  # Adding types of Pizza
crust_type = ['Thin', 'Regular', 'Thick']  # Adding crust types
# Adding toppings
topping = ['Pepperoni', 'Sausage', 'Chicken', 'Bacon', 'Green pepper', 'Onion', 'Tomatoes', 'Jalapenos', 'Black olives']
extras = ['BreadSticks', 'Salad', 'Wings', 'Soda']  # Adding extras


# functions ..........................................
# First of all we will be adding all the functions
def check_info():
    secondWn = Toplevel()  # Adding second window
    secondWn.title('Confirm Order')  # Adding window title
    secondWn.geometry('480x720')  # Configuring window size
    # Adding label that displays the name of the customer
    tk.Label(secondWn, text=f'PIZZA ORDER FOR:    {customer_Entry.get()} ').place(x=40, y=40)
    # Adding Label tha displays the ordered pizza size
    tk.Label(secondWn, text=f'SIZE:  {radio_button.get()}').place(x=40, y=80)
    # Adding label that displays crust type
    tk.Label(secondWn, text=f'CRUST TYPE:   {combo.get()} ').place(x=40, y=120)
    # Adding Label that displays the topping selected by the customer
    # for i in topping_list.curselection():
    toppingValue = ''
    for i in topping_list.curselection():
        toppingValue = toppingValue + str(topping_list.get(i)) + '\n'
    tk.Label(secondWn, text=f'TOPPING:\n{toppingValue}').place(x=40, y=170)
    checkBoxValue1 = checkBoxVar1.get()
    checkBoxValue2 = checkBoxVar2.get()
    checkBoxValue3 = checkBoxVar3.get()
    # Adding Label the displays the 'extras' selected by the customer
    tk.Label(secondWn, text=f'EXTRAS:\n {checkBoxValue1}  {checkBoxValue2}  {checkBoxValue3}').place(x=40, y=290)
    # Adding label that displays comments by customers
    tk.Label(secondWn, text=f'COMMENTS:\n{other_comments_Entry.get(1.0, END)}').place(x=40, y=350)
    # Adding button that submits the order
    tk.Button(secondWn, text='OK', command=lambda: secondWn.destroy()).place(x=200, y=400)

    # Displaying an image of pizza
    frame = Frame(secondWn, width=100, height=50)  # Adding a frame to display the image in
    frame.pack()
    frame.place(x=40, y=450, width=300, height=300, )  # Configuring the frame size
    # Adding the image location
    myImage = ImageTk.PhotoImage(Image.open("/Users/muhammadhannan/Desktop/pythonProject Final project /pizza2.webp"))
    # Adding label to put the frame in so the image can be displayed
    label = tk.Label(frame, image=myImage)
    label.pack()
    label = tk.Label(root)


# By adding this function you can reset the Pizza order page
def reset():
    # csValue=customer_Entry.get()
    customer_Entry.delete(0, END)
    # rValue=radio_button.get()
    radio_button.set('Medium')
    # crust_Value=combo.get()
    crustTypeCombo.current(0)
    ec1.deselect()
    ec2.deselect()
    ec3.deselect()
    # other_comments_Value=other_comments_Entry.get(1.0,END)
    other_comments_Entry.delete(1.0, END)


# costumer info .......................................
# Adding label that asks customers name
tk.Label(wn, text='Customer Name:', font='Ariel 12 bold').place(x=40, y=20)
customer_Entry = tk.Entry(wn, width=30)  # Adding text box to write the name
customer_Entry.place(x=150, y=20)  # Configuring text box

# pizza size ...........................................
# Adding label that asks pizza size
tk.Label(wn, text='Pizza Size:', font='Ariel 12 bold').place(x=100, y=60)
col = 1  # configuring pizza size
xr = 150
# Adding radiobutton for pizza size ...............................
radio_button = tk.StringVar()
# Configuring radiobutton
radio_button.set('medium')
tk.Radiobutton(wn, text='Small', variable=radio_button, value='Small').place(x=170, y=60)
tk.Radiobutton(wn, text='Medium', variable=radio_button, value='Medium').place(x=230, y=60)
tk.Radiobutton(wn, text='Large', variable=radio_button, value='Large').place(x=310, y=60)

# crust type ............................................
# Adding label to ask crust type
tk.Label(wn, text='Crust type:', font='Ariel 12 bold').place(x=100, y=100)
# Adding combo box
combo = tk.StringVar()
crustTypeCombo = ttk.Combobox(wn, textvariable=combo, values=crust_type, width=10)  # configuring combo box
crustTypeCombo.place(x=200, y=100)
crustTypeCombo.current(0)

# topping ...............................................
# Adding label to display toppings
tk.Label(wn, text='Topping:', font='Ariel 12 bold').place(x=100, y=145)
# Adding list box
topping_list = tk.Listbox(wn, selectmode=MULTIPLE)
topping_list.place(x=200, y=140.)  # Configuring list box
for t in topping:
    topping_list.insert(END, t)

# extras ................................................
# Adding label to display Extras
tk.Label(wn, text='Extras:', font='Ariel 12 bold').place(x=40, y=320)
# Adding check box
checkBoxVar1 = tk.StringVar()
checkBoxVar2 = tk.StringVar()
checkBoxVar3 = tk.StringVar()
checkBoxVar4 = tk.StringVar()
# Configuring check box
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
# Adding label for display other comments
tk.Label(wn, text='Other Comments:', font='Ariel 12 bold').place(x=40, y=360)
other_comments_Entry = tk.Text(wn, width=33, height=10)  # Configuring text box
other_comments_Entry.place(x=155, y=360)
# buttons
# Adding button to place order
tk.Button(wn, text='Place Order', padx=6, pady=2, width=12, command=check_info).place(x=100, y=600)
# Adding button to reset order page
tk.Button(wn, text='Reset', padx=6, pady=2, width=12, command=reset).place(x=270, y=600)
# Adding Pizza Place logo
tk.Label(wn, text=f'Pizza Barn', font='Ariel 20 bold italic').place(x=190, y=650)

# Displaying image that show the pizza place
frame = Frame(wn, width=100, height=50)
frame.pack()
frame.place(x=500, y=50, width=500, height=500, )  # Configuring image
# Adding image location
myImage1 = ImageTk.PhotoImage(Image.open("/Users/muhammadhannan/Desktop/pythonProject Final project /pizza1.webp"))
# Adding label to display image
label = Label(frame, image=myImage1)
label.pack()

wn.mainloop()  # Closing loop
