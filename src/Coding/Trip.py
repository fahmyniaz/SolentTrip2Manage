from datetime import datetime


class Trip:

    __id = 0

    def __init__(self, name: str, start_date: datetime, contact: str, trip_coordinator):

        Trip.__id += 1

        self.tripID = Trip.__id
        self.name = name
        self.start_date = start_date
        self.contact = contact
        self.trip_coordinator = trip_coordinator

        self.passengers = []
        self.itinerary = []




