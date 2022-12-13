from datetime import datetime
from src.Code.SystemUser import SystemUser
from src.Code.Trip import Trip
from src.Code.TripManager import TripManager
from src.Code.TripCoordinator import TripCoordinator
from src.Code.Traveller import Traveller


class Administrator(SystemUser):
    def __init__(self, name: str, contact: str):
        super().__init__(name, contact)

        self.trip_managers = []

    def createTripManager(self, name: str, contact: str):
        tripManager = TripManager(name, contact)
        self.trip_managers.append(tripManager)

        return tripManager

    def createCoordinator(self, name: str, contact: str):
        tripManager = TripManager(self.name, self.contact)
        found = False
        for manager in self.trip_managers:
            if self.name == manager.name:
                tripManager = manager
                found = True
        if not found:
            self.trip_managers.append(tripManager)
        return tripManager.createCoordinator(name, contact)

    def updateCoordinator(self, tripCoordinator: TripCoordinator,
                          name: str,
                          contact: str):
        tripManager = TripManager(name, contact)
        return tripManager.updateCoordinator(tripCoordinator, name, contact)

    def deleteCoordinator(self, tripCoordinator: TripCoordinator):
        tripManager = TripManager("", "")
        return tripManager.deleteCoordinator(tripCoordinator)

    def createManagerTrip(self,
                   name: str,
                   start_date: datetime,
                   contact: str,
                   trip_coordinator: TripCoordinator):
        tripManager = TripManager(self.name, self.contact)
        for manager in self.trip_managers:
            if manager.name == self.name:
                tripManager = manager
        return tripManager.createManagerTrip(name, start_date, contact, trip_coordinator)

    def updateManagerTrip(self, trip: Trip, name: str, start_date: datetime, contact: str):
        tripManager = TripManager(name, contact)
        return tripManager.updateManagerTrip(trip, name, start_date, contact)

    def deleteTrip(self, trip: Trip):
        tripManager = TripManager("", "")
        return tripManager.deleteTrip(trip)

    def createPassenger(self,
                        trip: Trip,
                        name: str,
                        address: str,
                        dob: datetime,
                        emergency_contact: str,
                        gov_id: {type: str, id: str},
                        payment: int):
        tripManager = TripManager("admin", "admin")
        tripCoordinator = TripCoordinator("admin", "admin", tripManager)
        return tripCoordinator.createPassenger(trip, name, address, dob, emergency_contact, gov_id, payment)

    def updatePassenger(self,
                        traveller: Traveller,
                        name: str,
                        address: str,
                        dob: datetime,
                        emergency_contact: str,
                        gov_id):
        tripManager = TripManager("admin", "admin")
        tripCoordinator = TripCoordinator("admin", "admin", tripManager)
        return tripCoordinator.updatePassenger(traveller, name, address, dob, emergency_contact, gov_id)

    def createTrip(self,
                   name: str,
                   start_date: datetime,
                   contact: str):
        tripManager = TripManager("admin", "admin")
        tripCoordinator = TripCoordinator("admin", "admin", tripManager)
        return tripCoordinator.createTrip(name, start_date, contact)

    def updateTrip(self,
                   trip: Trip,
                   name: str,
                   start_date: datetime,
                   contact: str):
        tripManager = TripManager("admin", "admin")
        tripCoordinator = TripCoordinator("admin", "admin", tripManager)
        return tripCoordinator.updateTrip(trip, name, start_date, contact)

    def addTripLeg(self,
                   trip: Trip,
                   start_loc: str,
                   destination: str,
                   transport_contact: str,
                   transport_mode: str):
        tripManager = TripManager("admin", "admin")
        tripCoordinator = TripCoordinator("admin", "admin", tripManager)
        return tripCoordinator.addTripLeg(trip, start_loc, destination, transport_contact, transport_mode)

    def generateItinerary(self, trip: Trip):
        tripManager = TripManager("admin", "admin")
        tripCoordinator = TripCoordinator("admin", "admin", tripManager)
        return tripCoordinator.generateItinerary(trip)

    def printCoordinatorInvoice(self):
        tripManager = TripManager("admin", "admin")
        tripCoordinator = TripCoordinator("admin", "admin", tripManager)
        return tripCoordinator.printCoordinatorInvoice()

    def printManagerInvoice(self):
        tripManager = TripManager("", "")
        return tripManager.printManagerInvoice()

    def updateManager(self, tripManager: TripManager,
                      name: str,
                      contact: str):
        if tripManager in self.trip_managers:
            tripManager.name = name
            tripManager.contact = contact
            return 1

        return 0

    def deleteManager(self, tripManager: TripManager):
        if tripManager in self.trip_managers:
            # first we should delete all the coordinators under manageer
            for tripCoordinator in tripManager.trip_coordinators:
                # This will delete all the data contain in a trip coordinator
                tripManager.deleteCoordinator(tripCoordinator)

            tripManager.trip_coordinators.clear()
            tripManager.trips_under_supervision.clear()

            self.trip_managers.remove(tripManager)

            return 1

        return 0

    def totalInvoice(self):
        return_str = "Total Trip Invoice in System, Administrator : " + self.name + "\n" + \
                     "#--#"*20 + "\n\n"

        managerAvailable = False

        for manager in self.trip_managers:
            return_str += manager.printManagerInvoice() + "\n" + \
                            "-**-"*20 + "\n"
            managerAvailable = True

        if not managerAvailable:
            return_str += "No Trip Manager Available\n"

        return_str += "Contact Number - Admin : " + self.contact

        return return_str



