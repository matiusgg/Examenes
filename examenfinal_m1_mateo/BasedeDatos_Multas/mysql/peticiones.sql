-- Peticiones para BD Multas Coches

-- 1ra Peticion: Cuantos infractores son de Nacionalidad USA

SELECT COUNT(dni) AS Cantidadinfractores, Nacionalidad FROM infractor WHERE Nacionalidad = 'USA' GROUP BY Nacionalidad;

-- 2da Peticion: Cuales son los infractores que han hecho multa en la localizacion de Las Avenidad

SELECT i.dni, t.Localizacion, i.placaAuto, i.nombre, i.apellido
FROM tipomulta AS t
JOIN infractor AS i
ON t.dni = i.dni
WHERE localizacion = 'Las Avenidas'
GROUP BY t.dni;

-- 3ra Peticion: Cual agente tiene igual o mas de 20 multas realizadas y cual es su zona asignada
SELECT agente_ID, nombre, apellido, Nmultas, zonaAsignada FROM agente WHERE Nmultas >= 20;

-- 4ta Peticion: Cuales infractores tienen multas superiores a 50.00 euros y que tipo de multa tienen, ademas de cual agente los multo

SELECT i.dni, i.nombre, t.precio, t.tipodemulta, a.agente_ID
FROM tipomulta AS t
JOIN infractor AS i
ON t.dni = i.dni
JOIN agente AS a
ON a.agente_ID = t.agente_ID
WHERE precio > 50.00 
GROUP BY t.dni;

-- 5ta Peticion: Cuales son los infractores que estan con el Estado activo con su debida placa de coche.

SELECT dni, nombre, apellido, Estado, placaAuto FROM infractor WHERE Estado = 1;

