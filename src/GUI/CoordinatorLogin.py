import tkinter as tk
import tkinter.font as tkf

from src.GUI.TripCoordinatorPage import TripCoordinatorPage


class CoordinatorLogin:

    COORDINATORS = []

    def __init__(self, figure):

        # setting title
        figure.title("Trip Coordinator Login")
        # setting window size
        figure["bg"] = "#e3e8cd"
        width = 700
        height = 500
        screenwidth = figure.winfo_screenwidth()
        screenheight = figure.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        figure.geometry(alignstr)
        figure.resizable(width=False, height=False)

        title = tk.Label(figure)
        title["bg"] = "#6bcbcc"
        ft = tkf.Font(family='Times', size=28)
        title["font"] = ft
        title["fg"] = "#010101"
        title["justify"] = "center"
        title["text"] = "T R I P   C O O R D I N A T O R"
        title.place(x=0, y=0, width=width, height=52)

        lb_username = tk.Label(figure)
        lb_username["bg"] = "#1e90ff"
        ft = tkf.Font(family='Times', size=12, weight="normal")
        lb_username["font"] = ft
        lb_username["fg"] = "#000000"
        lb_username["justify"] = "center"
        lb_username["text"] = "Username"
        lb_username.place(x=170, y=190, width=80, height=40)

        self.edit_username = tk.Entry(figure)
        self.edit_username["bg"] = "#5e94db"
        self.edit_username["borderwidth"] = "5px"
        self.edit_username["relief"] = tk.FLAT
        ft = tkf.Font(family='Times', size=12, weight="normal")
        self.edit_username["font"] = ft
        self.edit_username["fg"] = "#333333"
        self.edit_username["justify"] = "left"
        self.edit_username["text"] = ""
        self.edit_username.place(x=250, y=190, width=250, height=40)

        lb_contact = tk.Label(figure)
        lb_contact["bg"] = "#1e90ff"
        ft = tkf.Font(family='Times', size=12, weight="normal")
        lb_contact["font"] = ft
        lb_contact["fg"] = "#000000"
        lb_contact["justify"] = "center"
        lb_contact["text"] = "Password"
        lb_contact.place(x=170, y=270, width=80, height=40)

        self.edit_contact = tk.Entry(figure)
        self.edit_contact["bg"] = "#5e94db"
        self.edit_contact["borderwidth"] = "5px"
        self.edit_contact["relief"] = tk.FLAT
        ft = tkf.Font(family='Times', size=12, weight="normal")
        self.edit_contact["font"] = ft
        self.edit_contact["fg"] = "#333333"
        self.edit_contact["justify"] = "left"
        self.edit_contact["text"] = ""
        self.edit_contact["show"] = "*"
        self.edit_contact.place(x=250, y=270, width=250, height=40)

        btn_login = tk.Button(figure)
        btn_login["activebackground"] = "#5e75db"
        btn_login["anchor"] = "center"
        btn_login["bg"] = "#5e94db"
        btn_login["borderwidth"] = "1px"
        btn_login["relief"] = tk.GROOVE
        ft = tkf.Font(family='Times', size=15)
        btn_login["font"] = ft
        btn_login["fg"] = "#000000"
        btn_login["justify"] = "center"
        btn_login["text"] = "LOGIN"
        btn_login.place(x=220, y=390, width=250, height=40)
        btn_login["command"] = lambda: self.btnLoginHandler(figure)

    def btnLoginHandler(self, figure):
        username = self.edit_username.get()
        contact = self.edit_contact.get()

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
