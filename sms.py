from tkinter import *
from tkinter import  ttk
import pymysql
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        
        title=Label(self.root,text="Student Mangement System",font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)
        #********** All variable*********
        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        
        self.search_by=StringVar()
        self.search_txt=StringVar()
        #**************Manage Frame**********************
        Manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_frame.place(x=20,y=100,width=475,height=580)
        m_title=Label(Manage_frame,text="Manage Student",bg="crimson",fg="white",font=("times new roman",25,"bold"))
        m_title.grid(row=0,columnspan=2,pady=15)
        
        lbl_roll=Label(Manage_frame,text="Roll no.",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
  
        txt_roll=Entry(Manage_frame,textvariable=self.roll_no_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        
        lbl_name=Label(Manage_frame,text="Name",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        
        txt_name=Entry(Manage_frame,textvariable=self.name_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email=Label(Manage_frame,text="Email",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        
        txt_email=Entry(Manage_frame,textvariable=self.email_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        
        lbl_gender=Label(Manage_frame,text="Gender",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        combo_gender=ttk.Combobox(Manage_frame,textvariable=self.gender_var,font=("times new roman",9,"bold"),state="readonly")
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")
     

        lbl_contact=Label(Manage_frame,text="Contact",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        
        txt_contact=Entry(Manage_frame,textvariable=self.contact_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_dob=Label(Manage_frame,text="D.O.B.",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        
        txt_dob=Entry(Manage_frame,textvariable=self.dob_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        
        lbl_addr=Label(Manage_frame,text="Address",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        lbl_addr.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_addr=Text(Manage_frame,width=19,height=3)
        self.txt_addr.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        #*******button Frame*******
        btn_frame=Frame(Manage_frame,bd=4,relief=RIDGE,bg="crimson")
        btn_frame.place(x=10,y=500,width=450)

        addbutton=Button(btn_frame,text="Add",width=10,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
        updatebutton=Button(btn_frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebutton=Button(btn_frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clearbutton=Button(btn_frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        #**************Detail Frame**********************
        Detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_frame.place(x=530,y=100,width=790,height=580)
        
        
        lbl_search=Label(Detail_frame,text="Search By",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        
        combo_search=ttk.Combobox(Detail_frame,width=10,textvariable=self.search_by,font=("times new roman",10,"bold"),state="readonly")
        combo_search['values']=("roll_no","name","contact")
        combo_search.grid(row=0,column=1,pady=10,padx=20,sticky="w")

        txt_search=Entry(Detail_frame,textvariable=self.search_txt,font=("times new roman",10,"bold"),bd=4,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        searchbtn=Button(Detail_frame,text="Search",width=10,pady=3,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showbtn=Button(Detail_frame,text="Show All",width=10,pady=3,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)
        
        #**************Table Frame****************
        Table_frame=Frame(Detail_frame,bd=4,relief=RIDGE,bg="crimson")
        Table_frame.place(x=10,y=70,width=760,height=500)
        scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        
        self.Student_table.heading("roll",text="Roll No")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email Id")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B.")
        self.Student_table.heading("address",text="Address")

        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=60)
        self.Student_table.column("name",width=110)
        self.Student_table.column("email",width=110)
        self.Student_table.column("gender",width=110)
        self.Student_table.column("contact",width=110)
        self.Student_table.column("dob",width=110)
        self.Student_table.column("address",width=110)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_student(self):
        if self.roll_no_var.get()=="" or self.name_var.get()=="":
            ttk.messagebox.showerror("Error","All Fields are requred!")
        else:
            con=pymysql.connect(host='localhost',user='root',password='root',database='stm')
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s);",(
                self.roll_no_var.get(),
                self.name_var.get(),
                self.email_var.get(),
                self.gender_var.get(),
                self.contact_var.get(),
                self.dob_var.get(),
                self.txt_addr.get('1.0',END)
            ))
            con.commit()
            ttk.messagebox.showinfo("Success","Record has been inserted")
            self.fetch_data()
            con.close()
    def fetch_data(self):
        con=pymysql.connect(host='localhost',user='root',password='root',database='stm')
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
                con.commit()
        con.close()
    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.contact_var.set("")
        self.gender_var.set("")
        self.dob_var.set("")
        self.txt_addr.delete("1.0",END)

    def get_cursor(self,ev):
        cursr_row=self.Student_table.focus()
        contents=self.Student_table.item(cursr_row)
        row=contents['values']
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.contact_var.set(row[3])
        self.gender_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_addr.delete("1.0",END)
        self.txt_addr.insert(END,row[6])
    def update_data(self):
        con=pymysql.connect(host='localhost',user='root',password='root',database='stm')
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,addr=%s where roll_no=%s ;",(
                self.name_var.get(),
                self.email_var.get(),
                self.gender_var.get(),
                self.contact_var.get(),
                self.dob_var.get(),
                self.txt_addr.get('1.0',END),
                self.roll_no_var.get()
            ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    def delete_data(self):
        con=pymysql.connect(host='localhost',user='root',password='root',database='stm')
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s;",self.roll_no_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    def search_data(self):
        con=pymysql.connect(host='localhost',user='root',password='root',database='stm')
        cur=con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
                con.commit()
        con.close()
root=Tk()   

ob=Student(root)
root.mainloop()