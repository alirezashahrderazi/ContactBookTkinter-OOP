from tkinter import *
import tkinter.messagebox as tm
import webbrowser
import os
#pip
import pyperclip

class MainPage(Frame):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PATH=os.path.join(BASE_DIR,"data_file.txt")
    def __init__(self, master):
        super().__init__(master)


        self.nameLable=Label(self,text="Contact Name",font=('calibri',18))
        self.nameEntry=Entry(self,bg='white',font=('calibri',18))
        self.phoneLable=Label(self,text="Contact Phone",font=('calibri',18))
        self.phoneEntry=Entry(self,bg='white',font=('calibri',18))
        self.addBtn=Button(self,text='Add Contact',width=15,fg='white',bg='#121212',font=('calibri',14),command=self.add_contact)
        self.saveBtn=Button(self,text='Save List',width=15,fg='white',bg='#121212',font=('calibri',14),command=self.save_list)
        self.copyPhoneBtn=Button(self,text='Copy Phone Number',width=18,font=('calibri',14),fg='white',bg='#121212',command=self.copy_number)
        self.deletBtn=Button(self,text='  Delet Contact  ',width=18,font=('calibri',14),fg='white',bg='#121212',command=self.delet_contact)
        self.openSaveBtn=Button(self,text='  Open Save File ',width=18,font=('calibri',14),fg='white',bg='#121212',command=self.open_list)
        self.exitBtn=Button(self,text='Exit App',width=18,font=('calibri',14),fg='white',bg='#121212',command=self.exit)
        self.listBox=Listbox(self,width=50,height=8)

        self.nameLable.grid(column=0,row=0,columnspan=2)
        self.nameEntry.grid(column=0,row=1,columnspan=2)
        self.phoneLable.grid(column=0,row=2,columnspan=2)
        self.phoneEntry.grid(column=0,row=3,columnspan=2)

        self.addBtn.grid(column=0,row=4,columnspan=2,pady=4)
        self.saveBtn.grid(column=0,row=5,columnspan=2,pady=4)
        self.copyPhoneBtn.grid(column=0,row=6)
        self.deletBtn.grid(column=1,row=6)
        self.openSaveBtn.grid(column=0,row=7)
        self.exitBtn.grid(column=1,row=7)
        self.listBox.grid(column=0,row=8,columnspan=3,pady=4)





  
        self.pack()

        
    def exit(self):
        choice=tm.askquestion('Exit Application','Are you sure want to close the application')
        if choice=='yes':
            self.master.destroy()

    def add_contact(self):
        contact_string=self.nameEntry.get()+':'+self.phoneEntry.get()
        self.listBox.insert(END,contact_string)
        self.nameEntry.delete(0,END)        
        self.phoneEntry.delete(0,END)

    def delet_contact(self):
        self.listBox.delete(ANCHOR)

    def save_list(self):
        with open(self.PATH,'w')as f:
            list_tuple=self.listBox.get(0,END)
            for item in list_tuple:
                if item.endswith('\n'):
                    f.write(item)
                else:
                    f.write(item+'\n')

    def open_list(self):
        webbrowser.open(self.BASE_DIR)

    def openDB(self):
        if os.path.isfile(self.PATH):
            with open(self.PATH,'r')as f:
                for line in f:
                    self.listBox.insert(END,line) 
                    
    def copy_number(self):
        select_contact=self.listBox.get(ANCHOR)
        number=select_contact.split(':')  
        pyperclip.copy(number[1].replace('\n',''))  



    @staticmethod
    def loading():
        root = Tk()
        MainPage(root)
        root.title('Contact Book')
        root.resizable(0,0)
        root.overrideredirect(True)
        #root.attributes('-topmost', 1)
        #=============================== Window - Center=========================
        window_width = 450
        window_height = 450
        # get the screen dimension
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        # set the position of the window to the center of the screen
        root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        root.mainloop()



