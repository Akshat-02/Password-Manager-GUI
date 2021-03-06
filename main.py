
import email
from tkinter import *
from tkinter import messagebox
from tkinter import font
import gen_passwd
import pyperclip as clip
import json

# ---------------------------Constants and globa variables ----------------------- #
PINK = "#e2979c"
RED = "#e7305b"
CUTE_RED = "#FF8080"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WEIRD_BLUE = "#1C658C"
FONT_NAME = "Courier"

# ----------------------------Search website------------------------------------- #

def search_website():
    website_name = website_entry.get()

    #checking if website entry is empty
    if len(website_name) == 0:
        messagebox.showwarning(title= "Need Input", message= "Please provide some data!")

        return                    # if it is empty then exit the function and it won't run further

    with open("shadow.json", "r") as data_file:
        data = json.load(data_file)

    try:
        email = data[website_name]["Username/Email"]
        passwd = data[website_name]["Plain text Password"]

    except KeyError as error_msg:
        messagebox.showerror(title= "Error", message= f"No information found for website: {error_msg}")
        
    else:                                         # backslash (\) is used to indicate a line continuation

        yes = messagebox.askyesno(title= f"Website: {website_name}", message= f"""Email/Username:     {email}\n\
Password:    {passwd}\n\n Do you want to copy password to clibboard?""")

        if yes:
            clip.copy(passwd)              #Using pyperclip module to copy the password in clipboard
        
    finally:
        website_entry.delete(0, END)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pass_gen():
    passwd_gen.delete(0, END)         #Clearing the password field incase user click generate button again to avoid appending

    password = gen_passwd.password_generator()        #Retrieving generated password from gen_passwd module
    passwd_gen.insert(END, password)

    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def pass_save():

    #Getting the user input wth get() method
    website_name = website_entry.get()                 
    uname = uname_entry.get()
    passwd = passwd_gen.get()


    json_dict = {
        website_name:{
            "Username/Email": uname,
            "Plain text Password": passwd
        }
    }

    # Condition to check for empty entry fields (Should be alerted for this)
    if len(website_name) == 0 or len(passwd) == 0:
        
        # Usig messagebox module in tkinter for dialogue boxes
        messagebox.showwarning(title= "Something's missing", message= "One or more fields are empty!")        

    else:
        confirm = messagebox.askokcancel(title= "Confirm", message=f"""Save these details:- \n\n \
Website:    {website_name}\n Email/Username:    {uname}\n Password:    {passwd}""")
        
        if confirm:

            #Using pyperclip module to copy the password in clipboard    
            clip.copy(passwd)           

            try:
                with open("shadow.json", "r") as pass_file:
                    #reading old data
                    data = json.load(pass_file)                   #load() method is used to read the file for json data where loads() is for json string

                    #updating with new data
                    data.update(json_dict)                        #update() method is used to update old data with new data

            except FileNotFoundError:
                with open("shadow.json", "w") as pass_file:
                    #writing updated data to the json file
                    json.dump(json_dict, pass_file, indent=4)

            else:
                with open("shadow.json", "w") as pass_file:
                    json.dump(data, pass_file, indent=4)
                

            #Clearing the data in entry widgets once the Add button is clicked.
            website_entry.delete(0, END)                # 0 is the first index and END is the last index
            uname_entry.delete(0, END)                  # this is the range we want the data to get cleared
            passwd_gen.delete(0, END)

            uname_entry.insert(END, "@gmail.com")       # Adding the default username text back



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


search = Button(text= "Search", width=15, command= search_website, bg = GREEN)

search.grid(row=1, column=2)



window.mainloop()