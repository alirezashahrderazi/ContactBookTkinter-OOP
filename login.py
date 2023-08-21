from tkinter import *
import tkinter.messagebox as tm

from master import MainPage


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        #======================= Entrys And Labels ========================
        self.nameLable=Label(self,text="User Name",font=('calibri',14))
        self.nameEntry=Entry(self,bg='white',fg='#121212',width=15,borderwidth=2,font=('calibri',16))
        self.passworLable=Label(self,text="Password",font=('calibri',14),justify=LEFT)
        self.passwordEntry=Entry(self,bg='white',fg='#121212',width=15,borderwidth=2,font=('calibri',16))
        #======================= Button ========================
        self.loginBtn=Button(self,text='Login',bg='#121212',fg='white',padx=125,font=('calibri',20),command=self.login)
        self.exitBtn=Button(self,text='Exit',bg='#121212',fg='white',padx=135 ,font=('calibri',20),command=self.exit)
       
        self.nameLable.grid(column=1,row=0,pady=10)
        self.nameEntry.grid(column=1,row=1)
        self.passworLable.grid(column=1,row=2)
        self.passwordEntry.grid(column=1,row=3)
        self.loginBtn.grid(column=1,row=4,pady=10)
        self.exitBtn.grid(column=1,row=5)
        


        self.pack()

    def exit(self):
        choice=tm.askquestion('Exit Application','Are you sure want to close the application')
        if choice=='yes':
            self.master.destroy()


 
    def login(self):
        username = self.nameEntry.get()
        password = self.passwordEntry.get()
        if username == "a" and password == "a":
            self.master.destroy()
            MainPage.loading()
        else:
            tm.showerror("Login error", "Incorrect username Or Password")   

    @staticmethod
    def loading():
        root = Tk()
        LoginFrame(root)
        root.title('Contact Book')
        root.resizable(0,0)
        root.overrideredirect(True)
        root.attributes('-topmost', 1)
        #=============================== Window - Center=========================
        window_width = 400
        window_height = 400
        # get the screen dimension
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        # set the position of the window to the center of the screen
        root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        root.mainloop()




