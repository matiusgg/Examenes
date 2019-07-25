-- CREACION  TABLAS MULTAS COCHES MYSQL

-- Inicio de las Tablas de la BD de centromedicopac.sql

-- Usuario/Conductor

CREATE TABLE IF NOT EXISTS infractor (
    
    dni int(10) AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(40) NOT NULL,
    domicilio VARCHAR(60) NOT NULL,
    CPostal VARCHAR(10) NOT NULL,
    Nacionalidad VARCHAR(3) NOT NULL,
    Fnacimiento DATE NOT NULL,
    poblacion VARCHAR(50) NOT NULL DEFAULT 'palma',
    email VARCHAR(50) UNIQUE,
    Telefono varchar(50) NOT NULL,
    Estado TINYINT(1) NOT NULL DEFAULT 1,
    alta TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Comentario TEXT,
    placaAuto VARCHAR(6) NOT NULL,
    PRIMARY KEY (dni)
);

INSERT INTO infractor(dni, nombre, apellido, domicilio, CPostal, Nacionalidad, Fnacimiento, poblacion, email, Telefono, Estado, alta, placaAuto)
VALUES (234537488, 4656985698, 'Emilia', 'Smith', 'buenos aires', 32345, 'USA', '1999-01-03', 'new york', 'smithxd@gmail.com', 64932047, 1, '2016-03-05', 'AB656'), 
(548653498, 4655864566, 'jhon', 'Ortega', 'montevideo', 56746, 'URU', '1988-01-02', 'montevideo', 'montevideo1988@gmail.com', 64955656, 1, '2016-07-04', 'HO546'),
(555967857, 4667675434, 'Pablo', 'Gimenez', 'Sao Pablo', 65645, 'BRS', '1977-12-22', 'brasilia', 'pablog99@gmail.com', 64566566, 1, '2017-06-04', 'YT456');

-- Tipos de Multas

CREATE TABLE IF NOT EXISTS tipomulta (

multa_ID int(5) AUTO_INCREMENT,
dni int(10),
agente_ID int(5),
tipodeMulta ENUM ('Exceso de Velocidad', 'Mal estacionado', 'Choque leve a otro vehiculo', 'agresion al Agente', 'Desorden Publico', 'Incumplimiento Señales Transito') NOT NULL,
precio DOUBLE(6,2) NOT NULL,
Cantidad int(2), -- Cantidad de veces realizada esa infraccion
antecedentesCarcel TINYINT(1) DEFAULT 0,
Comentario TEXT,
Localizacion VARCHAR(50) NOT NULL,
PRIMARY KEY (multa_ID),
FOREIGN KEY (dni) REFERENCES infractor(dni),
FOREIGN KEY (agente_ID) REFERENCES agente(agente_ID)

);

INSERT INTO tipomulta(multa_ID, dni, agente_ID, tipodeMulta, precio, Cantidad, antecedentesCarcel, Localizacion)
VALUES (6457, 234537488, 43555, 1, 20.00, 3, 0, 'Las Avenidas'), 
(3444, 548653498, 45436, 4, 100.00, 4, 1, 'Calle Aragon'),
(3234, 555967857, 88787, 5, 50.00, 1, 0, 'Catedral Palma');

-- Agente

CREATE TABLE IF NOT EXISTS agente (
    agente_ID int(5) AUTO_INCREMENT,
    dni VARCHAR(10) NOT NULL UNIQUE,
    NSS VARCHAR(15) NOT NULL UNIQUE,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(40) NOT NULL,
    domicilio VARCHAR(60) NOT NULL,
    CPostal VARCHAR(10) NOT NULL,
    Nacionalidad VARCHAR(3) NOT NULL,
    Fnacimiento DATE NOT NULL,
    poblacion VARCHAR(50) NOT NULL DEFAULT 'palma',
    email VARCHAR(50) UNIQUE,
    Telefono varchar(50) NOT NULL,
    Estado TINYINT(1) NOT NULL DEFAULT 1,
    alta TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    zonaAsignada VARCHAR(60) NOT NULL,
    Nmultas int(2),
    Comentario TEXT,
    PRIMARY KEY (agente_ID)
);

INSERT INTO agente (agente_ID, dni, NSS, nombre, apellido, domicilio, CPostal, Nacionalidad, Fnacimiento, poblacion, email, Telefono, Estado, alta, zonaAsignada, Nmultas)
VALUES (43555, 4467445466, 353643553675878, 'Gabriela', 'gonzalez', 'madrid', 64554, 'ESP', '1975-02-18', 'palma', 'gonzalez00@gmail.com', 64975467, 1, '2010-04-04', 'Centro Palma' 23), 
(45436, 4672323456, 654563435647456, 'Jason', 'Garcia', 'palma', 87666, 'ARG', '1976-03-24', 'madrid', 'garcial01@gmail.com', 64223656, 1, '2006-05-09', 'Centro Palma', 19), 
(88787, 4212434355, 654453765788768, 'Emanuel', 'Cortes', 'barcelona', 26621, 'FRA', '1980-10-23', 'palma', 'emanuelxd@gmail.com', 65542222, 1, '2007-07-02', 'Paseo Maritimo' 20);

-- Empresa de los Agentes de Transito

CREATE TABLE empresatransito (
    empresa_ID int(10) AUTO_INCREMENT,
    nEmpresa VARCHAR(20) NOT NULL,
    direccion VARCHAR(100) NOT NULL, 
    poblacion VARCHAR(20) NOT NULL DEFAULT 'Palma',
    Codpostal VARCHAR(5) NOT NULL,
    Telefono VARCHAR(15) NOT NULL,
    email VARCHAR(40) NOT NULL UNIQUE,
    fAlta TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Fecha en la que la empresa inicio su trabajo',
    descripcion TEXT,
    PRIMARY KEY (empresa_ID)
);

-- En este caso pueden ser solo una empresa, pero decidi que si son en distintas ciudades serian diferentes empresa, aunque prefectamente solo puede ser una

INSERT INTO empresatransito (empresa_ID, nEmpresa, direccion, poblacion, Codpostal, Telefono, email, fAlta) 
VALUES (422355, 'TransitoBalear', 'calle las avenidad', 'madrid', 13381, 45657777, 'medici00@gmail.com', '2012-05-04'), 
(451163, 'MallorcaTransito', 'calle plaza garau', 'barcelona', 22866, 35944247, 'centremedicbest@gmail.com', '2006-08-09'), 
(887555, 'TheBestTransito', 'calle pere garau', 'palma', 45621, 45531177, 'medicinaspalma@gmail.com', '2009-09-02');


