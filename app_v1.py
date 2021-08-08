### Imports ###
from tkinter import *
import os
from PIL import ImageTk, Image

### Main Screen ###
master = Tk()
master.title('GUI Banking')

### Functions ###
def register():
    # Variables
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    # Register Screen
    register_screen = Toplevel(master)
    register_screen.title('Register')
    # Labels
    Label(register_screen, text='Create account', font=('Calibri', 12)).grid(
        row=0, sticky=N, pady=10)
    Label(register_screen, text='Name', font=('Calibri', 12)).grid(
        row=1, sticky=W)
    Label(register_screen, text='Age', font=('Calibri', 12)).grid(
        row=2, sticky=W)
    Label(register_screen, text='Gender', font=('Calibri', 12)).grid(
        row=3, sticky=W)
    Label(register_screen, text='Password', font=('Calibri', 12)).grid(
        row=4, sticky=W)
    notif = Label(register_screen, font=('Calibri', 12))
    notif.grid(row=6, sticky=N, pady=10)
    # Entries
    Entry(register_screen, textvariable=temp_name).grid(row=1, column=1)
    Entry(register_screen, textvariable=temp_age).grid(row=2, column=1)
    Entry(register_screen, textvariable=temp_gender).grid(row=3, column=1)
    Entry(register_screen, textvariable=temp_password, show='*').grid(row=4, column=1)
    # Button
    Button(register_screen, text='Register', command=finish_rego, font=('Calibri', 12)).grid(
        row=5, sticky=N, pady=10)

def finish_rego():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()
    if name=='' or age=='' or gender=='' or password=='':
        notif.config(fg='red', text='All fields are required!')
        return
    for name_check in all_accounts:
        if name + '.txt' == name_check:
            notif.config(fg='red', text='Account already exists!')
            return
        else:
            new_file = open(name + '.txt', 'w')
            new_file.write(name + '\n')
            new_file.write(password + '\n')
            new_file.write(age + '\n')
            new_file.write(gender + '\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg='green', text='Account successfully created!')

def login_session():
    global login_name
    all_accounts = os.listdir()
    # returns a list containing the names of the entries in the directory given by path
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()
    for name in all_accounts:
        if name == login_name + '.txt':
            file = open(name, 'r')
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[1]
            # Account Dashboard
            if login_password == password:
                login_screen.destroy()
                acc_dashboard = Toplevel(master)
                acc_dashboard.title('Account Dashboard')
                # Labels
                Label(acc_dashboard, text='Account Dashboard', font=('Calibri', 12)).grid(
                    row=0, sticky=N, pady=10)
                Label(acc_dashboard, text='Welcome ' + name[:-4], font=('Calibri', 12)).grid(
                    row=1, sticky=N, pady=5)
                # Buttons
                Button(acc_dashboard, text='Personal Information', font=('Calibri', 12), width=30, 
                command=personal_info).grid(row=2, sticky=N, padx=10)
                Button(acc_dashboard, text='Deposit', font=('Calibri', 12), width=30, 
                command=deposit).grid(row=3, sticky=N, padx=10)
                Button(acc_dashboard, text='Withdraw', font=('Calibri', 12), width=30,
                command=withdraw).grid(row=4, sticky=N, padx=10)
                Label(acc_dashboard).grid(row=5, sticky=N, pady=10)
                return
            else:
                login_notif.config(fg='red', text='Incorrect password!')
                return
        login_notif.config(fg='red', text='This account does not exist!')
    
def personal_info():
    # Variables
    file = open(login_name + '.txt', 'r')
    file_data = file.read()
    user_info = file_data.split('\n')
    info_name = user_info[0]
    info_age = user_info[2]
    info_gender = user_info[3]
    info_balance = user_info[4]
    # Screen
    personal_info_screen = Toplevel(master)
    personal_info_screen.title('Personal Information')
    # Labels
    Label(personal_info_screen, text='Personal Information', font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(personal_info_screen, text='Name: ' + info_name, font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(personal_info_screen, text='Age: ' + info_age, font=('Calibri', 12)).grid(row=2, sticky=W)
    Label(personal_info_screen, text='Gender: ' + info_gender, font=('Calibri', 12)).grid(row=3, sticky=W)
    Label(personal_info_screen, text='Balance: ' + info_balance, font=('Calibri', 12)).grid(row=4, sticky=W)

def deposit():
    global amount
    global deposit_notif
    global cur_bal_label
    amount = StringVar()
    file = open(login_name + '.txt', 'r')
    file_data = file.read()
    user_info = file_data.split('\n')
    info_balance = user_info[4]
    # Deposit Screen
    deposit_screen = Toplevel(master)
    deposit_screen.title('Deposit')
    # Labels
    Label(deposit_screen, text='Deposit', font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    cur_bal_label = Label(deposit_screen, text='Current Balance: ' + info_balance, font=('Calibri', 12))
    cur_bal_label.grid(row=1, sticky=W)
    Label(deposit_screen, text='Amount: ', font=('Calibri', 12)).grid(row=2, sticky=W)
    deposit_notif = Label(deposit_screen, font=('Calibri', 12))
    deposit_notif.grid(row=4, sticky=N, pady=5)
    # Entry
    Entry(deposit_screen, textvariable=amount).grid(row=2, column=1)
    # Button
    Button(deposit_screen, text='Finish', font=('Calibri', 12), command=finish_deposit).grid(row=3, sticky=W, padx=5, pady=5)

def finish_deposit():
    if amount.get() == '':
        deposit_notif.config(fg='red', text='Amount is required!')
        return
    if float(amount.get()) <= 0:
        deposit_notif.config(fg='red', text='Positive amount is required!')
        return
    file = open(login_name + '.txt', 'r+')
    file_data = file.read()
    info = file_data.split('\n')
    cur_bal = info[4]
    new_bal = cur_bal
    new_bal = float(new_bal) + float(amount.get())
    file_data = file_data.replace(cur_bal, str(new_bal))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    cur_bal_label.config(fg='green', text='Current balance: ' + str(new_bal))
    deposit_notif.config(fg='green', text='Balance successfully updated!')

def withdraw():
    global withdraw_amount
    global withdraw_notif
    global cur_bal_label
    withdraw_amount = StringVar()
    file = open(login_name + '.txt', 'r')
    file_data = file.read()
    user_info = file_data.split('\n')
    info_balance = user_info[4]
    # Deposit Screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title('Withdraw')
    # Labels
    Label(withdraw_screen, text='Withdraw', font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    cur_bal_label = Label(withdraw_screen, text='Current Balance: ' + info_balance, font=('Calibri', 12))
    cur_bal_label.grid(row=1, sticky=W)
    Label(withdraw_screen, text='Amount: ', font=('Calibri', 12)).grid(row=2, sticky=W)
    withdraw_notif = Label(withdraw_screen, font=('Calibri', 12))
    withdraw_notif.grid(row=4, sticky=N, pady=5)
    # Entry
    Entry(withdraw_screen, textvariable=withdraw_amount).grid(row=2, column=1)
    # Button
    Button(withdraw_screen, text='Finish', font=('Calibri', 12), command=finish_withdraw).grid(row=3, sticky=W, padx=5, pady=5)


def finish_withdraw():
    if withdraw_amount.get() == '':
        withdraw_notif.config(fg='red', text='Amount is required!')
        return
    if float(withdraw_amount.get()) <= 0:
        withdraw_notif.config(fg='red', text='Positive amount is required!')
        return
    file = open(login_name + '.txt', 'r+')
    file_data = file.read()
    info = file_data.split('\n')
    cur_bal = info[4]

    if float(withdraw_amount.get()) > float(cur_bal):
        withdraw_notif.config(fg='red', text='Insufficient funds!')
        return
    new_bal = cur_bal
    new_bal = float(new_bal) - float(withdraw_amount.get())
    file_data = file_data.replace(cur_bal, str(new_bal))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    cur_bal_label.config(fg='green', text='Current balance: ' + str(new_bal))
    withdraw_notif.config(fg='green', text='Balance successfully updated!')

def login():
    # Variables
    global temp_login_name
    global temp_login_password
    global login_screen
    global login_notif
    temp_login_name = StringVar()
    temp_login_password = StringVar()

    # Log In Screen
    login_screen = Toplevel(master)
    login_screen.title('Log In')

    # Labels
    Label(login_screen, text='Log In', font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(login_screen, text='Username', font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(login_screen, text='Password', font=('Calibri', 12)).grid(row=2, sticky=W)
    login_notif = Label(login_screen, font=('Calibri', 12))
    login_notif.grid(row=4, sticky=N)

    # Entries
    Entry(login_screen, textvariable=temp_login_name).grid(row=1, column=1, padx=5)
    Entry(login_screen, textvariable=temp_login_password, show='*').grid(row=2, column=1, padx=5)

    # Buttons
    Button(login_screen, text='Log In', command=login_session, width=15, font=('Calibri', 12)).grid(
        row=3, sticky=W, padx=5, pady=5)

### Image Import ###
img = Image.open('img/secure.jpeg')
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

### Labels ###
Label(master, text='Bank of Python', font=('Calibri', 14)).grid(row=0, sticky=N, pady=10)
Label(master, text='Secure Transactions', font=('Calibri', 12)).grid(row=1, sticky=N)
Label(master, image=img).grid(row=2, sticky=N, pady=15)

### Buttons ###
Button(master, text='Register', font=('Calibri', 12), width=20, command=register).grid(row=3, sticky=N)
Button(master, text='Log In', font=('Calibri', 12), width=20, command=login).grid(row=4, sticky=N, pady=10)

master.mainloop()