from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage





class Employee:

    def __init__(self,root):
        self.root=root
        root.geometry("900x500+200+50")
        root.title("Qr Generator | Developed By AzKaR")
        root.resizable(False,False)
        title=Label(self.root,text="  Qr Code Generator  | By AzKaR",font=("times new roman",40),bg='#053246',anchor='w',fg='white')
        title.place(x=0,y=0,relwidth=True)




        #=========Frame================
        emp=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp.place(x=50,y=100,w=500,h=380)

        emp_title=Label(emp,text="  Qr Code Generator",font=("goudy old style",20),bg='#053246',fg='white')
        emp_title.place(x=0,y=0,relwidth=True)





        #========Label===========
        lbl_emp=Label(emp,text="Employee Code",font=("times new roman",15,'bold'),bg='white')
        lbl_emp.place(x=50,y=60)

        lbl_name=Label(emp,text="Name",font=("times new roman",15,'bold'),bg='white')
        lbl_name.place(x=50,y=100)

        lbl_department=Label(emp,text="Department",font=("times new roman",15,'bold'),bg='white')
        lbl_department.place(x=50,y=140)

        lbl_designation=Label(emp,text="Desination",font=("times new roman",15,'bold'),bg='white')
        lbl_designation.place(x=50,y=180)


        #=============variable for the entery field============
        self.var_code=StringVar()
        self.var_name=StringVar()
        self.var_depart=StringVar()
        self.var_desination=StringVar()


        #=============Entry field=================

        txt_emp=Entry(emp,font=("times new roman",15,'italic'),bg='lightyellow',textvariable=self.var_code)
        txt_emp.place(x=250,y=60)

        txt_name=Entry(emp,font=("times new roman",15,'italic'),bg='lightyellow',textvariable=self.var_name)
        txt_name.place(x=250,y=100)

        txt_department=Entry(emp,font=("times new roman",15,'italic'),bg='lightyellow',textvariable=self.var_depart)
        txt_department.place(x=250,y=140)

        txt_designation=Entry(emp,font=("times new roman",15,'italic'),bg='lightyellow',textvariable=self.var_desination)
        txt_designation.place(x=250,y=180)




        #=============Buttons================
        btn_generate=Button(emp,text='QR Generate',font=("times new roman",18,'bold'),fg='white',bg='#2196f3',command=self.genrate).place(x=90,y=250,w=180,h=30)
        clr_generate=Button(emp,text='Clear',font=("times new roman",18,'bold'),fg='white',bg='#607d8b',command=self.clear).place(x=280,y=250,w=90,h=30)




        #=================status bar===============
        self.massage=""
        self.lbl_msg=Label(emp,text=self.massage,bg='white',fg='green',font=("times new roman",20,'bold'))
        self.lbl_msg.place(x=0,y=320,relwidth=True)




        #========= QR Frame================
        qr_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_frame.place(x=600,y=100,w=250,h=380)

        Qr_title=Label(qr_frame,text="Employee Qr Code",font=("goudy old style",20),bg='#053246',fg='white')
        Qr_title.place(x=0,y=0,relwidth=True)


        #==========QR image=======
        self.qr_code=Label(qr_frame,text="No QR\n Available",font=("times new roman",15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,w=180,h=180)


        

    #=============button command function======================

    def genrate(self):
        # print(f"{self.var_code.get()}\t {self.var_name.get()}\t {self.var_depart.get()}\t {self.var_desination.get()}")
        if self.var_code.get()=="" or self.var_name.get()=="" or self.var_depart.get()=="" or self.var_desination.get()=="":
            self.massage="All fields are requied!!!"
            self.lbl_msg.config(text=self.massage,bg='white',fg='red',font=("times new roman",20,'bold'))

        else:
            qr_data=f"Employee Id: {self.var_code.get()}\nEmployee Name: {self.var_name.get()}\nDepartment: {self.var_depart.get()}\nDesination: {self.var_desination.get()}"

           


            qr_code=qrcode.make(qr_data)
            # print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])    #install resize image module to use this feature
            qr_code.save("Emp"+str(self.var_code.get())+'.png')    #now saving the image with png format 

            self.im=ImageTk.PhotoImage(file="Emp"+str(self.var_code.get())+'.png')

            # print(self.im)
            self.qr_code.config(image=self.im)
                     
            self.massage="QR Generated successfully!!!"
            self.lbl_msg.config(text=self.massage,bg='white',fg='green',font=("times new roman",20,'bold'))

    def clear(self):
        self.var_code.set(value="")
        self.var_name.set(value="")
        self.var_depart.set(value="")
        self.var_desination.set(value="")
        self.qr_code.config(image="")
        self.lbl_msg.config(text="")



root=Tk()
ob=Employee(root)
root.mainloop()