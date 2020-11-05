# epidemiological_data
Epidemiological data collection and visualization system

## Requisitos para um correto funcionamento / Build do Sistema:

* Instalar todas as Bilbiotecas presentes no requirements.txt:

pip install -r requirements.txt

* Pode se utilizar do banco de dados MySQL ou SQLite, basta mudar o valor da variável (SQLALCHEMY_DATABASE_URI) que está no arquivo (config.py):

* Após o ajuste do banco, faça o Migrate:

python run.py db migrate

python run.py db upgrade

* Para rodar o projeto localmente:

python run.py runserver


 
## Link do video da primeira entra:
https://youtu.be/gB9v6th3vRUs
