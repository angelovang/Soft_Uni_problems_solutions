from tkinter import *
import random
import time
import datetime
from tkinter import messagebox
import tkinter as t
import pymysql as p


def homepage():
    root = t.Tk()  # creating a  window
    root.title("home_page")  # title name in window

    root.geometry('1920x1080')  # creating the size of the window
    root.configure(background="lawn green")
    t1 = t.Label(root, text="Welcome", font=("Bradley Hand ITC", 50, "bold"), bg="lawn green",
                 fg="black")  # creating the text
    t1.place(x=580, y=120)  # placing the txt

    t1 = t.Label(root, text="To", font=("Bradley Hand ITC", 50, "bold"), bg="lawn green",
                 fg="black")  # creating the text
    t1.place(x=680, y=220)

    t1 = t.Label(root, text="The Cafe Managment System", font=("Bradley Hand ITC", 50, "bold"), bg="lawn green",
                 fg="black")  # creating the text
    t1.place(x=320, y=320)
    b2 = t.Button(root, text="Click here to login or sign up", font=("FZshuTi", 25), width=30, bg="gold1", fg="black",
                  command=emp)
    b2.place(x=450, y=550)
    root.mainloop()


def emp():
    root = t.Tk()  # creating a windo
    root.title("employ login_page")  # title name in window
    root.geometry('1920x1080')  # creating the size of the window
    root.configure(background="lawn green")
    t1 = t.Label(root, text="Employee Service", font=("FZshuTi", 50), bg="gold", fg="black",
                 width=40)  # creating the text
    t1.place(x=0, y=50)  # placing the txt

    t1 = t.Label(root, text="Please select whether login or sign-up:-", font=("Segoe UI", 25), bg="lawn green",
                 fg="black", width=40)  # creating the text
    t1.place(x=400, y=350)

    b2 = t.Button(root, text="Login", font=("Gill Sans MT", 25), width=12, bg="Black", fg="White", command=login)
    b2.place(x=460, y=500)
    b1 = t.Button(root, text="Sign Up", font=("Gill Sans MT", 25), width=12, bg="Black", fg="White", command=signup)
    b1.place(x=860, y=500)


def signup():
    root = t.Tk()  # creating a window
    root.title("Registration_page")  # title name in window
    root.geometry('1920x1080')  # creating the size of the window
    root.configure(background="lawn green")
    t1 = t.Label(root, text="Signup", font=("FZshuTi", 40), bg="gold", width=50,
                 fg="Black")  # creating the text
    t1.place(x=0, y=50)  # placing the txt

    u1 = t.Label(root, text="Username:", font=("Gill Sans MT", 20), bg="lawn green")  # creating the text
    u1.place(x=500, y=200)  # placing the text
    # Username textbox
    global ue1
    ue1 = t.Entry(root, font=("bold", 15), width=25)  # creating the text box
    ue1.place(x=700, y=200)

    # password label
    p1 = t.Label(root, text="Password:", font=("Gill Sans MT", 20), bg="lawn green")
    p1.place(x=500, y=250)
    global u2
    u2 = t.Entry(root, font=("bold", 15), show='*', width=25)  # creating the text box for password
    u2.place(x=700, y=250)

    # retype pwd label
    i1 = t.Label(root, text="Retype-pwd:", font=("Gill Sans MT", 20), bg="lawn green")
    i1.place(x=500, y=300)
    # retype pass textbox
    global i2
    i2 = t.Entry(root, font=("bold", 15), show='*', width=25)
    i2.place(x=700, y=300)

    # email label
    i3 = t.Label(root, text="Email:", font=("Gill Sans MT", 20), bg="lawn green")
    i3.place(x=500, y=350)
    # email textbox
    global i4
    i4 = t.Entry(root, font=("bold", 15), width=25)
    i4.place(x=700, y=350)

    # Gender label
    i5 = t.Label(root, text="Gender:", font=("Gill Sans MT", 20), bg="lawn green")
    i5.place(x=500, y=400)
    # gender radiobutton
    global ge1
    ge1 = t.IntVar()
    m = t.Radiobutton(root, text="Male", font=(15), value=1, variable=ge1, width=10, bg="lawn green", fg="Black")
    m.place(x=700, y=405)
    global f
    f = t.Radiobutton(root, text="female", font=(15), value=2, variable=ge1, width=10, bg="lawn green", fg="Black")
    f.place(x=800, y=405)

    i5 = t.Label(root, text="Mobileno:", font=("Gill Sans MT", 20), bg="lawn green")
    i5.place(x=500, y=450)
    global m1
    m1 = t.Entry(root, font=("bold", 15), width=25)
    m1.place(x=700, y=450)

    # creating submit button
    b2 = t.Button(root, text="Submit", font=("Gill Sans MT", 25), width=10, bg="Black", fg="White", command=insert_reg)
    b2.place(x=520, y=600)
    b2 = t.Button(root, text="Back", font=("Gill Sans MT", 25), width=10, bg="Black", fg="White", command=emp)
    b2.place(x=780, y=600)
    root.mainloop()


def insert_reg():
    # capturing the data
    uname = str(ue1.get())
    pwd = str(u2.get())
    rpwd = str(i2.get())
    email = str(i4.get())
    gen = str(ge1.get())
    mobile = int(m1.get())

    if (pwd == rpwd):
        try:
            print("11")
            connection = p.connect(host='localhost', db='project', user='root', password='1234')
            s = connection.cursor()
            print("1")
            sql = "insert into register(name,pwd,email,gender,mobile) values('%s','%s','%s','%s','%s')" % (
            uname, pwd, email, gen, mobile)
            i = s.execute(sql)
            connection.commit()
            if (i == 1):
                login()
            else:
                print("data is not inserted")
                signup()
        except Exception:
            print(Exception.args())

    else:
        print("wrong password")


def login():
    root1 = t.Tk()  # creating a window
    root1.title("Loginpage")  # title name in window
    root1.geometry('1920x1080')  # creating the size of the window
    root1.configure(background="lawn green")
    t1 = t.Label(root1, text="Login to continue:", font=("FZshuTi", 40), width=50, bg="gold",
                 fg="Black")  # creating the text
    t1.place(x=0, y=50)  # placing the txt

    u1 = t.Label(root1, text="Username:", font=("Gill Sans MT", 30), bg="lawn green")  # creating the text
    u1.place(x=520, y=250)  # placing the text

    # Username textbox
    global ul1
    ul1 = t.Entry(root1, font=("bold", 20), width=30)  # creating the text box
    ul1.place(x=710, y=268)

    # password label
    p1 = t.Label(root1, text="Password:", font=("Gill Sans MT", 30), bg="lawn green")
    p1.place(x=520, y=350)
    global lp
    lp = t.Entry(root1, font=("bold", 20), show='*', width=30)  # creating the text box for password
    lp.place(x=710, y=368)

    global b2
    # creating login button
    b2 = t.Button(root1, text="Login", font=("Gill Sans MT", 28), width=10, bg="Black", fg="White", command=uloginvalid)
    b2.place(x=520, y=500)
    b2 = t.Button(root1, text="Back", font=("Gill Sans MT", 28), width=10, bg="Black", fg="White", command=emp)
    b2.place(x=780, y=500)
    root1.mainloop()


def uloginvalid():
    user = str(ul1.get())
    print(user)

    pwd = str(lp.get())
    print(pwd)
    try:
        print("11")
        connection = p.connect(host='localhost', db='project', user='root', password='1234')
        s = connection.cursor()

        sql = "select * from register where name='" + user + "' and pwd='" + pwd + "'"
        i = s.execute(sql)
        connection.commit()
        print(i)
        if (i == 1):
            mainy()

        else:
            med()
            login()

    except Exception:
        print(Exception.args())


def med():
    med = messagebox.showinfo('Sorry', 'Wrong Username and Password')


def mainy():
    root = t.Tk()
    root.geometry("1920x1080")
    root.title("Cafe Management System")
    root.configure(background="SteelBlue2")

    Tops = Frame(root, width=1350, height=100, bd=8, relief="raise")
    Tops.pack(side=TOP)

    f1 = Frame(root)
    f1.pack(side=LEFT)

    f2 = Frame(root)
    f2.pack(side=RIGHT)

    f1a = Frame(f1)
    f1a.pack(side=TOP)

    f2a = Frame(f1)
    f2a.pack(side=BOTTOM)

    ft2 = Frame(f2)
    ft2.pack(side=TOP)
    fb2 = Frame(f2)
    fb2.pack(side=BOTTOM)

    f1aa = Frame(f1a)
    f1aa.pack(side=LEFT)
    f1ab = Frame(f1a)
    f1ab.pack(side=RIGHT)

    f2aa = Frame(f2a)
    f2aa.pack(side=LEFT)

    f2ab = Frame(f2a)
    f2ab.pack(side=RIGHT)

    Tops.configure(background='olivedrab1')
    f1.configure(background='olivedrab1')
    f2.configure(background='olivedrab1')

    lblInfo = Label(Tops, font=("Showcard Gothic", 40), text=" \t Sit Read & Drink Cafe \t\t", bd=40, bg="hot pink")
    lblInfo.grid(row=0, column=0)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BUTTONS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    btnReceipt = t.Button(root, padx=16, pady=1, bd=4, bg="olivedrab1", fg="green", font=('arial', 8, 'bold'), width=5,
                          text="Receipt", command=Receipt)
    btnReceipt.place(x="1200", y="750")
    btnReset = t.Button(root, padx=16, pady=1, bd=4, bg="olivedrab1", fg="green", font=('arial', 8, 'bold'), width=5,
                        text="Reset", command=reset)
    btnReset.place(x="1300", y="750")
    btnExit = t.Button(root, padx=16, pady=1, bd=4, bg="olivedrab1", fg="green", font=('arial', 8, 'bold'), width=5,
                       text="LogOut", command=qExit)
    btnExit.place(x="1400", y="750")
    global txtReceipt
    txtReceipt = Text(root, height=35, width=57)
    txtReceipt.pack()

    txtReceipt.place(x="1050", y="170")
    x = random.randint(10908, 500876)

    randomRef = str(x)

    txtReceipt.insert(END, "\t\t\tBILLno." + randomRef)
    txtReceipt.insert(END, "\t\t\t\t\t\t\t\tSit Read & Drink Cafe")

    txtReceipt.insert(END, "\t\t\t\t\tItems:\t\tQuantity\t\tPrice:\n")

    lblReceipt = Label(root, font=('arial', 12, 'bold'), text="Receipt", bd=2)
    lblReceipt.place(x="1250", y="150")

    global var1
    global var2
    global var3
    global var4
    global var5
    global var6
    global var7
    global var8
    global var9
    global var10
    global var11
    global var12
    global var13
    global var14
    global var15
    global var16

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    var13 = IntVar()
    var14 = IntVar()
    var15 = IntVar()
    var16 = IntVar()

    Receipt_Ref = StringVar()
    PaidTax = StringVar()
    SubTotal = StringVar()
    TotalCost = StringVar()
    ServiceCharge = StringVar()

    global E_Tea
    global E_Espresso
    global E_Iced_Tea
    global E_Simple_Coffee
    global E_Cappuccino
    global E_Fullcream_Coffee
    global E_American_Coffee
    global E_Iced_Cappuccino
    global E_Coffee_Cake
    global E_Red_Velvet_Cake
    global E_Black_Forest_Cake
    global E_Cream_Cake
    global E_White_Chocolate_Cake
    global E_Sweet_Strawberry_Cake
    global E_Black_Chocolate_Cake
    global E_Simple_Cake

    E_Tea = IntVar()
    E_Espresso = IntVar()
    E_Iced_Tea = IntVar()
    E_Simple_Coffee = IntVar()
    E_Cappuccino = IntVar()
    E_Fullcream_Coffee = IntVar()
    E_American_Coffee = IntVar()
    E_Iced_Cappuccino = IntVar()

    E_Coffee_Cake = IntVar()
    E_Red_Velvet_Cake = IntVar()
    E_Black_Forest_Cake = IntVar()
    E_Cream_Cake = IntVar()
    E_White_Chocolate_Cake = IntVar()
    E_Sweet_Strawberry_Cake = IntVar()
    E_Black_Chocolate_Cake = IntVar()
    E_Simple_Cake = IntVar()

    Tea = t.Label(root, text="Tea \t\t\t", font=('arial', 15), bg="lawn green")
    Tea.place(x="100", y="300")
    Espresso = t.Label(root, text="Espresso \t\t \t", font=('arial', 15), bg="hot pink")
    Espresso.place(x="100", y="350")
    Iced_Tea = t.Label(root, text="Iced Tea \t\t\t ", font=('arial', 15), bg="lawn green")
    Iced_Tea.place(x="100", y="400")
    Simple_Coffee = t.Label(root, text="Simple_Coffee  \t\t ", font=('arial', 15), bg="hot pink")
    Simple_Coffee.place(x="100", y="450")
    Cappuccino = t.Label(root, text="Cappuccino \t\t ", font=('arial', 15), bg="lawn green")
    Cappuccino.place(x="100", y="500")
    Fullcream_Coffee = t.Label(root, text="Fullcream Coffee \t\t ", font=('arial', 15), bg="hot pink")
    Fullcream_Coffee.place(x="100", y="550")
    American_Coffee = t.Label(root, text="American Coffee \t\t", font=('arial', 15), bg="lawn green")
    American_Coffee.place(x="100", y="600")
    Iced_Cappuccino = t.Label(root, text="Iced Cappuccino \t\t ", font=('arial', 15), bg="hot pink")
    Iced_Cappuccino.place(x="100", y="650")

    Coffee_Cake = t.Label(root, text="Coffee Cake\t\t", font=('arial', 15), bg="hot pink")
    Coffee_Cake.place(x="400", y="300")
    Red_Velvet_Cake = t.Label(root, text="Red Velvet Cake\t\t", font=('arial', 15), bg="lawn green")
    Red_Velvet_Cake.place(x="400", y="350")
    Black_Forest_Cake = t.Label(root, text="Black Forest Cake\t\t", font=('arial', 15), bg="hot pink")
    Black_Forest_Cake.place(x="400", y="400")
    Cream_Cake = t.Label(root, text="Cream Cake\t\t", font=('arial', 15), bg="lawn green")
    Cream_Cake.place(x="400", y="450")
    White_Chocolate_Cake = t.Label(root, text="White Chocolate Cake\t", font=('arial', 14), bg="hot pink")
    White_Chocolate_Cake.place(x="400", y="500")
    Sweet_Strawberry_Cake = t.Label(root, text="Sweet Strawberry Cake\t", font=('arial', 14), bg="lawn green")
    Sweet_Strawberry_Cake.place(x="400", y="550")
    Black_Chocolate_Cake = t.Label(root, text="Black Chocolate Cake\t", font=('arial', 15), bg="hot pink")
    Black_Chocolate_Cake.place(x="400", y="600")
    Simple_Cake = t.Label(root, text="Simple Cake\t\t", font=('arial', 15), bg="lawn green")
    Simple_Cake.place(x="400", y="650")

    txtTea = Entry(master=root, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_Tea,
                   state=NORMAL)
    txtTea.place(x="300", y="290")
    E_Tea = txtTea
    txtEspresso = Entry(master=root, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_Espresso,
                        state=NORMAL)
    txtEspresso.place(x="300", y="340")
    E_Espresso = txtEspresso
    txtIced_Tea = Entry(master=root, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_Iced_Tea,
                        state=NORMAL)
    txtIced_Tea.place(x="300", y="390")
    E_Iced_Tea = txtIced_Tea
    txtSimple_Coffee = Entry(master=root, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                             textvariable=E_Simple_Coffee, state=NORMAL)
    txtSimple_Coffee.place(x="300", y="440")
    E_Simple_Coffee = txtSimple_Coffee
    txtCappuccino = Entry(master=root, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                          textvariable=E_Cappuccino, state=NORMAL)
    txtCappuccino.place(x="300", y="490")
    E_Cappuccino = txtCappuccino
    txtFullcream_Coffee = Entry(master=root, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                                textvariable=E_Fullcream_Coffee, state=NORMAL)
    txtFullcream_Coffee.place(x="300", y="540")
    E_Fullcream_Coffee = txtFullcream_Coffee
    txtAmerican_Coffee = Entry(master=root, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                               textvariable=E_American_Coffee, state=NORMAL)
    txtAmerican_Coffee.place(x="300", y="590")
    E_American_Coffee = txtAmerican_Coffee
    txtIced_Cappuccino = Entry(master=root, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                               textvariable=E_Iced_Cappuccino, state=NORMAL)
    txtIced_Cappuccino.place(x="300", y="640")
    E_Iced_Cappuccino = txtIced_Cappuccino
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Enter widget for CAKES<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    txtCoffee_Cake = Entry(master=root, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                           textvariable=E_Coffee_Cake, state=NORMAL)
    txtCoffee_Cake.place(x="600", y="290")
    E_Coffee_Cake = txtCoffee_Cake
    txtRed_Velvet_Cake = Entry(master=root, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                               textvariable=E_Red_Velvet_Cake, state=NORMAL)
    txtRed_Velvet_Cake.place(x="600", y="340")
    E_Red_Velvet_Cake = txtRed_Velvet_Cake
    txtBlack_Forest_Cake = Entry(master=root, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                                 textvariable=E_Black_Forest_Cake, state=NORMAL)
    txtBlack_Forest_Cake.place(x="600", y="390")
    E_Black_Forest_Cake = txtBlack_Forest_Cake
    txtCream_Cake = Entry(master=root, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                          textvariable=E_Cream_Cake, state=NORMAL)
    txtCream_Cake.place(x="600", y="440")
    E_Cream_Cake = txtCream_Cake
    txtWhite_Chocolate_Cake = Entry(master=root, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                                    textvariable=E_White_Chocolate_Cake, state=NORMAL)
    txtWhite_Chocolate_Cake.place(x="600", y="490")
    E_White_Chocolate_Cake = txtWhite_Chocolate_Cake
    txtSweet_Strawberry_Cake = Entry(master=root, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                                     textvariable=E_Sweet_Strawberry_Cake, state=NORMAL)
    txtSweet_Strawberry_Cake.place(x="600", y="540")
    E_Sweet_Strawberry = txtSweet_Strawberry_Cake
    txtBlack_Chocolate_Cake = Entry(master=root, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                                    textvariable=E_Black_Chocolate_Cake, state=NORMAL)
    txtBlack_Chocolate_Cake.place(x="600", y="590")
    E_Black_Chocolate_Cake = txtBlack_Chocolate_Cake
    txtSimple_Cake = Entry(master=root, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                           textvariable=E_Simple_Cake, state=NORMAL)
    txtSimple_Cake.place(x="600", y="640")
    E_Simple_Cake = txtSimple_Cake

    root.mainloop()


def Receipt():
    Item1 = float(E_Tea.get())
    print(Item1)
    Item2 = float(E_Espresso.get())
    Item3 = float(E_Iced_Tea.get())
    Item4 = float(E_Simple_Coffee.get())
    Item5 = float(E_Cappuccino.get())
    Item6 = float(E_Fullcream_Coffee.get())
    Item7 = float(E_American_Coffee.get())
    Item8 = float(E_Iced_Cappuccino.get())
    Item9 = float(E_Coffee_Cake.get())
    Item10 = float(E_Red_Velvet_Cake.get())
    Item11 = float(E_Black_Forest_Cake.get())
    Item12 = float(E_Cream_Cake.get())
    Item13 = float(E_White_Chocolate_Cake.get())
    Item14 = float(E_Sweet_Strawberry_Cake.get())
    Item15 = float(E_Black_Chocolate_Cake.get())
    Item16 = float(E_Simple_Cake.get())

    PriceofDrinks = (Item1 * 10) + (Item2 * 50) + (Item3 * 30) + (Item4 * 35) + (Item5 * 60) + (Item6 * 90) + (
                Item7 * 70) + (Item8 * 80)
    PriceofCakes = (Item9 * 50) + (Item10 * 70) + (Item11 * 50) + (Item12 * 60) + (Item13 * 69.9) + (Item14 * 40) + (
                Item15 * 20) + (Item16 * 30)

    DrinksPrice = " ₹" + str('%.2f' % (PriceofDrinks))
    CakesPrice = " ₹" + str('%.2f' % (PriceofCakes))

    SC = " ₹" + str('%.2f' % (11.3))

    SubTotalofITEMS = " ₹" + str('%.2f' % (PriceofDrinks + PriceofCakes + 11.3))

    Tax = " ₹" + str('%.2f' % ((PriceofDrinks + PriceofCakes + 11.3) * 0.15))

    TT = ((PriceofDrinks + PriceofCakes + 11.3) * 0.15)
    TC = "₹" + str('%.2f' % (PriceofDrinks + PriceofCakes + 11.3 + TT))

    if int(E_Tea.get()) > 0:
        print("data is inserting")
        txtReceipt.insert(END, "Tea:\t\t\t" + str(E_Tea.get()) + "\t" + str('₹%.2f' % (float(E_Tea.get()) * 10)) + "\n")
    if int(E_Espresso.get()) > 0:
        txtReceipt.insert(END, "Espresso:\t\t\t" + str(E_Espresso.get()) + "\t" + str(
            '₹%.2f' % (float(E_Espresso.get()) * 50)) + '\n')
    if int(E_Iced_Tea.get()) > 0:
        txtReceipt.insert(END, "Iced Tea:\t\t\t" + str(E_Iced_Tea.get()) + "\t" + str(
            '₹%.2f' % (float(E_Iced_Tea.get()) * 30)) + '\n')
    if int(E_Simple_Coffee.get()) > 0:
        txtReceipt.insert(END, "Simple Coffee:\t\t\t" + str(E_Simple_Coffee.get()) + "\t" + str(
            '₹%.2f' % (float(E_Simple_Coffee.get()) * 35)) + '\n')
    if int(E_Cappuccino.get()) > 0:
        txtReceipt.insert(END, "Cappuccino:\t\t\t" + str(E_Cappuccino.get()) + "\t" + str(
            '₹%.2f' % (float(E_Cappuccino.get()) * 60)) + '\n')
    if int(E_Fullcream_Coffee.get()) > 0:
        txtReceipt.insert(END, "Fullcream Coffee:\t\t\t" + str(E_Fullcream_Coffee.get()) + "\t" + str(
            '₹%.2f' % (float(E_Fullcream_Coffee.get()) * 90)) + '\n')
    if int(E_American_Coffee.get()) > 0:
        txtReceipt.insert(END, "American Coffee:\t\t\t" + str(E_American_Coffee.get()) + "\t" + str(
            '₹%.2f' % (float(E_American_Coffee.get()) * 70)) + '\n')
    if int(E_Iced_Cappuccino.get()) > 0:
        txtReceipt.insert(END, "Iced Cappuccino:\t\t\t" + str(E_Iced_Cappuccino.get()) + "\t" + str(
            '₹%.2f' % (float(E_Iced_Cappuccino.get()) * 80)) + '\n')
    if int(E_Coffee_Cake.get()) > 0:
        txtReceipt.insert(END, "Coffee Cake:\t\t\t" + str(E_Coffee_Cake.get()) + "\t" + str(
            '₹%.2f' % (float(E_Coffee_Cake.get()) * 50)) + '\n')
    if int(E_Red_Velvet_Cake.get()) > 0:
        txtReceipt.insert(END, "Red Velvet Cake:\t\t\t" + str(E_Red_Velvet_Cake.get()) + "\t" + str(
            '₹%.2f' % (float(E_Red_Velvet_Cake.get()) * 70)) + '\n')
    if int(E_Black_Forest_Cake.get()) > 0:
        txtReceipt.insert(END, "Black Forest Cake:\t\t\t" + str(E_Black_Forest_Cake.get()) + "\t" + str(
            '₹%.2f' % (float(E_Black_Forest_Cake.get()) * 50)) + '\n')
    if int(E_Cream_Cake.get()) > 0:
        txtReceipt.insert(END, "Cream Cake:\t\t\t" + str(E_Cream_Cake.get()) + "\t" + str(
            '₹%.2f' % (float(E_Cream_Cake.get()) * 60)) + '\n')
    if int(E_White_Chocolate_Cake.get()) > 0:
        txtReceipt.insert(END, "White Chocolate Cake:\t\t" + str(E_White_Chocolate_Cake.get()) + "\t\t" + str(
            '₹%.2f' % (float(E_White_Chocolate_Cake.get()) * 69.9)) + '\n')
    if int(E_Sweet_Strawberry_Cake.get()) > 0:
        txtReceipt.insert(END, "Sweet Strawberry Cake:\t\t" + str(E_Sweet_Strawberry_Cake.get()) + "\t\t" + str(
            '₹%.2f' % (float(E_Sweet_Strawberry_Cake.get()) * 40)) + '\n')
    if int(E_Black_Chocolate_Cake.get()) > 0:
        txtReceipt.insert(END, "Black Chocolate Cake:\t\t" + str(E_Black_Chocolate_Cake.get()) + "\t\t" + str(
            '₹%.2f' % (float(E_Black_Chocolate_Cake.get()) * 20)) + '\n')
    if int(E_Simple_Cake.get()) > 0:
        txtReceipt.insert(END, "Simple Cake:\t\t\t" + str(E_Simple_Cake.get()) + "\t" + str(
            '₹%.2f' % (float(E_Simple_Cake.get()) * 30)) + '\n\n')
    txtReceipt.insert(END, "---------------------------------------------------------")
    txtReceipt.insert(END, "Total Cost:\t" + SubTotalofITEMS + "\n")
    txtReceipt.insert(END, "Tax Paid:\t" + Tax + "\n")
    txtReceipt.insert(END, 'Service Charge:\t' + SC + "\n")
    txtReceipt.insert(END, "SubTotal:\t" + TC + "\n")
    txtReceipt.insert(END, "\n\n\n\n\n\t\tTHANKYOU FOR SHOPPING!\n\t\tPlease visit again ")


def qExit():
    qExit = messagebox.askyesno("Log Out?", "Do you want to Logout of this account?")
    if qExit > 0:
        emp()


def reset():
    txtReceipt.delete("1.0", END)

    E_Tea.setvar("0")
    E_Espresso.setvar("0")
    E_Iced_Tea.setvar("0")
    E_Simple_Coffee.setvar("0")
    E_Cappuccino.setvar("0")
    E_Fullcream_Coffee.setvar("0")
    E_American_Coffee.setvar("0")
    E_Iced_Cappuccino.setvar("0")
    E_Coffee_Cake.setvar("0")
    E_Red_Velvet_Cake.setvar("0")
    E_Black_Forest_Cake.setvar("0")
    E_Cream_Cake.setvar("0")
    E_White_Chocolate_Cake.setvar("0")
    E_Sweet_Strawberry_Cake.set("0")
    E_Black_Chocolate_Cake.setvar("0")
    E_Simple_Cake.setvar("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    txtReceipt.place(x="1050", y="170")
    x = random.randint(10908, 500876)
    x = x + 1
    randomRef = str(x)
    txtReceipt.insert(END, "\t\t\tBILLno." + randomRef)
    txtReceipt.insert(END, "\t\t\t\t\t\t\t\tSit Read & Drink Cafe")

    txtReceipt.insert(END, "\t\t\t\t\tItems:\t\tQuantity\t\tPrice:\n")
    txtReceipt.insert(END, "---------------------------------------------------------")