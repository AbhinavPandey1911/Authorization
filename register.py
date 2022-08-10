from cProfile import label
import imp
import re
from sys import byteorder
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector;
import hashlib

class Register_window:
    def __init__(self,root):
     self.root=root
     self.root.title("Registration Window")
     self.root.geometry("1600x900")
     self.bgRW=ImageTk.PhotoImage(file=r"C:\Users\abhin\Pictures\backuserauth.jpg")
     lbl_bgRW=Label(self.root,image=self.bgRW)
     lbl_bgRW.place(x=0,y=0,relwidth=1,relheight=1)
     frame=Frame(self.root,bg="black")
     frame.place(x=500,y=150,width=500,height=450)
     display=lbl=Label(frame,text="Please Enter the Following",font=("times new roman",20,"bold"),fg="white",bg="black")
     display.place(x=150,y=0)

     #username entry
     username=lbl=Label(frame,text=" Username",font=("times new roman",20,"bold"),fg="white",bg="black")
     username.place(x=0,y=170)
     self.txtuser=Entry(frame,font=("open sans",20,"bold"),fg="black",bg="white")
     self.txtuser.place(x=150,y=170)

     #password entry
     #label password
     pwd=lbl=Label(frame,text="password",font=("times new roman",20,"bold"),fg="white",bg="black")
     pwd.place(x=0,y=250)

     self.txtpwd=Entry(frame,font=("open sans",20,"bold"),fg="black",bg="white")
     self.txtpwd.place(x=150,y=250)     

     #submit button
     btn=Button(frame,text="Register",command=self.email_pwd_check,font=("times new roman",15,"bold"),border=3,relief=RIDGE,fg="white",bg="red")
     btn.place(x=200,y=300,height=40,width=100)

    def email_pwd_check(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        s=self.txtuser.get()
        if(re.fullmatch(regex,s)):
            if(self.txtpwd.get()!=""):
                con=mysql.connector.connect(host='localhost',user='root',password='abhinav1234',database='users_tkinkters')
                mycursor=con.cursor()
                query=("select * from users_data where email=%s")
                value=(self.txtuser.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                if row!=None:
                    messagebox.showerror("Users Already Exists","please try another credentials")
                else:
                    s="INSERT INTO users_data (email,password) VALUES (%s,%s)"
                    result = hashlib.sha256(self.txtpwd.get().encode())
                    b1=(self.txtuser.get(),result.hexdigest())
                    mycursor.execute(s,b1)
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Successfully")
        else :
            messagebox.showerror("Error","Please Put credentials Properly")
if __name__=="__main__":
 root=Tk() 
 app=Register_window(root)
 root.mainloop()

