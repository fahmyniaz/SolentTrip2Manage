import tkinter as tk
import tkinter.font as tkf
from src.User_Interface.TripCoordinatorPage import TripCoordinatorPage


class CoordinatorLogin:

    COORDINATORS = []

    def __init__(self, figure):
        figure.title("Trip Coordinator Login")
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
        ft = tkf.Font(family='Times', size=28)
        title["font"] = ft
        title["fg"] = "#800000"
        title["justify"] = "center"
        title["text"] = "TRIP COORDINATOR"
        title.place(x=0, y=0, width=width, height=52)

        lbl_uname = tk.Label(figure)
        lbl_uname["bg"] = "#d7fcb8"
        ft = tkf.Font(family='Arial', size=12, weight="normal")
        lbl_uname["font"] = ft
        lbl_uname["fg"] = "#000000"
        lbl_uname["justify"] = "center"
        lbl_uname["text"] = "Username"
        lbl_uname.place(x=170, y=110, width=80, height=40)

        self.edit_uname = tk.Entry(figure)
        self.edit_uname["bg"] = "#FFFFFF"
        self.edit_uname["borderwidth"] = "5px"
        self.edit_uname["relief"] = tk.FLAT
        ft = tkf.Font(family='Arial', size=12, weight="normal")
        self.edit_uname["font"] = ft
        self.edit_uname["fg"] = "#333333"
        self.edit_uname["justify"] = "left"
        self.edit_uname["text"] = ""
        self.edit_uname.place(x=250, y=110, width=250, height=40)

        lbl_psw = tk.Label(figure)
        lbl_psw["bg"] = "#d7fcb8"
        ft = tkf.Font(family='Arial', size=12, weight="normal")
        lbl_psw["font"] = ft
        lbl_psw["fg"] = "#000000"
        lbl_psw["justify"] = "center"
        lbl_psw["text"] = "Password"
        lbl_psw.place(x=170, y=190, width=80, height=40)

        self.edit_psw = tk.Entry(figure)
        self.edit_psw["bg"] = "#ffffff"
        self.edit_psw["borderwidth"] = "5px"
        self.edit_psw["relief"] = tk.FLAT
        ft = tkf.Font(family='Arial', size=12, weight="normal")
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
        btn_login["fg"] = "#ffffff"
        btn_login["justify"] = "center"
        btn_login["text"] = "LOGIN"
        btn_login.place(x=280, y=280, width=180, height=40)
        btn_login["command"] = lambda: self.btnLoginHandler(figure)

        lb1 = tk.Label(figure)
        lb1["bg"] = "#d7fcb8"
        ft = tkf.Font(family='Arial', size=13, weight="normal")
        lb1["font"] = ft
        lb1["fg"] = "red"
        lb1["justify"] = "center"
        lb1["text"] = "Please make sure you enter the username and password you have given during registration."
        lb1.place(x=0, y=390, width=800, height=40)

    def btnLoginHandler(self, figure):
        username = self.edit_uname.get()
        contact = self.edit_psw.get()

        isValidUser = self.authonticate(username, contact)

        if isValidUser:
            coordinatorFigure = tk.Toplevel(figure)
            TripCoordinatorPage(coordinatorFigure, username, contact)
            figure.withdraw()
            coordinatorFigure.mainloop()

        else:
            print("Login Failed")

    @staticmethod
    def authonticate(username: str, contact: str):
        for coordinator in CoordinatorLogin.COORDINATORS:
            if coordinator.name == username and coordinator.contact == contact:
                return True
        return False


if __name__ == "__main__":
    root = tk.Tk()
    app = CoordinatorLogin(root)
    root.mainloop()
