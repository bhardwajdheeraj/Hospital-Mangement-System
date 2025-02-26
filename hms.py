from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1450x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEfect=StringVar() 
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()

      
      
        lbtitle=Label(self.root,bd=20,relief=RIDGE,text="+ HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbtitle.pack(side=TOP,fill=X)
        
#  ===========  dataframe =================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1450,height=400)
        
        DataframeLeft=LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,font=("arial",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,font=("arial",12,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=420,height=350)

        # =======================buttons frame===========

        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1450,height=70)
   
        # =======================Detailes frame===========

        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1450,height=190)
       
#    Datafeame left=================================
        lblNameTablet=Label(DataframeLeft,text="Names OF Tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,font=("times new roman",12,"bold"),width=33)

        comNametablet["value"]=("Nice","Corona Vacine","Acentaminophen","Adderall","Amlodipine","Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Refrence No:",padx=2,pady=6)
        lblref.grid(row=1,column=0,sticky=W)
        textref=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.ref,width=35)
        textref.grid(row=1,column=1)

        lblDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=6)
        lblDose.grid(row=2,column=0,sticky=W)
        textDose=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.Dose,width=35)
        textDose.grid(row=2,column=1)
   
        lblNoOftablets=Label(DataframeLeft,font=("arial",12,"bold"),text="No Of Tablets::",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        textNoOftablets=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.NumberofTablets,width=35)
        textNoOftablets.grid(row=3,column=1)

        lbllot=Label(DataframeLeft,font=("arial",12,"bold"),text="Lot",padx=2,pady=6)
        lbllot.grid(row=4,column=0,sticky=W)
        textlot=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.Lot,width=35)
        textlot.grid(row=4,column=1)

        lblIssueDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        textIssueDate=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.Issuedate,width=35)
        textIssueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        textExpDate=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.ExpDate,width=35)
        textExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        textDailyDose=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.DailyDose,width=35)
        textDailyDose.grid(row=7,column=1)
      

        lblSideEffect=Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        textsideEffect=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.sideEfect,width=35)
        textsideEffect.grid(row=8,column=1)

        lblFurtherinfo=Label(DataframeLeft,font=("arial",12,"bold"),text="Further Information:",padx=2,pady=6)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        textFurtherinfo=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.FurtherInformation,width=35)
        textFurtherinfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataframeLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        textBloodPressure=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.DrivingUsingMachine,width=35)
        textBloodPressure.grid(row=1,column=3)

        lblStrong=Label(DataframeLeft,font=("arial",12,"bold"),text="Strong Advice:",padx=2,pady=6)
        lblStrong.grid(row=2,column=2,sticky=W)
        textStrong=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.StorageAdvice,width=35)
        textStrong.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        textMedicine=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.HowToUseMedication,width=35)
        textMedicine.grid(row=3,column=3)

        lblPatientId=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Id",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        textPatientId=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PatientId,width=35)
        textPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(DataframeLeft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        textNhsNumber=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.nhsNumber,width=35)
        textNhsNumber.grid(row=5,column=3)


        lblPatientName=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        textPatientName=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PatientName,width=35)
        textPatientName.grid(row=6,column=3)

        lblDob=Label(DataframeLeft,font=("arial",12,"bold"),text="Date Of Birth:",padx=2,pady=6)
        lblDob.grid(row=7,column=2,sticky=W)
        textDob=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.DateOfBirth,width=35)
        textDob.grid(row=7,column=3)


        lblPatientAddress=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Address",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        textPatientAddress=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PatientAddress,width=35)
        textPatientAddress.grid(row=8,column=3)

        
        # ===============================DataframeRight========

        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        # =================Buttons===========

        btnPrescription=Button(Buttonframe,command=self.iPrectioption,text="Presciption",bg="green",fg='white',font=("arial",12,"bold"),width=20)
        btnPrescription.grid(row=0,column=0)
        btnPrescriptionData=Button(Buttonframe,command=self.iPrescriptionDate,text="Presciption Data",bg="green",fg='white',font=("arial",12,"bold"),width=20)
        btnPrescriptionData.grid(row=0,column=1)
       
        btnUpdate=Button(Buttonframe,command=self.update_data,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=20)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=20)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=20)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,command=self.iExit,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=20)
        btnExit.grid(row=0,column=5)


        # ===================Table==============================

        # ====================Scrollbar==================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)


        self.hospital_table = ttk.Treeview(
        Detailsframe,
        columns=("nameoftable", "ref", "does", "nooftablets", "lot", "issuedate", "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob", "address"),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set
        )


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        

        self.hospital_table.heading("nameoftable", text="Name of Tablets")
        self.hospital_table.heading("ref", text="Reference")
        self.hospital_table.heading("does", text="Dose")  
        self.hospital_table.heading("nooftablets", text="Number of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Expiry Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="Date of Birth")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"]="headings"

        

        self.hospital_table.column("nameoftable", width=150)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("does", width=100)  
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=150)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=200)


        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)


        self.fetch_data()


#        ==================Functinality Declration============
    def iPrescriptionDate(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
                conn=mysql.connector.connect(host="localhost",username="root",password="Dheeraj@123",database="mydata")
                my_cursor=conn.cursor() 
                my_cursor.execute("insert into hospital_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                      self.Nameoftablets.get(),
                                                                                                      self.ref.get(),
                                                                                                      self.Dose.get(),
                                                                                                      self.NumberofTablets.get(),
                                                                                                      self.Lot.get(),
                                                                                                      self.Issuedate.get(),
                                                                                                      self.ExpDate.get(),
                                                                                                      self.DailyDose.get(),
                                                                                                      self.StorageAdvice.get(),
                                                                                                      self.nhsNumber.get(),
                                                                                                      self.PatientName.get(),
                                                                                                      self.DateOfBirth.get(),
                                                                                                      self.PatientAddress.get()

                                                                                                        ))  
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("Success","Record has been inserted")                                                                                       

 
    def update_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Dheeraj@123",database="mydata")
        my_cursor=conn.cursor() 
        my_cursor.execute("update hospital_table set NameOfTablets=%s,Dose=%s,No_Of_Tablets=%s,Lot=%s,Issue_Date=%s,Exp_Date=%s, Daily_Date=%s,StorageAdvice=%s,NHSNumber=%s,Patient_Name=%s,DOB=%s,Address=%s,where ref=%s",(
                                                                                                      self.Nameoftablets.get(),
                                                                                                      self.Dose.get(),
                                                                                                      self.NumberofTablets.get(),
                                                                                                      self.Lot.get(),
                                                                                                      self.Issuedate.get(),
                                                                                                      self.ExpDate.get(),
                                                                                                      self.DailyDose.get(),
                                                                                                      self.StorageAdvice.get(),
                                                                                                      self.nhsNumber.get(),
                                                                                                      self.PatientName.get(),
                                                                                                      self.DateOfBirth.get(),
                                                                                                      self.PatientAddress.get(),
                                                                                                      self.ref.get()
                                                                                                      ))

                                                                                                      

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Dheeraj@123", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM hospital_table")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children()) 
        for i in rows:
            self.hospital_table.insert("", END, values=i) 
        conn.close()
      
    

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0]),
        self.ref.set(row[1]),
        self.Dose.set(row[2]),
        self.NumberofTablets.set(row[3]),
        self.Lot.set(row[4]),        
        self.Issuedate.set(row[5]),
        self.ExpDate.set(row[6]),
        self.DailyDose.set(row[7]),
        self.StorageAdvice.set(row[8]),                                        
        self.nhsNumber.set(row[9]),
        self.PatientName.set(row[10]),
        self.DateOfBirth.set(row[11]),
        self.PatientAddress.set(row[12])


    def iPrectioption(self):
        self.txtPrescription.insert(END,"name of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Number Of Tablets:\t\t\t"+self.NumberofTablets.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.Issuedate.get()+"\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t"+self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.sideEfect.get()+"\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"StorageAdvice:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"DrivingUsingMachine:\t\t\t"+self.DrivingUsingMachine.get()+"\n")
        self.txtPrescription.insert(END,"PatientId:\t\t\t"+self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"NHSNumber:\t\t\t"+self.nhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"PatientName:\t\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END,"DateOfBirth:\t\t\t"+self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END,"PatientAddress:\t\t\t"+self.PatientAddress.get()+"\n")



    def idelete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Dheeraj@123",database="mydata")
        my_cursor=conn.cursor() 
        query="delete from hospital_table where Ref=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Patient's details has been deleted successfully")


    def clear(self):
        self.Nameoftablets.set(""),
        self.ref.set(""), 
        self.Dose.set(""),
        self.NumberofTablets.set(""),
        self.Lot.set(""),
        self.Issuedate.set(""),                                                                                                       self.Issuedate.get(),
        self.ExpDate.set(""),
        self.DailyDose.set(""),
        self.sideEfect.set(""),
        self.FurtherInformation.set(""),
        self.StorageAdvice.set(""),
        self.DrivingUsingMachine.set(""),
        self.HowToUseMedication.set(""),
        self.PatientId.set(""),
        self.nhsNumber.set(""),
        self.PatientName.set(""),
        self.DateOfBirth.set(""),
        self.PatientAddress.set(""),
        self.txtPrescription.delete("1.0",END)
                                                                               
    def iExit(self):
        iExit=messagebox.askyesno("Hospital management System","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return

root=Tk()
ob=Hospital(root)
root.mainloop()