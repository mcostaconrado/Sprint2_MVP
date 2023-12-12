from model.avaliador import Avaliador
from model.modelo import Model
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

# To run: pytest -v test_modelos.py

# Instanciação das Classes
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados = "database/Testes.csv"

# Carga dos dados
dataset = pd.read_csv(url_dados, usecols=[1, 2, 3, 4, 6, 8, 10, 11, 13, 14, 15, 16, 17, 18])

# Separando em dados de entrada e saída
X = dataset.iloc[:, 0:-1]
Y = dataset.iloc[:, -1]
    
#Metodo para testar o CART
def test_modelo_CART():  
    # Importando o modelo de árvore de decisão
    path = 'ml_model/HotelReservation_CART_model.pkl'
    modelo = pickle.load(open(path, 'rb'))
    
    scaler = StandardScaler().fit(X) # aplicação da padronização no conjunto de treino 
    rescaledX = scaler.transform(X)
    acuracia, recall, precisao, f1 = avaliador.avaliar(modelo, rescaledX, Y)
    
    assert acuracia >= 0.70
