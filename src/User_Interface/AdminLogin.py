import tkinter as tk
import tkinter.font as tkf

from src.Coding.Administrator import Administrator
from src.User_Interface.AdministratorPage import AdministratorPage


class AdminLogin:
    main_admin = Administrator("admin", "pw1234")
    ADMIN = [main_admin]

    def __init__(self, figure):
        figure.title("Login Page")
        figure["bg"] = "#d7fcb8"
        width = 750
        height = 450
        screenwidth = figure.winfo_screenwidth()
        screenheight = figure.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        figure.geometry(alignstr)
        figure.resizable(width=False, height=False)

        title = tk.Label(figure)
        title["bg"] = "#d7fcb8"
        ft = tkf.Font(family='Arial', size=22)
        title["font"] = ft
        title["fg"] = "#800000"
        title["justify"] = "center"
        title["text"] = "Solent Trip Management Login page"
        title.place(x=0, y=0, width=width, height=52)

        lbl_username = tk.Label(figure)
        lbl_username["bg"] = "#d7fcb8"
        ft = tkf.Font(family='Arial', size=14, weight="normal")
        lbl_username["font"] = ft
        lbl_username["fg"] = "#000000"
        lbl_username["justify"] = "center"
        lbl_username["text"] = "Username"
        lbl_username.place(x=150, y=110, width=90, height=40)

        self.edit_username = tk.Entry(figure)
        self.edit_username["bg"] = "white"
        self.edit_username["borderwidth"] = "5px"
        self.edit_username["relief"] = tk.FLAT
        ft = tkf.Font(family='Helvetica', size=17, weight="normal")
        self.edit_username["font"] = ft
        self.edit_username["fg"] = "cyan4"
        self.edit_username["justify"] = "left"
        self.edit_username["text"] = ""
        self.edit_username.place(x=250, y=110, width=250, height=40)

        lbl_psw = tk.Label(figure)
        lbl_psw["bg"] = "#d7fcb8"
        ft = tkf.Font(family='Arial', size=14, weight="normal")
        lbl_psw["font"] = ft
        lbl_psw["fg"] = "#000000"
        lbl_psw["justify"] = "center"
        lbl_psw["text"] = "Password"
        lbl_psw.place(x=150, y=190, width=90, height=40)

        self.edit_psw = tk.Entry(figure)
        self.edit_psw["bg"] = "white"
        self.edit_psw["borderwidth"] = "5px"
        self.edit_psw["relief"] = tk.FLAT
        ft = tkf.Font(family='Times', size=12, weight="normal")
        self.edit_psw["font"] = ft
        self.edit_psw["fg"] = "#333333"
        self.edit_psw["justify"] = "left"
        self.edit_psw["text"] = ""
        self.edit_psw["show"] = "*"
        self.edit_psw.place(x=250, y=190, width=250, height=40)

        btn_login = tk.Button(figure)
        btn_login["activebackground"] = "#5e75db"
        btn_login["anchor"] = "center"
        btn_login["bg"] = "cyan4"
        btn_login["borderwidth"] = "1px"
        btn_login["relief"] = tk.GROOVE
        ft = tkf.Font(family='Arial', size=15)
        btn_login["font"] = ft
        btn_login["fg"] = "#FFFFFF"
        btn_login["justify"] = "center"
        btn_login["text"] = "LOGIN"
        btn_login.place(x=280, y=280, width=180, height=40)
        btn_login["command"] = lambda: self.btnLoginHandler(figure)

        lbl1 = tk.Label(figure)
        lbl1["bg"] = "#d7fcb8"
        ft = tkf.Font(family='Arial', size=14, weight="normal")
        lbl1["font"] = ft
        lbl1["fg"] = "#000000"
        lbl1["justify"] = "center"
        lbl1["text"] = "Username - admin / Password - pw1234"
        lbl1.place(x=180, y=350, width=400, height=40)

        lbl2 = tk.Label(figure)
        lbl2["bg"] = "#d7fcb8"
        ft = tkf.Font(family='Arial', size=13, weight="normal")
        lbl2["font"] = ft
        lbl2["fg"] = "red"
        lbl2["justify"] = "center"
        lbl2["text"] = "Please make sure you enter the correct password to open the next window."
        lbl2.place(x=0, y=390, width=800, height=40)

    def btnLoginHandler(self, figure):
        username = self.edit_username.get()
        contact = self.edit_psw.get()

        isValidUser = self.authonticate(username, contact)

        if isValidUser:
            adminFigure = tk.Toplevel(figure)
            AdministratorPage(adminFigure, username, contact)
            figure.withdraw()
            adminFigure.mainloop()

        else:
            print("Login Failed")

    @staticmethod
    def authonticate(username: str, contact: str):
        for admin in AdminLogin.ADMIN:
            if admin.name == username and admin.contact == contact:
                return True
        return False


if __name__ == "__main__":
    root = tk.Tk()
    app = AdminLogin(root)
    root.mainloop()
