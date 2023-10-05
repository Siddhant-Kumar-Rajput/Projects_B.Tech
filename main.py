from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MsgBox
import mysql.connector as mysql

def Login():
    log_in = e_log.get()
    password = e_pas.get()

#in case of empty text field

    if (log_in == "" or password == ""):
        MsgBox.showinfo("LogIn Status", "All fields are required")
        e_log.delete(0, 'end')
        e_pas.delete(0, 'end')
    else:
        con = mysql.connect(host='localhost', user="root", password="YOURPASSWORD", database="python_tkinter")
        cursor = con.cursor()
        sql = "select * from login_data where log = %s and pas = %s"
        cursor.execute(sql, [log_in, password])
        result = cursor.fetchall()
        if result:
            MsgBox.showinfo("", "Login Success")
            base.destroy()
            page2()
            return True

        else:
            MsgBox.showinfo("", "Incorrect LoginId or Password")
            return False

def page2():
    root = Tk()
    root.geometry("600x300")
    root.title("Sport Event Participation List")

    heading = Label(root, text='Details Menu', font=('Bold', 30))
    heading.place(x=30, y=5)

    StdID = Label(root, text='Student ID', font=('Bold', 10))
    StdID.place(x=30, y=60)
    e_StdID = Entry()
    e_StdID.place(x=150, y=60)

    StdName = Label(root, text='Name', font=('Bold', 10))
    StdName.place(x=30, y=90)
    e_StdName = Entry()
    e_StdName.place(x=150, y=90)

    Team = Label(root, text='Team Name', font=('Bold', 10))
    Team.place(x=30, y=120)
    e_Team = Entry()
    e_Team.place(x=150, y=120)

    def insert():
        StdID = e_StdID.get()
        StdName = e_StdName.get()
        Team = e_Team.get()

        if (StdID == "" or StdName == "" or Team == ""):
            MsgBox.showinfo("Insert Status", "All fields are required")
        else:
            con = mysql.connect(host='localhost', user="root", password="YOURPASSWORD", database="python_tkinter")
            cursor = con.cursor()
            cursor.execute("insert into student_details values('" + StdID + "','" + StdName + "','" + Team + "')")
            cursor.execute("commit")

            e_StdID.delete(0, 'end')
            e_StdName.delete(0, 'end')
            e_Team.delete(0, 'end')

            show()

            MsgBox.showinfo("Insert Status", "Insert Successful")
            con.close()

    def delete():
        if (e_StdID.get() == ""):
            MsgBox.showinfo("Delete Status", "Student ID is Mandatory")
        else:
            con = mysql.connect(host='localhost', user="root", password="YOURPASSWORD", database="python_tkinter")
            cursor = con.cursor()
            cursor.execute("delete from student_details where StdID='" + e_StdID.get() + "' ")
            cursor.execute("commit")

            e_StdID.delete(0, 'end')
            e_StdName.delete(0, 'end')
            e_Team.delete(0, 'end')

            show()

            MsgBox.showinfo("Delete Status", "Delete Successful")
            con.close()

    def update():
        StdID = e_StdID.get()
        StdName = e_StdName.get()
        Team = e_Team.get()

        if (StdID == "" or StdName == "" or Team == ""):
            MsgBox.showinfo("Update Status", "All fields are required")
        else:
            con = mysql.connect(host='localhost', user="root", password="YOURPASSWORD", database="python_tkinter")
            cursor = con.cursor()
            cursor.execute("update student_details set StdName= '" + StdName + "' , Team='" + Team + "' where StdID='" + StdID + "' ")
            cursor.execute("commit")

            e_StdID.delete(0, 'end')
            e_StdName.delete(0, 'end')
            e_Team.delete(0, 'end')

            show()

            MsgBox.showinfo("Update Status", "Update Successful")
            con.close()

    def get():
        if (e_StdID.get() == ""):
            MsgBox.showinfo("Fetch Status", "Student ID is Mandatory")
        else:
            con = mysql.connect(host='localhost', user="root", password="YOURPASSWORD", database="python_tkinter")
            cursor = con.cursor()
            cursor.execute("select * from student_details where StdID='" + e_StdID.get() + "' ")
            rows = cursor.fetchall()

            for row in rows:
                e_StdName.insert(0, row[1])
                e_Team.insert(0, row[2])

            MsgBox.showinfo("Fetch Status", "Fetch Successful")
            con.close()

    def show():
        con = mysql.connect(host='localhost', user="root", password="YOURPASSWORD", database="python_tkinter")
        cursor = con.cursor()
        cursor.execute("select * from student_details")
        rows = cursor.fetchall()
        box.delete(0, box.size())

        for row in rows:
            insertData = str(row[0]) + '         ' + row[1] + '         ' + str(row[2])
            box.insert(box.size() + 1, insertData)

        con.close()

    b1 = ttk.Button(root, text='Insert', command=insert)
    b1.place(x=30, y=160)

    b2 = ttk.Button(root, text='Delete', command=delete)
    b2.place(x=110, y=160)

    b3 = ttk.Button(root, text='Update', command=update)
    b3.place(x=190, y=160)

    b4 = ttk.Button(root, text='Get', command=get)
    b4.place(x=270, y=160)

    box = Listbox(root)
    box.place(x=370, y=50)
    show()

    root.mainloop()


base = Tk()
base.geometry("600x300")
base.title("Login Page")

heading = Label(base, text='Login page', font=('Bold', 40))
heading.place(x=160, y=10)

log = Label(base, text='Login Id', font=('Bold', 10))
log.place(x=180, y=100)
e_log = Entry()
e_log.place(x=280, y=100)

pas = Label(base, text='Password', font=('Bold', 10))
pas.place(x=180, y=130)
e_pas = Entry()
e_pas.place(x=280, y=130)
e_pas.config(show="*")

click = ttk.Button(base, text='Login', command=Login)
click.place(x=280, y=160)

base.mainloop()