import tkinter as tk
import tkinter.font as tkf
from tkinter import ttk
from src.User_Interface.TripManagerPage import TripManagerPage
from src.Coding.Administrator import Administrator
from src.User_Interface.TripCoordinatorPage import TripCoordinatorPage
from src.User_Interface.ManagerLogin import ManagerLogin


class AdministratorPage:

    def __init__(self, figure, username, contact):
        self.MANAGERS = {"CHOOSE BELOW": None}

        all_users = Administrator.SYSTEM_USERS
        self.user = None

        for user in all_users:
            if user.name == username and user.contact == contact:
                self.user = user

        if self.user is None:
            raise ModuleNotFoundError

        for manager in self.user.trip_managers:
            self.MANAGERS[manager.name] = manager

        figure.title("Admin")

        figure["bg"] = "#e3e8cd"
        width = 800
        height = 400
        screenwidth = figure.winfo_screenwidth()
        screenheight = figure.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        figure.geometry(alignstr)
        figure.resizable(width=False, height=False)

        TitleLabel = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=18)
        TitleLabel["bg"] = "#e3e8cd"
        TitleLabel["font"] = ft
        TitleLabel["fg"] = "#800000"
        TitleLabel["text"] = "Manage Trip Page"
        TitleLabel.place(x=300, y=20, width=218, height=30)

        SelManager = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        SelManager["bg"] = "#e3e8cd"
        SelManager["font"] = ft
        SelManager["fg"] = "black"
        SelManager["justify"] = "center"
        SelManager["text"] = "Manager"
        SelManager.place(x=215, y=70, width=160, height=30)

        self.combo_select_manager = ttk.Combobox(figure,
                                                 state="readonly",
                                                 values=list(self.MANAGERS.keys()),
                                                 textvariable=tk.StringVar())
        self.combo_select_manager.grid(column=1, row=5)
        self.combo_select_manager.place(x=350, y=70, width=176, height=30)
        self.combo_select_manager.current(0)

        NameAdm = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        NameAdm["bg"] = "#e3e8cd"
        NameAdm["font"] = ft
        NameAdm["fg"] = "black"
        NameAdm["justify"] = "center"
        NameAdm["text"] = "Name"
        NameAdm.place(x=235, y=110, width=100, height=30)

        self.edit_manager_name = tk.Entry(figure)
        self.edit_manager_name["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_manager_name["font"] = ft
        self.edit_manager_name["fg"] = "#008080"
        self.edit_manager_name["justify"] = "left"
        self.edit_manager_name["text"] = ""
        self.edit_manager_name.place(x=350, y=110, width=176, height=30)

        PswAdm = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        PswAdm["bg"] = "#e3e8cd"
        PswAdm["font"] = ft
        PswAdm["fg"] = "black"
        PswAdm["justify"] = "center"
        PswAdm["text"] = "Password"
        PswAdm.place(x=250, y=150, width=100, height=30)

        self.edit_manager_psw = tk.Entry(figure)
        self.edit_manager_psw["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_manager_psw["font"] = ft
        self.edit_manager_psw["fg"] = "#008080"
        self.edit_manager_psw["justify"] = "left"
        self.edit_manager_psw["text"] = ""
        self.edit_manager_psw.place(x=350, y=150, width=176, height=30)

        btn_manager_view = tk.Button(figure)
        btn_manager_view["bg"] = "#efefef"
        ft = tkf.Font(family='Arial', size=12)
        btn_manager_view["font"] = ft
        btn_manager_view["fg"] = "#008080"
        btn_manager_view["justify"] = "center"
        btn_manager_view["text"] = "Manager Access"
        btn_manager_view.place(x=250, y=230, width=176, height=30)
        btn_manager_view["command"] = lambda: self.btnOpenManagerHandler(figure, username, contact)

        btn_coordinator_view = tk.Button(figure)
        btn_coordinator_view["bg"] = "#efefef"
        ft = tkf.Font(family='Arial', size=12)
        btn_coordinator_view["font"] = ft
        btn_coordinator_view["fg"] = "#008080"
        btn_coordinator_view["justify"] = "center"
        btn_coordinator_view["text"] = "Coordinator Access"
        btn_coordinator_view.place(x=450, y=230, width=176, height=30)
        btn_coordinator_view["command"] = lambda: self.btnOpenCoordinatorHandler(figure, username, contact)

        btn_add_manager = tk.Button(figure)
        btn_add_manager["bg"] = "green"
        ft = tkf.Font(family='Arial', size=12)
        btn_add_manager["font"] = ft
        btn_add_manager["fg"] = "#FFFFFF"
        btn_add_manager["justify"] = "center"
        btn_add_manager["text"] = "Create Manager"
        btn_add_manager.place(x=150, y=300, width=150, height=30)
        btn_add_manager["command"] = self.btnAddManagerHandler

        btn_update_manager = tk.Button(figure)
        btn_update_manager["bg"] = "blue"
        ft = tkf.Font(family='Arial', size=12)
        btn_update_manager["font"] = ft
        btn_update_manager["fg"] = "#FFFFFF"
        btn_update_manager["justify"] = "center"
        btn_update_manager["text"] = "Update Manager"
        btn_update_manager.place(x=330, y=300, width=150, height=30)
        btn_update_manager["command"] = self.btnUpdateManagerHandler

        btn_delete_manager = tk.Button(figure)
        btn_delete_manager["bg"] = "red"
        ft = tkf.Font(family='Arial', size=12)
        btn_delete_manager["font"] = ft
        btn_delete_manager["fg"] = "#FFFFFF"
        btn_delete_manager["justify"] = "center"
        btn_delete_manager["text"] = "Delete Manager"
        btn_delete_manager.place(x=510, y=300, width=150, height=30)
        btn_delete_manager["command"] = self.btnDeleteManagerHandler


    def btnOpenManagerHandler(self, figure, username, contact):
        managerFigure = tk.Toplevel(figure)
        TripManagerPage(managerFigure, username, contact)
        managerFigure.mainloop()

    def btnOpenCoordinatorHandler(self, figure, username, contact):
        coordinatorFigure = tk.Toplevel(figure)
        TripCoordinatorPage(coordinatorFigure, username, contact)
        coordinatorFigure.mainloop()

    def btnAddManagerHandler(self):
        name = self.edit_manager_name.get()
        contact = self.edit_manager_psw.get()

        newManager = self.user.createTripManager(name, contact)

        ManagerLogin.MANAGERS.append(newManager)
        self.MANAGERS[newManager.name] = newManager

        print("Manager Created Successfully!!!")
        self.edit_manager_name.delete(0, tk.END)
        self.edit_manager_psw.delete(0, tk.END)
        self.combo_select_manager.configure(values=list(self.MANAGERS.keys()))

    def btnUpdateManagerHandler(self):
        update_obj_name = self.combo_select_manager.get()
        update_object = self.MANAGERS[update_obj_name]

        new_name = self.edit_manager_name.get()
        new_contact = self.edit_manager_psw.get()

        update_result = self.user.updateManager(update_object, new_name, new_contact)

        if update_result == 1:
            print("Updated Successfully!!!")
            self.MANAGERS[new_name] = self.MANAGERS.pop(update_obj_name)
            self.combo_select_manager.configure(values=list(self.MANAGERS.keys()))

            self.combo_select_manager.current(0)
            self.edit_manager_name.delete(0, tk.END)
            self.edit_manager_psw.delete(0, tk.END)

        else:
            print("Oops!!! Update Failed!!!")

    def btnDeleteManagerHandler(self):

        delete_obj_name = self.combo_select_manager.get()
        delete_object = self.MANAGERS[delete_obj_name]

        delete_result = self.user.deleteManager(delete_object)

        if delete_result == 1:
            print("Deleted Successfully " + delete_obj_name)
            self.MANAGERS.pop(delete_obj_name)
            ManagerLogin.MANAGERS.remove(delete_object)
            self.combo_select_manager.configure(values=list(self.MANAGERS.keys()))
            self.combo_select_manager.current(0)
            self.edit_manager_name.delete(0, tk.END)
            self.edit_manager_psw.delete(0, tk.END)

        else:
            print("Oops!!! Delete Manager Failed!!!")

    def btnInvoicePrinter(self):
        print(self.user.totalInvoice())


if __name__ == "__main__":
    root = tk.Tk()
    app = AdministratorPage(root, "admin", "pw1234")
    root.mainloop()
