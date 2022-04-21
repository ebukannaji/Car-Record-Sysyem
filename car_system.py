from tkinter import*
from tkinter import ttk,messagebox
smoke=Tk()
smoke.title("Car Part Records")
smoke.geometry("1280x720")
bg_color="#990099"

#==================Variable=======================
ref_var=IntVar()
name_var=StringVar()
gender_var=StringVar()
email_var=StringVar()
phone_var=StringVar()
carmake_var=StringVar()
desi_var=StringVar()
price_var=IntVar()
#==================Funtion=======================
def add():
    if ref_var.get()=="" or name_var.get()=="" or gender_var.get()==""or email_var.get()=="" or phone_var.get()=="" or carmake_var.get()==" "or desi_var.get()=="" or price_var.get()=="":
     messagebox.showerror("Error","All feilds are required ?")
    else:
        textarea.delete(1.0,END)
        textarea.insert(END, "\n=============================================")
        textarea.insert(END,f"\nCar Ref\t\t\t\t{ref_var.get()}")
        textarea.insert(END, "\n=============================================")
        textarea.insert(END, f"\n\nFullName\t\t\t\t{name_var.get()}")
        textarea.insert(END, f"\nEmail id\t\t\t\t{email_var.get()}")
        textarea.insert(END, f"\nGender \t\t\t\t{gender_var.get()}")
        textarea.insert(END, f"\nDesignation\t\t\t\t{desi_var.get()}")
        textarea.insert(END, f"\nStaff no\t\t\t\t{phone_var.get()}")
        textarea.insert(END, f"\n  Price\t\t\t\t{price_var.get()}")
        textarea.insert(END, f"\nCar Make\t\t\t\t{txt_carmake.get(1.0,END)}")
        textarea.insert(END, "\n\n#############################################")
        
def save():
    data=textarea.get(1.0,END)
    f1=open("records/"+str(ref_var.get())+"txt","w")
    f1.write(data)
    f1.close()
    messagebox.showinfo("Saved",f"Ref:{ref_var.get()}Saved Successfully")

def print():
    data=textarea.get(1.0,END)
    
        
#==================Heading========================
title=Label(smoke,text="Car Part Record System",bg="navy blue",fg="white",font=("times new roman",35,"bold"))
title.pack(fill=X)


#===================Left frame details==============
F1=Frame(smoke,bg="navy blue",relief=RIDGE,bd=15)
F1.place(x=10,y=80,width=650,height=540)

lbl_ref=Label(F1,text="Car Ref:",font=("times new roman",20,"bold"),fg="white",bg="navy blue")
lbl_ref.grid(row=0,column=0,padx=30,pady=10)
txt_ref=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7,textvariable=ref_var)
txt_ref.grid(row=0,column=1,pady=10,sticky="w")


lbl_name=Label(F1,text="Full Name:",font=("times new roman",20,"bold"),fg="white",bg="navy blue")
lbl_name.grid(row=1,column=0,padx=30,pady=10)
txt_name=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7,textvariable=name_var)
txt_name.grid(row=1,column=1,pady=10,sticky="w")


lbl_email=Label(F1,text="Email Id:",font=("times new roman",20,"bold"),fg="white",bg="navy blue")
lbl_email.grid(row=2,column=0,padx=30,pady=10)
txt_email=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7,textvariable=email_var)
txt_email.grid(row=2,column=1,pady=10,sticky="w")

lbl_gender=Label(F1,text="Staff Gender:",font=("times new roman",20,"bold"),fg="white",bg="navy blue")
lbl_gender.grid(row=3,column=0,padx=30,pady=10)


combo_gender=ttk.Combobox(F1,font=("times new roman",19),textvariable=gender_var)
combo_gender["value"]=("male","female","others")
combo_gender.grid(row=3,column=1,pady=10)


lbl_des=Label(F1,text="Designation:",font=("times new roman",20,"bold"),fg="white",bg="navy blue")
lbl_des.grid(row=4,column=0,padx=30,pady=10)


combo_des=ttk.Combobox(F1,font=("times new roman",19),textvariable=desi_var)
combo_des["value"]=("exhaust","radiator","front bumper","headlight")
combo_des.grid(row=4,column=1,pady=10)


lbl_no=Label(F1,text="Staff No:",font=("times new roman",20,"bold"),fg="white",bg="navy blue")
lbl_no.grid(row=5,column=0,padx=30,pady=10)
txt_no=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7,textvariable=phone_var)
txt_no.grid(row=5,column=1,pady=10,sticky="w")


lbl_price=Label(F1,text="Price:",font=("times new roman",20,"bold"),fg="white",bg="navy blue")
lbl_price.grid(row=6,column=0,padx=30,pady=10)
txt_price=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7,textvariable=price_var)
txt_price.grid(row=6,column=1,pady=10,sticky="w")


lbl_carmake=Label(F1,text="Car Make:",font=("times new roman",20,"bold"),fg="white",bg="navy blue")
lbl_carmake.grid(row=7,column=0,padx=30,pady=10)
txt_carmake=Text(F1,width=40,height=3,font=("times new rommon",10),relief=RIDGE,bd=7)
txt_carmake.grid(row=7,column=1,pady=5,sticky="w")


#===================Right frame details==============
F2=Frame(smoke,bg="navy blue",relief=RIDGE,bd=15)
F2.place(x=665,y=80,width=610,height=540)

lbl_t=Label(F2,text="Car Part Details",font=("arial 15 bold"),fg="black",bd=7,relief=GROOVE)
lbl_t.pack(fill=X)
scrol=Scrollbar(F2,orient=VERTICAL)
scrol.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font="arial 15",yscrollcommand=scrol.set)
textarea.pack(fill=BOTH)
scrol.config(command=textarea.yview)

#======================Buttons=======================
F3=Frame(smoke,bg="navy blue",relief=RIDGE,bd=15)
F3.place(x=10,y=615,width=1260,height=100)

btn1=Button(F3,text="Add Record",font="arial 20 bold",bg="white",fg="crimson",width=10,command=add)
btn1.grid(row=0,column=0,padx=25,pady=7)

btn2=Button(F3,text="Save",font="arial 20 bold",bg="white",fg="crimson",width=10,command=save)
btn2.grid(row=0,column=1,padx=25,pady=7)

btn3=Button(F3,text="Print",font="arial 20 bold",bg="white",fg="crimson",width=10)
btn3.grid(row=0,column=2,padx=25,pady=7)

btn4=Button(F3,text="Reset",font="arial 20 bold",bg="white",fg="crimson",width=10)
btn4.grid(row=0,column=3,padx=25,pady=7)

btn5=Button(F3,text="Exit",font="arial 20 bold",bg="white",fg="crimson",width=10)
btn5.grid(row=0,column=4,padx=25,pady=7)










smoke.mainloop()
