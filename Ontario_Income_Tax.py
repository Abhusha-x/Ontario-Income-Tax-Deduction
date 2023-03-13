# Program : Ontario Income Tax Deduction
# Name    : Ghimire, Abhusha
# Date    : November 30, 2021
# Description : Gives users calculations about their income tax.

import tkinter

def exit_program ():
    exit()

#Assigns value to the money inputs
def eligibility_assignment(a, b):
    x = a / (b * 2)
    if (x > 0.5):
        money_list[6] = 0.5
        #value cannot be over 0.5 no matter the amount of money present
    else:
        money_list[6] = x

#Checks to see if number is valid and within 2 decimal digits
def number_valid(x):
    if ((x.isdigit() == True) and (x[0] != "")):
        valid = True
    elif ((x[0:-3].isdigit() == True) and (x[-2:].isdigit() == True) and (x[-3] == ".")):
        if (x[0] != ""):
            valid = True
    elif ((x[0:-2].isdigit() == True) and (x[-1:].isdigit() == True) and (x[-2] == ".")):
        if (x[0] != ""):
            valid = True
    else:
        valid = False
    return valid

#Calculates tax according to Ontario tax brackets
def tax_calculator(a):
    if (a <= 45142):
        b = 0.0505 * a
    elif (45142 < a <= 90287):
        x = a - 45142
        b = 0.0915 * x + 2280
    elif (90287 < a <= 150000):
        x = a - 90287
        b = 0.1116 * x + 6411
    elif (150000 < a <= 220000):
        x = a - 150000
        b = 0.1216 * x + 13075
    else:
        x = a - 220000
        b = 0.1316 * x + 21587
    tax_list[0] = b

#Gives value to radiobutton inputs
def money_function():
    if (information[0] == "Married"):
        money_list[0] = 0.0100
    elif (information[0] == "Unmarried"):
        money_list[0] = 0.0000
    if (information[1] == "Yes, full-time"):
        money_list[1] = 0.0175
    elif (information[1] == "Yes, part-time"):
        money_list[1] = 0.0100
    elif (information[1] == "No"):
        money_list[1] = 0.0000
    if (information[2] == "First-time homeowner"):
        money_list[2] = 0.0150
    elif (information[2] == "Experienced homeowner"):
        money_list[2] = 0.0050
    elif (information[2] == "No property"):
        money_list[2] = 0.0000
    if (information[3] == "65+"):
        money_list[3] = 0.0500
    elif (information[3] == "16-25"):
        money_list[3] = 0.0005
    elif (information[3] == "26-64"):
        money_list[3] = 0.0000
    if (information[4] == "1"):
        money_list[4] = 0.0200
    elif (information[4] == "2+"):
        money_list[4] = 0.0300
    elif (information[4] == "0"):
        money_list[4] = 0.0000
    if (information[5] == "Yes"):
        money_list[5] = 0.0500
    elif (information[5] == "No"):
        money_list[5] = 0.0000

#Calculates tax after deduction
def deduction_calculator(a):
    b = a - money_list[0] * a
    c = b - money_list[1] * b
    d = c - money_list[2] * c
    e = d - money_list[3] * d
    f = e - money_list[4] * e
    g = f - money_list[5] * f
    h = g - money_list[6] * g
    deduction_list[0] = h

def marital_function():
    input_marital = marital_selected.get()
    information[0] = input_marital #Appends to list

#Creates marital radiobuttons
def marital_button(x, y, z):
    global marital
    marital = tkinter.Radiobutton(input_window, bg="White", text=x, width=30)
    marital.configure(anchor="w", variable=marital_selected, value=x, command=marital_function)
    marital.grid(row=y, column=z)

def student_function():
    input_student = student_selected.get()
    information[1] = input_student

#Creates students radiobuttons
def student_button(x, y, z):
    global student
    student = tkinter.Radiobutton(input_window, bg="White", text=x, width=30)
    student.configure(anchor="w", variable=student_selected, value=x, command=student_function)
    student.grid(row=y, column=z)

def home_function():
    input_home = home_selected.get()
    information[2] = input_home

#Creates homeownership radiobuttons
def home_button(x, y, z):
    global home
    home = tkinter.Radiobutton(input_window, bg="White", text=x, width=30)
    home.configure(anchor="w", variable=home_selected, value=x, command=home_function)
    home.grid(row=y, column=z)

def age_function():
    input_age = age_selected.get()
    information[3] = input_age

#Creates age radiobuttons
def age_button(x, y, z):
    global age
    age = tkinter.Radiobutton(input_window, bg="White", text=x, width=30)
    age.configure(anchor="w", variable=age_selected, value=x, command=age_function)
    age.grid(row=y, column=z)

def children_function():
    input_children = children_selected.get()
    information[4] = input_children

#Creates children radiobuttons
def children_button(x, y, z):
    global children
    children = tkinter.Radiobutton(input_window, bg="White", text=x, width=30)
    children.configure(anchor="w", variable=children_selected, value=x, command=children_function)
    children.grid(row=y, column=z)

def disabled_function():
    input_disabled = disabled_selected.get()
    information[5] = input_disabled

#Creates disabled radiobuttons
def disabled_button(x, y, z):
    global disabled
    disabled = tkinter.Radiobutton(input_window, bg="White", text=x, width=30)
    disabled.configure(anchor="w", variable=disabled_selected, value=x, command=disabled_function)
    disabled.grid(row=y, column=z)

#What happens when the charity value is entered
def charity_b_click():
    charity_money = entry_charity.get()
    if (number_valid(charity_money) == True):
        if (charity_clicked == 1):
            button_charity.configure(text="Got it!", bg="#8CEE7A")
            charity_money = float(charity_money)
            checkbutton[0] = charity_money
    elif (number_valid(charity_money) != True):
        checkbutton[0] = 0
        button_charity.configure(text="Invalid number try again.", bg="#ED6A6A")
    else:
        button_charity.configure(text="Invalid number try again.", bg="#ED6A6A")

#What happens when the debt value is entered
def debt_b_click():
    debt_money = entry_debt.get()
    if (number_valid(debt_money) == True):
        if (debt_clicked == 1):
            button_debt.configure(text="Got it!", bg="#8CEE7A")
            debt_money = float(debt_money)
            checkbutton[1] = debt_money
    elif (number_valid(debt_money) == False):
        checkbutton[1] = 0
        button_debt.configure(text="Invalid number try again.", bg="#ED6A6A")
    else:
        button_debt.configure(text="Invalid number try again.", bg="#ED6A6A")

#What happens when the savings value is entered
def savings_b_click():
    savings_money = entry_savings.get()
    if (number_valid(savings_money) == True):
        if (savings_clicked == 1):
            button_savings.configure(text="Got it!", bg="#8CEE7A")
            savings_money = float(savings_money)
            checkbutton[2] = savings_money
    elif (number_valid(savings_money) == False):
        checkbutton[2] = 0
        button_savings.configure(text="Invalid number try again.", bg="#ED6A6A")
    else:
        button_savings.configure(text="Invalid number try again.", bg="#ED6A6A")

#What happens when the charity checkbutton is clicked
def charity_command():
    global entry_charity, charity_clicked, button_charity
    charity_clicked = charity_click.get()

    #Creates button and entry area
    if (charity_clicked == 1):
        entry_charity = tkinter.Entry(input_window, bg = "White", width=30)
        entry_charity.grid(row=15, column=2)
        button_charity = tkinter.Button(input_window, anchor="w", width=25)
        button_charity.configure(text="Enter amount in CAD")
        button_charity.configure(command=charity_b_click)
        button_charity.grid(row=15, column=3)

    #Covers the button and entry area with white labels
    elif (charity_clicked == 0):
        label_charity = tkinter.Label(input_window, bg = "White", width=30)
        label_charity.grid(row=15, column=2)
        label_charity = tkinter.Label(input_window, bg = "White", width=30, height=2)
        label_charity.grid(row=15, column=3)
        checkbutton[0] = 0

#What happens when the debt checkbutton is clicked
def debt_command():
    global entry_debt, debt_clicked, button_debt
    debt_clicked = debt_click.get()

    #Creates button and entry area
    if (debt_clicked == 1):
        entry_debt = tkinter.Entry(input_window, bg = "White", width=30)
        entry_debt.grid(row=16, column=2)
        button_debt = tkinter.Button(input_window, anchor="w", width=25)
        button_debt.configure(text="Enter amount in CAD")
        button_debt.configure(command=debt_b_click)
        button_debt.grid(row=16, column=3)

    #Covers the button and entry area with white labels
    elif (debt_clicked == 0):
        label_debt = tkinter.Label(input_window, bg = "White", width=30)
        label_debt.grid(row=16, column=2)
        label_debt = tkinter.Label(input_window, bg = "White", width=30, height=2)
        label_debt.grid(row=16, column=3)
        checkbutton[1] = 0
    
#What happens when the savings checkbutton is clicked
def savings_command():
    global entry_savings, savings_clicked, button_savings
    savings_clicked = savings_click.get()

    #Creates button and entry area
    if (savings_clicked == 1):
        entry_savings = tkinter.Entry(input_window, bg = "White", width=30)
        entry_savings.grid(row=17, column=2)
        button_savings = tkinter.Button(input_window, anchor="w", width=25)
        button_savings.configure(text="Enter amount in CAD")
        button_savings.configure(command=savings_b_click)
        button_savings.grid(row=17, column=3)

    #Covers the button and entry area with white labels
    elif (savings_clicked == 0):
        label_savings = tkinter.Label(input_window, bg = "White", width=30)
        label_savings.grid(row=17, column=2)
        label_savings = tkinter.Label(input_window, bg = "White", width=30, height=2)
        label_savings.grid(row=17, column=3)
        checkbutton[2] = 0

#What happens when calculate button is clicked
def calculate_click():
    global gross_label, net_pre, net_post, tax_pre, tax_post, deduction_label
    income_input = input_income.get()
    
    if ((income_input != "0") and (number_valid(income_input) == True)): #Input validity
        income_input = float(income_input)
        message_calculate.configure(text="")
        money_function()
        tax_calculator(income_input)

        #Appends money entered
        total_checkbutton[0] = checkbutton[0] + checkbutton[1] + checkbutton[2]
        #Assigns the money value and appends to money_list
        eligibility_assignment(total_checkbutton[0], income_input)

        #Calculates deduction
        deduction_calculator(tax_list[0])

        #Calculates other categories
        net_pre_num = income_input - tax_list[0]
        net_post_num = income_input - deduction_list[0]
        saved_total = tax_list[0] - deduction_list[0]

        #Configures labels
        gross_label.configure(text="$ %0.2f" %income_input)
        net_pre.configure(text="$ %0.2f" %net_pre_num)
        net_post.configure(text="$ %0.2f" %net_post_num)
        tax_pre.configure(text="$ %0.2f" %tax_list[0])
        tax_post.configure(text="$ %0.2f" %deduction_list[0])
        deduction_label.configure(text="$ %0.2f" %saved_total)
    elif (income_input == "0"):
        gross_label.configure(text="$ 0.00")
        net_pre.configure(text="$ 0.00")
        net_post.configure(text="$ 0.00")
        tax_pre.configure(text="$ 0.00")
        tax_post.configure(text="$ 0.00")
        deduction_label.configure(text="$ 0.00")
    else:
        message_calculate.configure(text="INVALID: Enter up to 2 decimal digits")
        message_calculate.configure(fg="#ED6A6A")

#Creates empty labels for design for all frames
def empty_label(x, y, z):
    empty = tkinter.Label(x, bg="White", width=1)
    empty.grid(row=y, column=z)

#Creates prompt labels for input_window
def prompt_label(x, y, z):
    prompt = tkinter.Label(input_window, width=30, anchor="w", bg="White", text=x)
    prompt.grid(row=y, column=z)

#Creates prompt labels for output_window
def output_label(x, y, z):
    output_label = tkinter.Label(output_window, width=30, anchor="e", bg="White", text=x)
    output_label.configure(font="bold")
    output_label.grid(row=y, column=z)

def main():

    #Global variables, lists, etc.
    global information, tax_list, money_list, deduction_list, checkbutton
    global window, exit_window, banner_window, input_window, output_window
    global marital_selected, student_selected, home_selected
    global age_selected, children_selected, disabled_selected
    global input_income, message_calculate, total_checkbutton
    global gross_label, net_pre, net_post, tax_pre, tax_post, deduction_label
    global charity_click, debt_click, savings_click
    global button_charity, button_debt, button_savings

    #All the lists being used
    information = ["", "", "", "", "", ""]
    tax_list = [""]
    money_list = ["", "", "", "", "", "", ""]
    deduction_list = [""]
    checkbutton = [0, 0, 0]
    total_checkbutton = [0]

    #Creating window
    window = tkinter.Tk()
    window.title("Government of Ontario")
    window.geometry("725x800")
    window.configure(background="White")

    #Creating frames
    exit_window = tkinter.Frame(window, bg="White")
    exit_window.grid(row=0, column=0)

    banner_window = tkinter.Frame(window, bg="White")
    banner_window.grid(row=1, column=0)

    input_window = tkinter.Frame(window, bg="White")
    input_window.grid(row=2, column=0)

    output_window = tkinter.Frame(window, bg="White")
    output_window.grid(row=3, column=0)

    #Making radiobutton variables into strings
    marital_selected = tkinter.StringVar()
    student_selected = tkinter.StringVar()
    home_selected = tkinter.StringVar()
    age_selected = tkinter.StringVar()
    children_selected = tkinter.StringVar()
    single_selected = tkinter.StringVar()
    disabled_selected = tkinter.StringVar()

    #Making checkbutton variables into integers
    charity_click = tkinter.IntVar()
    debt_click = tkinter.IntVar()
    savings_click = tkinter.IntVar()

    empty = tkinter.Label(exit_window, bg="White", width=98)
    empty.grid(row=0, column=0)

    #Creates exit button
    exit_button = tkinter.Button(exit_window, text="X", command = exit_program, width=3)
    exit_button.configure(bg="#ED6A6A", fg="White")
    exit_button.grid(row=0, column=1)

    #Creates heading "Ontario Income Tax Deduction
    title = tkinter.Label(banner_window, bg="White", text="Ontario Income Tax Deduction")
    title.configure(font=("Times new", 20, "bold"), anchor="center")
    title.grid(row=0, column=0)

    empty_label(input_window, 0, 0)
    empty_label(input_window, 1, 1)

    #Marital radiobuttons
    prompt_label("Select your marital status:", 2, 1)
    marital_button("Married", 3, 1)
    marital.invoke()
    marital_button("Unmarried", 4, 1)

    #Student radiobuttons
    prompt_label("Are you a student?", 2, 2)
    student_button("Yes, full-time", 3, 2)
    student.invoke()
    student_button("Yes, part-time", 4, 2)
    student_button("No", 5, 2)

    #Homeownership radiobuttons
    prompt_label("Select your homeownership status:", 2, 3)
    home_button("No property", 3, 3)
    home.invoke()
    home_button("First-time homeowner", 4, 3)
    home_button("Experienced homeowner", 5, 3)

    empty_label(input_window, 6, 1)
    empty_label(input_window, 7, 1)

    #Age radiobuttons
    prompt_label("Indicate your age:", 8, 1)
    age_button("16-25", 9, 1)
    age.invoke()
    age_button("26-64", 10, 1)
    age_button("65+", 11, 1)

    #Children radiobuttons
    prompt_label("Number of children:", 8, 2)
    children_button("0", 9, 2)
    children.invoke()
    children_button("1", 10, 2)
    children_button("2+", 11, 2)

    #Disability radiobuttons
    prompt_label("Do you have a disablity?", 8, 3)
    disabled_button("Yes", 9, 3)
    disabled.invoke()
    disabled_button("No", 10, 3)

    empty_label(input_window, 12, 1)
    empty_label(input_window, 13, 1)

    #Creating checkbuttons
    prompt_label("Within 365 days you have... :", 14, 1)

    #Empty labels are height 2 in the very beginning so that buttons could be
    #hidden completely without chaning the desing
    label_random = tkinter.Label(input_window, bg = "White", width=30, height=2)
    label_random.grid(row=15, column=3)

    label_random = tkinter.Label(input_window, bg = "White", width=30, height=2)
    label_random.grid(row=16, column=3)

    label_random = tkinter.Label(input_window, bg = "White", width=30, height=2)
    label_random.grid(row=17, column=3)

    #Charity checkbutton
    charity_button = tkinter.Checkbutton(input_window, bg="White", variable=charity_click)
    charity_button.configure(text="donated to charity.", width=30, anchor="w")
    charity_button.configure(command=charity_command)
    charity_button.grid(row=15, column=1)

    #Debt checkbutton
    debt_button = tkinter.Checkbutton(input_window, bg="White", variable=debt_click)
    debt_button.configure(text="payed off your student debt.", width=30, anchor="w")
    debt_button.configure(command=debt_command)
    debt_button.grid(row=16, column=1)

    #Savings checkbutton
    savings_button = tkinter.Checkbutton(input_window, bg="White", variable=savings_click)
    savings_button.configure(text="invested in your savings account.", width=30, anchor="w")
    savings_button.configure(command=savings_command)
    savings_button.grid(row=17, column=1)  

    empty_label(input_window, 18, 1)
    empty_label(input_window, 19, 1)

    #Creates income entry label
    income_label = tkinter.Label(input_window, width=30, anchor="e", bg="White")
    income_label.configure(text="Enter your income (CAD):")
    income_label.grid(row=20, column=1)

    #Creates income entry
    input_income = tkinter.Entry(input_window, bg = "White", width=30)
    input_income.grid(row=20, column=2)

    #Creates calculate button
    calculate_button = tkinter.Button(input_window, text="Calculate", anchor="w")
    calculate_button.configure(command = calculate_click)
    calculate_button.grid(row = 20, column = 3)

    #Useful when configuring to say "INVALID"
    message_calculate = tkinter.Label(input_window, text="", anchor="center", bg="White")
    message_calculate.grid(row=21, column=2)

    empty_label(output_window, 0, 0)
    empty_label(output_window, 0, 2)
    empty_label(output_window, 0, 4)

    #Output labels are created in output_window frame
    output_label("Gross Income:", 1, 3)
    output_label("Net Income (Pre-Deduction):", 2, 3)
    output_label("Net Income:", 3, 3)
    output_label("Tax (Pre-Deduction):", 4, 3)
    output_label("Tax:", 5, 3)
    output_label("Deducted:", 6, 3)
    
    #Outputs gross income when configured
    gross_label = tkinter.Label(output_window, width=30, anchor="w", bg="White", text="$ 0.00")
    gross_label.configure(font="bold")
    gross_label.grid(row=1, column=5)

    #Outputs net income pre-deduction when configured
    net_pre = tkinter.Label(output_window, width=30, anchor="w", bg="White", text="$ 0.00")
    net_pre.configure(font="bold")
    net_pre.grid(row=2, column=5)

    #Outputs net income post-deduction when configured
    net_post = tkinter.Label(output_window, width=30, anchor="w", bg="White", text="$ 0.00")
    net_post.configure(font="bold")
    net_post.grid(row=3, column=5)

    #Outputs tax pre-deduction when configured
    tax_pre = tkinter.Label(output_window, width=30, anchor="w", bg="White", text="$ 0.00")
    tax_pre.configure(font="bold")
    tax_pre.grid(row=4, column=5)

    #Outputs tax post-deduction when configured
    tax_post = tkinter.Label(output_window, width=30, anchor="w", bg="White", text="$ 0.00")
    tax_post.configure(font="bold")
    tax_post.grid(row=5, column=5)

    #Outputs total tax deduction when configured
    deduction_label = tkinter.Label(output_window, width=30, anchor="w", bg="White", text="$ 0.00")
    deduction_label.configure(font="bold")
    deduction_label.grid(row=6, column=5)
    
    window.mainloop()

main()
