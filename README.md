# CRUD-python
Um CRUD feito em python usando o microframework Flask

## Rodando a API
**primeiro crie uma venv**

Linux e macOS:
```
  python3 -m venv nome-do-ambiente
```

Windows:
```
  python -m venv nome-do-ambiente
```
**Iniciando a venv**

Linux e macOS:
```
source nome_do_ambiente/bin/activate
```
ou 
```
. /nome_do_ambiente/bin/activate
```

Windows:
```
nome_do_ambiente\Scripts\activate
```
após inicializar a venv instale as dependencias 
```
pip install -r requirements.txt
```
agora rode com o comando:
```
python app.py
```

## **Endpoints**

### _GET_
- pega todos os usuarios
```
/
```
- pega um usuario
```
/{id}
```
### _POST_
- rota
```
/
```
- corpo da requisição 

```
{
  "name": "John Doe",
  "email": "john_doe@gmail.com",
  "age": 20,
  "password": "john_doe123"
}
```
### _PUT_
- rota
```
/{id}
```
- corpo da requisição 

```
{
  "name": "John Doe 2",
  "email": "john_doe2@gmail.com",
  "age": 20,
  "password": "john_doe123"
}
```
### _DELETE_
```
/{id}
```
