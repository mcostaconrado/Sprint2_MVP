# Sprint2_MVP

Este trabalho é o MVP da Sprint 2 - Qualidade de Software, Segurança e Sistemas Inteligentes, pertencente ao curso de Pós Graduação em Engenharia de Software, da PUC-Rio.

O trabalho implementa um software de reservas hoteleiras capaz de prever, dadas algumas características, se uma reserva será cancelada ou não. Para isso, foi treinado um modelo de Machine Learning a partir de dados presentes na [pasta do diretório](https://github.com/mcostaconrado/Sprint2_MVP/tree/main/api/database/). 

Mais detalhes da construção e treinamento do modelo disponível no [Colab](https://colab.research.google.com/drive/1KCSItcGmaXr1hT8MltAaF6WcOu96xu9v#scrollTo=JAIp6d9w5QG8)


## Para iniciar o sistema

Primeiramente, é necessário realizar o clone deste repositório:

```
$ git clone https://github.com/mcostaconrado/Sprint2_MVP.git
```

O repositório conta com o arquivo `requirements.txt`. Nele, se encontram todas as bibliotecas Python que terão que ser instaladas para que o projeto possa ser executado.
É recomendado, embora não obrigatório, realizar essas instalações em um ambiente virtual do tipo [virtualenv], a fim de não se misturar versões com outros possíveis projetos na máquina. Utilizando a versão 3.9 do Python, essa etapa pode ser realizada com os comandos a seguir:

```
$ python3.9 -m venv env_app
$ source env_app/bin/activate
```

Após isso, já no ambiente virtual, é realizado o download de dependências do projeto com o comando a seguir:

```
(env_app)$ pip install -r requirements.txt
```

Finalmente, para executar o backend, basta digitar o comando abaixo:

```
(env_app)$ pip install -r requirements.txt
$ flask run --host 0.0.0.0 --port 5000
```

Também é possível rodar o código acima adicionando, ao fim, o parâmetro `--reload`. Este parâmetro faz com que o servidor da aplicação seja reinicado automaticamente após qualquer mudança do código fonte. Pode ser útil em casos de desenvolvimento e debug.

Para verificar o status do sistema em execução, basta abrir o link abaixo no navegador:
[http://localhost:5000/#/](http://localhost:5000/#/)

Após executar o Flask com o backend implementado, basta abrir o arquivo "front/index.html" no navegador. A página web mostrará um formulário com as entradas necessárias para realizar as predições. Ao clicar em "Predict", o backend realiza a predição utilizando o modelo treinado, retornando o resultado em tela.


## Encerrando o sistema

Para encerrar o servidor, basta digitar Ctrl + C no terminal de execução, e ele será interrompido.

Para sair do ambiente virtual, digite o comando a seguir:
```
(env_app)$ deactivate
```