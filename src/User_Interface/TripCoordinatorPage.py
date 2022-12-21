import tkinter as tk
import tkinter.font as tkf
from datetime import datetime
from tkinter import ttk

from src.Coding.ModeOfTravel import ModeOfTravel
from src.Coding.TripCoordinator import TripCoordinator


class TripCoordinatorPage:

    def __init__(self, figure, username, contact):

        self.TRIPS = {"+ CREATE TRIP": None}
        self.PASSENGERS = {}
        all_users = TripCoordinator.SYSTEM_USERS
        self.user = None
        for user in all_users:
            if user.name == username and user.contact == contact:
                self.user = user
        if self.user is None:
            raise ModuleNotFoundError
        if hasattr(self.user, 'tripsCoordinating'):
            for trip in self.user.tripsCoordinating:
                self.TRIPS[trip.name] = trip

        if hasattr(self.user, 'passangers'):
            for passenger in self.user.passangers:
                self.PASSENGERS[passenger.name] = passenger
        figure.title("Trip Coordinator")
        figure["bg"] = "#e3e8cd"
        width = 1000
        height = 450
        screenwidth = figure.winfo_screenwidth()
        screenheight = figure.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        figure.geometry(alignstr)
        figure.resizable(width=False, height=False)

        LblTitle = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=16)
        LblTitle["bg"] = "#e3e8cd"
        LblTitle["font"] = ft
        LblTitle["fg"] = "#800000"
        LblTitle["justify"] = "left"
        LblTitle["text"] = "Trip Management"
        LblTitle.place(x=10, y=5, width=250, height=33)

        lbl_seltrip = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_seltrip["bg"] = "#e3e8cd"
        lbl_seltrip["font"] = ft
        lbl_seltrip["fg"] = "#333333"
        lbl_seltrip["justify"] = "center"
        lbl_seltrip["text"] = "Select Trip"
        lbl_seltrip.place(x=5, y=45, width=100, height=30)

        self.combo_trip = ttk.Combobox(figure,
                                       state="readonly",
                                       values=list(self.TRIPS.keys()),
                                       textvariable=tk.StringVar())
        self.combo_trip.grid(column=1, row=5)
        self.combo_trip.place(x=100, y=45, width=176, height=30)
        self.combo_trip.current(0)

        lbl_trName = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_trName["bg"] = "#e3e8cd"
        lbl_trName["font"] = ft
        lbl_trName["fg"] = "#333333"
        lbl_trName["justify"] = "center"
        lbl_trName["text"] = "Trip Name"
        lbl_trName.place(x=5, y=90, width=100, height=30)

        self.edit_trip_name = tk.Entry(figure)
        self.edit_trip_name["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_trip_name["font"] = ft
        self.edit_trip_name["fg"] = "#333333"
        self.edit_trip_name["justify"] = "left"
        self.edit_trip_name["text"] = ""
        self.edit_trip_name.place(x=100, y=90, width=176, height=30)

        lbl_stDate = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_stDate["bg"] = "#e3e8cd"
        lbl_stDate["font"] = ft
        lbl_stDate["fg"] = "#333333"
        lbl_stDate["justify"] = "center"
        lbl_stDate["text"] = "Start Date"
        lbl_stDate.place(x=5, y=140, width=100, height=30)

        self.edit_start_date = tk.Entry(figure)
        self.edit_start_date["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_start_date["font"] = ft
        self.edit_start_date["fg"] = "#333333"
        self.edit_start_date["justify"] = "left"
        self.edit_start_date["text"] = ""
        self.edit_start_date.place(x=100, y=140, width=176, height=30)

        lbl_ConNo = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_ConNo["bg"] = "#e3e8cd"
        lbl_ConNo["font"] = ft
        lbl_ConNo["fg"] = "#333333"
        lbl_ConNo["justify"] = "center"
        lbl_ConNo["text"] = "Contact No"
        lbl_ConNo.place(x=5, y=190, width=100, height=30)

        self.edit_contact_no = tk.Entry(figure)
        self.edit_contact_no["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_contact_no["font"] = ft
        self.edit_contact_no["fg"] = "#333333"
        self.edit_contact_no["justify"] = "left"
        self.edit_contact_no["text"] = ""
        self.edit_contact_no.place(x=100, y=190, width=176, height=30)

        btn_add_trip = tk.Button(figure)
        btn_add_trip["bg"] = "green"
        ft = tkf.Font(family='Arial', size=12)
        btn_add_trip["font"] = ft
        btn_add_trip["fg"] = "#FFFFFF"
        btn_add_trip["justify"] = "center"
        btn_add_trip["text"] = "Add Trip"
        btn_add_trip.place(x=70, y=250, width=70, height=30)
        btn_add_trip["command"] = self.btnAddTripHandler

        btn_update_trip = tk.Button(figure)
        btn_update_trip["bg"] = "blue"
        ft = tkf.Font(family='Arial', size=12)
        btn_update_trip["font"] = ft
        btn_update_trip["fg"] = "#FFFFFF"
        btn_update_trip["justify"] = "center"
        btn_update_trip["text"] = "Update"
        btn_update_trip.place(x=180, y=250, width=70, height=30)
        btn_update_trip["command"] = self.btnUpdateTripHandler

        lbl_stLoc = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_stLoc["bg"] = "#e3e8cd"
        lbl_stLoc["font"] = ft
        lbl_stLoc["fg"] = "#333333"
        lbl_stLoc["justify"] = "center"
        lbl_stLoc["text"] = "Start Location"
        lbl_stLoc.place(x=315, y=40, width=120, height=30)

        self.edit_leg_start_loc = tk.Entry(figure)
        self.edit_leg_start_loc["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_leg_start_loc["font"] = ft
        self.edit_leg_start_loc["fg"] = "#333333"
        self.edit_leg_start_loc["justify"] = "left"
        self.edit_leg_start_loc["text"] = ""
        self.edit_leg_start_loc.place(x=440, y=40, width=180, height=30)

        lbl_dest = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_dest["bg"] = "#e3e8cd"
        lbl_dest["font"] = ft
        lbl_dest["fg"] = "#333333"
        lbl_dest["justify"] = "center"
        lbl_dest["text"] = "Destination"
        lbl_dest.place(x=310, y=90, width=120, height=30)

        self.edit_leg_dest = tk.Entry(figure)
        self.edit_leg_dest["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_leg_dest["font"] = ft
        self.edit_leg_dest["fg"] = "#333333"
        self.edit_leg_dest["justify"] = "left"
        self.edit_leg_dest["text"] = ""
        self.edit_leg_dest.place(x=440, y=90, width=180, height=30)

        lbl_transCont = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_transCont["bg"] = "#e3e8cd"
        lbl_transCont["font"] = ft
        lbl_transCont["fg"] = "#333333"
        lbl_transCont["justify"] = "center"
        lbl_transCont["text"] = "Transport Contact"
        lbl_transCont.place(x=280, y=140, width=180, height=30)

        self.edit_leg_trans_cont = tk.Entry(figure)
        self.edit_leg_trans_cont["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_leg_trans_cont["font"] = ft
        self.edit_leg_trans_cont["fg"] = "#333333"
        self.edit_leg_trans_cont["justify"] = "left"
        self.edit_leg_trans_cont["text"] = ""
        self.edit_leg_trans_cont.place(x=440, y=140, width=180, height=30)

        lbl_transMod = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=10)
        lbl_transMod["font"] = ft
        lbl_transMod["fg"] = "#333333"
        lbl_transMod["justify"] = "center"
        lbl_transMod["text"] = "Transport Mode"
        lbl_transMod.place(x=320, y=190, width=120, height=30)

        self.combo_tp_mode = ttk.Combobox(figure,
                                          state="readonly",
                                          values=[mode.value for mode in ModeOfTravel],
                                          textvariable=tk.StringVar())
        self.combo_tp_mode.grid(column=1, row=5)
        self.combo_tp_mode.place(x=440, y=190, width=180, height=30)
        self.combo_tp_mode.current(0)

        btn_add_trip_leg = tk.Button(figure)
        btn_add_trip_leg["bg"] = "green"
        ft = tkf.Font(family='Arial', size=12)
        btn_add_trip_leg["font"] = ft
        btn_add_trip_leg["fg"] = "#ffffff"
        btn_add_trip_leg["justify"] = "center"
        btn_add_trip_leg["text"] = "Add Trip Leg"
        btn_add_trip_leg.place(x=390, y=250, width=200, height=30)
        btn_add_trip_leg["command"] = self.btnAddTripLegHandler

        btn_print_Info = tk.Button(figure)
        btn_print_Info["bg"] = "#1c802e"
        ft = tkf.Font(family='Arial', size=14)
        btn_print_Info["font"] = ft
        btn_print_Info["fg"] = "#ffffff"
        btn_print_Info["justify"] = "center"
        btn_print_Info["text"] = "Print Trip Info"
        btn_print_Info.place(x=580, y=390, width=180, height=50)
        btn_print_Info["command"] = self.btnItineraryPrinter

        btn_print_invoice = tk.Button(figure)
        btn_print_invoice["bg"] = "#1c802e"
        ft = tkf.Font(family='Arial', size=14)
        btn_print_invoice["font"] = ft
        btn_print_invoice["fg"] = "#ffffff"
        btn_print_invoice["justify"] = "center"
        btn_print_invoice["text"] = "Print Invoice"
        btn_print_invoice.place(x=800, y=390, width=180, height=50)
        btn_print_invoice["command"] = self.btnInvoicePrinter

        lbl_PasMan = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=16)
        lbl_PasMan["bg"] = "#e3e8cd"
        lbl_PasMan["font"] = ft
        lbl_PasMan["fg"] = "#800000"
        lbl_PasMan["justify"] = "left"
        lbl_PasMan["text"] = "Passenger Management"
        lbl_PasMan.place(x=670, y=5, width=250, height=30)

        lbl_SelTrp = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_SelTrp["bg"] = "#e3e8cd"
        lbl_SelTrp["font"] = ft
        lbl_SelTrp["fg"] = "#333333"
        lbl_SelTrp["justify"] = "center"
        lbl_SelTrp["text"] = "Select Trip"
        lbl_SelTrp.place(x=660, y=40, width=80, height=30)

        self.combo_trip_select_passenger = ttk.Combobox(figure,
                                                        state="readonly",
                                                        values=list(self.TRIPS.keys())[1:],
                                                        textvariable=tk.StringVar())
        self.combo_trip_select_passenger.grid(column=1, row=5)
        self.combo_trip_select_passenger.place(x=750, y=40, width=176, height=30)
        self.combo_trip_select_passenger.current()

        lbl_Name = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_Name["bg"] = "#e3e8cd"
        lbl_Name["font"] = ft
        lbl_Name["fg"] = "#333333"
        lbl_Name["justify"] = "center"
        lbl_Name["text"] = "Name"
        lbl_Name.place(x=650, y=90, width=70, height=30)

        self.edit_pas_name = tk.Entry(figure)
        self.edit_pas_name["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_pas_name["font"] = ft
        self.edit_pas_name["fg"] = "#333333"
        self.edit_pas_name["justify"] = "left"
        self.edit_pas_name["text"] = ""
        self.edit_pas_name.place(x=750, y=90, width=176, height=30)

        lbl_Address = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_Address["bg"] = "#e3e8cd"
        lbl_Address["font"] = ft
        lbl_Address["fg"] = "#333333"
        lbl_Address["justify"] = "center"
        lbl_Address["text"] = "Address"
        lbl_Address.place(x=660, y=140, width=70, height=30)

        self.edit_address = tk.Entry(figure)
        self.edit_address["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_address["font"] = ft
        self.edit_address["fg"] = "#333333"
        self.edit_address["justify"] = "left"
        self.edit_address["text"] = ""
        self.edit_address.place(x=750, y=140, width=176, height=30)

        lbl_dob = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_dob["bg"] = "#e3e8cd"
        lbl_dob["font"] = ft
        lbl_dob["fg"] = "#333333"
        lbl_dob["justify"] = "center"
        lbl_dob["text"] = "DOB"
        lbl_dob.place(x=650, y=190, width=70, height=30)

        self.edit_dob = tk.Entry(figure)
        self.edit_dob["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_dob["font"] = ft
        self.edit_dob["fg"] = "#333333"
        self.edit_dob["justify"] = "left"
        self.edit_dob["text"] = ""
        self.edit_dob.place(x=750, y=190, width=176, height=30)

        lbl_contNo = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_contNo["bg"] = "#e3e8cd"
        lbl_contNo["font"] = ft
        lbl_contNo["fg"] = "#333333"
        lbl_contNo["justify"] = "center"
        lbl_contNo["text"] = "Contact No"
        lbl_contNo.place(x=660, y=240, width=80, height=30)

        self.edit_pas_psw = tk.Entry(figure)
        self.edit_pas_psw["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_pas_psw["font"] = ft
        self.edit_pas_psw["fg"] = "#333333"
        self.edit_pas_psw["justify"] = "left"
        self.edit_pas_psw["text"] = ""
        self.edit_pas_psw.place(x=750, y=240, width=176, height=30)

        lbl_pay = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_pay["bg"] = "#e3e8cd"
        lbl_pay["font"] = ft
        lbl_pay["fg"] = "#333333"
        lbl_pay["justify"] = "center"
        lbl_pay["text"] = "Payment (GBP)"
        lbl_pay.place(x=660, y=290, width=90, height=30)

        self.edit_pay = tk.Entry(figure)
        self.edit_pay["borderwidth"] = "1px"
        ft = tkf.Font(family='Arial', size=12)
        self.edit_pay["font"] = ft
        self.edit_pay["fg"] = "#333333"
        self.edit_pay["justify"] = "left"
        self.edit_pay["text"] = ""
        self.edit_pay.place(x=750, y=290, width=177, height=30)

        btn_add_passenger = tk.Button(figure)
        btn_add_passenger["bg"] = "green"
        ft = tkf.Font(family='Arial', size=12)
        btn_add_passenger["font"] = ft
        btn_add_passenger["fg"] = "#FFFFFF"
        btn_add_passenger["justify"] = "center"
        btn_add_passenger["text"] = "Add Passenger"
        btn_add_passenger.place(x=750, y=340, width=180, height=30)
        btn_add_passenger["command"] = self.btnAddPassengerHandler

        lbl_sel_Pas = tk.Label(figure)
        ft = tkf.Font(family='Arial', size=12)
        lbl_sel_Pas["bg"] = "#e3e8cd"
        lbl_sel_Pas["font"] = ft
        lbl_sel_Pas["fg"] = "#333333"
        lbl_sel_Pas["justify"] = "center"
        lbl_sel_Pas["text"] = "Select Passenger"
        lbl_sel_Pas.place(x=10, y=340, width=130, height=30)

        self.combo_select_passenger = ttk.Combobox(figure,
                                                   state="readonly",
                                                   values=list(self.PASSENGERS.keys()),
                                                   textvariable=tk.StringVar())
        self.combo_select_passenger.grid(column=1, row=5)
        self.combo_select_passenger.place(x=150, y=340, width=230, height=30)
        self.combo_select_passenger.current()

        btn_updte_pas = tk.Button(figure)
        btn_updte_pas["bg"] = "blue"
        ft = tkf.Font(family='Arial', size=12)
        btn_updte_pas["font"] = ft
        btn_updte_pas["fg"] = "#FFFFFF"
        btn_updte_pas["justify"] = "center"
        btn_updte_pas["text"] = "Update Passenger"
        btn_updte_pas.place(x=400, y=340, width=150, height=30)
        btn_updte_pas["command"] = self.btnUpdatePassengerHandler

    def btnAddTripHandler(self):
        trip_name = self.edit_trip_name.get()
        trip_date = datetime(*map(int, self.edit_start_date.get().split("-")))
        trip_contact = self.edit_contact_no.get()

        new_trip: object = self.user.createTrip(trip_name,
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
            self.edit_contact_no.delete(0, tk.END)

            print("Adding trip to " + new_trip.name + " successfull")
        else:
            print("Creating trip failed")

    def btnUpdateTripHandler(self):
        update_trip_name = self.combo_trip.get()
        trip = self.TRIPS[update_trip_name]

        trip_name = self.edit_trip_name.get()
        trip_date = datetime(*map(int, self.edit_start_date.get().split("-")))
        trip_contact = self.edit_contact_no.get()

        update_result = self.user.updateTrip(trip, trip_name, trip_date, trip_contact)

        if update_result == 1:
            print("Updating " + trip.name + " Successfull")

            self.TRIPS[trip_name] = self.TRIPS.pop(update_trip_name)

            self.combo_trip.configure(values=list(self.TRIPS.keys()))
            self.combo_trip.current(0)

            self.edit_trip_name.delete(0, tk.END)
            self.edit_start_date.delete(0, tk.END)
            self.edit_contact_no.delete(0, tk.END)

        else:
            print("Update Failed")

    def btnAddTripLegHandler(self):

        start_location = self.edit_leg_start_loc.get()
        destination = self.edit_leg_dest.get()
        transport_contact = self.edit_leg_trans_cont.get()
        transport_mode = ModeOfTravel[self.combo_tp_mode.get()]

        trip = self.TRIPS[self.combo_trip.get()]

        new_trip_leg = self.user.addTripLeg(trip,
                                            start_location,
                                            destination,
                                            transport_contact,
                                            transport_mode)

        if new_trip_leg is not None:
            print("Added Trip Leg Successfully for " + trip.name)

            self.edit_leg_start_loc.delete(0, tk.END)
            self.edit_leg_dest.delete(0, tk.END)
            self.edit_leg_trans_cont.delete(0, tk.END)
            self.combo_trip.current(0)
            self.combo_tp_mode.current(0)

        else:
            print("Trip added failed")

    def btnAddPassengerHandler(self):

        trip = self.TRIPS[self.combo_trip_select_passenger.get()]
        name = self.edit_pas_name.get()
        address = self.edit_address.get()
        dob = datetime(*map(int, self.edit_dob.get().split("-")))
        contact = self.edit_pas_psw.get()

        payment = self.edit_pay.get()

        new_passenger = self.user.createPassenger(trip,
                                                  name,
                                                  address,
                                                  dob,
                                                  contact,
                                                  payment)

        if new_passenger is not None:
            print("Created Passenger " + new_passenger.name + " Successfully")

            self.PASSENGERS[new_passenger.name] = new_passenger

            self.combo_select_passenger.configure(values=list(self.PASSENGERS.keys()))
            self.combo_select_passenger.current(0)
            self.combo_trip_select_passenger.current(0)

            self.edit_pas_name.delete(0, tk.END)
            self.edit_address.delete(0, tk.END)
            self.edit_dob.delete(0, tk.END)
            self.edit_pas_psw.delete(0, tk.END)
            self.edit_pay.delete(0, tk.END)

        else:
            print("Created Passenger Failed")

    def btnUpdatePassengerHandler(self):

        passenger = self.PASSENGERS[self.combo_select_passenger.get()]
        name = self.edit_pas_name.get()
        address = self.edit_address.get()
        dob = datetime(*map(int, self.edit_dob.get().split("-")))
        contact = self.edit_pas_psw.get()
        update_result = self.user.updatePassenger(passenger,
                                                  name,
                                                  address,
                                                  dob,
                                                  contact)

        if update_result == 1:
            print("Updated Passenger " + passenger.name + " Successfully")

            self.combo_select_passenger.configure(values=list(self.PASSENGERS.keys()))
            self.combo_select_passenger.current(0)
            self.combo_trip_select_passenger.current(0)

            self.edit_pas_name.delete(0, tk.END)
            self.edit_address.delete(0, tk.END)
            self.edit_dob.delete(0, tk.END)
            self.edit_pas_psw.delete(0, tk.END)

        else:
            print("Update Failed")

    def btnItineraryPrinter(self):
        trip = self.TRIPS[self.combo_trip.get()]

        if trip is not None:
            print(self.user.generateItinerary(trip))
        else:
            print("Please select a trip to print Invoice")

    def btnInvoicePrinter(self):
        print(self.user.printCoordinatorInvoice())


if __name__ == "__main__":
    root = tk.Tk()
    app = TripCoordinatorPage(root, "test", "pw1234")
    root.mainloop()
