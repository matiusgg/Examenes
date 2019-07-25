-- Datos de las BD en las tablas

-- Infractor

INSERT INTO infractor(dni, nombre, apellido, domicilio, CPostal, Nacionalidad, Fnacimiento, poblacion, email, Telefono, Estado, alta, placaAuto)
VALUES (234537488, 'Emilia', 'Smith', 'buenos aires', 32345, 'USA', '1999-01-03', 'new york', 'smithxd@gmail.com', 64932047, 1, '2016-03-05', 'AB656'), 
(548653498, 'jhon', 'Ortega', 'montevideo', 56746, 'URU', '1988-01-02', 'montevideo', 'montevideo1988@gmail.com', 64955656, 1, '2016-07-04', 'HO546'),
(555967857, 'Pablo', 'Gimenez', 'Sao Pablo', 65645, 'BRS', '1977-12-22', 'brasilia', 'pablog99@gmail.com', 64566566, 1, '2017-06-04', 'YT456');

-- Tipo de Multa

INSERT INTO tipomulta(multa_ID, dni, agente_ID, tipodeMulta, precio, Cantidad, antecedentesCarcel, Localizacion)
VALUES (6457, 234537488, 4355, 1, 20.00, 3, 0, 'Las Avenidas'), 
(3444, 548653498, 4543, 4, 100.00, 4, 1, 'Calle Aragon'),
(3234, 555967857, 8878, 5, 50.00, 1, 0, 'Catedral Palma');

-- Agente

INSERT INTO agente (agente_ID, dni, NSS, nombre, apellido, domicilio, CPostal, Nacionalidad, Fnacimiento, poblacion, email, Telefono, Estado, alta, zonaAsignada, Nmultas)
VALUES (4355, 4467445466, 353643553675878, 'Gabriela', 'gonzalez', 'madrid', 64554, 'ESP', '1975-02-18', 'palma', 'gonzalez00@gmail.com', 64975467, 1, '2010-04-04', 'Centro Palma', 23), 
(4543, 4672323456, 654563435647456, 'Jason', 'Garcia', 'palma', 87666, 'ARG', '1976-03-24', 'madrid', 'garcial01@gmail.com', 64223656, 1, '2006-05-09', 'Centro Palma', 19), 
(8878, 4212434355, 654453765788768, 'Emanuel', 'Cortes', 'barcelona', 26621, 'FRA', '1980-10-23', 'palma', 'emanuelxd@gmail.com', 65542222, 1, '2007-07-02', 'Paseo Maritimo', 20);



-- Empresa Transito


INSERT INTO empresatransito (empresa_ID, nEmpresa, direccion, poblacion, Codpostal, Telefono, email, fAlta) 
VALUES (422355, 'TransitoBalear', 'calle las avenidad', 'madrid', 13381, 45657777, 'medici00@gmail.com', '2012-05-04'), 
(451163, 'MallorcaTransito', 'calle plaza garau', 'barcelona', 22866, 35944247, 'centremedicbest@gmail.com', '2006-08-09'), 
(887555, 'TheBestTransito', 'calle pere garau', 'palma', 45621, 45531177, 'medicinaspalma@gmail.com', '2009-09-02');


