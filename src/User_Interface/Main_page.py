import tkinter as tk
import tkinter.font as tkf
from tkinter import Label

from PIL import Image,ImageTk
from tkinter import *

from src.User_Interface.ManagerLogin import ManagerLogin
from src.User_Interface.AdminLogin import AdminLogin
from src.User_Interface.CoordinatorLogin import CoordinatorLogin


class App:
    def __init__(self, figure):
        figure.title("Solent Trip Main Page")
        figure["bg"] = "#e3e8cd"
        width = 850
        height = 250
        screenwidth = figure.winfo_screenwidth()
        screenheight = figure.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        figure.geometry(alignstr)
        figure.resizable(width=False, height=False)

        title = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=26)
        title["bg"] = "#e3e8cd"
        title["font"] = ft
        title["fg"] = "#800000"
        title["justify"] = "center"
        title["text"] = " Solent Trip Management"
        title.place(x=0, y=0, width=width, height=52)

        btn_admin = tk.Button(figure)
        btn_admin["activebackground"] = "#57ef57"
        btn_admin["anchor"] = "center"
        btn_admin["bg"] = "#008080"
        btn_admin["bd"] = 1
        ft = tkf.Font(family='Arial', size=22)
        btn_admin["font"] = ft
        btn_admin["fg"] = "#ffffff"
        btn_admin["justify"] = "center"
        btn_admin["text"] = "Admin"
        btn_admin.place(x=20, y=100, width=270, height=100)
        btn_admin["command"] = lambda: self.btnAdminHandler(figure)

        btn_manager = tk.Button(figure)
        btn_manager["activebackground"] = "#57ef57"
        btn_manager["anchor"] = "center"
        btn_manager["bg"] = "#008080"
        btn_manager["bd"] = 1
        ft = tkf.Font(family='Times', size=22)
        btn_manager["font"] = ft
        btn_manager["fg"] = "#ffffff"
        btn_manager["justify"] = "center"
        btn_manager["text"] = "Manager"
        btn_manager.place(x=300, y=100, width=250, height=100)
        btn_manager["command"] = lambda: self.btnManagerHandler(figure)

        btn_coordinator = tk.Button(figure)
        btn_coordinator["activebackground"] = "#57ef57"
        btn_coordinator["anchor"] = "center"
        btn_coordinator["bg"] = "#008080"
        btn_coordinator["bd"] = 1
        ft = tkf.Font(family='Times', size=22)
        btn_coordinator["font"] = ft
        btn_coordinator["fg"] = "#ffffff"
        btn_coordinator["justify"] = "center"
        btn_coordinator["text"] = "Coordinator"
        btn_coordinator.place(x=560, y=100, width=250, height=100)
        btn_coordinator["command"] = lambda: self.btnCoordinatorHandler(figure)



    @staticmethod
    def btnAdminHandler(figure):
        adminLoginFigure = tk.Toplevel(figure)
        AdminLogin(adminLoginFigure)
        adminLoginFigure.mainloop()

    @staticmethod
    def btnManagerHandler(figure):
        managerLoginFigure = tk.Toplevel(figure)
        ManagerLogin(managerLoginFigure)
        managerLoginFigure.mainloop()

    @staticmethod
    def btnCoordinatorHandler(figure):
        coorLoginFigure = tk.Toplevel(figure)
        CoordinatorLogin(coorLoginFigure)
        coorLoginFigure.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
