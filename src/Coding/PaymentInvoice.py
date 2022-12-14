from datetime import datetime

from src.Coding.Traveller import Traveller
from src.Coding.Trip import Trip


class PaymentInvoice:

    __id = 0

    def __init__(self, trip: Trip, passenger: Traveller, payment: int):

        PaymentInvoice.__id += 1
        self.id = PaymentInvoice.__id
        self.trip = trip
        self.passenger = passenger
        self.payment = payment
        self.paymentDate = datetime.now()
        passenger.paymentInvoice.append(self)

    def __str__(self):
        return_str = "Invoice ID : " + str(self.id) + \
                     ", Trip : " + self.trip.name + \
                     ", passenger : " + self.passenger.name + \
                     ", payment :" + str(self.payment) + \
                     ", Payment date : " + str(self.paymentDate)

        return return_str
