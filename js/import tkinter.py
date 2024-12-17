import tkinter
from tkinter import ttk
from tkinter import messagebox

global books_list
global customers_list

books_list = []
customers_list = {}

class Customer:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return [book.title for book in self.books]

    def return_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return True
        return False

    def show_books(self):
        return [book.title for book in self.books]

class Book:
    def __init__(self, title):
        self.title = title

class Library_branch:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.cards = []

    def add_book(self, book):
        self.books.append(book)
        return [book.title for book in self.books]

    def create_card(self, card_id, customer):
        card = Library_card(card_id, customer, self)
        self.cards.append(card)
        return card

class Library_card:
    def __init__(self, card_id, customer, branch):
        self.ID = card_id
        self.customer = customer
        self.branch = branch

class Employee:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def add_book(self, book_title):
        book = Book(book_title)
        return self.branch.add_book(book)

    def assign_card(self, customer, card_id):
        return self.branch.create_card(card_id, customer)

branch1 = Library_branch("District Branch")
employee1 = Employee("Abdalla", branch1)

customer1 = Customer("Aya", "aya123", "pass1")
customer2 = Customer("Osama", "osama456", "pass2")
customers_list[customer1.username] = customer1
customers_list[customer2.username] = customer2

def logout(window):
    window.withdraw()
    log.deiconify()

def handle_customer_login():
    username = user_entry.get()
    password = pass_entry.get()

    if username in customers_list and customers_list[username].password == password:
        global current_customer
        current_customer = customers_list[username]
        log.withdraw()
        cus.deiconify()
    else:
        messagebox.showerror("Error", "Invalid username or password")

def handle_employee_login():
    username = user_entry.get()
    password = pass_entry.get()

    if username == "admin" and password == "admin123":
        log.withdraw()
        emp.deiconify()
    else:
        messagebox.showerror("Error", "Invalid username or password")

def handle_login():
    if c.get() == "Customer":
        handle_customer_login()
    elif c.get() == "Admin":
        handle_employee_login()

def handle_add_book():
    book_title = emp_entry.get()
    if book_title:
        updated_books = employee1.add_book(book_title)
        messagebox.showinfo("Success", f"Book '{book_title}' has been added, Available books: {', '.join(updated_books)}")
        emp_entry.delete(0, tkinter.END)
    else:
        messagebox.showwarning("Error", "Enter a book title")

def handle_assign_card():
    username = cus2_entry.get()
    card_id = card_entry.get()

    if username in customers_list:
        customer = customers_list[username]
        card = employee1.assign_card(customer, card_id)
        messagebox.showinfo("Success", f"Card {card.ID} assigned to {customer.name}")
        cus2_entry.delete(0, tkinter.END)
        card_entry.delete(0, tkinter.END)
    else:
        messagebox.showwarning("warning", "Customer not exist")

def handle_check_out():
    book_title = cus_entry.get()
    for book in branch1.books:
        if book.title == book_title:
            current_customer.add_book(book)
            branch1.books.remove(book)
            messagebox.showinfo("Success", f"Book '{book_title}'has been checked out")
            return
    messagebox.showerror("Error", "Book not exist")

def handle_return_book():
    book_title = cus_entry.get()
    if current_customer.return_book(book_title):
        book = Book(book_title)
        branch1.add_book(book)
        messagebox.showinfo("Success", f"Book '{book_title}' has been returned")
    else:
        messagebox.showerror("Error", "Book not found in the list")

################login####################
log = tkinter.Tk()
log.title("Login Form")
log.geometry("400x400")

frame = tkinter.Frame(log)

lst = ["Customer", "Admin"]

c = ttk.Combobox(frame, values=lst, width=17, state="readonly")
c.grid(row=1, column=1, padx=20)
c.set("Customer")

select = tkinter.Label(frame, text="Select Role", font=50)
select.grid(row=1, column=0)

log_Label = tkinter.Label(frame, text="Login", font=500)
log_Label.grid(row=0, column=1, columnspan=2, pady=40)

user_label = tkinter.Label(frame, text="Username", font=50)
user_label.grid(row=2, column=0)

user_entry = tkinter.Entry(frame)
user_entry.grid(row=2, column=1, padx=20)

pass_label = tkinter.Label(frame, text="Password", font=50)
pass_label.grid(row=3, column=0)

pass_entry = tkinter.Entry(frame, show="*")
pass_entry.grid(row=3, column=1, padx=20)

log_button = tkinter.Button(frame, text="Submit", command=handle_login)
log_button.grid(row=4, column=0, columnspan=2, pady=30)

frame.pack()

#################cus################3
cus = tkinter.Toplevel(log)
cus.title("Customer Form")
cus.geometry("400x400")
cus.withdraw()

frame1 = tkinter.Frame(cus)

cus_Label = tkinter.Label(frame1, text="Customer", font=500)
cus_Label.grid(pady=10, padx=50)

book_Label = tkinter.Label(frame1, text="Enter Book", font=5)
book_Label.grid(pady=10, row=1, column=0)

cus_entry = tkinter.Entry(frame1)
cus_entry.grid(row=1, column=1)

check_button = tkinter.Button(frame1, text="Check Out", command=handle_check_out)
check_button.grid(pady=5, row=2, column=0)

return_button = tkinter.Button(frame1, text="Return", command=handle_return_book)
return_button.grid(row=2, column=1)

logout_button = tkinter.Button(frame1, text="Logout", command=lambda: logout(cus))
logout_button.grid(row=3, column=0, columnspan=2, pady=10)

frame1.pack()

####################emp################3
emp = tkinter.Toplevel(log)
emp.title("Employee Form")
emp.geometry("400x400")
emp.withdraw()

frame2 = tkinter.Frame(emp)

emp_Label = tkinter.Label(frame2, text="Employee", font=500)
emp_Label.grid(pady=10, padx=50)

book_Label = tkinter.Label(frame2, text="Enter Book", font=5)
book_Label.grid(pady=10, row=1, column=0)

emp_entry = tkinter.Entry(frame2)
emp_entry.grid(row=1, column=1)

add_button = tkinter.Button(frame2, text="Add Book", command=handle_add_book)
add_button.grid(row=2, column=0)

cus2_Label = tkinter.Label(frame2, text="Enter username", font=5)
cus2_Label.grid(pady=10, row=3, column=0)

cus2_entry = tkinter.Entry(frame2)
cus2_entry.grid(row=3, column=1)

card_Label = tkinter.Label(frame2, text="Assign Card (Username, ID)", font=5)
card_Label.grid(pady=10, row=4, column=0)

card_entry = tkinter.Entry(frame2)
card_entry.grid(row=4, column=1)

assign_button = tkinter.Button(frame2, text="Assign Card", command=handle_assign_card)
assign_button.grid(row=5, column=0)

logout_button = tkinter.Button(frame2, text="Logout", command=lambda: logout(emp))
logout_button.grid(row=6, column=0, columnspan=2, pady=10)

frame2.pack()

log.mainloop()
