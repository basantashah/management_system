from tkinter import*
from PIL import Image, ImageTk


class EMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768")
        self.root.title("Employee Management System | DEVELOPED BY SUMESH")
        self.root.config(bg="#16a085")

        #==================== TITLE ================================
        self.icon_title=PhotoImage(file="images/bg.png")
        title=Label(self.root, text="Employee Management System",image=self.icon_title, compound=LEFT, font=("Gotham",40,"bold"),bg="Orange",fg="white",anchor="w",padx=100).place(x=0,y=0,relwidth=1,height=70)

        #===== LOGGOUT =============================================
        btn_logout=Button(self.root,text="Logout",font=("Gotham",15,"bold"), bg="Dark Red",fg="white",cursor="hand2").place(x=1200,y=10,height=50,width=150)

        #==== CLOCK =====================================================
        self.lbl_clock = Label(self.root, text="Welcome to Employee Management System\t\t  Time: HH:MM;SS", font=("Gotham", 15), bg="Green", fg="white")
        self.lbl_clock.place(x=0,y=70,relwidt=1,height=30)

        #==== LEFT MENU ===================================================
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((310,200), Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root, bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=300,height=570)

        lbl_menuLogo=Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.icon_side = PhotoImage(file="images/side.png")

        lbl_menu=Label(LeftMenu, text="Menu", font=("Gotham", 20), bg="#009688").pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu, text="AddEmployee",command=self.employee,image=self.icon_side, compound=LEFT,padx=5, anchor="w", font=("Gotham", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier = Button(LeftMenu, text="Bank Details", image=self.icon_side, compound=LEFT, padx=4, anchor="w",font=("Gotham", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_category = Button(LeftMenu, text="Provident Fund", image=self.icon_side, compound=LEFT, padx=4, anchor="w",font=("Gotham", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_product = Button(LeftMenu, text="Salary Sheet", image=self.icon_side, compound=LEFT, padx=4, anchor="w",font=("Gotham", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_sales = Button(LeftMenu, text="Sales", image=self.icon_side, compound=LEFT, padx=4, anchor="w",font=("Gotham", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_exit = Button(LeftMenu, text="Exit", image=self.icon_side, compound=LEFT, padx=4, anchor="w",font=("Gotham", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)

        #===== CONTENT ====================================================

        self.lbl_employee=Label(self.root,text="Add Employee\n[0]", bd=5, relief=RIDGE,bg="#33bbf9",fg="white",font=("Goudy old style",20,"bold"))
        self.lbl_employee.place(x=410, y=120, height=150, width=200)

        self.lbl_supplier= Label(self.root, text="View Employee\n[0]", bd=5, relief=RIDGE, bg="#ff5722", fg="white",font=("Goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=750, y=120, height=150, width=200)

        self.lbl_category = Label(self.root, text="Update Employee\n[0]", bd=5, relief=RIDGE, bg="#009688", fg="white",font=("Goudy old style", 20, "bold"))
        self.lbl_category.place(x=1090, y=120, height=150, width=200)

        self.lbl_product = Label(self.root, text="Add Salary\n[0]", bd=5, relief=RIDGE, bg="#607d8b", fg="white",font=("Goudy old style", 20, "bold"))
        self.lbl_product.place(x=410, y=300, height=150, width=200)

        self.lbl_sales = Label(self.root, text="View Salary\n[0]", bd=5, relief=RIDGE, bg="#ffc107", fg="white",font=("Goudy old style", 20, "bold"))
        self.lbl_sales.place(x=750, y=300, height=150, width=200)

        # ==== FOOTER =====================================================

        lbl_footer=Label(self.root, text="EMS- Employee Management System | Developed By Global Digitronix \n For any Techinal Issue Contact: 98xxxxxxxx", padx=5000, font=("Gotham", 10), bg="#4d636d", fg="white" )
        lbl_footer.place(x=0, y=670, width=1360, height=35)

#========================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        

if __name__=="__main__":
    root=Tk()
    obj=EMS(root)
    root.mainloop()