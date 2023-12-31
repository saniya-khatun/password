from tkinter import *
import random
from tkinter import messagebox
window = Tk()
window.config(padx=20,pady=20)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [(random.choice(letters)) for _ in range(nr_letters)]
    password_numbers = [(random.choice(numbers)) for _ in range(nr_numbers)]
    password_symbols = [(random.choice(symbols)) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols



    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    print(f"Your password is: {password}")

    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    
    if website =="" or password =="":
        messagebox.showwarning(title="ERROR",message="you left some fills empty")
    else:
        is_ok = messagebox.askokcancel(title=f"{email}", message=f"these are the detailes entered:\n website: {website} \n password: {password}" )
        if is_ok:
            f = open("save.txt","a")
            f.write(f"{website}!!{email}!!{password} \n")
            f.close()
            website_entry.delete(0, END)
            password_entry.delete(0,END)






# ---------------------------- UI SETUP ------------------------------- #
canvas= Canvas(width=200,height=189)
logo_image =PhotoImage(file="logo.png")
canvas.create_image(100, 100, image =logo_image)
canvas.grid(column=1,row=0)

# labels
website_label = Label(text="website")
website_label.grid(column=0,row=1)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1,column=1,columnspan=2)

email_username = Label(text="EmailUsername")
email_username.grid(column=0,row=2)

email_entry = Entry(width=35)
email_entry.grid(row =2 , column=1,columnspan=2)
email_entry.insert(0, 'saniyakhatun@gmail.com')
password_label = Label(text="Password")
password_label.grid(column=0,row=3)

password_entry = Entry(width=35)
password_entry.grid(row=3 , column=1,columnspan=2)

create_password_button = Button(text="create password",width=13,command=create_password)
create_password_button.grid(row=3,column=2)

add_button = Button(text="Add",width=30,command=save)
add_button.grid(row = 4 , column=1,columnspan=2)


window.mainloop()