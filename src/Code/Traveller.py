from datetime import datetime


class Traveller:

    __id = 0

    def __init__(self, name: str,
                 address: str,
                 dob: datetime,
                 emergency_contact: str):
        Traveller.__id += 1

        self.id = Traveller.__id
        self.name = name
        self.address = address
        self.dob = dob
        self.emergency_contact = emergency_contact

        self.paymentInvoice = []
