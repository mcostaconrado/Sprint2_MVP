from pydantic import BaseModel
from typing import Optional, List
from model.reserva import Reserva
import json
import numpy as np

class ReservaSchema(BaseModel):
    """ Define como um nova reserva a ser inserida deve ser representada
    """
    
    no_of_adults: int = 0
    no_of_children: int = 0
    no_of_weekend_nights: int = 0
    no_of_week_nights: int = 0
    required_car_parking_space: int = 0
    lead_time: int = 0
    arrival_month: int = 0
    arrival_date: int = 0
    repeated_guest: int = 0
    no_of_previous_cancellations: int = 0
    no_of_previous_bookings_Not_Cancelled: int = 0
    avg_price_per_room: int = 0
    no_of_special_requests: int = 0
    
class ReservaViewSchema(BaseModel):
    """Define como uma reserva será retornada
    """
    id: int = 1
    no_of_adults: int = 0
    no_of_children: int = 0
    no_of_weekend_nights: int = 0
    no_of_week_nights: int = 0
    required_car_parking_space: int = 0
    lead_time: int = 0
    arrival_month: int = 0
    arrival_date: int = 0
    repeated_guest: int = 0
    no_of_previous_cancellations: int = 0
    no_of_previous_bookings_Not_Cancelled: int = 0
    avg_price_per_room: int = 0
    no_of_special_requests: int = 0
    outcome: int = None
    
class ReservaBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no id da reserva.
    """
    id: int = 1

class ListaReservaSchema(BaseModel):
    """Define como uma lista de reserva será representada
    """
    pacientes: List[ReservaSchema]

    
class ReservaDelSchema(BaseModel):
    """Define como uma reserva para deleção será representada
    """
    id: int = 1
    
# Apresenta apenas os dados de uma reserva    
def apresenta_reserva(reserva: Reserva):
    """ Retorna uma representação da reserva seguindo o schema definido em
        Reserva ViewSchema.
    """

    return {
        "no_of_adults": reserva.no_of_adults,
        "no_of_children": reserva.no_of_children,
        "no_of_weekend_nights": reserva.no_of_weekend_nights,
        "no_of_week_nights": reserva.no_of_week_nights,
        "required_car_parking_space": reserva.required_car_parking_space,
        "lead_time": reserva.lead_time,
        "arrival_month": reserva.arrival_month,
        "arrival_date": reserva.arrival_date,
        "repeated_guest": reserva.repeated_guest,
        "no_of_previous_cancellations": reserva.no_of_previous_cancellations,
        "no_of_previous_bookings_Not_Cancelled": reserva.   no_of_previous_bookings_Not_Cancelled,
        "avg_price_per_room": reserva.avg_price_per_room,
        "no_of_special_requests": reserva.no_of_special_requests,
        "outcome": reserva.outcome
    }
    
# Apresenta uma lista de reservas
def apresenta_reservas(pacientes: List[Reserva]):
    """ Retorna uma representação da reserva seguindo o schema definido em
        ReservaViewSchema.
    """
    result = []
    for reserva in reservas:
        result.append({
            "id": reserva.id,
            "no_of_adults": reserva.no_of_adults,
            "no_of_children": reserva.reserva.no_of_children,
            "no_of_weekend_nights": reserva.no_of_weekend_nights,
            "no_of_week_nights": reserva.no_of_week_nights,
            "required_car_parking_space": reserva.required_car_parking_space,
            "lead_time": reserva.lead_time,
            "arrival_month": reserva.arrival_month,
            "arrival_date": reserva.arrival_date,
            "repeated_guest": reserva.repeated_guest,
            "no_of_previous_cancellations": reserva.no_of_previous_cancellations,
            "no_of_previous_bookings_Not_Cancelled": no_of_previous_bookings_Not_Cancelled,
            "avg_price_per_room": reserva.avg_price_per_room,
            "no_of_special_requests": reserva.no_of_special_requests,
            "outcome": reserva.outcome
        })

    return {"reservas": result}

