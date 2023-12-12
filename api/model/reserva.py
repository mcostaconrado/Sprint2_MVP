from datetime import datetime
from typing import Union

class Reserva():

    def __init__(   self, no_of_adults: int, no_of_children: int, 
                    no_of_weekend_nights: int, no_of_week_nights: int,
                    required_car_parking_space: int, lead_time: int, arrival_month: int, arrival_date: int,
                    repeated_guest: int, no_of_previous_cancellations: int, no_of_previous_bookings_Not_Cancelled: int,
                    avg_price_per_room,no_of_special_requests: int, outcome: int):
        
        self.no_of_adults = no_of_adults
        self.no_of_children = no_of_children
        self.no_of_weekend_nights = no_of_weekend_nights
        self.no_of_week_nights = no_of_week_nights
        self.required_car_parking_space = required_car_parking_space
        self.lead_time = lead_time
        self.arrival_month = arrival_month
        self.arrival_date = arrival_date
        self.repeated_guest = repeated_guest
        self.no_of_previous_cancellations = no_of_previous_cancellations
        self.no_of_previous_bookings_Not_Cancelled =no_of_previous_bookings_Not_Cancelled
        self.avg_price_per_room = avg_price_per_room
        self.no_of_special_requests = no_of_special_requests
        self.outcome = outcome
        