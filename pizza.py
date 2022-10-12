# importing the packages
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# creating the root window

root = tk.Tk()

# main window

root.title("Tasty Pizza")  # title of the window


# opening 1st image file

# resizing the image

# opening 2nd image file

# resizing the image

# setting 1st image in label l3


# setting 2nd image in label l4

# displaying a menu for pizza using a label with font and size of text

# displaying a menu for hot dog


# entry box with font and size


# function to calculate price of pizza and hot
# dog separately
def calc():
    s1 = t1.get()  # taking all the contents from 1st entry
    s2 = t2.get()  # taking all the contents from 2nd entry

    pizza = s1.split(sep=',')  # separating each item from s1
    hotdog = s2.split(sep=',')  # separating each item from s1

    len1 = len(pizza)  # finding the length(number of items or pizza)
    len2 = len(hotdog)  # finding the length(number of items or hot dogs)

    priceOfPizza = len1 * 8.99  # multiplying number of pizza with price of 1
    priceOfHotdog = len2 * 1.99  # multiplying number of hot dogs with price of 1

    # displaying in a message box
    s = 'price of pizza : {} price of hot dog : {}'.format(priceOfPizza, priceOfHotdog)
    messagebox.showinfo('price of pizza and hot dog', s)

    # returning price of pizza ,hot dog ,list of pizza names and hot dog names
    return priceOfPizza, priceOfHotdog, pizza, hotdog


def total():
    # collecting price of pizzas, hot dogs and names of pizza and hot dogs
    pr_pizza, pr_hotdog, pizza, hotdog = calc()
    total = pr_pizza + pr_hotdog  # finding total price

    s = 'Total price : {:5.2f}'.format(total)

    child_w = Toplevel(root)  # creating another window
    child_w.geometry("350x350")  # size of child window
    child_w.grid_location(x=300, y=300)  # location of child window
    child_w.title("total price")  # title of the window
    # creating label widgets
    label_child = Label(child_w, text=s, font=('Helvetica 15'))
    label_child.place(x=20, y=50)  # positioning the label

    l2 = Label(child_w, text="you have ordered", font=('Helvetica 15'))
    l2.place(x=20, y=100)  # positioning the label

    s2 = ' '.join(pizza) + " " + ' '.join(hotdog)
    l3 = Label(child_w, text=s2, font=('Helvetica 15'))
    l3.place(x=20, y=150)  # positioning the label

# creating the buttons

# click this button to calculate price of pizza and hot dog separately
