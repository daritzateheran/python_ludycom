## Python Ludycom
A simple backend example with python.

#### Installation

```
git clone https://github.com/daritzateheran/python_ludycom.git
cd python_ludycom
python -m venv venv
```
Install the require packages inside the virtual enviroment.

#### Optional: Docker

```
docker-compose up
docker exec -it ludycomdb bash
mysql -u root -proot
use python_ludycom
```
#### SQL
```
CREATE SCHEMA `python_ludycom` ;
```
```
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
```
```
CREATE TABLE `transactions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `idUser` int(11) DEFAULT NULL,
  `lat` float DEFAULT NULL,
  `lon` float DEFAULT NULL,
  `city` varchar(100) NOT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idtransactions_UNIQUE` (`id`),
  KEY `id_idx` (`idUser`),
  CONSTRAINT `id` FOREIGN KEY (`idUser`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
```

#### Usage

**POST /users**
Create a user in the database.
##### Body
```
{
  "id": 0,
  "name": "xaiena",
  "email": "xaiena@example.com",
  "password": "12345678"
}

```
##### Response
```
{
  "msg": "User created",
  "name": "ludycom@example.com"
}
```

**GET /login**
Log in and return an access token.

##### Body
```
{
  "email": "ludycom@example.com",
  "password": "12345678"
}

```
##### Response
```
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Imx1ZHljb21AZXhhbXBsZS5jb20iLCJleHBpcmVzIjoxNjgyMzk3OTI0LjY3NDQ5Njd9.4lgc10r86LiTjAqOO7yBhcQ72nZCCEFoVrDV5fNpVY4"
}
```
**GET /getRestaurants/{city}**
Returns a list of restaurants near a location according to the city. This endpoint is protected and it's necessary to add the Authorization header.

###### Header
```
Authorization:
Bearer {access_token}
```

###### Response
```
{
  "Near restaurants": [
    "",
    "Local food restaurant",
    "Local food restaurant",
    "La Cacerola",
    "Caseros a su Gusto - C.C. Gran Plaza",
    "Restaurant Bolivar",
    "Los Asados",
    "Toppings bar",
    "Aquí Paró Lucho",
    "Pizzeria bar",
    "Mi Pueblo",
    "Aspasia",
    "",
    "Govindas",
    "Cafetería Boyaca",
    "",
    "Saludable",
    "Restaurante catena",
    "Hotsun Arroz Express",
    "Restaurante Palma Seca"
  ],
  "email": "ludycom@example.com"
}
```
**GET /historic**
Returns a list of all the historical transactions made.
###### Header
```
Authorization:
Bearer {access_token}
```
```
###### Response
```
{
  "Transations": [
    {
      "id": 1,
      "idUser": 31,
      "lat": -74.7989,
      "lon": -10.9811,
      "city": "Barranquilla",
      "date": "2023-04-24T22:18:57"
    },
    {
      "id": 2,
      "idUser": 31,
      "lat": -74.7989,
      "lon": -10.9811,
      "city": "Barranquilla",
      "date": "2023-04-24T22:19:48"
    },
    {
      "id": 3,
      "idUser": 31,
      "lat": -74.0836,
      "lon": -4.65346,
      "city": "Bogotá",
      "date": "2023-04-24T22:21:45"
    },
    {
      "id": 4,
      "idUser": 31,
      "lat": -74.0836,
      "lon": -4.65346,
      "city": "Bogotá",
      "date": "2023-04-24T22:35:40"
    },
    {
      "id": 5,
      "idUser": 31,
      "lat": -74.0836,
      "lon": -4.65346,
      "city": "Bogotá",
      "date": "2023-04-24T22:36:11"
    },
    {
      "id": 6,
      "idUser": 31,
      "lat": -76.6527,
      "lon": -6.21805,
      "city": "Medellin",
      "date": "2023-04-24T23:44:38"
    },
    {
      "id": 7,
      "idUser": 31,
      "lat": -75.5736,
      "lon": -6.24434,
      "city": "Medellín",
      "date": "2023-04-24T23:44:50"
    },
    {
      "id": 8,
      "idUser": 32,
      "lat": -75.5736,
      "lon": -6.24434,
      "city": "Medellín",
      "date": "2023-04-24T23:45:51"
    }
  ],
  "email": "ludycom@example.com"
}
```