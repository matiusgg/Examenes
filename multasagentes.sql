-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-06-2019 a las 14:58:53
-- Versión del servidor: 10.1.38-MariaDB
-- Versión de PHP: 7.3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `multasagentes`
--
CREATE DATABASE IF NOT EXISTS `multasagentes` DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci;
USE `multasagentes`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `agente`
--

CREATE TABLE `agente` (
  `id_Agente` int(10) UNSIGNED NOT NULL,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `telefono` int(10) NOT NULL,
  `correo` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `poblacion` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `codigoPostal` int(6) NOT NULL,
  `fNacimiento` datetime NOT NULL,
  `fechaActivo` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `dni` int(10) NOT NULL,
  `nss` int(14) NOT NULL,
  `zonaAsignada` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `Nacionalidad` varchar(3) COLLATE utf8_spanish_ci NOT NULL,
  `activo` tinyint(4) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `agente`
--

INSERT INTO `agente` (`id_Agente`, `nombre`, `telefono`, `correo`, `poblacion`, `codigoPostal`, `fNacimiento`, `fechaActivo`, `dni`, `nss`, `zonaAsignada`, `Nacionalidad`, `activo`) VALUES
(1, 'Pedro Alvarez', 64342434, 'pedro@gmail.com', 'palma de mallorca', 7005, '1988-03-12 00:00:00', '2017-02-28 23:00:00', 42121233, 222645657, 'Las avenidas', 'ESP', 1),
(2, 'Alberto Perez', 64534334, 'alberto@gmail.com', 'Palma de mallorca', 7001, '1977-05-05 00:00:00', '2016-04-23 22:00:00', 46557676, 677676875, 'calle 31 de diciembre', 'ESP', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `infractor`
--

CREATE TABLE `infractor` (
  `dni` int(10) UNSIGNED NOT NULL,
  `nombre` varchar(120) COLLATE utf8_spanish_ci NOT NULL,
  `correo` varchar(80) COLLATE utf8_spanish_ci NOT NULL,
  `telefono` int(10) NOT NULL,
  `poblacion` varchar(70) COLLATE utf8_spanish_ci NOT NULL,
  `codigoPostal` int(6) NOT NULL,
  `fNacimiento` datetime NOT NULL,
  `fechaActivo` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `direccion` varchar(80) COLLATE utf8_spanish_ci NOT NULL,
  `nacionalidad` varchar(3) COLLATE utf8_spanish_ci NOT NULL,
  `activo` tinyint(4) NOT NULL DEFAULT '1',
  `placaAuto` varchar(6) COLLATE utf8_spanish_ci NOT NULL,
  `cantidadMultas` int(3) NOT NULL,
  `id_Agente` int(10) NOT NULL,
  `tipoMultas` varchar(100) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `infractor`
--

INSERT INTO `infractor` (`dni`, `nombre`, `correo`, `telefono`, `poblacion`, `codigoPostal`, `fNacimiento`, `fechaActivo`, `direccion`, `nacionalidad`, `activo`, `placaAuto`, `cantidadMultas`, `id_Agente`, `tipoMultas`) VALUES
(47567659, 'Carlos Perez', 'carlos@gmail.com', 643423434, 'Palma de mallorca', 7009, '1980-06-06 00:00:00', '2019-06-14 11:42:07', 'Calle las margaritas', 'ESP', 1, '03MGT', 1, 1, 'mal_estacionado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipomultas`
--

CREATE TABLE `tipomultas` (
  `id_Multa` int(10) UNSIGNED NOT NULL,
  `tipoMulta` enum('mal_estacionado','choque_leve_a_otro individuo','maxima_velocidad_superada','agresion_a_personal_del_transito','Desorden_publico','Incumplimiento_señales_transito') COLLATE utf8_spanish_ci NOT NULL,
  `precio` double NOT NULL,
  `comentario` text COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `tipomultas`
--

INSERT INTO `tipomultas` (`id_Multa`, `tipoMulta`, `precio`, `comentario`) VALUES
(9, '', 80, 'COCHE QUE HA SUPERADO LOS PARAMETROS DE VELOCIDAD SEGUN LAS NORMAS DE TRANSITO'),
(10, '', 150, 'COCHE QUE GENERO UN ACCIDENTE CON OTRO COCHE DE NIVEL BAJO-MEDIO SEGUN LAS NORMAS Y PARAMETROS DE TRANSITO'),
(12, '', 50, 'COCHE MAL POSICIONADO DENTRO DE LAS NORMAS DE TRANSITO'),
(14, '', 350, 'CONTACTO FISICO INDEBIDO, AGRESION POR PARTE DEL CONDUCTOR DEL VEHICULO QUE POSTERIORMENTE GENERO DAÑOS FISICOS O PSICOLOGICOS AL AGENTE DE TRANSITO'),
(16, '', 100, 'MULTA POR DESORDEN PUBLICO SEGUN LOS PARAMETROS DE NORMAS DE TRANSITO'),
(17, '', 60, 'Falta de cumplimiento de las normas y no cumplir con las señales a su alrededor de transito');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `agente`
--
ALTER TABLE `agente`
  ADD PRIMARY KEY (`id_Agente`),
  ADD UNIQUE KEY `dni` (`dni`),
  ADD UNIQUE KEY `correo` (`correo`);

--
-- Indices de la tabla `infractor`
--
ALTER TABLE `infractor`
  ADD PRIMARY KEY (`dni`),
  ADD UNIQUE KEY `correo` (`correo`);

--
-- Indices de la tabla `tipomultas`
--
ALTER TABLE `tipomultas`
  ADD PRIMARY KEY (`id_Multa`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `agente`
--
ALTER TABLE `agente`
  MODIFY `id_Agente` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `infractor`
--
ALTER TABLE `infractor`
  MODIFY `dni` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47567660;

--
-- AUTO_INCREMENT de la tabla `tipomultas`
--
ALTER TABLE `tipomultas`
  MODIFY `id_Multa` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
