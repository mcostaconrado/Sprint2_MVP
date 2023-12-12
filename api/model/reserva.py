from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union


# colunas = Pregnancies,Glucose,BloodPressure,SkinThickness,test,BMI,DiabetesPedigreeFunction,Age,Outcome
'''
colunas = no_of_adults, no_of_children, no_of_weekend_nights,no_of_week_nights,
required_car_parking_space,lead_time,arrival_month,arrival_date,repeated_guest,no_of_previous_cancellations,
no_of_previous_bookings_Not_Cancelled,avg_price_per_room,no_of_special_requests,booking_status


'''

class Reserva():
    
    '''
    __tablename__ = 'reserva'
    
    id = Column(Integer, primary_key=True)
    no_of_adults = Column("no_of_adults", Integer)
    no_of_children = Column("no_of_children", Integer)
    no_of_weekend_nights = Column("no_of_weekend_nights", Integer)
    no_of_week_nights = Column("no_of_week_nights", Integer)
    required_car_parking_space = Column("required_car_parking_space", Integer)
    lead_time = Column("lead_time", Integer)
    arrival_month = Column("arrival_month", Integer)
    arrival_date = Column("arrival_date", Integer)
    repeated_guest = Column("repeated_guest", Integer)
    no_of_previous_cancellations = Column("no_of_previous_cancellations", Integer)
    no_of_previous_bookings_Not_Cancelled = Column("no_of_previous_bookings_Not_Cancelled", Integer)
    avg_price_per_room = Column("avg_price_per_room", Float)
    no_of_special_requests = Column("no_of_special_requests", Integer)
    outcome = Column("outcome", Integer)

    data_insercao = Column(DateTime, default=datetime.now())
    '''
    
    def __init__(   self, no_of_adults: int, no_of_children: int, 
                    no_of_weekend_nights: int, no_of_week_nights: int,
                    required_car_parking_space: int, lead_time: int, arrival_month: int, arrival_date: int,
                    repeated_guest: int, no_of_previous_cancellations: int, no_of_previous_bookings_Not_Cancelled: int,
                    avg_price_per_room,no_of_special_requests: int, outcome: int):
        
        """
        Cria uma Reserva

        Arguments:
            no_of_adults:  Número de adultos na reserva
            no_of_children:  Número de crianças na reserva
            no_of_weekend_nights:  Número de noites de fins de semana (sábado e domingo)
            no_of_week_nights:  Número de noites de dias de semana
            required_car_parking_space:  {0, 1} se foi solicitada vaga para carro
            lead_time:  Número de dias de antedecência da reserva
            arrival_month:  Mês de chegada da reserva (1 a 12)
            arrival_date:  Dia do mês de chegada da reserva (1 a 31)
            repeated_guest:  {0,1} se o cliente já teve uma reserva feita antes
            no_of_previous_cancellations:  Quantas vezes este cliente já cancelou em oportunidades anteriores
            no_of_previous_bookings_Not_Cancelled:  Quantas vezes este cliente já se hospedou anteriormente sem cancelar 
            avg_price_per_room:  Valor cobrado pelo quarto
            no_of_special_requests:  Número de pedidos (exigências) especiais feitos pelo cliente
            outcome:  Predição do modelo
            name: nome do paciente
            
        """
        
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
        