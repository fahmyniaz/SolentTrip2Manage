import enum


class TripLeg:
    def __init__(self,
                 start_loc: str,
                 destination: str,
                 transport_contact: str,
                 transport_mode: enum.Enum):
        self.start_loc = start_loc
        self.destination = destination
        self.transport_contact = transport_contact
        self.transport_mode = transport_mode

    def __str__(self) -> str:
        return_value = "Starting Location : " + self.start_loc + ", Destination : " + self.destination + \
                       ", Transport : " + self.transport_contact + ", Transport Mode : " + self.transport_mode.value

        return return_value



        

