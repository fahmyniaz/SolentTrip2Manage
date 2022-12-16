from datetime import datetime

from src.Code.SystemUser import SystemUser
from src.Code.Trip import Trip
from src.Code.TripCoordinator import TripCoordinator


class TripManager(SystemUser):
    def __init__(self, name: str, contact: str):
        super().__init__(name, contact)

        self.trip_coordinators = []
        self.trips_under_supervision = []\

    def createCoordinator(self, name: str, contact: str):
        """
        Create a coordinator with default username and password
        :param name: Name of the coordinator
        :param contact: Contact of the username
        :return: coordinator object created
        """
        tripCoordinator = TripCoordinator(name, contact, self)

        self.trip_coordinators.append(tripCoordinator)

        return tripCoordinator

    def updateCoordinator(self, tripCoordinator: TripCoordinator,
                          name: str,
                          contact: str):
        """
        This can be used to update trip coordinaters account details
        :param tripCoordinator: TripCoordinator that needed to be updated
        :param name: new Name
        :param contact: new contact
        :return: 1 if succesfull, 0 if not
        """

        if tripCoordinator in self.trip_coordinators:
            tripCoordinator.name = name
            tripCoordinator.contact = contact
            return 1

        return 0

    def deleteCoordinator(self, tripCoordinator: TripCoordinator):
        """
        This will remove a given trip coordinator and his refferences in the system
        :param tripCoordinator: trip coordinator
        :return: 1 if success, 0 if not
        """
        if tripCoordinator in self.trip_coordinators:

            # clearing all the trips under trip coordinator
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
        """
        this will create new trip for a given trip coordinator
        :param name: Name of the trip
        :param start_date: starting date of the trip
        :param contact: contact number of the trip
        :param trip_coordinator: trip coordinator that handles the trip
        :return: created trip, None if invaldi
        """

        if trip_coordinator in self.trip_coordinators:
            # creating the trip for the coorfinator
            trip = trip_coordinator.createTrip(name, start_date, contact)

            return trip

        return None

    def updateManagerTrip(self, trip: Trip, name: str, start_date: datetime, contact: str):
        """
        Check whether trip is under the Managers suppervision if it is do the update
        :param trip: trip to be updated
        :param name: New name
        :param start_date: new start date
        :param contact: new contact
        :return: 1 if success, 0 if not
        """
        if trip in self.trips_under_supervision:
            trip.name = name
            trip.start_date = start_date
            trip.contact = contact

            return 1

        return 0

    def deleteTrip(self, trip: Trip):
        """
        check whether the given trip is under managers supervision and remove the given trip
        :param trip: trip object to be removed
        :return: 1 if succesfull, 0 if not
        """
        if trip in self.trips_under_supervision:
            trip.trip_coordinator.tripsCoordinating.remove(trip)
            self.trips_under_supervision.remove(trip)

            return 1

        return 0

    def printManagerInvoice(self):
        return_str = "Total Trip Invoice for Manager " + self.name + "\n" +\
                     "####################################################" + "\n\n"

        coordinatorAvailable = False

        for coordinator in self.trip_coordinators:
            return_str += coordinator.printCoordinatorInvoice() + "\n" + \
                          "--------------------------------------------------------" + "\n"
            coordinatorAvailable = True

        if not coordinatorAvailable:
            return_str += "No Trip Coordinators Available\n"

        return_str += "Contact Number - Manager : " + self.contact

        return return_str



