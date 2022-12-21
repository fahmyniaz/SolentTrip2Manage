import tkinter as tk
import tkinter.font as tkf
from datetime import datetime
from tkinter import ttk

from src.Coding.TripManager import TripManager
from src.User_Interface.CoordinatorLogin import CoordinatorLogin


class TripManagerPage:

    def __init__(self, figure, username, contact):

        self.TRIPS = {"+ CREATE NEW": None}
        self.COORDINATORS = {"+ CREATE NEW": None}
        all_users = TripManager.SYSTEM_USERS
        self.user = None
        for user in all_users:
            if user.name == username and user.contact == contact:
                self.user = user
        if self.user is None:
            raise ModuleNotFoundError
        if hasattr(self.user, 'trips_under_supervision'):
            for trip in self.user.trips_under_supervision:
                self.TRIPS[trip.name] = trip

        if hasattr(self.user, 'trip_coordinators'):
            for coordinator in self.user.trip_coordinators:
                self.COORDINATORS[coordinator.name] = coordinator
        figure.title("Trip Management")
        figure["bg"] = "#e3e8cd"
        width = 1000
        height = 450
        screenwidth = figure.winfo_screenwidth()
        screenheight = figure.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        figure.geometry(alignstr)
        figure.resizable(width=False, height=False)

        lbl_Title = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=18)
        lbl_Title["bg"] = "#e3e8cd"
        lbl_Title["font"] = ft
        lbl_Title["fg"] = "#800000"
        lbl_Title["justify"] = "left"
        lbl_Title["text"] = "Trip Management"
        lbl_Title.place(x=20, y=5, width=350, height=33)

        lbl_sel_trip = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_sel_trip["bg"] = "#e3e8cd"
        lbl_sel_trip["font"] = ft
        lbl_sel_trip["fg"] = "#333333"
        lbl_sel_trip["justify"] = "center"
        lbl_sel_trip["text"] = "Select Trip"
        lbl_sel_trip.place(x=30, y=45, width=100, height=30)

        self.combo_trip = ttk.Combobox(figure,
                                       state="readonly",
                                       values=list(self.TRIPS.keys()),
                                       textvariable=tk.StringVar())
        self.combo_trip.grid(column=1, row=5)
        self.combo_trip.place(x=180, y=45, width=176, height=30)
        self.combo_trip.current(0)

        lbl_TrName = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_TrName["bg"] = "#e3e8cd"
        lbl_TrName["font"] = ft
        lbl_TrName["fg"] = "#333333"
        lbl_TrName["justify"] = "center"
        lbl_TrName["text"] = "Trip Name"
        lbl_TrName.place(x=30, y=90, width=100, height=30)

        self.edit_trip_name = tk.Entry(figure)
        self.edit_trip_name["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_trip_name["font"] = ft
        self.edit_trip_name["fg"] = "#333333"
        self.edit_trip_name["justify"] = "left"
        self.edit_trip_name["text"] = ""
        self.edit_trip_name.place(x=180, y=90, width=176, height=30)

        lbl_StDate = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=10)
        lbl_StDate["bg"] = "#e3e8cd"
        lbl_StDate["font"] = ft
        lbl_StDate["fg"] = "#333333"
        lbl_StDate["justify"] = "center"
        lbl_StDate["text"] = "Start Date (YYYY-MM-DD)"
        lbl_StDate.place(x=10, y=140, width=180, height=30)

        self.edit_start_date = tk.Entry(figure)
        self.edit_start_date["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_start_date["font"] = ft
        self.edit_start_date["fg"] = "#333333"
        self.edit_start_date["justify"] = "left"
        self.edit_start_date["text"] = ""
        self.edit_start_date.place(x=180, y=140, width=176, height=30)

        lbl_trConNo = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_trConNo["bg"] = "#e3e8cd"
        lbl_trConNo["font"] = ft
        lbl_trConNo["fg"] = "#333333"
        lbl_trConNo["justify"] = "center"
        lbl_trConNo["text"] = "Contact Number"
        lbl_trConNo.place(x=25, y=190, width=150, height=30)

        self.edit_trip_contact_no = tk.Entry(figure)
        self.edit_trip_contact_no["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_trip_contact_no["font"] = ft
        self.edit_trip_contact_no["fg"] = "#333333"
        self.edit_trip_contact_no["justify"] = "left"
        self.edit_trip_contact_no["text"] = ""
        self.edit_trip_contact_no.place(x=180, y=190, width=176, height=30)

        lbl_Sel_Cord = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_Sel_Cord["bg"] = "#e3e8cd"
        lbl_Sel_Cord["font"] = ft
        lbl_Sel_Cord["fg"] = "#333333"
        lbl_Sel_Cord["justify"] = "center"
        lbl_Sel_Cord["text"] = "Select Coordinator"
        lbl_Sel_Cord.place(x=30, y=240, width=150, height=30)

        self.combo_select_trip_coordinator = ttk.Combobox(figure,
                                                          state="readonly",
                                                          values=list(self.COORDINATORS.keys())[1:],
                                                          textvariable=tk.StringVar())
        self.combo_select_trip_coordinator.grid(column=1, row=5)
        self.combo_select_trip_coordinator.place(x=180, y=240, width=176, height=30)
        self.combo_select_trip_coordinator.current()

        btn_add_trip = tk.Button(figure)
        btn_add_trip["bg"] = "green"
        ft = tkf.Font(family='Arial', size=12)
        btn_add_trip["font"] = ft
        btn_add_trip["fg"] = "#ffffff"
        btn_add_trip["justify"] = "center"
        btn_add_trip["text"] = "Add Trip"
        btn_add_trip.place(x=60, y=290, width=120, height=50)
        btn_add_trip["command"] = self.btnAddTripHandler

        btn_update_trip = tk.Button(figure)
        btn_update_trip["bg"] = "blue"
        ft = tkf.Font(family='Arial', size=12)
        btn_update_trip["font"] = ft
        btn_update_trip["fg"] = "#ffffff"
        btn_update_trip["justify"] = "center"
        btn_update_trip["text"] = "Update Trip"
        btn_update_trip.place(x=220, y=290, width=120, height=50)
        btn_update_trip["command"] = self.btnUpdateTripHandler

        btn_delete_trip = tk.Button(figure)
        btn_delete_trip["bg"] = "red"
        ft = tkf.Font(family='Arial', size=12)
        btn_delete_trip["font"] = ft
        btn_delete_trip["fg"] = "#ffffff"
        btn_delete_trip["justify"] = "center"
        btn_delete_trip["text"] = "Delete Trip"
        btn_delete_trip.place(x=140, y=370, width=120, height=50)
        btn_delete_trip["command"] = self.btnDeleteTripHandler

        lbl_Coor_Man = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=18)
        lbl_Coor_Man["bg"] = "#e3e8cd"
        lbl_Coor_Man["font"] = ft
        lbl_Coor_Man["fg"] = "#800000"
        lbl_Coor_Man["justify"] = "left"
        lbl_Coor_Man["text"] = "Coordinator Management"
        lbl_Coor_Man.place(x=600, y=5, width=350, height=33)

        lbl_Sel_Cor = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_Sel_Cor["bg"] = "#e3e8cd"
        lbl_Sel_Cor["font"] = ft
        lbl_Sel_Cor["fg"] = "#333333"
        lbl_Sel_Cor["justify"] = "center"
        lbl_Sel_Cor["text"] = "Select Coordinator"
        lbl_Sel_Cor.place(x=600, y=45, width=150, height=30)

        self.combo_select_coordinator = ttk.Combobox(figure,
                                                     state="readonly",
                                                     values=list(self.COORDINATORS.keys()),
                                                     textvariable=tk.StringVar())
        self.combo_select_coordinator.grid(column=1, row=5)
        self.combo_select_coordinator.place(x=750, y=45, width=176, height=30)
        self.combo_select_coordinator.current(0)

        lbl_Name = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_Name["bg"] = "#e3e8cd"
        lbl_Name["font"] = ft
        lbl_Name["fg"] = "#333333"
        lbl_Name["justify"] = "center"
        lbl_Name["text"] = "Name"
        lbl_Name.place(x=585, y=90, width=100, height=30)

        self.edit_coordinator_name = tk.Entry(figure)
        self.edit_coordinator_name["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_coordinator_name["font"] = ft
        self.edit_coordinator_name["fg"] = "#333333"
        self.edit_coordinator_name["justify"] = "left"
        self.edit_coordinator_name["text"] = ""
        self.edit_coordinator_name.place(x=750, y=90, width=176, height=30)

        lbl_psw = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_psw["bg"] = "#e3e8cd"
        lbl_psw["font"] = ft
        lbl_psw["fg"] = "#333333"
        lbl_psw["justify"] = "center"
        lbl_psw["text"] = "Password"
        lbl_psw.place(x=600, y=140, width=100, height=30)

        self.edit_coor_psw = tk.Entry(figure)
        self.edit_coor_psw["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_coor_psw["font"] = ft
        self.edit_coor_psw["fg"] = "#333333"
        self.edit_coor_psw["justify"] = "left"
        self.edit_coor_psw["text"] = ""
        self.edit_coor_psw.place(x=750, y=140, width=176, height=30)

        btn_add_coordinator = tk.Button(figure)
        btn_add_coordinator["bg"] = "green"
        ft = tkf.Font(family='Arial', size=12)
        btn_add_coordinator["font"] = ft
        btn_add_coordinator["fg"] = "#ffffff"
        btn_add_coordinator["justify"] = "center"
        btn_add_coordinator["text"] = "Add Coordinator"
        btn_add_coordinator.place(x=615, y=200, width=150, height=50)
        btn_add_coordinator["command"] = self.btnAddCoordinatorHandler

        btn_update_coordinator = tk.Button(figure)
        btn_update_coordinator["bg"] = "blue"
        ft = tkf.Font(family='Arial', size=12)
        btn_update_coordinator["font"] = ft
        btn_update_coordinator["fg"] = "#ffffff"
        btn_update_coordinator["justify"] = "center"
        btn_update_coordinator["text"] = "Update Coordinator"
        btn_update_coordinator.place(x=785, y=200, width=150, height=50)
        btn_update_coordinator["command"] = self.btnUpdateCoordinatorHandler

        btn_delete_coordinator = tk.Button(figure)
        btn_delete_coordinator["bg"] = "red"
        ft = tkf.Font(family='Arial', size=12)
        btn_delete_coordinator["font"] = ft
        btn_delete_coordinator["fg"] = "#ffffff"
        btn_delete_coordinator["justify"] = "center"
        btn_delete_coordinator["text"] = "Delete Coordinator"
        btn_delete_coordinator.place(x=700, y=270, width=150, height=50)
        btn_delete_coordinator["command"] = self.btnDeleteCoordinatorHandler

        btn_print_invoice = tk.Button(figure)
        btn_print_invoice["bg"] = "green"
        ft = tkf.Font(family='Arial', size=18)
        btn_print_invoice["font"] = ft
        btn_print_invoice["fg"] = "#ffffff"
        btn_print_invoice["justify"] = "center"
        btn_print_invoice["text"] = "Print Invoice"
        btn_print_invoice.place(x=620, y=360, width=320, height=60)
        btn_print_invoice["command"] = self.btnInvoicePrinter

    def btnAddTripHandler(self):
        trip_name = self.edit_trip_name.get()
        trip_date = datetime(*map(int, self.edit_start_date.get().split("-")))
        trip_contact = self.edit_trip_contact_no.get()

        trip_coordinator_name = self.combo_select_trip_coordinator.get()
        trip_coordinator = None

        if trip_coordinator_name in self.COORDINATORS:
            trip_coordinator = self.COORDINATORS[trip_coordinator_name]

        new_trip = self.user.createManagerTrip(trip_name,
                                        trip_date,
                                        trip_contact,
                                        trip_coordinator)
        if new_trip is not None:
            self.TRIPS[new_trip.name] = new_trip
            self.combo_trip.configure(values=list(self.TRIPS.keys()))

            self.edit_trip_name.delete(0, tk.END)
            self.edit_start_date.delete(0, tk.END)
            self.edit_trip_contact_no.delete(0, tk.END)
            self.combo_select_trip_coordinator.current(0)

            print("Successfully Added trip to " + new_trip.name + " ")
        else:
            print("Oops!!! Creating trip failed")

    def btnUpdateTripHandler(self):
        update_trip_name = self.combo_trip.get()
        trip = self.TRIPS[update_trip_name]

        trip_name = self.edit_trip_name.get()
        trip_date = datetime(*map(int, self.edit_start_date.get().split("-")))
        trip_contact = self.edit_trip_contact_no.get()

        update_result = self.user.updateManagerTrip(trip, trip_name, trip_date, trip_contact)

        if update_result == 1:
            print("Successfully Updated " + trip.name + " ")

            self.TRIPS[trip_name] = self.TRIPS.pop(update_trip_name)

            self.combo_trip.configure(values=list(self.TRIPS.keys()))
            self.combo_trip.current(0)

            self.edit_trip_name.delete(0, tk.END)
            self.edit_start_date.delete(0, tk.END)
            self.edit_trip_contact_no.delete(0, tk.END)

        else:
            print("Oops!!! Update Failed")

    def btnDeleteTripHandler(self):
        delete_obj_name = self.combo_trip.get()
        delete_object = self.TRIPS[delete_obj_name]

        delete_result = self.user.deleteTrip(delete_object)

        if delete_result == 1:
            print("Successfully deleted " + delete_obj_name)
            self.TRIPS.pop(delete_obj_name)

            self.combo_trip.configure(values=list(self.TRIPS.keys()))

            self.combo_trip.current(0)

            self.edit_trip_name.delete(0, tk.END)
            self.edit_start_date.delete(0, tk.END)
            self.edit_trip_contact_no.delete(0, tk.END)

        else:
            print("Oops!!! Delete Trip Failed")

    def btnAddCoordinatorHandler(self):
        name = self.edit_coordinator_name.get()
        contact = self.edit_coor_psw.get()

        new_coordinator = self.user.createCoordinator(name, contact)

        CoordinatorLogin.COORDINATORS.append(new_coordinator)
        self.COORDINATORS[new_coordinator.name] = new_coordinator

        print("Trip Coordinator Added Successfully")
        self.edit_coordinator_name.delete(0, tk.END)
        self.edit_coor_psw.delete(0, tk.END)

        self.combo_select_coordinator.configure(values=list(self.COORDINATORS.keys()))
        self.combo_select_trip_coordinator.configure(values=list(self.COORDINATORS.keys())[1:])
        self.combo_select_trip_coordinator.current(0)

    def btnUpdateCoordinatorHandler(self):

        update_obj_name = self.combo_select_coordinator.get()
        update_object = self.COORDINATORS[update_obj_name]

        new_name = self.edit_coordinator_name.get()
        new_contact = self.edit_coor_psw.get()
        update_result = self.user.updateCoordinator(update_object, new_name, new_contact)

        if update_result == 1:
            print("Successfully Updated ")

            self.COORDINATORS[new_name] = self.COORDINATORS.pop(update_obj_name)
            self.combo_select_coordinator.configure(values=list(self.COORDINATORS.keys()))
            self.combo_select_trip_coordinator.configure(values=list(self.COORDINATORS.keys())[1:])

            self.combo_select_coordinator.current(0)
            self.combo_select_trip_coordinator.set("")
            self.edit_coordinator_name.delete(0, tk.END)
            self.edit_coor_psw.delete(0, tk.END)

        else:
            print("Oops!!! Update Failed")

    def btnDeleteCoordinatorHandler(self):
        delete_onj_name = self.combo_select_coordinator.get()
        delete_object = self.COORDINATORS[delete_onj_name]

        delete_result = self.user.deleteCoordinator(delete_object)

        if delete_result == 1:
            print("Successfully Deleted " + delete_onj_name)
            self.COORDINATORS.pop(delete_onj_name)
            CoordinatorLogin.COORDINATORS.remove(delete_object)

            self.combo_select_coordinator.configure(values=list(self.COORDINATORS.keys()))
            self.combo_select_trip_coordinator.configure(values=list(self.COORDINATORS.keys())[1:])

            self.combo_select_coordinator.current(0)
            self.combo_select_trip_coordinator.set("")
            self.edit_coordinator_name.delete(0, tk.END)
            self.edit_coor_psw.delete(0, tk.END)

        else:
            print("Oops!!! Delete Coordinator Failed")

    def btnInvoicePrinter(self):
        print(self.user.printManagerInvoice())


if __name__ == "__main__":
    root = tk.Tk()
    app = TripManagerPage(root, "test", "1234")
    root.mainloop()
