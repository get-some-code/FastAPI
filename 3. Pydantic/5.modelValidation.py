from pydantic import BaseModel, Field, model_validator
from typing import Annotated


class HotelBooking(BaseModel):
    customerName: str
    rooms: Annotated[int, Field(ge=1)]
    guests: Annotated[int, Field(ge=1)]
    nights: Annotated[int, Field(ge=1)]

    @model_validator(mode="after")
    def validate_booking(self):

        # At least one guest per room
        if self.guests < self.rooms:
            raise ValueError(
                "Each room must have at least one guest."
            )

        # Maximum 4 guests per room
        if self.guests > self.rooms * 4:
            raise ValueError(
                "A room can accommodate a maximum of 4 guests."
            )

        return self


def book_hotel(booking: HotelBooking):
    print("----- Booking Confirmed -----")
    print("Customer :", booking.customerName)
    print("Rooms    :", booking.rooms)
    print("Guests   :", booking.guests)
    print("Nights   :", booking.nights)
    print("-----------------------------\n")


booking1 = {
    "customerName": "Virat Kohli",
    "rooms": 2,
    "guests": 5,
    "nights": 3
}

booking2 = {
    "customerName": "Rohit Sharma",
    "rooms": 3,
    "guests": 2,
    "nights": 2
}

booking3 = {
    "customerName": "MS Dhoni",
    "rooms": 2,
    "guests": 10,
    "nights": 1
}

# Valid booking
book_hotel(HotelBooking(**booking1))

# Invalid: Guests < Rooms
book_hotel(HotelBooking(**booking2))

# Invalid: More than 4 guests per room
book_hotel(HotelBooking(**booking3))