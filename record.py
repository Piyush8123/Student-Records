from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.tix import *
from tkinter.messagebox import *
import json
import os
from PIL import Image, ImageTk


def allocatecourse():
    stu = {}
    cid = ''
    stu['Stu_Course'] = list()
    stuid = e10.get()
    print(stuid)
    coursename = e11.get()
    with open("Course.json") as f:
        cr = json.load(f)
    for i in cr['Courses']:
        if i['CourseName'] == coursename:
            cid = i['CourseID']
    print(cid)
    if stuid not in uniq_rollno:
        showinfo('ERROR-ROLLNO', 'This Rollno does not exist')
        print(uniq_rollno)
    else:
        student['Rollno'] = stuid
        student['CourseID'] = cid
        if os.path.isfile("Allocation.json"):
            with open('Allocation.json', 'r') as f:
                stu = json.load(f)
            stu['Stu_Course'].append(student)
            with open('Allocation.json', 'w') as f:
                json.dump(stu, f)
        else:
            with open('Allocation.json', 'w') as f:
                stu['Stu_Course'] = []
                stu['Stu_Course'].append(student)
                json.dump(stu, f)

        showinfo('Save', 'The course has been Allocated')
        e10.delete(0, END)
        e11.delete(0, END)


def load():
    global treev
    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=1, bd=1, font=('Calibri', 11))
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

    treev = ttk.Treeview(tab2, style="mystyle.Treeview", selectmode='browse')

    treev.pack(side='top', fill=X)

    verscrlbar = ttk.Scrollbar(tab2,
                               orient="vertical",
                               command=treev.yview)

    verscrlbar.pack(side='right')

    treev.configure(xscrollcommand=verscrlbar.set)

    treev["columns"] = ("Rollno", "Name", "Gender", "Address", "PhoneNo", "Batch", "Hostel")

    treev['show'] = 'headings'
    treev.column("#0", width=70, minwidth=70, stretch=NO, anchor=W)
    treev.column("Name", width=110, minwidth=110, stretch=NO, anchor=E)
    treev.column("Gender", width=110, minwidth=110, stretch=NO)
    treev.column("Address", width=110, minwidth=110, stretch=NO)
    treev.column("PhoneNo", width=110, minwidth=110, stretch=NO)
    treev.column("Batch", width=110, minwidth=110, stretch=NO)
    treev.column("Hostel", width=110, minwidth=110, stretch=NO, anchor='e')

    treev.heading("Rollno", text="Rollno ", anchor=W, command=lambda: loadStutree(treev))
    treev.heading("Name", text="Name   ", anchor=E)
    treev.heading("Gender", text="Gender ", anchor=W)
    treev.heading("Address", text="Address", anchor=W)
    treev.heading("PhoneNo", text="PhoneNo", anchor='w')
    treev.heading("Batch", text="Batch  ", anchor='w')
    treev.heading("Hostel", text="Hostel ", anchor='e')


def loadStutree(treev):
    if treev:
        for i in treev.get_children():
            treev.delete(i)
    stu = {}
    if os.path.isfile("Student.json"):
        with open('Student.json', 'r') as f:
            stu = json.load(f)
    else:
        stu = {"Students": [
            {"Rollno": '', "Name": '', "Gender": '', "Phone no": '', "address": '', 'Batch': '', 'Hostel': ''}]}
    for i in stu['Students']:
        treev.insert("", 'end', text="",
                     values=(i["Rollno"], i["Name"], i["Gender"], i['address'], i['Phone no'], i['Batch'], i['Hostel']))


def loadcourses():
    global treevc
    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=1, bd=0, font=('Calibri', 11))
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

    treevc = ttk.Treeview(tab4, style="mystyle.Treeview", selectmode='browse')
    treevc.pack(side=TOP)

    verscrlbar = ttk.Scrollbar(tab4,
                               orient="vertical",
                               command=treevc.yview)

    verscrlbar.pack(side='right')

    treevc.configure(xscrollcommand=verscrlbar.set)

    treevc["columns"] = ("CourseID", "CourseName")

    treevc['show'] = 'headings'
    treevc.column("#0", width=50, minwidth=50, stretch=NO, anchor=W)
    treevc.column("CourseName", width=200, minwidth=200, stretch=NO, anchor=E)

    treevc.heading("CourseID", text="CourseID ", anchor=W, command=lambda: loadCoutree(treevc))
    treevc.heading("CourseName", text="CourseName   ", anchor=E)


def loadCoutree(treevc):
    if treevc:
        for i in treevc.get_children():
            treevc.delete(i)
    course = {}
    if os.path.isfile("Course.json"):
        with open('Course.json', 'r') as f:
            course = json.load(f)
    else:
        course = {"Courses": [{"CourseID": '', "CourseName": ''}]}
    for i in course['Courses']:
        treevc.insert("", 'end', text="", values=(i["CourseID"], i["CourseName"]))


def savecourse():
    stu = {}
    stu['Courses'] = list()
    courseid = e7.get()
    coursename = e8.get()

    if courseid not in uniq_courseid:
        uniq_courseid.append(courseid)
        student['CourseID'] = courseid
        student['CourseName'] = coursename
        if os.path.isfile("Course.json"):
            with open('Course.json', 'r') as f:
                stu = json.load(f)
            stu['Courses'].append(student)
            with open('Course.json', 'w') as f:
                json.dump(stu, f)
        else:
            with open('Course.json', 'w') as f:
                stu['Courses'] = []
                stu['Courses'].append(student)
                json.dump(stu, f)

        showinfo('Save', 'Your record has been saved')
        e7.delete(0, END)
        e8.delete(0, END)


    else:
        showerror('Course ID error:', 'Course ID should be uniq\nThis CourseID has already been recorded')
        e7.delete(0, END)

def save():
    stu = {}
    stu['Students'] = list()
    name = e1.get()
    rollno = e2.get()
    gender = var.get()
    address = e4.get()
    phoneno = e5.get()
    batch = e6.get()
    hostel = var1.get()
    if rollno not in uniq_rollno:
        uniq_rollno.append(rollno)
        student['Rollno'] = rollno
        student['Name'] = name
        student['Gender'] = gender
        student['address'] = address
        student['Phone no'] = phoneno
        student['Batch'] = batch
        student['Hostel'] = hostel
        if os.path.isfile("Student.json"):
            with open('Student.json', 'r') as f:
                stu = json.load(f)
            stu['Students'].append(student)
            with open('Student.json', 'w') as f:
                json.dump(stu, f)
        else:
            with open('Student.json', 'w') as f:
                stu['Students'] = []
                stu['Students'].append(student)
                json.dump(stu, f)

        showinfo('Save', 'Your record has been saved')
        e1.delete(0, END)
        e2.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)

    else:
        showerror('Roll no error:', 'Roll no should be uniq\nThis roll no has already been recorded')
        e2.delete(0, END)


def clearcourse():
    e7.delete(0, END)
    e8.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
    e20.delete(0, END)
    e21.delete(0, END)
    e22.delete(0, END)
    e23.delete(0, END)
    e30.delete(0, END)


def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)


def remove(tip):
    tip.subwidget('label').forget()
    for index, sub in enumerate(tip.subwidgets_all()):
        if index > 0:
            sub.configure(bg='white')


def populate(event):
    global clist
    clist = []
    with open("Course.json") as f:
        cr = json.load(f)
    for i in cr['Courses']:
        clist.append(i['CourseName'])
    e11['values'] = tuple(clist)


def popular(event):
    global crlist
    crlist = []
    with open("Course.json") as f:
        cr = json.load(f)
    for i in cr['Courses']:
        crlist.append(i['CourseName'])
    e30['value'] = tuple(crlist)





def populaterollons():
    if os.path.isfile("Student.json"):
        with open('Student.json', 'r') as f:
            stu = json.load(f)
        for i in stu['Students']:
            uniq_rollno.append(i['Rollno'])


def populatecourses():
    if os.path.isfile("Course.json"):
        with open('Course.json', 'r') as f:
            stu = json.load(f)
        for i in stu['Courses']:
            uniq_courseid.append(i['CourseID'])
            uniq_coursename.append(i['CourseName'])



def loadmarks():
    global tree
    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=1, bd=0, font=('Calibri', 11))
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

    tree = ttk.Treeview(tab7, style="mystyle.Treeview", selectmode='browse')
    tree.pack(side=TOP)

    verscrlbar = ttk.Scrollbar(tab7,
                               orient="vertical",
                               command=tree.yview)

    verscrlbar.pack(side='right')

    tree.configure(xscrollcommand=verscrlbar.set)

    tree["columns"] = ("Student Name", "Course Name","Marks")

    tree['show'] = 'headings'
    tree.column("#0", width=50, minwidth=50, stretch=NO, anchor=W)
    tree.column("Course Name", width=200, minwidth=200, stretch=NO, anchor=E)
    tree.column("Marks", width=200, minwidth=200, stretch=NO, anchor=E)

    tree.heading("Student Name", text="Student Name ", anchor=W, command=lambda: loadMarktree(tree))
    tree.heading("Course Name", text="Course Name   ", anchor=E)
    tree.heading("Marks", text="Marks   ", anchor=E)

def loadMarktree(tree):
    if tree:
        for i in tree.get_children():
            tree.delete(i)
    score = {}
    if os.path.isfile("Marks.json"):
        with open('Marks.json', 'r') as f:
            score = json.load(f)
    else:
        score = {"Scores": [
            {"Student Name": '', "Course Name": '', "Marks": ''}]}
    for i in score['Scores']:
        tree.insert("", 'end', text="", values=(i["Student Name"], i["Course Name"], i["Marks"]))

def savemarks():
    stu = {}
    stu['Scores'] = list()
    studentid = e20.get()
    studentname = e21.get()
    coursename = e30.get()
    marks = e23.get()

    if studentid not in uniq_studentid:
        uniq_studentid.append(studentid)
        student['Student Name'] = studentname
        student['Course Name'] = coursename
        student['Marks'] = marks
        if os.path.isfile("Marks.json"):
                    with open('Marks.json', 'r') as f:
                        stu = json.load(f)
                    stu['Scores'].append(student)
                    with open('Marks.json', 'w') as f:
                        json.dump(stu, f)
        else:
            with open('Marks.json', 'w') as f:
                            stu['Scores'] = []
                            stu['Scores'].append(student)
                            json.dump(stu, f)


        showinfo('Save', 'Your record has been saved')
        e20.delete(0, END)
        e21.delete(0, END)
        e22.delete(0, END)
        e23.delete(0, END)
        e30.delete(0, END)

    else:
        showerror('Empty Space error:', 'You cannot left these fields empty!!')

def delete_all():
    for record in tree.get_children():
        tree.delete(record)

def delete():
    d = tree.selection()[0]
    tree.delete(d)

######################################################################
student = {}
sflag, cflag = True, True
treev = None

uniq_rollno = list()
uniq_courseid = list()
uniq_studentid = list()
uniq_coursename = list()
clist = []
root = Tk()
root.state('zoomed')
root.title('Student Record Keeping Application')
populaterollons()
populatecourses()
frame1 = Frame(root, width=900, height=400, bg='black')
frame1.pack(side=TOP, fill=BOTH)
for i in range(3):
    frame1.columnconfigure(i, weight=1)

image = Image.open('chitkara-university.gif')
render = ImageTk.PhotoImage(image)

imagegif = Image.open('mygif.gif')
rendergif = ImageTk.PhotoImage(imagegif)

lbl_head = Label(frame1, bg='Black', image=render)
lbl_head.grid(row=0, column=2, sticky='ne')

image2 = ImageTk.Image.open('explore.gif')
render2 = ImageTk.PhotoImage(image2)

lbl_head2 = Label(frame1, bg='Black', image=render2)
lbl_head2.grid(row=0, column=0, sticky='nw')

lbl_head2 = Label(frame1, text='Chitkara University', bg='Black', fg='White', font=('Aharoni', 25))
lbl_head2.grid(row=0, column=1, sticky='n')

lbl_subhead = Label(frame1, text='STUDENT DATABASE', font=('Times new Roman', 20), fg='White', bg='Black')
lbl_subhead.grid(row=1, column=1)

frame2 = Frame(root, height=400, width=900, bg='Black')
frame2.pack(side=TOP, fill=BOTH)

for i in range(3):
    frame2.columnconfigure(i, weight=1)

frame2_left = Frame(frame2, height=400, width=200, bg='black')
frame2_left.pack(side=LEFT, fill=BOTH)
lbl_gif = Label(frame2_left, bg='Black', image=rendergif)
lbl_gif.pack(pady=125)

frame2_middle = Frame(frame2, height=400, width=400, bg='White')
frame2_middle.pack(side=LEFT, fill=BOTH)

frame2_right = Frame(frame2, height=400, width=200, bg='black')
frame2_right.pack(side=RIGHT, fill=BOTH)
tabControl = ttk.Notebook(frame2_middle, padding=10)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6 = ttk.Frame(tabControl)
tab7 = ttk.Frame(tabControl)

tabControl.add(tab1, text='New Student')
tabControl.add(tab2, text='Display')
tabControl.add(tab3, text='Course Creation')
tabControl.add(tab4, text='Display Courses')
tabControl.add(tab5, text='Course Allocation')
tabControl.add(tab6, text ='Marks Allocation')
tabControl.add(tab7, text ='Display Marks')

tabControl.pack(expand=1, fill="both")

for i in range(7):
    tab1.columnconfigure(i, weight=1)
for i in range(10):
    tab1.rowconfigure(i, weight=1)

for i in range(4):
    tab3.columnconfigure(i, weight=1)

for i in range(8):
    tab3.rowconfigure(i, weight=1)

for i in range(4):
    tab5.columnconfigure(i, weight=1)

for i in range(8):
    tab5.rowconfigure(i, weight=1)

for i in range(8):
    tab6.rowconfigure(i, weight=1)
for i in range(10):
    tab6.columnconfigure(i, weight=1)

lbl1 = Label(tab1, text='Enter Your Name  ', font=('Biome', 12), fg='Black')
lbl1.grid(row=0, column=2, sticky='e')

lbl2 = Label(tab1, text='Enter Your Rollno  ', font=('Biome', 12), fg='Black')
lbl2.grid(row=1, column=2, sticky='e')

lbl3 = Label(tab1, text='Choose your Gender  ', font=('Biome', 12), fg='Black')
lbl3.grid(row=2, column=2, sticky='e')

lbl4 = Label(tab1, text='Address for Correspondence  ', font=('Biome', 12), fg='Black')
lbl4.grid(row=3, column=2, sticky='e')

lbl5 = Label(tab1, text='Phone No  ', font=('Biome', 12), fg='Black')
lbl5.grid(row=4, column=2, sticky='e')

n = StringVar()
lbl6 = Label(tab1, text='Your Batch  ', font=('Biome', 12), fg='Black')
lbl6.grid(row=5, column=2, sticky='e')

lbl7 = Label(tab1, text='Hostel[Y/N]  ', font=('Biome', 12), fg='Black')
lbl7.grid(row=6, column=2, sticky='e')

e1 = Entry(tab1, font=('Biome', 12))
e1.grid(row=0, column=7, sticky='e', ipadx=100)
tip1 = Balloon(tab1)
tip1.message.config(fg='Black', font=('Times new Roman', 10))  ##balloon message
remove(tip1)
tip1.bind_widget(e1, balloonmsg='Please Enter your Full Name')

e2 = Entry(tab1, font=('Biome', 12))
e2.grid(row=1, column=7, sticky='e', ipadx=100)
tip2 = Balloon(tab1)
tip2.message.config(fg='Black', font=('Times new Roman', 10))
remove(tip2)
tip2.bind_widget(e2, balloonmsg='Please Enter your Roll no')

var = StringVar()
var.set('Male')
e3 = Radiobutton(tab1, text='Male', value='Male', variable=var)
e3.grid(row=2, column=7, sticky='w')

e3_1 = Radiobutton(tab1, text='Female', value='Female', variable=var)
e3_1.grid(row=2, column=7, sticky='e')

e4 = Entry(tab1, font=('Biome', 12))
e4.grid(row=3, column=7, sticky='e', ipadx=100)
tip4 = Balloon(tab1)
tip4.message.config(fg='Black', font=('Times new Roman', 10))
remove(tip4)
tip4.bind_widget(e4, balloonmsg='Complete Address')

e5 = Entry(tab1, font=('Biome', 12))
e5.grid(row=4, column=7, sticky='e', ipadx=100)
tip5 = Balloon(tab1)
tip5.message.config(fg='Black', font=('Times new Roman', 10))
remove(tip5)
tip5.bind_widget(e5, balloonmsg='Please Enter Phone no in Numerics Only')

e6 = ttk.Combobox(tab1, width=27, textvariable=n)
e6['values'] = (' Batch 2020',
                ' Batch 2019',
                ' Batch 2018',
                ' Batch 2017'
                )
e6.grid(row=5, column=7, sticky='e')
tip6 = Balloon(tab1)
tip6.message.config(fg='Black', font=('Times new Roman', 10))
remove(tip6)
tip6.bind_widget(e6, balloonmsg='Please Enter Your Batch\n Either in Roman or numerical')

var1 = BooleanVar()
var1.set(True)
c1 = Checkbutton(tab1, text='Click if you need Hostel Facility', variable=var1, onvalue=1, offvalue=0)
c1.grid(row=6, column=7, sticky='e')

btn1 = Button(tab1, text="Save", font=('Biome', 11), command=save, width=15)
btn1.grid(row=7, column=4, sticky="e")
tip7 = Balloon(tab1)
tip7.message.config(fg='Black', font=('Times new Roman', 10))
remove(tip7)
tip7.bind_widget(btn1, balloonmsg='Save record')

btn2 = Button(tab1, text="Clear", font=('Biome', 11), command=clear, width=15)
btn2.grid(row=7, column=5, sticky="w")
tip8 = Balloon(tab1)
tip8.message.config(fg='Black', font=('Times new Roman', 10))
remove(tip8)
tip8.bind_widget(btn2, balloonmsg='Clear record')
################################################################################
lbl1 = Label(tab3, text='Course ID  ', font=('Biome', 12), fg='Black')
lbl1.grid(row=1, column=1, sticky='e')

lbl2 = Label(tab3, text='Course Name  ', font=('Biome', 12), fg='Black')
lbl2.grid(row=2, column=1, sticky='e')

e7 = Entry(tab3, font=('Biome', 12))
e7.grid(row=1, column=2, sticky='e', ipadx=100)
tip1 = Balloon(tab1)
tip1.message.config(fg='Black', font=('Times new Roman', 10))
remove(tip1)
tip1.bind_widget(e7, balloonmsg='Please Enter the Course ID')

e8 = Entry(tab3, font=('Biome', 12))
e8.grid(row=2, column=2, sticky='e', ipadx=100)
tip2 = Balloon(tab3)
tip2.message.config(fg='Black', font=('Times new Roman', 10))
remove(tip2)
tip2.bind_widget(e8, balloonmsg='Please Enter the Course Name')

btn1 = Button(tab3, text="Save", font=('Biome', 11), command=savecourse, width=15)
btn1.grid(row=4, column=2, sticky="w")
tip7 = Balloon(tab3)
tip7.message.config(fg='Black', font=('Times new Roman', 10))
remove(tip7)
tip7.bind_widget(btn1, balloonmsg='Save record')

btn2 = Button(tab3, text="Clear", font=('Biome', 11), command=clearcourse, width=15)
btn2.grid(row=4, column=2, sticky="e")
tip8 = Balloon(tab3)
tip8.message.config(fg='Black', font=('Times new Roman', 10))
remove(tip8)
tip8.bind_widget(btn2, balloonmsg='Clear record')
#######################################################################################
lbl11 = Label(tab5, text='Student Rollno  ', font=('Biome', 12), fg='Black')
lbl11.grid(row=1, column=1, sticky='e')

lbl12 = Label(tab5, text='Course Name  ', font=('Biome', 12), fg='Black')
lbl12.grid(row=2, column=1, sticky='e')

e10 = Entry(tab5, font=('Biome', 12))
e10.grid(row=1, column=2, sticky='e', ipadx=100)
tip1 = Balloon(tab5)
tip1.message.config(fg='Black', font=('Times new Roman', 10))
remove(tip1)
tip1.bind_widget(e1, balloonmsg='Please Enter the Course ID')
f = StringVar()
e11 = ttk.Combobox(tab5, width=27, textvariable=f)
# with open("Course.json") as f:
#     cn = json.load(f)
# for i in cn['Courses']:
#     clist.append(i['CourseName'])
# populate()
e11['values'] = tuple(clist)
e11.bind("<FocusIn>", populate)

e11.grid(row=2, column=2, sticky='e', ipadx=100)

tip2 = Balloon(tab5)
tip2.message.config(fg='Black', font=('Times new Roman', 10))
remove(tip2)
tip2.bind_widget(e11, balloonmsg='Please Choose the Course Name')

btn11 = Button(tab5, text="Allocate", font=('Biome', 11), command=allocatecourse, width=15)
btn11.grid(row=4, column=2, sticky="w")
tip7 = Balloon(tab5)
tip7.message.config(fg='Black', font=('Times new Roman', 10))
remove(tip7)
tip7.bind_widget(btn11, balloonmsg='Allocate Course')

btn12 = Button(tab5, text="Clear", font=('Biome', 11), command=clearcourse, width=15)
btn12.grid(row=4, column=2, sticky="e")
tip8 = Balloon(tab5)
tip8.message.config(fg='Black', font=('Times new Roman', 10))
remove(tip8)
tip8.bind_widget(btn12, balloonmsg='Clear record')
load()
loadcourses()

btn13 = Button(tab2, text="Show Students", bg='black', fg='white', font=('Biome', 11),
               command=lambda: loadStutree(treev), width=15)
btn13.pack(side=BOTTOM)
tip8 = Balloon(tab2)
tip8.message.config(fg='Black', font=('Times new Roman', 10))
remove(tip8)
tip8.bind_widget(btn13, balloonmsg='Show List')

btn14 = Button(tab4, text="Show Courses", bg='black', fg='white', font=('Biome', 11),
               command=lambda: loadCoutree(treevc), width=15)
btn14.pack(side=BOTTOM)
tip8 = Balloon(tab4)
tip8.message.config(fg='Black', font=('Times new Roman', 10))
remove(tip8)
tip8.bind_widget(btn14, balloonmsg='Show Courses')

lbl13 = Label(tab6,text='Student Rollno  ', font=('Biome', 12), fg='Black')
lbl13.grid(row=1,column=1,sticky='e')

lbl14 = Label(tab6, text='Student Name  ', font=('Biome', 12), fg='Black')
lbl14.grid(row=2, column=1, sticky='e')

lbl15 = Label(tab6, text='Course Name  ', font=('Biome', 12), fg='Black')
lbl15.grid(row=3, column=1, sticky='e')

lbl16 = Label(tab6, text='Marks  ', font=('Biome', 12), fg='Black')
lbl16.grid(row=4, column=1, sticky='e')

e20 = Entry(tab6, font=('Biome', 12))
e20.grid(row=1, column=2, sticky='e', ipadx=100)

e21 = Entry(tab6, font=('Biome', 12))
e21.grid(row=2, column=2, sticky='e', ipadx=100)

e22 = Entry(tab6, font=('Biome', 12))
e22.grid(row=3, column=2, sticky='e', ipadx=100)

e23 = Entry(tab6, font=('Biome', 12))
e23.grid(row=4, column=2, sticky='e', ipadx=100)

x = StringVar()
e30 = ttk.Combobox(tab6, width=27, textvariable=x)
e30['value'] = tuple(clist)
e30.bind("<FocusIn>", popular)
e30.grid(row=3, column=2, sticky='e', ipadx=100)


btn15 = Button(tab6, text="Save", font=('Biome', 11), command=savemarks, width=15)
btn15.grid(row=6, column=2, sticky="w")

btn16 = Button(tab6, text="Clear", font=('Biome', 11), command=clearcourse, width=15)
btn16.grid(row=6, column=2, sticky="e")

loadmarks()
btn17 = Button(tab7, text="Show Marks", bg='black', fg='white', font=('Biome', 11),
               command=lambda: loadMarktree(tree), width=15)
btn17.pack(side=BOTTOM)

btn18 = Button(tab7, text="Delete Record ", bg='black', fg='white', font=('Biome', 11),
               command=delete, width=15)
btn18.pack(side=LEFT)

btn19 = Button(tab7, text="Delete All Records ", bg='black', fg='white', font=('Biome', 11),
               command=delete_all, width=15)
btn19.pack(side=RIGHT)

################################################################################
info_lbl = Label(root, text='Department of Computer Science & Engineering', width=900, height=150, font=('Impact', 12),
                 bg='Black', fg='White')
info_lbl.pack(fill=BOTH, side=BOTTOM)
root.mainloop()
