from calendar import c
from tkinter import *
from xmlrpc.client import Unmarshaller
from numpy import save

from pyparsing import col

# ---------------------------Constants and globa variables ----------------------- #
PINK = "#e2979c"
RED = "#e7305b"
CUTE_RED = "#FF8080"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WEIRD_BLUE = "#1C658C"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pass_gen():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #

def pass_save():
    pass

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50, bg = None)

#using Canvas class to create an instance
canvas = Canvas(width= 200, height= 200)

logo = PhotoImage(file="logo.png")         #Creating an image object of the logo to use with canvas.
canvas.create_image(100, 100, image= logo)         #Using canvas to create an image inside it 
canvas.grid(row=0, column=1)


#lables

website_name = Label(text= "Website: ", font=("arial", 8, "bold"))
website_name.config(pady=2)                               #Setting y-padding to 2

website_name.grid(row=1, column=0)


email_username = Label(text= "Email/Username: ", font=("arial", 8, "bold"))
email_username.config(pady=2)                            #Setting y-padding to 2

email_username.grid(row=2, column=0)


passwd = Label(text= "Password: ", font=("arial", 8, "bold"))
passwd.config(pady=2)                                   #Setting y-padding to 2

passwd.grid(row=3, column=0)



# Entry fields
website_entry = Entry(width=35)
website_entry.focus()                        #focus() method puts the cursor to the specified entry field

website_entry.grid(row=1, column=1)


uname_entry = Entry(width=35)
uname_entry.insert(END, "@gmail.com")             #insert() method puts the text to the entry field by default at the specified index (0 or END)

uname_entry.grid(row=2, column=1)


passwd_gen = Entry(width=35)

passwd_gen.grid(row=3, column=1)



#Buttons

gen_pass = Button(text="Generate Password", command= pass_gen, bg= CUTE_RED)

gen_pass.grid(row=3, column=2)


save_pass = Button(text= "Add",width= 21 ,command= pass_save, bg= WEIRD_BLUE, fg= "white")
save_pass.config(pady=1)

save_pass.grid(row=4, column=1)




window.mainloop()