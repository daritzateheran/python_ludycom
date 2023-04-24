## Python Ludycom
A simple backend example with python.

##### Installation

```
git clone https://github.com/daritzateheran/express_ludycom.git
```
##### DB SCRIPTS
```
CREATE SCHEMA `python_ludycom` ;

CREATE TABLE `python_ludycom`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NULL,
  `email` VARCHAR(100) NOT NULL,
  `password` VARCHAR(500) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC));

CREATE TABLE `python_ludycom`.`transactions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `idUser` INT NULL,
  `lat` FLOAT NULL,
  `lon` FLOAT NULL,
  `date` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `idtransactions_UNIQUE` (`id` ASC),
  INDEX `id_idx` (`idUser` ASC),
  CONSTRAINT `id`
    FOREIGN KEY (`idUser`)
    REFERENCES `python_ludycom`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

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