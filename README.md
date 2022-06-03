# Teste back-end
​

## Como usar
​
**Clonar este repositório e rodar os comandos:**
​


Caso queira instalar as dependencias desse projeto em um ambiente virtal:
```
python -m venv venv

LINUX:
source venv/bin/activate

WINDOWS:
venv/Scripts/Activate ou venv\Scripts\activate.bat

```
​
```
pip install -r requirements.txt

python manage.py migration

python manage.py runerver
```
​
## Como acessar

- [http://localhost:8000/api/v1/students/](http://localhost:8000/api/v1/students/) 

Listar todos os alunos:
- [GET] [http://localhost:8000/api/v1/students/](http://localhost:8000/api/v1/students/) 

Buscar aluno:
- [GET] [http://localhost:8000/api/v1/students/1](http://localhost:8000/api/v1/students/1) 

Criação de novo aluno:
- [POST] [http://localhost:8000/api/v1/students/](http://localhost:8000/api/v1/students/) 
```
{
    "name":"Nome Aluno",
    "idade":22,
    "registration":2022,
    "curso":"Curso"
}
```
​