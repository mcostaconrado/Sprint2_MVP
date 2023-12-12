import numpy as np
import pickle
import joblib
from sklearn.preprocessing import StandardScaler


class Model:
    
    def carrega_modelo(path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        elif path.endswith('.joblib'):
            model = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    def preditor(model, form):
        """Realiza a predição de um paciente com base no modelo treinado
        """
        X_input = np.array([
                            form.no_of_adults,
                            form.no_of_children,
                            form.no_of_weekend_nights,
                            form.no_of_week_nights,
                            form.required_car_parking_space,
                            form.lead_time,
                            form.arrival_month,
                            form.arrival_date,
                            form.repeated_guest,
                            form.no_of_previous_cancellations,
                            form.no_of_previous_bookings_Not_Cancelled,
                            form.avg_price_per_room,
                            form.no_of_special_requests,  
                        ])
        # Faremos o reshape para que o modelo entenda que estamos passando
        X_input = X_input.reshape(1, -1)
        scaler = StandardScaler().fit(X_input) # aplicação da padronização no conjunto de treino 
        rescaledX = scaler.transform(X_input)
        diagnosis = model.predict(rescaledX)

        return int(diagnosis[0])