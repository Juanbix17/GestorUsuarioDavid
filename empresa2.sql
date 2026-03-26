-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-03-2026 a las 18:22:03
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `empresa2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamentos`
--

CREATE TABLE `departamentos` (
  `id_area` int(11) NOT NULL,
  `nom_area` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `departamentos`
--

INSERT INTO `departamentos` (`id_area`, `nom_area`) VALUES
(1, 'Sistemas'),
(2, 'Cafeteria2');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `Id` int(11) NOT NULL,
  `DocumentoEmple` varchar(50) NOT NULL,
  `NombreEmple` varchar(50) NOT NULL,
  `ApellidoEmple` varchar(50) NOT NULL,
  `Cargo` varchar(50) NOT NULL,
  `SalarioB` decimal(10,2) NOT NULL,
  `HoraExtra` int(11) DEFAULT NULL,
  `Bonificacion` decimal(10,2) DEFAULT NULL,
  `salud` decimal(10,2) DEFAULT NULL,
  `pension` decimal(10,2) DEFAULT NULL,
  `Salarioneto` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`Id`, `DocumentoEmple`, `NombreEmple`, `ApellidoEmple`, `Cargo`, `SalarioB`, `HoraExtra`, `Bonificacion`, `salud`, `pension`, `Salarioneto`) VALUES
(1, '45623', 'Geiferson', 'Sanchez', 'Contador', 45.00, 300000, 3235000.00, 129400.00, 129400.00, 2976200.00),
(2, '1462', 'Garniel', 'Botas', 'empleado', 30.00, 20000, 2910000.00, 116400.00, 116400.00, 2677200.00),
(3, '134654', 'Andres', 'Cuervo', 'empleado', 80.00, 500000, 3540000.00, 141600.00, 141600.00, 3256800.00),
(4, '2828', 'johanna', 'cifuentes', 'gerente', 5860000.00, 20, 800000.00, 234400.00, 234400.00, 5391200.00);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int(11) NOT NULL,
  `usuario` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `rol` varchar(45) DEFAULT NULL,
  `docuemple` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `usuario`, `password`, `rol`, `docuemple`) VALUES
(2, 'David', '2004', 'administrador', NULL),
(3, 'Akaelix', '987456', 'empleado', '516568');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  ADD PRIMARY KEY (`id_area`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`Id`),
  ADD UNIQUE KEY `DocumentoEmple` (`DocumentoEmple`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  MODIFY `id_area` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
