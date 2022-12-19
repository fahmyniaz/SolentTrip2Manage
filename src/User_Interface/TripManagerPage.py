import tkinter as tk
import tkinter.font as tkf
from datetime import datetime
from tkinter import ttk

from src.Code.TripManager import TripManager
from src.User_Interface.CoordinatorLogin import CoordinatorLogin


class TripManagerPage:

    def __init__(self, figure, username, contact):

        self.TRIPS = {"+ CREATE NEW": None}
        self.COORDINATORS = {"+ CREATE NEW": None}

        # user
        all_users = TripManager.SYSTEM_USERS
        self.user = None

        # get the current user in the session
        for user in all_users:
            if user.name == username and user.contact == contact:
                self.user = user

        # if the user is not found
        if self.user is None:
            raise ModuleNotFoundError

        # retrieving trips and coordinators from the user
        if hasattr(self.user, 'trips_under_supervision'):
            for trip in self.user.trips_under_supervision:
                self.TRIPS[trip.name] = trip

        if hasattr(self.user, 'trip_coordinators'):
            for coordinator in self.user.trip_coordinators:
                self.COORDINATORS[coordinator.name] = coordinator

        # setting title
        figure.title("Trip Management")

        # setting window size
        figure["bg"] = "#e3e8cd"
        width = 1000
        height = 450
        screenwidth = figure.winfo_screenwidth()
        screenheight = figure.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        figure.geometry(alignstr)
        figure.resizable(width=False, height=False)

        GLabel_654 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=18)
        GLabel_654["bg"] = "#e3e8cd"
        GLabel_654["font"] = ft
        GLabel_654["fg"] = "#800000"
        GLabel_654["justify"] = "left"
        GLabel_654["text"] = "Trip Management"
        GLabel_654.place(x=20, y=5, width=350, height=33)

        GLabel_515 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_515["bg"] = "#e3e8cd"
        GLabel_515["font"] = ft
        GLabel_515["fg"] = "#333333"
        GLabel_515["justify"] = "center"
        GLabel_515["text"] = "Select Trip"
        GLabel_515.place(x=30, y=45, width=100, height=30)

        self.combo_trip = ttk.Combobox(figure,
                                       state="readonly",
                                       values=list(self.TRIPS.keys()),
                                       textvariable=tk.StringVar())
        self.combo_trip.grid(column=1, row=5)
        self.combo_trip.place(x=180, y=45, width=176, height=30)
        self.combo_trip.current(0)

        GLabel_230 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_230["bg"] = "#e3e8cd"
        GLabel_230["font"] = ft
        GLabel_230["fg"] = "#333333"
        GLabel_230["justify"] = "center"
        GLabel_230["text"] = "Trip Name"
        GLabel_230.place(x=30, y=90, width=100, height=30)

        self.edit_trip_name = tk.Entry(figure)
        self.edit_trip_name["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_trip_name["font"] = ft
        self.edit_trip_name["fg"] = "#333333"
        self.edit_trip_name["justify"] = "left"
        self.edit_trip_name["text"] = ""
        self.edit_trip_name.place(x=180, y=90, width=176, height=30)

        GLabel_766 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_766["bg"] = "#e3e8cd"
        GLabel_766["font"] = ft
        GLabel_766["fg"] = "#333333"
        GLabel_766["justify"] = "center"
        GLabel_766["text"] = "Start Date (YYYY-MM-DD)"
        GLabel_766.place(x=30, y=140, width=100, height=30)

        self.edit_start_date = tk.Entry(figure)
        self.edit_start_date["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_start_date["font"] = ft
        self.edit_start_date["fg"] = "#333333"
        self.edit_start_date["justify"] = "left"
        self.edit_start_date["text"] = ""
        self.edit_start_date.place(x=180, y=140, width=176, height=30)

        GLabel_trip_contact = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_trip_contact["bg"] = "#e3e8cd"
        GLabel_trip_contact["font"] = ft
        GLabel_trip_contact["fg"] = "#333333"
        GLabel_trip_contact["justify"] = "center"
        GLabel_trip_contact["text"] = "Contact Number"
        GLabel_trip_contact.place(x=25, y=190, width=150, height=30)

        self.edit_trip_contact = tk.Entry(figure)
        self.edit_trip_contact["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_trip_contact["font"] = ft
        self.edit_trip_contact["fg"] = "#333333"
        self.edit_trip_contact["justify"] = "left"
        self.edit_trip_contact["text"] = ""
        self.edit_trip_contact.place(x=180, y=190, width=176, height=30)

        GLabel_515 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_515["bg"] = "#e3e8cd"
        GLabel_515["font"] = ft
        GLabel_515["fg"] = "#333333"
        GLabel_515["justify"] = "center"
        GLabel_515["text"] = "Select Coordinator"
        GLabel_515.place(x=30, y=240, width=150, height=30)

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

        # TRIP COORDINATOR SETTINGS
        GLabel_955 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=18)
        GLabel_955["bg"] = "#e3e8cd"
        GLabel_955["font"] = ft
        GLabel_955["fg"] = "#800000"
        GLabel_955["justify"] = "left"
        GLabel_955["text"] = "Coordinator Management"
        GLabel_955.place(x=600, y=5, width=350, height=33)

        GLabel_587 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_587["bg"] = "#e3e8cd"
        GLabel_587["font"] = ft
        GLabel_587["fg"] = "#333333"
        GLabel_587["justify"] = "center"
        GLabel_587["text"] = "Select Coordinator"
        GLabel_587.place(x=600, y=45, width=150, height=30)

        self.combo_select_coordinator = ttk.Combobox(figure,
                                                     state="readonly",
                                                     values=list(self.COORDINATORS.keys()),
                                                     textvariable=tk.StringVar())
        self.combo_select_coordinator.grid(column=1, row=5)
        self.combo_select_coordinator.place(x=750, y=45, width=176, height=30)
        self.combo_select_coordinator.current(0)

        GLabel_564 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_564["bg"] = "#e3e8cd"
        GLabel_564["font"] = ft
        GLabel_564["fg"] = "#333333"
        GLabel_564["justify"] = "center"
        GLabel_564["text"] = "Name"
        GLabel_564.place(x=585, y=90, width=100, height=30)

        self.edit_coordinator_name = tk.Entry(figure)
        self.edit_coordinator_name["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_coordinator_name["font"] = ft
        self.edit_coordinator_name["fg"] = "#333333"
        self.edit_coordinator_name["justify"] = "left"
        self.edit_coordinator_name["text"] = ""
        self.edit_coordinator_name.place(x=750, y=90, width=176, height=30)

        GLabel_377 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_377["bg"] = "#e3e8cd"
        GLabel_377["font"] = ft
        GLabel_377["fg"] = "#333333"
        GLabel_377["justify"] = "center"
        GLabel_377["text"] = "Password"
        GLabel_377.place(x=600, y=140, width=100, height=30)

        self.edit_coordinator_contact = tk.Entry(figure)
        self.edit_coordinator_contact["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_coordinator_contact["font"] = ft
        self.edit_coordinator_contact["fg"] = "#333333"
        self.edit_coordinator_contact["justify"] = "left"
        self.edit_coordinator_contact["text"] = ""
        self.edit_coordinator_contact.place(x=750, y=140, width=176, height=30)

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
        trip_contact = self.edit_trip_contact.get()

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
            self.edit_trip_contact.delete(0, tk.END)
            self.combo_select_trip_coordinator.current(0)

            print("Successfully Added trip to " + new_trip.name + " ")
        else:
            print("Oops!!! Creating trip failed")

    def btnUpdateTripHandler(self):
        update_trip_name = self.combo_trip.get()
        trip = self.TRIPS[update_trip_name]

        trip_name = self.edit_trip_name.get()
        trip_date = datetime(*map(int, self.edit_start_date.get().split("-")))
        trip_contact = self.edit_trip_contact.get()

        update_result = self.user.updateManagerTrip(trip, trip_name, trip_date, trip_contact)

        if update_result == 1:
            print("Successfully Updated " + trip.name + " ")

            self.TRIPS[trip_name] = self.TRIPS.pop(update_trip_name)

            self.combo_trip.configure(values=list(self.TRIPS.keys()))
            self.combo_trip.current(0)

            self.edit_trip_name.delete(0, tk.END)
            self.edit_start_date.delete(0, tk.END)
            self.edit_trip_contact.delete(0, tk.END)

        else:
            print("Oops!!! Update Failed")

    def btnDeleteTripHandler(self):
        delete_obj_name = self.combo_trip.get()
        delete_object = self.TRIPS[delete_obj_name]

        delete_result = self.user.deleteTrip(delete_object)

        if delete_result == 1:
            print("Successfully deleted " + delete_obj_name)
            self.TRIPS.pop(delete_obj_name)

            # updating combo box
            self.combo_trip.configure(values=list(self.TRIPS.keys()))

            # assigning default values
            self.combo_trip.current(0)

            self.edit_trip_name.delete(0, tk.END)
            self.edit_start_date.delete(0, tk.END)
            self.edit_trip_contact.delete(0, tk.END)

        else:
            print("Oops!!! Delete Trip Failed")

    def btnAddCoordinatorHandler(self):
        name = self.edit_coordinator_name.get()
        contact = self.edit_coordinator_contact.get()

        new_coordinator = self.user.createCoordinator(name, contact)

        CoordinatorLogin.COORDINATORS.append(new_coordinator)
        self.COORDINATORS[new_coordinator.name] = new_coordinator

        print("Trip Coordinator Added Successfully")
        self.edit_coordinator_name.delete(0, tk.END)
        self.edit_coordinator_contact.delete(0, tk.END)

        # This will update the combo box
        self.combo_select_coordinator.configure(values=list(self.COORDINATORS.keys()))
        self.combo_select_trip_coordinator.configure(values=list(self.COORDINATORS.keys())[1:])
        self.combo_select_trip_coordinator.current(0)

    def btnUpdateCoordinatorHandler(self):

        # code to find the coordinator object to update
        update_obj_name = self.combo_select_coordinator.get()
        update_object = self.COORDINATORS[update_obj_name]

        new_name = self.edit_coordinator_name.get()
        new_contact = self.edit_coordinator_contact.get()
        update_result = self.user.updateCoordinator(update_object, new_name, new_contact)

        if update_result == 1:
            print("Successfully Updated ")

            # Changing drop down dictionary
            self.COORDINATORS[new_name] = self.COORDINATORS.pop(update_obj_name)
            self.combo_select_coordinator.configure(values=list(self.COORDINATORS.keys()))
            self.combo_select_trip_coordinator.configure(values=list(self.COORDINATORS.keys())[1:])

            # assigning default values
            self.combo_select_coordinator.current(0)
            self.combo_select_trip_coordinator.set("")
            self.edit_coordinator_name.delete(0, tk.END)
            self.edit_coordinator_contact.delete(0, tk.END)

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

            # updating combo box
            self.combo_select_coordinator.configure(values=list(self.COORDINATORS.keys()))
            self.combo_select_trip_coordinator.configure(values=list(self.COORDINATORS.keys())[1:])

            # assigning default values
            self.combo_select_coordinator.current(0)
            self.combo_select_trip_coordinator.set("") # clear the text field of the combo box
            self.edit_coordinator_name.delete(0, tk.END)
            self.edit_coordinator_contact.delete(0, tk.END)

        else:
            print("Oops!!! Delete Coordinator Failed")

    def btnInvoicePrinter(self):
        print(self.user.printManagerInvoice())


if __name__ == "__main__":
    root = tk.Tk()
    app = TripManagerPage(root, "test", "1234")
    root.mainloop()
