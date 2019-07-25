-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-06-2019 a las 16:21:19
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
-- Base de datos: `restaurante`
--
CREATE DATABASE IF NOT EXISTS `restaurante` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `restaurante`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id_clientes` int(10) NOT NULL,
  `nombre` varchar(225) NOT NULL,
  `apellidos` varchar(225) NOT NULL,
  `localidad` varchar(225) DEFAULT NULL,
  `telefono` int(10) NOT NULL,
  `gmail` varchar(255) NOT NULL,
  `dni` varchar(11) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id_clientes`, `nombre`, `apellidos`, `localidad`, `telefono`, `gmail`, `dni`) VALUES
(1, 'Alberto', 'Restrepo', 'palma', 546456, 'wertwert@gmail.com', '647568'),
(2, 'Daenerys', 'Restrepo', 'palma', 546456, 'gofstarkgof@gmail.com', '647568'),
(3, 'Alberto', 'maons', 'new york', 454354, 'gfdgd@gmail.com', '3343446');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `elementospedido`
--

CREATE TABLE `elementospedido` (
  `id_pedidos` int(10) DEFAULT NULL,
  `cantidad` int(3) DEFAULT NULL,
  `id_productos` int(10) DEFAULT NULL,
  `nombreProducto` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedido`
--

CREATE TABLE `pedido` (
  `id_pedidos` int(10) NOT NULL,
  `fechaPedido` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `estado` tinyint(1) DEFAULT '1',
  `id_clientes` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos`
--

CREATE TABLE `pedidos` (
  `id_pedidos` int(10) NOT NULL,
  `estado` tinyint(1) DEFAULT '1',
  `fechaPedido` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id_productos` int(10) NOT NULL,
  `nombreProducto` varchar(45) NOT NULL,
  `ingredientes` text NOT NULL,
  `precio` double(4,2) NOT NULL,
  `estado` tinyint(1) DEFAULT '1',
  `categoria` varchar(200) DEFAULT NULL,
  `imagen` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id_productos`, `nombreProducto`, `ingredientes`, `precio`, `estado`, `categoria`, `imagen`) VALUES
(1, 'Hamburguesa clasica', 'pan suave, tomate, lechuga, carne de ternera', 3.00, 1, 'Comida Rapida', 'clasica.jpg'),
(2, 'Hamburguesa Combox3', 'pan suave, tocino, Carne de ternera, Huevo frito, Lechuga, Peperoni, tomate, cebolla', 6.00, 1, 'Comida Rapida', 'combo3.jpg'),
(3, 'Fanta Naranja Grande', 'liquido con condimentos sabor naranja, azucar', 1.00, 1, 'Liquidos', 'fanta.jpg'),
(4, 'Coca Cola Media', 'ingredientes coca cola', 1.00, 1, 'Liquidos', 'cocaCola.jpg'),
(5, 'Patatas Fritas', 'patatas fritas', 1.80, 1, 'Comida Rapìda', 'Patatas.jpg'),
(6, 'Monster Energy', 'ingredientes monster energy', 1.00, 1, 'Liquidos', 'Monster.jpeg'),
(7, 'Agua', 'agua para refrescarte', 0.90, 1, 'Liquidos', 'Agua.jpg'),
(8, 'Cerveza', 'alcohol', 2.00, 1, 'Liquidos', 'Cerveza.jpg'),
(9, 'Oreo Golden', 'nata, chocolate oreo, helado vainilla', 3.00, 1, 'Postres', 'Oreo.jpg'),
(10, 'Helado', 'base de vainilla con nata', 1.00, 1, 'Postres', 'Helado.jpg'),
(11, 'Brownie', 'chocolate, nata, mani', 3.00, 1, 'Postres', 'Brownie.jpg');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id_clientes`),
  ADD UNIQUE KEY `gmail` (`gmail`);

--
-- Indices de la tabla `elementospedido`
--
ALTER TABLE `elementospedido`
  ADD KEY `id_pedidos` (`id_pedidos`),
  ADD KEY `id_productos` (`id_productos`);

--
-- Indices de la tabla `pedido`
--
ALTER TABLE `pedido`
  ADD PRIMARY KEY (`id_pedidos`),
  ADD KEY `id_clientes` (`id_clientes`);

--
-- Indices de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`id_pedidos`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id_productos`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id_clientes` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `pedido`
--
ALTER TABLE `pedido`
  MODIFY `id_pedidos` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id_productos` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `elementospedido`
--
ALTER TABLE `elementospedido`
  ADD CONSTRAINT `id_pedidos` FOREIGN KEY (`id_pedidos`) REFERENCES `pedidos` (`id_pedidos`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `id_productos` FOREIGN KEY (`id_productos`) REFERENCES `productos` (`id_productos`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `pedido`
--
ALTER TABLE `pedido`
  ADD CONSTRAINT `id_clientes` FOREIGN KEY (`id_clientes`) REFERENCES `clientes` (`id_clientes`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
