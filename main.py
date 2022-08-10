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

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1600x900")
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\abhin\Pictures\backuserauth.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=150,width=500,height=450)
        img1=Image.open(r"C:\Users\abhin\Pictures\user.jpg")
        img1=img1.resize((100,100))
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=200,y=140)

        #label username
        username=lbl=Label(frame,text="Username",font=("times new roman",20,"bold"),fg="white",bg="black")
        username.place(x=0,y=170)

        self.txtuser=Entry(frame,font=("open sans",20,"bold"),fg="black",bg="white")
        self.txtuser.place(x=150,y=170)
   
        #label password
        pwd=lbl=Label(frame,text="password",font=("times new roman",20,"bold"),fg="white",bg="black")
        pwd.place(x=0,y=250)

        self.txtpwd=Entry(frame,font=("open sans",20,"bold"),fg="black",bg="white")
        self.txtpwd.place(x=150,y=250)
        
        #button
        btn=Button(frame,text="Login",command=self.email_pwd_check,font=("times new roman",15,"bold"),border=3,relief=RIDGE,fg="white",bg="red")
        btn.place(x=200,y=300,height=40,width=100)


        #new user
        btn=Button(frame,text="New User",font=("times new roman",15,"bold"),border=0,relief=RIDGE,fg="white",bg="black")
        btn.place(x=0,y=350,height=40,width=250)

        #forgotpwd
        btn=Button(frame,text="Forgot Password?",font=("times new roman",15,"bold"),border=0,relief=RIDGE,fg="white",bg="black")
        btn.place(x=0,y=400,height=40,width=250)

    def email_pwd_check(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        s=self.txtuser.get()
        if(re.fullmatch(regex,s)):
            con=mysql.connector.connect(host='localhost',user='root',password='abhinav1234',database='users_tkinkters')
            mycursor=con.cursor()
            query=("select * from users_data where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            #print(row[1])
            #print(hashlib.sha256(self.txtpwd.get().encode()).hexdigest())
            pwd=hashlib.sha256(self.txtpwd.get().encode()).hexdigest()
            if self.txtuser.get()==row[0] and pwd==row[1]:
                messagebox.showinfo("Welcome")
            else :
                messagebox.showerror("Wrong Credentials")
        else:
            messagebox.showerror("Error format")   
 
         
if __name__=="__main__":
 root=Tk() 
 app=Login_Window(root)
 root.mainloop()