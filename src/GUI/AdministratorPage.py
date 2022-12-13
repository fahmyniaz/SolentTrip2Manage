import tkinter as tk
import tkinter.font as tkf
from tkinter import ttk

from src.Code.Administrator import Administrator
from src.GUI.ManagerLogin import ManagerLogin
from src.GUI.TripManagerPage import TripManagerPage
from src.GUI.TripCoordinatorPage import TripCoordinatorPage


class AdministratorPage:

    def __init__(self, figure, username, contact):

        self.MANAGERS = {"Choose below": None}

        # user
        all_users = Administrator.SYSTEM_USERS
        self.user = None

        # get the current user in the session
        for user in all_users:
            if user.name == username and user.contact == contact:
                self.user = user

        # if the user is not found
        if self.user is None:
            raise ModuleNotFoundError

        for manager in self.user.trip_managers:
            self.MANAGERS[manager.name] = manager

        # setting title
        figure.title("Admin")

        # setting window size
        width = 800
        height = 400
        screenwidth = figure.winfo_screenwidth()
        screenheight = figure.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        figure.geometry(alignstr)
        figure.resizable(width=False, height=False)

        TitleLabel = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=18)
        TitleLabel["font"] = ft
        TitleLabel["fg"] = "#800000"
        TitleLabel["text"] = "Manage Trip Page"
        TitleLabel.place(x=300, y=20, width=218, height=30)

        GLabel_587 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_587["font"] = ft
        GLabel_587["fg"] = "#008080"
        GLabel_587["justify"] = "center"
        GLabel_587["text"] = "Choose Manager"
        GLabel_587.place(x=30, y=70, width=100, height=30)

        self.combo_select_manager = ttk.Combobox(figure,
                                                 state="readonly",
                                                 values=list(self.MANAGERS.keys()),
                                                 textvariable=tk.StringVar())
        self.combo_select_manager.grid(column=1, row=5)
        self.combo_select_manager.place(x=140, y=70, width=176, height=30)
        self.combo_select_manager.current(0)

        GLabel_564 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_564["font"] = ft
        GLabel_564["fg"] = "#008080"
        GLabel_564["justify"] = "center"
        GLabel_564["text"] = "Name"
        GLabel_564.place(x=30, y=110, width=100, height=30)

        self.edit_manager_name = tk.Entry(figure)
        self.edit_manager_name["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_manager_name["font"] = ft
        self.edit_manager_name["fg"] = "#008080"
        self.edit_manager_name["justify"] = "left"
        self.edit_manager_name["text"] = ""
        self.edit_manager_name.place(x=140, y=110, width=176, height=30)

        GLabel_377 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_377["font"] = ft
        GLabel_377["fg"] = "#008080"
        GLabel_377["justify"] = "center"
        GLabel_377["text"] = "Password"
        GLabel_377.place(x=30, y=150, width=100, height=30)

        self.edit_manager_contact = tk.Entry(figure)
        self.edit_manager_contact["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_manager_contact["font"] = ft
        self.edit_manager_contact["fg"] = "#008080"
        self.edit_manager_contact["justify"] = "left"
        self.edit_manager_contact["text"] = ""
        self.edit_manager_contact.place(x=140, y=150, width=176, height=30)

        btn_manager_view = tk.Button(figure)
        btn_manager_view["bg"] = "#efefef"
        ft = tkf.Font(family='Arial', size=12)
        btn_manager_view["font"] = ft
        btn_manager_view["fg"] = "#008080"
        btn_manager_view["justify"] = "center"
        btn_manager_view["text"] = "Manager Access"
        btn_manager_view.place(x=140, y=190, width=176, height=30)
        btn_manager_view["command"] = lambda: self.btnOpenManagerHandler(figure, username, contact)

        btn_coordinator_view = tk.Button(figure)
        btn_coordinator_view["bg"] = "#efefef"
        ft = tkf.Font(family='Arial', size=12)
        btn_coordinator_view["font"] = ft
        btn_coordinator_view["fg"] = "#008080"
        btn_coordinator_view["justify"] = "center"
        btn_coordinator_view["text"] = "Coordinator Access"
        btn_coordinator_view.place(x=140, y=230, width=176, height=30)
        btn_coordinator_view["command"] = lambda: self.btnOpenCoordinatorHandler(figure, username, contact)

        btn_add_manager = tk.Button(figure)
        btn_add_manager["bg"] = "#FFFFFF"
        ft = tkf.Font(family='Arial', size=12)
        btn_add_manager["font"] = ft
        btn_add_manager["fg"] = "Green"
        btn_add_manager["justify"] = "center"
        btn_add_manager["text"] = "Create Manager"
        btn_add_manager.place(x=150, y=300, width=150, height=30)
        btn_add_manager["command"] = self.btnAddManagerHandler

        btn_update_manager = tk.Button(figure)
        btn_update_manager["bg"] = "#FFFFFF"
        ft = tkf.Font(family='Arial', size=12)
        btn_update_manager["font"] = ft
        btn_update_manager["fg"] = "Blue"
        btn_update_manager["justify"] = "center"
        btn_update_manager["text"] = "Update Manager"
        btn_update_manager.place(x=330, y=300, width=150, height=30)
        btn_update_manager["command"] = self.btnUpdateManagerHandler

        btn_delete_manager = tk.Button(figure)
        btn_delete_manager["bg"] = "#FFFFFF"
        ft = tkf.Font(family='Arial', size=12)
        btn_delete_manager["font"] = ft
        btn_delete_manager["fg"] = "Red"
        btn_delete_manager["justify"] = "center"
        btn_delete_manager["text"] = "Delete Manager"
        btn_delete_manager.place(x=510, y=300, width=150, height=30)
        btn_delete_manager["command"] = self.btnDeleteManagerHandler

        btn_print_invoice = tk.Button(figure)
        btn_print_invoice["bg"] = "Green"
        ft = tkf.Font(family='Times', size=14)
        btn_print_invoice["font"] = ft
        btn_print_invoice["fg"] = "White"
        btn_print_invoice["justify"] = "center"
        btn_print_invoice["text"] = "Print Receipt"
        btn_print_invoice.place(x=580, y=350, width=180, height=50)
        btn_print_invoice["command"] = self.btnInvoicePrinter

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
        contact = self.edit_manager_contact.get()

        newManager = self.user.createTripManager(name, contact)

        ManagerLogin.MANAGERS.append(newManager)
        self.MANAGERS[newManager.name] = newManager

        print("Manager Created Successfully!!!")
        self.edit_manager_name.delete(0, tk.END)
        self.edit_manager_contact.delete(0, tk.END)

        # This will update the combo box
        self.combo_select_manager.configure(values=list(self.MANAGERS.keys()))

    def btnUpdateManagerHandler(self):

        # code to find the manager object to update
        update_obj_name = self.combo_select_manager.get()
        update_object = self.MANAGERS[update_obj_name]

        new_name = self.edit_manager_name.get()
        new_contact = self.edit_manager_contact.get()

        update_result = self.user.updateManager(update_object, new_name, new_contact)

        if update_result == 1:
            print("Update Successful!!!")

            # Changing drop down dictionary
            self.MANAGERS[new_name] = self.MANAGERS.pop(update_obj_name)
            self.combo_select_manager.configure(values=list(self.MANAGERS.keys()))

            # assigning default values
            self.combo_select_manager.current(0)
            self.edit_manager_name.delete(0, tk.END)
            self.edit_manager_contact.delete(0, tk.END)

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

            # updating combo box
            self.combo_select_manager.configure(values=list(self.MANAGERS.keys()))

            # assigning default values
            self.combo_select_manager.current(0)
            self.edit_manager_name.delete(0, tk.END)
            self.edit_manager_contact.delete(0, tk.END)

        else:
            print("Oops!!! Delete Manager Failed!!!")

    def btnInvoicePrinter(self):
        print(self.user.totalInvoice())


if __name__ == "__main__":
    root = tk.Tk()
    app = AdministratorPage(root, "admin", "pw1234")
    root.mainloop()
