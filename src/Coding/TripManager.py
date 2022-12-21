from datetime import datetime
from src.Coding.TripCoordinator import TripCoordinator
from src.Coding.SystemUser import SystemUser
from src.Coding.Trip import Trip

class TripManager(SystemUser):
    def __init__(self, name: str, contact: str):
        super().__init__(name, contact)
        self.trip_coordinators = []
        self.trips_under_supervision = []\

    def createCoordinator(self, name: str, contact: str):
        tripCoordinator = TripCoordinator(name, contact, self)
        self.trip_coordinators.append(tripCoordinator)
        return tripCoordinator

    def updateCoordinator(self, tripCoordinator: TripCoordinator,
                          name: str,
                          contact: str):
        if tripCoordinator in self.trip_coordinators:
            tripCoordinator.name = name
            tripCoordinator.contact = contact
            return 1
        return 0

    def deleteCoordinator(self, tripCoordinator: TripCoordinator):
        if tripCoordinator in self.trip_coordinators:
            for trip in tripCoordinator.tripsCoordinating:
                self.trips_under_supervision.remove(trip)
            tripCoordinator.tripsCoordinating.clear()
            tripCoordinator.passangers.clear()
            self.trip_coordinators.remove(tripCoordinator)
            return 1
        return 0

    def createManagerTrip(self,
                   name: str,
                   start_date: datetime,
                   contact: str,
                   trip_coordinator: TripCoordinator):
        if trip_coordinator in self.trip_coordinators:
            trip = trip_coordinator.createTrip(name, start_date, contact)
            return trip
        return None

    def updateManagerTrip(self, trip: Trip, name: str, start_date: datetime, contact: str):
        if trip in self.trips_under_supervision:
            trip.name = name
            trip.start_date = start_date
            trip.contact = contact
            return 1
        return 0

    def deleteTrip(self, trip: Trip):
        if trip in self.trips_under_supervision:
            trip.trip_coordinator.tripsCoordinating.remove(trip)
            self.trips_under_supervision.remove(trip)
            return 1
        return 0

    def printManagerInvoice(self):
        return_str = "Invoice for Manager " + self.name + "\n" +\
                     "*****************" + "\n\n"

        coordinatorAvailable = False

        for coordinator in self.trip_coordinators:
            return_str += coordinator.printCoordinatorInvoice() + "\n" + \
                          "*********" + "\n"
            coordinatorAvailable = True

        if not coordinatorAvailable:
            return_str += "No Coordinators Available\n"
        return_str += "Contact Number Manager : " + self.contact
        return return_str



