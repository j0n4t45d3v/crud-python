# CRUD-python
Um CRUD feito em python usando o microframework Flask

## Rodando a API

Após inicializar um ambiente virtual instale as dependencias 
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
