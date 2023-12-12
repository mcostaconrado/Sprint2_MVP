# Sprint2_MVP

Este trabalho é o MVP da Sprint 2 - Qualidade de Software, Segurança e Sistemas Inteligentes, pertencente ao curso de Pós Graduação em Engenharia de Software, da PUC-Rio.

O trabalho implementa um software de reservas hoteleiras capaz de prever, dadas algumas características, se uma reserva será cancelada ou não. Para isso, foi treinado um modelo de Machine Learning a partir de dados presentes na pasta https://github.com/mcostaconrado/Sprint2_MVP/tree/main/api/database/. 

Mais detalhes da construção e treinamento do modelo: https://colab.research.google.com/drive/1KCSItcGmaXr1hT8MltAaF6WcOu96xu9v#scrollTo=JAIp6d9w5QG8


## Para executar o sistema

O sistema chama, no backend, o modelo treinado. Primeiramente, é necessário realizar o clone deste repositório:

```
$ git clone https://github.com/mcostaconrado/Sprint1_MVP_frontend.git
```

Para que a página manipule dados e tenha integração com o backend, é necessário executar as instruções presentes no README do projeto [MVP_Sprint1_backend](https://github.com/mcostaconrado/Sprint1_MVP_backend/blob/main/README.md)

Após isso, basta abrir o arquivo `index.html` no navegador, e a página estará disponível para realizar as predições