from datetime import datetime

from src.Code.PaymentRecipt import PaymentRecipt
from src.Code.SystemUser import SystemUser
from src.Code.Traveller import Traveller
from src.Code.Trip import Trip
from src.Code.TripLeg import TripLeg


class TripCoordinator(SystemUser):
    def __init__(self, name: str, contact: str, supervisour):
        """
        This will initialize the TripCoordinator
        :param name: Name of the Coordinator
        :param contact: contact number of the coordinator
        """
        super().__init__(name, contact)

        self.supervisour = supervisour

        self.tripsCoordinating = []
        self.passangers = []
        self.recipts = []

    def createPassenger(self,
                        trip: Trip,
                        name: str,
                        address: str,
                        dob: datetime,
                        emergency_contact: str,
                        payment: int):
        """
        This will create a new Traveller and add him/her to the selected trip
        :param trip: Trip that passenger is going
        :param name: Name of the Traveler
        :param address: Address of the Traveler
        :param dob: date of Birth Of the traveler
        :param emergency_contact: Emergency contact of the traveler
        :param gov_id: Dictionary containg government ID
        :param payment: payment for the trip
        :return: new Traveler object
        """
        traveller = Traveller(name, address, dob, emergency_contact)
        trip.passengers.append(traveller)
        self.passangers.append(traveller)

        TripCoordinator.__generateRecipt(self, trip, traveller, payment)

        return traveller

    def updatePassenger(self,
                        traveller: Traveller,
                        name: str,
                        address: str,
                        dob: datetime,
                        emergency_contact: str):
        """
        This will update the Traveller with new values
        :param traveller: Traveller that needed to be updated
        :param name: new Name of the traveller
        :param address: new Address
        :param dob: new DOB
        :param emergency_contact: new Emergency contact
        :param gov_id: new Gov ID
        :return: 1 if successfull. 0 if not
        """
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
        """
        This will create a new Trip
        :param name: Name of the trip
        :param start_date: starting date of the trip
        :param contact: contact of the trip
        :return: New Trip Object
        """

        trip = Trip(name, start_date, contact, self)

        self.tripsCoordinating.append(trip)
        self.supervisour.trips_under_supervision.append(trip)

        return trip

    def updateTrip(self,
                   trip: Trip,
                   name: str,
                   start_date: datetime,
                   contact: str):
        """
        This will update a given trip
        :param trip: Trip object that need to be updated
        :param name: Name of the trip
        :param start_date: starting date for the trip
        :param contact: contact of the trip
        :return: 1 if succesfull, 0 if not
        """
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
        """
        This will add a new TripLeg to a given trip
        :param trip: Trip which this leg need to be added
        :param start_loc: starting location for the leg
        :param destination: destination for the leg
        :param transport_contact: transport contact
        :param transport_mode: Mode of transportation
        :return: added trip leg, None if adding invalid
        """
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

    def __generateRecipt(self, trip: Trip, passenger: Traveller, payment: int):
        """
        This will generate a recipt for the passenger
        :param trip: Trip object
        :param passenger: Traveler object assigned as the passenger
        :param payment: Paid price for the trip
        :return: recipt
        """
        recipt = PaymentRecipt(trip, passenger, payment)
        self.recipts.append(recipt)  # this will add the recipt for the Corrdinaters recipts

        return recipt

    def printCoordinatorInvoice(self):
        """
        This will return the total invoice for the cordinator
        :return: printable invoice
        """
        return_str = "Invoice for the Trip Coordinator: " + self.name + "\n\n"

        recipts_available = False

        for recipt in self.recipts:
            return_str += str(recipt) + "\n"
            recipts_available = True

        if not recipts_available:
            return_str += "No Recipts Available\n"

        return_str += "Contact Number - Trip Coordinator : " + self.contact

        return return_str


