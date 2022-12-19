from datetime import datetime

from src.Code.PaymentInvoice import PaymentInvoice
from src.Code.SystemUser import SystemUser
from src.Code.Traveller import Traveller
from src.Code.Trip import Trip
from src.Code.TripLeg import TripLeg


class TripCoordinator(SystemUser):
    def __init__(self, name: str, contact: str, supervisour):
        super().__init__(name, contact)

        self.supervisour = supervisour

        self.tripsCoordinating = []
        self.passangers = []
        self.Invoice = []

    def createPassenger(self,
                        trip: Trip,
                        name: str,
                        address: str,
                        dob: datetime,
                        emergency_contact: str,
                        payment: int):

        traveller = Traveller(name, address, dob, emergency_contact)
        trip.passengers.append(traveller)
        self.passangers.append(traveller)

        TripCoordinator.__generateInvoice(self, trip, traveller, payment)

        return traveller

    def updatePassenger(self,
                        traveller: Traveller,
                        name: str,
                        address: str,
                        dob: datetime,
                        emergency_contact: str):

        if traveller in self.passangers:
            traveller.name = name
            traveller.address = address
            traveller.dob = dob
            traveller.emergency_contact = emergency_contact

            return 1

        return 0

    def createTrip(self,
                   name: str,
                   start_date: datetime,
                   contact: str):
        trip = Trip(name, start_date, contact, self)
        self.tripsCoordinating.append(trip)
        self.supervisour.trips_under_supervision.append(trip)

        return trip

    def updateTrip(self,
                   trip: Trip,
                   name: str,
                   start_date: datetime,
                   contact: str):
        if trip in self.tripsCoordinating:
            trip.name = name
            trip.start_date = start_date
            trip.contact = contact

            return 1

        return 0

    def addTripLeg(self,
                   trip: Trip,
                   start_loc: str,
                   destination: str,
                   transport_contact: str,
                   transport_mode: str):
        if trip in self.tripsCoordinating:
            trip_leg = TripLeg(start_loc, destination, transport_contact, transport_mode)
            trip.itinerary.append(trip_leg)
            return trip_leg
        return None

    def generateItinerary(self, trip: Trip):
        """
        This will return Itinerary for a given trip
        :param trip: Trip that the itinerary need to be generated
        :return: printable Itinerary, None if trip is not valid
        """
        if trip in self.tripsCoordinating:
            return_str = ""

            return_str += "Trip to " + trip.name + "\n\n"

            for tripLeg in trip.itinerary:
                return_str += str(tripLeg) + "\n"

            return return_str

        return None

    def __generateInvoice(self, trip: Trip, passenger: Traveller, payment: int):
        """
        This will generate a recipt for the passenger
        :param trip: Trip object
        :param passenger: Traveler object assigned as the passenger
        :param payment: Paid price for the trip
        :return: recipt
        """
        receipt = PaymentInvoice(trip, passenger, payment)
        self.receipts.append(receipt)

        return receipt

    def printCoordinatorInvoice(self):
        """
        This will return the total invoice for the cordinator
        :return: printable invoice
        """
        return_str = "Invoice for the Trip Coordinator: " + self.name + "\n\n"

        invoice_available = False

        for invoice in self.invoice:
            return_str += str(invoice) + "\n"
            invoice_available = True

        if not invoice_available:
            return_str += "No Invoice Available\n"

        return_str += "Contact Number - Trip Coordinator : " + self.contact

        return return_str


