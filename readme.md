## Python Ludycom
A simple backend example with python.

##### Installation

```
git clone https://github.com/daritzateheran/express_ludycom.git
```
##### DB SCRIPTS
```
CREATE SCHEMA `python_ludycom` ;

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;


CREATE TABLE `transactions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `idUser` int(11) DEFAULT NULL,
  `lat` float DEFAULT NULL,
  `lon` float DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idtransactions_UNIQUE` (`id`),
  KEY `id_idx` (`idUser`),
  CONSTRAINT `id` FOREIGN KEY (`idUser`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

```

PRUEBA TÉCNICA BACKEND PYTHON


Deberás de desarrollar un API REST con las siguientes
funcionalidades:


a. Registro de usuario.
b. Login de usuario.
c. Crear un endpoint para los usuarios logueados el cual reciba
una ciudad (o unas coordenadas) y retorne una lista de los
restaurantes cercanos a esta ciudad o coordenadas. Puedes
utilizar algún API público para esto.
d. Crear un endpoint donde puedes consultar la lista de las
transacciones realizadas históricamente.
e. Logout de usuario.


Lo más importante de este ejercicio es que lo que desarrolles (aparte de
funcionar) este muy bien implementado, que se vea la buena ingeniería
detrás del entregable. Esto es un porcentaje aún mayor que la
funcionalidad misma.

¡Crea un repositorio público en Github, sube todos los cambios
mencionados compártenos el enlace.

Authorization Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InVzZXJAZXhhbXBsZS5jb20iLCJleHBpcmVzIjoxNjgyMzczOTg0LjY4NjAyMzd9.MoxBeFpckSrMOV2f0UuHcl7LvMwqcKA9dkxSwHY2nmg