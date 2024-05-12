""" Ticket booking system

v1: calculate the total of one order
v2: validate the quantity of each ticket type and the total number of tickets per order
    changed the error label length to fit in the frame
"""


from tkinter import *

ADULT = 15
CHILD = 5
STUDENT = 10
MAX_TICKETS = 100

class Ticket:
    
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
    
    def calc_subtype_total(self):
        return self.price * int(self.quantity)


def collect_info():
    '''store info for each ticket type in a list'''
    order_list = []  # for one order
    order_list.append(Ticket(ADULT, quantity_adult.get()))
    order_list.append(Ticket(CHILD, quantity_child.get()))
    order_list.append(Ticket(STUDENT, quantity_student.get()))
    return order_list


def check_quantity(num):
    '''check the number in the entry box is an integer, not negative'''
    try:
        num = int(num)
        if num >= 0:
            return True
        else:
            return False
    except:
        return False


def check_total():
    '''check the total number of tickets is positive and not over the maximum limit'''
    adult = check_quantity(quantity_adult.get()) # check number of tickets for adults is valid
    child = check_quantity(quantity_child.get()) # check number of tickets for child is valid
    student = check_quantity(quantity_student.get()) # check number of tickets for students/senior is valid
    try:
        if adult and child and student: # if the number in each entry box is valid, then check the total number is also valid
            if 0 <= int(quantity_adult.get()) + int(quantity_child.get()) + int(quantity_student.get()) <= MAX_TICKETS:
                return "valid"
            else:
                return "exceeding limit"
    except ValueError: # if one of the entry boxes contains invalid input
        return "error"


def calculate():
    '''calculate the total price'''
    if check_total() == "valid":
        total_price = 0
        for order in collect_info():
            total_price += order.calc_subtype_total()    
        total_label.configure(text=f"${total_price:.2f}")
        error_label.configure(text="")
    elif check_total() == "exceeding limit":
        total_label.configure(text="Error")
        error_label.configure(text="Your order has exceeded the maximum number of tickets available")
    else:
        total_label.configure(text="Error")
        error_label.configure(text="Please enter positive integers in the boxes")
    

# main structure layout
root = Tk()
root.title("Ticket Booking System")
ticket_frame = Frame(root, width="500", height="400")
ticket_frame.grid(row=0, column=0, columnspan=2)

# labels for each ticket type
Label(ticket_frame, text = "Adult $15").grid(row=0, column=0, sticky="W")
Label(ticket_frame, text = "Child $5").grid(row=1, column=0, sticky="W")
Label(ticket_frame, text = "Student / Senior $10").grid(row=2, column=0, sticky="W")

# input boxes for number of each ticket type to order
quantity_adult = StringVar() # use StringVar in case user does not enter an integerw
quantity_adult.set("0")

quantity_child = StringVar()
quantity_child.set("0")

quantity_student = StringVar()
quantity_student.set("0")

entry_adult = Entry(ticket_frame, textvariable = quantity_adult)
entry_adult.grid(row=0, column=1, sticky="W")

entry_child = Entry(ticket_frame, textvariable = quantity_child)
entry_child.grid(row=1, column=1, sticky="W")

entry_student = Entry(ticket_frame, textvariable = quantity_student)
entry_student.grid(row=2, column=1, sticky="W")

# display the total order
Button(ticket_frame, text = "Total for the order:", command = calculate).grid(row=3, column=0, sticky="W", pady=10)
total_label = Label(ticket_frame, text = "$0.00")
total_label.grid(row=3, column=1, sticky="W", pady=10)

# label for error message
error_label = Label(ticket_frame, text = "", wraplength = "200")
error_label.grid(row=4, column=0, columnspan=2)


root.mainloop()