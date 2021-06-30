#import module
from tkinter import *
import tkinter.messagebox
import sqlite3

# class for Tkinter
class Product:
    def __init__(self,root):
        self.database = DataBase()
        self.database.connect()
        self.root=root
        self.root.geometry("1325x690")
        self.root.config(bg="yellow")

        self.pID=StringVar()
        self.pName = StringVar()
        self.pPrice = StringVar()
        self.pQty = StringVar()
        self.pCompany = StringVar()
        self.pContact=StringVar()




       #creating Frame----------------------------------------------
        mainFrame=Frame(self.root,bg="red")
        mainFrame.grid()

        headFrame=Frame(mainFrame,bd=1,padx=50,pady=10,bg="white",relief=RIDGE)
        headFrame.pack(side=TOP)
        self.title=Label(headFrame,font=("arial",30,"bold"),fg="red",text="  WAREHOUSE INVENTORY SALES AND PURCHASE SYSTEM  ",bg="white")
        self.title.grid()
        
        # --------------------------------Operation Frame---------------------------------------------
        
        operationFrame=Frame(mainFrame,bd=2,width=1250,height=60,padx=50,pady=20,bg="white",relief=RIDGE)
        operationFrame.pack(side=BOTTOM)


        #-----------------------------------------Body FRAME -------------------------------------------
        bodyFrame = Frame(mainFrame, bd=2, width=1240, height=400, padx=30, pady=20, bg="white", relief=RIDGE)
        bodyFrame.pack(side=BOTTOM)
        # -------------------------------------------Left Body Frame-----------------------
        leftBodyFrame = LabelFrame(bodyFrame, bd=2, width=850, height=380, padx=20, pady=5,text="product Item Details:",font=("arial",12,"bold"), bg="yellow", relief=RIDGE)
        leftBodyFrame.pack(side=LEFT)
        rightBodyFrame = LabelFrame(bodyFrame, bd=2, width=450, height=400, padx=20, pady=10,
                                   text="product Item Info:", font=("arial", 12, "bold"), bg="yellow", relief=RIDGE)
        rightBodyFrame.pack(side=RIGHT)
        # ____________________________Adding Widgets----------------------------------------------------
        self.label_PId=Label(leftBodyFrame,font=("arial",15,"bold"),text="Product ID",padx=2,bg="yellow",fg="blue")
        self.label_PName = Label(leftBodyFrame, font=("arial", 15, "bold"), text="Product Name:", padx=2,pady=3, bg="yellow",
                               fg="blue")
        self.label_pPrice = Label(leftBodyFrame, font=("arial", 15, "bold"), text="Product price:", padx=2,pady=3, bg="yellow",
                               fg="blue")
        self.label_pQTY = Label(leftBodyFrame, font=("arial", 15, "bold"), text="Product Quantity:", padx=2,pady=3, bg="yellow",
                               fg="blue")
        self.label_pCompany = Label(leftBodyFrame, font=("arial", 15, "bold"), text="MFg. Company:", padx=2,pady=3, bg="yellow",
                               fg="blue")
        self.label_Contact=Label(leftBodyFrame,font=("arial",15,"bold"),text="Company Contact",padx=2,pady=3,bg="yellow",fg="blue")
       # ----------------------------Dummy----------------------


        self.leb_Dum1=Label(leftBodyFrame,padx=2,pady=2,bg="yellow")
        self.leb_Dum2 = Label(leftBodyFrame, padx=2, pady=2,bg="yellow")
        self.leb_Dum3 = Label(leftBodyFrame, padx=2, pady=2,bg="yellow")
        self.leb_Dum4 = Label(leftBodyFrame, padx=2, pady=2,bg="yellow")
        self.leb_Dum1.grid(row=6,column=0,sticky=W)
        self.leb_Dum2.grid(row=7, column=0, sticky=W)
        self.leb_Dum3.grid(row=8, column=0, sticky=W)
        self.leb_Dum4.grid(row=9, column=0, sticky=W)
        ############################ScrollBar-------------------------------------------------
        scroll=Scrollbar(rightBodyFrame)
        scroll.grid(row=0,column=1,sticky="ns")

        self.productList=Listbox(rightBodyFrame,width=57,height=16,font=("arial",12,"bold"),yscrollcommand=scroll.set)
       #binded listbox select event
        self.productList.bind('<<ListboxSelect>>',self.productRec)
        self.productList.grid(row=0,column=0,padx=8)
        scroll.config(command=self.productList.yview)

        # ------------------------------------Buttons------------------------

        self.button_saveData=Button(operationFrame,text="Save",font=("aial",14,"bold"),bg="blue",fg="white",height=1,width=10,bd=4,command=self.insertcall)
        self.button_saveData.grid(row=0,column=0,padx=5)

        self.button_showData = Button(operationFrame, text="Show Data", font=("aial", 14, "bold"),bg="blue",fg="white",padx=5, height=1, width=10, bd=4,command=self.showcall)
        self.button_showData.grid(row=0, column=1,padx=5)

        self.button_resetData = Button(operationFrame, text="Reset", font=("aial", 14, "bold"),bg="blue",fg="white",padx=5, height=1, width=10, bd=4,command=self.reset)
        self.button_resetData.grid(row=0, column=2,padx=5)

        self.button_deleteData = Button(operationFrame, text="Delete", font=("aial", 14, "bold"),bg="blue",fg="white",padx=5, height=1, width=10, bd=4,command=self.deleteCall)
        self.button_deleteData.grid(row=0, column=3,padx=5)

        self.button_searchData = Button(operationFrame, text="Search", font=("aial", 14, "bold"),bg="blue",fg="white",padx=5, height=1, width=10, bd=4,command=self.searchcall)
        self.button_searchData.grid(row=0, column=4,padx=5)

        self.button_updateData = Button(operationFrame, text="Update", font=("aial", 14, "bold"),bg="blue",fg="white",padx=5, height=1, width=10, bd=4,command=self.updateCall)
        self.button_updateData.grid(row=0, column=5,padx=5)

        self.button_close = Button(operationFrame, text="Close", font=("aial", 14, "bold"), height=1,padx=5,bg="blue",fg="white", width=10, bd=4,command=self.close)
        self.button_close.grid(row=0, column=6,padx=5)






        self.label_PId.grid(row=0,column=0,sticky=W)
        self.label_PName.grid(row=1, column=0, sticky=W)
        self.label_pPrice.grid(row=2, column=0, sticky=W)
        self.label_pQTY.grid(row=3, column=0, sticky=W)
        self.label_pCompany.grid(row=4, column=0, sticky=W)
        self.label_Contact.grid(row=5, column=0, sticky=W)

        self.entery_PID=Entry(leftBodyFrame,font=("arial",15,"bold"),textvariable=self.pID,width=35)
        self.entery_pName = Entry(leftBodyFrame, font=("arial", 15, "bold"), textvariable=self.pName, width=35)
        self.entery_pPrice = Entry(leftBodyFrame, font=("arial", 15, "bold"), textvariable=self.pPrice, width=35)
        self.entery_PQTY = Entry(leftBodyFrame, font=("arial", 15, "bold"), textvariable=self.pQty, width=35)
        self.entery_pCompany = Entry(leftBodyFrame, font=("arial", 15, "bold"), textvariable=self.pCompany, width=35)
        self.entery_Contact = Entry(leftBodyFrame, font=("arial", 15, "bold"), textvariable=self.pContact, width=35)

        self.entery_PID.grid(row=0,column=1,padx=3,sticky=W)
        self.entery_pName.grid(row=1, column=1,padx=3, sticky=W)
        self.entery_pPrice.grid(row=2, column=1,padx=3, sticky=W)
        self.entery_PQTY.grid(row=3, column=1, padx=3,sticky=W)
        self.entery_pCompany.grid(row=4, column=1,padx=3, sticky=W)
        self.entery_Contact.grid(row=5, column=1,padx=3, sticky=W)

    def reset(self):
        print("in reset")
        self.entery_PID.delete(0, END)
        self.entery_pName.delete(0, END)
        self.entery_pPrice.delete(0, END)
        self.entery_PQTY.delete(0, END)
        self.entery_pCompany.delete(0, END)
        self.entery_Contact.delete(0, END)



    def close(self):
       print("close Method")
       close=tkinter.messagebox.askyesno("WAREHOUSE INVENTORY SALES AND PURCHASE SYSTEM","Really Do yo Want to Close Inventory")
       if close>0:
         self.root.destroy()
         print("Closed")

    def insertcall(self):
        print("in insert call mthoda")
        if((len(self.pID.get()) and len(self.pName.get()) and len(self.pPrice.get()) and len(self.pQty.get()) and len(self.pContact.get()))>0):
            self.database.insert(self.pID.get(),self.pName.get(),self.pQty.get(),self.pPrice.get(),self.pCompany.get(),self.pContact.get())
            # self.productList.delete(0,END)
            # self.productList.insert(END,self.pID.get(),self.pName.get(),self.pQty.get(),self.pPrice.get(),self.pCompany.get(),self.pContact.get())
            self.showcall()
        else:tkinter.messagebox.showinfo("inventory","please fill all the details")
        print("successfully inserteed.....")

    def showcall(self):
        print("in show call")
        self.productList.delete(0,END)
        row=self.database.show()
        print(type(row))
        for item in row:
            self.productList.insert(0,item)
            self.productList.insert(0,"-------------------------------------------------------------------------------")
        print("successfully data displayed")

    def productRec(self,event):
        print("in peoduct Rec")
        global pd
        searchpd=self.productList.curselection()[0]
        print(searchpd)
        pd=self.productList.get(searchpd)
        print(pd)
        self.entery_PID.delete(0,END)
        self.entery_pName.delete(0,END)
        self.entery_pPrice.delete(0,END)
        self.entery_PQTY.delete(0,END)
        self.entery_pCompany.delete(0,END)
        self.entery_Contact.delete(0,END)

        self.entery_PID.insert(END, pd[0])
        self.entery_pName.insert(END, pd[1])
        self.entery_pPrice.insert(END, pd[2])
        self.entery_PQTY.insert(END,pd[3])
        self.entery_pCompany.insert(END,pd[4])
        self.entery_Contact.insert(END,pd[5])


    def deleteCall(self):
        print("in delete call")
        if(len(self.pID.get())>0):
            self.database.delete(pd[0])
            self.reset()
            self.showcall()

    def searchcall(self):
        print("in search call")
        self.productList.delete(0,END)
        returned_by_dbsearch=self.database.search(self.pID.get(),self.pName.get(),self.pQty.get(),self.pPrice.get(),self.pCompany.get(),self.pContact.get())
        for ret in returned_by_dbsearch:
            self.productList.insert(END,ret,str(""))

        print("end of search Call")

    def updateCall(self):
        print("in update call")
        if(len(self.pID.get())>0):
            self.database.update(self.pID.get(),self.pName.get(),self.pQty.get(),self.pPrice.get(),self.pCompany.get(),self.pContact.get())
        self.showcall()
        print("update finished")







class DataBase:

    def connect(self):
        print("Database: In connect")
        conn=sqlite3.connect("inventory.db")
        cur=conn.cursor()
        cur.execute("create table if not exists product(pid integer primary key,pname text,price text,qty text,company text,contact text)")
        print("table created successfully")
        conn.commit()
        conn.close()

    def insert(self,pid,pname,price,qty,pcompany,contact):
        print("Database:in insert method")
        conn=sqlite3.connect("inventory.db")
        curr=conn.cursor()
        try:
         curr.execute("insert into product values(?,?,?,?,?,?)",(pid,pname,price,qty,pcompany,contact))
        except(sqlite3.IntegrityError):tkinter.messagebox.showinfo("info","Cheack product ID")
        conn.commit()
        conn.close()
        print("Database:End of insert")

    def show(self):
        print("Databse:in show meyhod")
        conn=sqlite3.connect("inventory.db")
        cur=conn.cursor()
        c=cur.execute("select * from product")
        print(f"Database: Something returned by select * query{c}")
        rows=cur.fetchall()
        conn.commit()
        conn.close()
        print("Database:End of show")
        print(type(conn))

        return rows

    def delete(self,pid):
        print("Database:inside delete")
        con=sqlite3.connect("inventory.db")
        curr=con.cursor()
        curr.execute("delete from product where pid=?",(pid,))
        con.commit()
        con.close()
        print(f"{pid} Record deletd")

    def search(self,pid="",name="",price="",qty="",pcompany="",contact=""):
        print("Database:In search method")
        conn=sqlite3.connect("inventory.db")
        cur=conn.cursor()
        cur.execute("select * from product where pid=? or pname=? or price=? or qty=? or company=? or contact=?",(pid,name,price,qty,pcompany,contact) )

        row=cur.fetchall()
        conn.commit()
        conn.close()
        print("Dtabase :End of search method")
        return row

    def update(self, pid="", name="", price="", qty="", pcompany="", contact=""):
        print("Database:In search method")
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("update product set pid=?,  pname=? ,price=? ,qty=? , company=? , contact=? where pid=?",(pid,name,price,qty,pcompany,contact,pd[0]))
        conn.commit()
        conn.close()
        print("End of Update")



        





if __name__=="__main__":
    root=Tk()
    product=Product(root)
    root.mainloop()
    database=DataBase()
    database.connect()
    
