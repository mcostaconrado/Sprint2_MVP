from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Reserva, Model
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="API - Cool Hotel", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
reserva_tag = Tag(name="Reserva", description="Adição, visualização, remoção e predição de reservas que serão canceladas")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# Rota de adição de reserva
@app.post('/reserva', tags=[reserva_tag],
          responses={"200": ReservaViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: ReservaSchema):
    """Predicts if a booking will be cancelled
    Returns the prediction
    
    Args:
        no_of_adults (int): number of adults
        no_of_children (int): number of children
        no_of_weekend_nights (int): number of weekend nights that will be spent
        no_of_week_nights (int): number of weekend nights that will be spent
        required_car_parking_space (bool): guest required a parking car space?
        lead_time (int): number of days between booking and check-in
        arrival_month (int): 1-12 number of the month (check-in)
        arrival_date (int): 1-31 number of the day (check-in)
        repeated_guest (bool): guest was already a client before?
        no_of_previous_cancellations (int): number of previous cancelled bookings made by the guest
        no_of_previous_bookings_Not_Cancelled (int): number of previous successful bookings made  by the guest
        avg_price_per_room (float): Room price
        no_of_special_requests (int): number of special requests made by the guest
         
    Returns:
        int: The final prediction
    """
    
    # Carregando modelo
    ml_path = 'ml_model/HotelReservation_CART_model.pkl'
    modelo = Model.carrega_modelo(ml_path)
    
    reserva = Reserva(
        no_of_adults = form.no_of_adults,
        no_of_children = form.no_of_children,
        no_of_weekend_nights = form.no_of_weekend_nights,
        no_of_week_nights = form.no_of_week_nights,
        required_car_parking_space = form.required_car_parking_space,
        lead_time = form.lead_time,
        arrival_month = form.arrival_month,
        arrival_date = form.arrival_date,
        repeated_guest = form.repeated_guest,
        no_of_previous_cancellations = form.no_of_previous_cancellations,
        no_of_previous_bookings_Not_Cancelled = form.no_of_previous_bookings_Not_Cancelled,
        avg_price_per_room = form.avg_price_per_room,
        no_of_special_requests = form.no_of_special_requests,
        outcome = Model.preditor(modelo, form)
    )

    return apresenta_reserva(reserva), 200
    '''
    logger.debug(f"Adicionando reserva: '{reserva}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se paciente já existe na base
        if session.query(Reserva).filter(Reserva.id == form.name).first():
            error_msg = "Paciente já existente na base :/"
            logger.warning(f"Erro ao adicionar paciente '{paciente.name}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando paciente
        session.add(paciente)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado paciente de nome: '{paciente.name}'")
        return apresenta_paciente(paciente), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar paciente '{paciente.name}', {error_msg}")
        return {"message": error_msg}, 400
    '''

