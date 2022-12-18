import tkinter as tk
import tkinter.font as tkf
from datetime import datetime
from tkinter import ttk

from src.Code.ModeOfTravel import ModeOfTravel
from src.Code.TripCoordinator import TripCoordinator


class TripCoordinatorPage:

    def __init__(self, figure, username, contact):

        self.TRIPS = {"+ Add New": None}
        self.PASSENGERS = {}

        # user
        all_users = TripCoordinator.SYSTEM_USERS
        self.user = None

        # get the current user in the session
        for user in all_users:
            if user.name == username and user.contact == contact:
                self.user = user

        # if the user is not found
        if self.user is None:
            raise ModuleNotFoundError

        # retrieving trips from the user instance
        if hasattr(self.user, 'tripsCoordinating'):
            for trip in self.user.tripsCoordinating:
                self.TRIPS[trip.name] = trip

        if hasattr(self.user, 'passangers'):
            for passenger in self.user.passangers:
                self.PASSENGERS[passenger.name] = passenger

        # setting title
        figure.title("Trip Coordinator")

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
        ft = tkf.Font(family='Arial', size=16)
        GLabel_654["bg"] = "#e3e8cd"
        GLabel_654["font"] = ft
        GLabel_654["fg"] = "#333333"
        GLabel_654["justify"] = "left"
        GLabel_654["text"] = "Trip Management"
        GLabel_654.place(x=10, y=5, width=250, height=33)

        GLabel_515 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_515["bg"] = "#e3e8cd"
        GLabel_515["font"] = ft
        GLabel_515["fg"] = "#333333"
        GLabel_515["justify"] = "center"
        GLabel_515["text"] = "Select Trip"
        GLabel_515.place(x=5, y=45, width=100, height=30)

        self.combo_trip = ttk.Combobox(figure,
                                       state="readonly",
                                       values=list(self.TRIPS.keys()),
                                       textvariable=tk.StringVar())
        self.combo_trip.grid(column=1, row=5)
        self.combo_trip.place(x=100, y=45, width=176, height=30)
        self.combo_trip.current(0)

        GLabel_230 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_230["bg"] = "#e3e8cd"
        GLabel_230["font"] = ft
        GLabel_230["fg"] = "#333333"
        GLabel_230["justify"] = "center"
        GLabel_230["text"] = "Trip Name"
        GLabel_230.place(x=5, y=90, width=100, height=30)

        self.edit_trip_name = tk.Entry(figure)
        self.edit_trip_name["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_trip_name["font"] = ft
        self.edit_trip_name["fg"] = "#333333"
        self.edit_trip_name["justify"] = "left"
        self.edit_trip_name["text"] = ""
        self.edit_trip_name.place(x=100, y=90, width=176, height=30)

        GLabel_766 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_766["bg"] = "#e3e8cd"
        GLabel_766["font"] = ft
        GLabel_766["fg"] = "#333333"
        GLabel_766["justify"] = "center"
        GLabel_766["text"] = "Start Date"
        GLabel_766.place(x=5, y=140, width=100, height=30)

        self.edit_start_date = tk.Entry(figure)
        self.edit_start_date["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_start_date["font"] = ft
        self.edit_start_date["fg"] = "#333333"
        self.edit_start_date["justify"] = "left"
        self.edit_start_date["text"] = ""
        self.edit_start_date.place(x=100, y=140, width=176, height=30)

        GLabel_trip_contact = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_trip_contact["bg"] = "#e3e8cd"
        GLabel_trip_contact["font"] = ft
        GLabel_trip_contact["fg"] = "#333333"
        GLabel_trip_contact["justify"] = "center"
        GLabel_trip_contact["text"] = "Contact No"
        GLabel_trip_contact.place(x=5, y=190, width=100, height=30)

        self.edit_trip_contact = tk.Entry(figure)
        self.edit_trip_contact["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_trip_contact["font"] = ft
        self.edit_trip_contact["fg"] = "#333333"
        self.edit_trip_contact["justify"] = "left"
        self.edit_trip_contact["text"] = ""
        self.edit_trip_contact.place(x=100, y=190, width=176, height=30)

        btn_add_trip = tk.Button(figure)
        btn_add_trip["bg"] = "#efefef"
        ft = tkf.Font(family='Arial', size=12)
        btn_add_trip["font"] = ft
        btn_add_trip["fg"] = "#000000"
        btn_add_trip["justify"] = "center"
        btn_add_trip["text"] = "Add Trip"
        btn_add_trip.place(x=70, y=250, width=70, height=30)
        btn_add_trip["command"] = self.btnAddTripHandler

        btn_update_trip = tk.Button(figure)
        btn_update_trip["bg"] = "#efefef"
        ft = tkf.Font(family='Arial', size=12)
        btn_update_trip["font"] = ft
        btn_update_trip["fg"] = "#000000"
        btn_update_trip["justify"] = "center"
        btn_update_trip["text"] = "Update"
        btn_update_trip.place(x=180, y=250, width=70, height=30)
        btn_update_trip["command"] = self.btnUpdateTripHandler

        TLHead = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=16)
        TLHead["bg"] = "#e3e8cd"
        TLHead["font"] = ft
        TLHead["fg"] = "#333333"
        TLHead["justify"] = "left"
        TLHead["text"] = "Trip Leg Management"
        TLHead.place(x=370, y=5, width=250, height=33)

        GLabel_148 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_148["bg"] = "#e3e8cd"
        GLabel_148["font"] = ft
        GLabel_148["fg"] = "#333333"
        GLabel_148["justify"] = "center"
        GLabel_148["text"] = "Start Location"
        GLabel_148.place(x=315, y=40, width=120, height=30)

        self.edit_leg_start_loc = tk.Entry(figure)
        self.edit_leg_start_loc["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_leg_start_loc["font"] = ft
        self.edit_leg_start_loc["fg"] = "#333333"
        self.edit_leg_start_loc["justify"] = "left"
        self.edit_leg_start_loc["text"] = ""
        self.edit_leg_start_loc.place(x=440, y=40, width=180, height=30)

        GLabel_275 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_275["bg"] = "#e3e8cd"
        GLabel_275["font"] = ft
        GLabel_275["fg"] = "#333333"
        GLabel_275["justify"] = "center"
        GLabel_275["text"] = "Destination"
        GLabel_275.place(x=310, y=90, width=120, height=30)

        self.edit_leg_destination = tk.Entry(figure)
        self.edit_leg_destination["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_leg_destination["font"] = ft
        self.edit_leg_destination["fg"] = "#333333"
        self.edit_leg_destination["justify"] = "left"
        self.edit_leg_destination["text"] = ""
        self.edit_leg_destination.place(x=440, y=90, width=180, height=30)

        GLabel_229 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_229["bg"] = "#e3e8cd"
        GLabel_229["font"] = ft
        GLabel_229["fg"] = "#333333"
        GLabel_229["justify"] = "center"
        GLabel_229["text"] = "Transport Contact"
        GLabel_229.place(x=280, y=140, width=180, height=30)

        self.edit_leg_tp_contact = tk.Entry(figure)
        self.edit_leg_tp_contact["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_leg_tp_contact["font"] = ft
        self.edit_leg_tp_contact["fg"] = "#333333"
        self.edit_leg_tp_contact["justify"] = "left"
        self.edit_leg_tp_contact["text"] = ""
        self.edit_leg_tp_contact.place(x=440, y=140, width=180, height=30)

        GLabel_630 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_630["bg"] = "#e3e8cd"
        GLabel_630["font"] = ft
        GLabel_630["fg"] = "#333333"
        GLabel_630["justify"] = "center"
        GLabel_630["text"] = "Transport Mode"
        GLabel_630.place(x=280, y=190, width=180, height=30)

        self.combo_tp_mode = ttk.Combobox(figure,
                                          state="readonly",
                                          values=[mode.value for mode in ModeOfTravel],
                                          textvariable=tk.StringVar())
        self.combo_tp_mode.grid(column=1, row=5)
        self.combo_tp_mode.place(x=440, y=190, width=180, height=30)
        self.combo_tp_mode.current(0)

        btn_add_trip_leg = tk.Button(figure)
        btn_add_trip_leg["bg"] = "#efefef"
        ft = tkf.Font(family='Arial', size=12)
        btn_add_trip_leg["font"] = ft
        btn_add_trip_leg["fg"] = "#000000"
        btn_add_trip_leg["justify"] = "center"
        btn_add_trip_leg["text"] = "Add Trip Leg"
        btn_add_trip_leg.place(x=390, y=250, width=200, height=30)
        btn_add_trip_leg["command"] = self.btnAddTripLegHandler

        # Passenger Management ------------------------------------------------------------------

        GLabel_955 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=16)
        GLabel_955["bg"] = "#e3e8cd"
        GLabel_955["font"] = ft
        GLabel_955["fg"] = "#333333"
        GLabel_955["justify"] = "left"
        GLabel_955["text"] = "Passenger Management"
        GLabel_955.place(x=670, y=5, width=250, height=30)

        GLabel_587 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_587["bg"] = "#e3e8cd"
        GLabel_587["font"] = ft
        GLabel_587["fg"] = "#333333"
        GLabel_587["justify"] = "center"
        GLabel_587["text"] = "Select Trip"
        GLabel_587.place(x=660, y=40, width=80, height=30)

        self.combo_trip_select_passenger = ttk.Combobox(figure,
                                                        state="readonly",
                                                        values=list(self.TRIPS.keys())[1:],
                                                        textvariable=tk.StringVar())
        self.combo_trip_select_passenger.grid(column=1, row=5)
        self.combo_trip_select_passenger.place(x=750, y=40, width=176, height=30)
        self.combo_trip_select_passenger.current()

        GLabel_564 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_564["bg"] = "#e3e8cd"
        GLabel_564["font"] = ft
        GLabel_564["fg"] = "#333333"
        GLabel_564["justify"] = "center"
        GLabel_564["text"] = "Name"
        GLabel_564.place(x=650, y=90, width=70, height=30)

        self.edit_passenger_name = tk.Entry(figure)
        self.edit_passenger_name["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_passenger_name["font"] = ft
        self.edit_passenger_name["fg"] = "#333333"
        self.edit_passenger_name["justify"] = "left"
        self.edit_passenger_name["text"] = ""
        self.edit_passenger_name.place(x=750, y=90, width=176, height=30)

        GLabel_377 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_377["bg"] = "#e3e8cd"
        GLabel_377["font"] = ft
        GLabel_377["fg"] = "#333333"
        GLabel_377["justify"] = "center"
        GLabel_377["text"] = "Address"
        GLabel_377.place(x=660, y=140, width=70, height=30)

        self.edit_address = tk.Entry(figure)
        self.edit_address["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_address["font"] = ft
        self.edit_address["fg"] = "#333333"
        self.edit_address["justify"] = "left"
        self.edit_address["text"] = ""
        self.edit_address.place(x=750, y=140, width=176, height=30)

        GLabel_639 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_639["bg"] = "#e3e8cd"
        GLabel_639["font"] = ft
        GLabel_639["fg"] = "#333333"
        GLabel_639["justify"] = "center"
        GLabel_639["text"] = "DOB"
        GLabel_639.place(x=650, y=190, width=70, height=30)

        self.edit_dob = tk.Entry(figure)
        self.edit_dob["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_dob["font"] = ft
        self.edit_dob["fg"] = "#333333"
        self.edit_dob["justify"] = "left"
        self.edit_dob["text"] = ""
        self.edit_dob.place(x=750, y=190, width=176, height=30)

        GLabel_64 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_64["bg"] = "#e3e8cd"
        GLabel_64["font"] = ft
        GLabel_64["fg"] = "#333333"
        GLabel_64["justify"] = "center"
        GLabel_64["text"] = "Contact No"
        GLabel_64.place(x=660, y=240, width=80, height=30)

        self.edit_passenger_contact = tk.Entry(figure)
        self.edit_passenger_contact["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_passenger_contact["font"] = ft
        self.edit_passenger_contact["fg"] = "#333333"
        self.edit_passenger_contact["justify"] = "left"
        self.edit_passenger_contact["text"] = ""
        self.edit_passenger_contact.place(x=750, y=240, width=176, height=30)

        GLabel_132 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_132["bg"] = "#e3e8cd"
        GLabel_132["font"] = ft
        GLabel_132["fg"] = "#333333"
        GLabel_132["justify"] = "center"
        GLabel_132["text"] = "Payment (£)"
        GLabel_132.place(x=660, y=290, width=90, height=30)

        self.edit_payment = tk.Entry(figure)
        self.edit_payment["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_payment["font"] = ft
        self.edit_payment["fg"] = "#333333"
        self.edit_payment["justify"] = "left"
        self.edit_payment["text"] = ""
        self.edit_payment.place(x=750, y=290, width=177, height=30)


        btn_add_passenger = tk.Button(figure)
        btn_add_passenger["bg"] = "#efefef"
        ft = tkf.Font(family='Arial', size=12)
        btn_add_passenger["font"] = ft
        btn_add_passenger["fg"] = "#000000"
        btn_add_passenger["justify"] = "center"
        btn_add_passenger["text"] = "Add Passenger"
        btn_add_passenger.place(x=750, y=340, width=180, height=30)
        btn_add_passenger["command"] = self.btnAddPassengerHandler

        GLabel_823 = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        GLabel_823["bg"] = "#e3e8cd"
        GLabel_823["font"] = ft
        GLabel_823["fg"] = "#333333"
        GLabel_823["justify"] = "center"
        GLabel_823["text"] = "Select Passenger"
        GLabel_823.place(x=10, y=360, width=130, height=30)

        self.combo_select_passenger = ttk.Combobox(figure,
                                                   state="readonly",
                                                   values=list(self.PASSENGERS.keys()),
                                                   textvariable=tk.StringVar())
        self.combo_select_passenger.grid(column=1, row=5)
        self.combo_select_passenger.place(x=150, y=360, width=230, height=30)
        self.combo_select_passenger.current()

        btn_update_passenger = tk.Button(figure)
        btn_update_passenger["bg"] = "#efefef"
        ft = tkf.Font(family='Arial', size=12)
        btn_update_passenger["font"] = ft
        btn_update_passenger["fg"] = "#000000"
        btn_update_passenger["justify"] = "center"
        btn_update_passenger["text"] = "Update Passenger"
        btn_update_passenger.place(x=400, y=360, width=150, height=30)
        btn_update_passenger["command"] = self.btnUpdatePassengerHandler

        btn_print_Info = tk.Button(figure)
        btn_print_Info["bg"] = "#efefef"
        ft = tkf.Font(family='Arial', size=12)
        btn_print_Info["font"] = ft
        btn_print_Info["fg"] = "#000000"
        btn_print_Info["justify"] = "center"
        btn_print_Info["text"] = "Print Trip Info"
        btn_print_Info.place(x=60, y=300, width=180, height=30)
        btn_print_Info["command"] = self.btnItineraryPrinter

        btn_print_invoice = tk.Button(figure)
        btn_print_invoice["bg"] = "#efefef"
        ft = tkf.Font(family='Arial', size=12)
        btn_print_invoice["font"] = ft
        btn_print_invoice["fg"] = "#000000"
        btn_print_invoice["justify"] = "center"
        btn_print_invoice["text"] = "Print Invoice"
        btn_print_invoice.place(x=390, y=300, width=180, height=30)
        btn_print_invoice["command"] = self.btnInvoicePrinter

    def btnAddTripHandler(self):
        trip_name = self.edit_trip_name.get()
        trip_date = datetime(*map(int, self.edit_start_date.get().split("-")))
        trip_contact = self.edit_trip_contact.get()

        new_trip = self.user.createTrip(trip_name,
                                        trip_date,
                                        trip_contact)
        if new_trip is not None:
            self.TRIPS[new_trip.name] = new_trip
            self.combo_trip.configure(values=list(self.TRIPS.keys()))
            self.combo_trip_select_passenger.configure(values=list(self.TRIPS.keys())[1:])

            self.combo_trip.current(0)
            self.combo_trip_select_passenger.current(0)

            self.edit_trip_name.delete(0, tk.END)
            self.edit_start_date.delete(0, tk.END)
            self.edit_trip_contact.delete(0, tk.END)

            print("Adding trip to " + new_trip.name + " successfull")
        else:
            print("Creating trip failed")

    def btnUpdateTripHandler(self):
        update_trip_name = self.combo_trip.get()
        trip = self.TRIPS[update_trip_name]

        trip_name = self.edit_trip_name.get()
        trip_date = datetime(*map(int, self.edit_start_date.get().split("-")))
        trip_contact = self.edit_trip_contact.get()

        update_result = self.user.updateTrip(trip, trip_name, trip_date, trip_contact)

        if update_result == 1:
            print("Updating " + trip.name + " Successfull")

            self.TRIPS[trip_name] = self.TRIPS.pop(update_trip_name)

            self.combo_trip.configure(values=list(self.TRIPS.keys()))
            self.combo_trip.current(0)

            self.edit_trip_name.delete(0, tk.END)
            self.edit_start_date.delete(0, tk.END)
            self.edit_trip_contact.delete(0, tk.END)

        else:
            print("Update Failed")

    def btnAddTripLegHandler(self):

        start_location = self.edit_leg_start_loc.get()
        destination = self.edit_leg_destination.get()
        transport_contact = self.edit_leg_tp_contact.get()
        transport_mode = TRAVEL_MODE[self.combo_tp_mode.get()]

        trip = self.TRIPS[self.combo_trip.get()]

        new_trip_leg = self.user.addTripLeg(trip,
                                            start_location,
                                            destination,
                                            transport_contact,
                                            transport_mode)

        if new_trip_leg is not None:
            print("Adding Trip Leg successfull for " + trip.name)

            self.edit_leg_start_loc.delete(0, tk.END)
            self.edit_leg_destination.delete(0, tk.END)
            self.edit_leg_tp_contact.delete(0, tk.END)
            self.combo_trip.current(0)
            self.combo_tp_mode.current(0)

        else:
            print("Trip adding failed")

    def btnAddPassengerHandler(self):

        trip = self.TRIPS[self.combo_trip_select_passenger.get()]
        name = self.edit_passenger_name.get()
        address = self.edit_address.get()
        dob = datetime(*map(int, self.edit_dob.get().split("-")))
        contact = self.edit_passenger_contact.get()

        doc_type = self.edit_doc_type.get()
        doc_id = self.edit_doc_id.get()

        payment = self.edit_payment.get()

        new_passenger = self.user.createPassenger(trip,
                                                  name,
                                                  address,
                                                  dob,
                                                  contact,
                                                  {doc_type, doc_id},
                                                  payment)

        if new_passenger is not None:
            print("Creating Passenger " + new_passenger.name + " successful")

            self.PASSENGERS[new_passenger.name] = new_passenger

            self.combo_select_passenger.configure(values=list(self.PASSENGERS.keys()))
            self.combo_select_passenger.current(0)
            self.combo_trip_select_passenger.current(0)

            self.edit_passenger_name.delete(0, tk.END)
            self.edit_address.delete(0, tk.END)
            self.edit_dob.delete(0, tk.END)
            self.edit_passenger_contact.delete(0, tk.END)

            self.edit_doc_type.delete(0, tk.END)
            self.edit_doc_id.delete(0, tk.END)

            self.edit_payment.delete(0, tk.END)

        else:
            print("Creating Passenger Failed")

    def btnUpdatePassengerHandler(self):

        passenger = self.PASSENGERS[self.combo_select_passenger.get()]
        name = self.edit_passenger_name.get()
        address = self.edit_address.get()
        dob = datetime(*map(int, self.edit_dob.get().split("-")))
        contact = self.edit_passenger_contact.get()

        doc_type = self.edit_doc_type.get()
        doc_id = self.edit_doc_id.get()

        update_result = self.user.updatePassenger(passenger,
                                                  name,
                                                  address,
                                                  dob,
                                                  contact,
                                                  {doc_type, doc_id})

        if update_result == 1:
            print("Updating Passenger " + passenger.name + " successful")

            self.combo_select_passenger.configure(values=list(self.PASSENGERS.keys()))
            self.combo_select_passenger.current(0)
            self.combo_trip_select_passenger.current(0)

            self.edit_passenger_name.delete(0, tk.END)
            self.edit_address.delete(0, tk.END)
            self.edit_dob.delete(0, tk.END)
            self.edit_passenger_contact.delete(0, tk.END)

            self.edit_doc_type.delete(0, tk.END)
            self.edit_doc_id.delete(0, tk.END)

        else:
            print("Update Failed")

    def btnItineraryPrinter(self):
        trip = self.TRIPS[self.combo_trip.get()]

        if trip is not None:
            print(self.user.generateItinerary(trip))
        else:
            print("Select a trip to print Itinerary")

    def btnInvoicePrinter(self):
        print(self.user.printCoordinatorInvoice())



if __name__ == "__main__":
    root = tk.Tk()
    app = TripCoordinatorPage(root, "test", "0000")
    root.mainloop()
