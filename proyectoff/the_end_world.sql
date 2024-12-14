-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-12-2024 a las 04:32:04
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
-- Base de datos: `the_end_world`
--
CREATE DATABASE IF NOT EXISTS `the_end_world` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `the_end_world`;

DELIMITER $$

-- Procedimientos de Jugadores
CREATE DEFINER=`root`@`localhost` PROCEDURE `RegistrarJugador` (IN `p_NombreUsuario` VARCHAR(100), IN `p_Nivel` INT, IN `p_Puntuacion` INT, IN `p_IDEquipo` INT) 
BEGIN
    INSERT INTO Jugadores (Nombre_Usuario, Nivel, Puntuacion, ID_Equipo)
    VALUES (p_NombreUsuario, p_Nivel, p_Puntuacion, p_IDEquipo);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ModificarJugador` (IN `p_IDJugador` INT, IN `p_NombreUsuario` VARCHAR(100), IN `p_Nivel` INT, IN `p_Puntuacion` INT, IN `p_IDEquipo` INT) 
BEGIN
    UPDATE Jugadores
    SET Nombre_Usuario = p_NombreUsuario, Nivel = p_Nivel, Puntuacion = p_Puntuacion, ID_Equipo = p_IDEquipo
    WHERE ID_Jugador = p_IDJugador;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `EliminarJugador` (IN `p_IDJugador` INT) 
BEGIN
    DELETE FROM Jugadores WHERE ID_Jugador = p_IDJugador;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ConsultarJugador` (IN `p_IDJugador` INT) 
BEGIN
    SELECT * FROM Jugadores WHERE ID_Jugador = p_IDJugador;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ConsultarTodosLosJugadores` () 
BEGIN
    SELECT * FROM Jugadores;
END$$

-- Procedimientos de Mundos
CREATE DEFINER=`root`@`localhost` PROCEDURE `RegistrarMundo` (IN `p_Grafo` JSON) 
BEGIN
    INSERT INTO Mundos (Grafo_Serializado)
    VALUES (p_Grafo);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ModificarMundo` (IN `p_IDMundo` INT, IN `p_Grafo` JSON) 
BEGIN
    UPDATE Mundos
    SET Grafo_Serializado = p_Grafo
    WHERE ID_Mundo = p_IDMundo;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `EliminarMundo` (IN `p_IDMundo` INT) 
BEGIN
    DELETE FROM Mundos WHERE ID_Mundo = p_IDMundo;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ConsultarMundo` (IN `p_IDMundo` INT) 
BEGIN
    SELECT * FROM Mundos WHERE ID_Mundo = p_IDMundo;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ConsultarTodosLosMundos` () 
BEGIN
    SELECT * FROM Mundos;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `InsertarConexion` (IN `p_IDMundo` INT, IN `p_Ubicacion1` VARCHAR(100), IN `p_Ubicacion2` VARCHAR(100), IN `p_Peso` INT) 
BEGIN
    -- Insertar nueva conexión en el grafo
    UPDATE Mundos
    SET Grafo_Serializado = JSON_SET(Grafo_Serializado, CONCAT('$."', p_Ubicacion1, '"."', p_Ubicacion2, '"'), p_Peso)
    WHERE ID_Mundo = p_IDMundo;
END$$

-- Procedimientos de Inventario
CREATE DEFINER=`root`@`localhost` PROCEDURE `RegistrarItemInventario` (IN `p_IDJugador` INT, IN `p_ClaveItem` VARCHAR(100), IN `p_DescripcionItem` TEXT) 
BEGIN
    INSERT INTO Inventario (ID_Jugador, Clave_Item, Descripcion_Item)
    VALUES (p_IDJugador, p_ClaveItem, p_DescripcionItem);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ModificarItemInventario` (IN `p_IDInventario` INT, IN `p_ClaveItem` VARCHAR(100), IN `p_DescripcionItem` TEXT) 
BEGIN
    UPDATE Inventario
    SET Clave_Item = p_ClaveItem, Descripcion_Item = p_DescripcionItem
    WHERE ID_Inventario = p_IDInventario;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `EliminarItemInventario` (IN `p_IDInventario` INT) 
BEGIN
    DELETE FROM Inventario WHERE ID_Inventario = p_IDInventario;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ConsultarItemInventario` (IN `p_IDInventario` INT) 
BEGIN
    SELECT * FROM Inventario WHERE ID_Inventario = p_IDInventario;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ConsultarInventarioJugador` (IN `p_IDJugador` INT) 
BEGIN
    SELECT * FROM Inventario WHERE ID_Jugador = p_IDJugador;
END$$

-- Procedimientos de Partidas
CREATE DEFINER=`root`@`localhost` PROCEDURE `RegistrarPartida` (IN `p_Fecha` DATE, IN `p_Equipo1` INT, IN `p_Equipo2` INT, IN `p_Resultado` VARCHAR(50), IN `p_IDMundo` INT) 
BEGIN
    INSERT INTO Partidas (Fecha, Equipo1, Equipo2, Resultado, ID_Mundo)
    VALUES (p_Fecha, p_Equipo1, p_Equipo2, p_Resultado, p_IDMundo);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ModificarPartida` (IN `p_IDPartida` INT, IN `p_Fecha` DATE, IN `p_Equipo1` INT, IN `p_Equipo2` INT, IN `p_Resultado` VARCHAR(50), IN `p_IDMundo` INT) 
BEGIN
    UPDATE Partidas
    SET Fecha = p_Fecha, Equipo1 = p_Equipo1, Equipo2 = p_Equipo2, Resultado = p_Resultado, ID_Mundo = p_IDMundo
    WHERE ID_Partida = p_IDPartida;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `EliminarPartida` (IN `p_IDPartida` INT) 
BEGIN
    DELETE FROM Partidas WHERE ID_Partida = p_IDPartida;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ConsultarPartida` (IN `p_IDPartida` INT) 
BEGIN
    SELECT * FROM Partidas WHERE ID_Partida = p_IDPartida;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ConsultarTodasLasPartidas` () 
BEGIN
    SELECT * FROM Partidas;
END$$

-- Procedimientos de Ranking
CREATE DEFINER=`root`@`localhost` PROCEDURE `ActualizarPuntuacion` (IN `p_IDJugador` INT, IN `p_NuevaPuntuacion` INT) 
BEGIN
    UPDATE Jugadores
    SET Puntuacion = p_NuevaPuntuacion
    WHERE ID_Jugador = p_IDJugador;
    
    UPDATE Ranking
    SET Puntuacion = p_NuevaPuntuacion
    WHERE ID_Jugador = p_IDJugador;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ConsultarRanking` () 
BEGIN
    SELECT * FROM Ranking
    ORDER BY Posicion ASC;
END$$

-- Procedimientos de Equipos
CREATE DEFINER=`root`@`localhost` PROCEDURE `RegistrarEquipo` (IN `p_NombreEquipo` VARCHAR(100), IN `p_Estadisticas` JSON) 
BEGIN
    INSERT INTO Equipos (Nombre_Equipo, Estadisticas)
    VALUES (p_NombreEquipo, p_Estadisticas);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ModificarEquipo` (IN `p_IDEquipo` INT, IN `p_NombreEquipo` VARCHAR(100), IN `p_Estadisticas` JSON) 
BEGIN
    UPDATE Equipos
    SET Nombre_Equipo = p_NombreEquipo, Estadisticas = p_Estadisticas
    WHERE ID_Equipo = p_IDEquipo;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `EliminarEquipo` (IN `p_IDEquipo` INT) 
BEGIN
    DELETE FROM Equipos WHERE ID_Equipo = p_IDEquipo;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ConsultarEquipo` (IN `p_IDEquipo` INT) 
BEGIN
    SELECT * FROM Equipos WHERE ID_Equipo = p_IDEquipo;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ConsultarTodosLosEquipos` () 
BEGIN
    SELECT * FROM Equipos;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipos`
--

CREATE TABLE `equipos` (
  `ID_Equipo` int(11) NOT NULL,
  `Nombre_Equipo` varchar(100) NOT NULL,
  `Estadisticas` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`Estadisticas`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `equipos`
--

INSERT INTO `equipos` (`ID_Equipo`, `Nombre_Equipo`, `Estadisticas`) VALUES
(1, 'Alpha', '{\"Victorias\": 10, \"Derrotas\": 2}'),
(2, 'Beta', '{\"Victorias\": 8, \"Derrotas\": 4}'),
(3, 'Gamma', '{\"Victorias\": 12, \"Derrotas\": 3}'),
(4, 'Delta', '{\"Victorias\": 7, \"Derrotas\": 5}'),
(5, 'Epsilon', '{\"Victorias\": 9, \"Derrotas\": 6}');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario`
--

CREATE TABLE `inventario` (
  `ID_Inventario` int(11) NOT NULL,
  `ID_Jugador` int(11) NOT NULL,
  `Clave_Item` varchar(100) NOT NULL,
  `Descripcion_Item` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inventario`
--

INSERT INTO `inventario` (`ID_Inventario`, `ID_Jugador`, `Clave_Item`, `Descripcion_Item`) VALUES
(1, 1, 'Sword1', 'Espada de acero'),
(2, 2, 'Shield1', 'Escudo básico'),
(3, 3, 'Potion1', 'Poción de vida'),
(4, 4, 'Bow1', 'Arco largo'),
(5, 5, 'Armor1', 'Armadura ligera');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jugadores`
--

CREATE TABLE `jugadores` (
  `ID_Jugador` int(11) NOT NULL,
  `Nombre_Usuario` varchar(100) NOT NULL,
  `Nivel` int(11) NOT NULL,
  `Puntuacion` int(11) NOT NULL,
  `ID_Equipo` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `jugadores`
--

INSERT INTO `jugadores` (`ID_Jugador`, `Nombre_Usuario`, `Nivel`, `Puntuacion`, `ID_Equipo`) VALUES
(1, 'Andres', 5, 150, 1),
(2, 'Brayan', 3, 800, 2),
(3, 'Carlos', 4, 950, 3),
(4, 'Fernando', 6, 1500, 4),
(5, 'MiguelActualizarPuntuacion', 7, 1800, 1),
(6, 'Player6', 8, 2000, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mundos`
--

CREATE TABLE `mundos` (
  `ID_Mundo` int(11) NOT NULL,
  `Grafo_Serializado` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`Grafo_Serializado`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `mundos`
--

INSERT INTO `mundos` (`ID_Mundo`, `Grafo_Serializado`) VALUES
(1, '{\"A\": {\"B\": 1, \"C\": 4}, \"B\": {\"A\": 1, \"C\": 2}, \"C\": {\"A\": 4, \"B\": 2}}'),
(2, '{\"X\": {\"Y\": 3, \"Z\": 5}, \"Y\": {\"X\": 3, \"Z\": 2}, \"Z\": {\"X\": 5, \"Y\": 2}}'),
(3, '{\"P\": {\"Q\": 7, \"R\": 9}, \"Q\": {\"P\": 7, \"R\": 3}, \"R\": {\"P\": 9, \"Q\": 3}}');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partidas`
--

CREATE TABLE `partidas` (
  `ID_Partida` int(11) NOT NULL,
  `Fecha` date NOT NULL,
  `Equipo1` int(11) DEFAULT NULL,
  `Equipo2` int(11) DEFAULT NULL,
  `Resultado` varchar(50) DEFAULT NULL,
  `ID_Mundo` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `partidas`
--

INSERT INTO `partidas` (`ID_Partida`, `Fecha`, `Equipo1`, `Equipo2`, `Resultado`, `ID_Mundo`) VALUES
(1, '2024-12-01', 1, 2, 'Equipo1', 1),
(2, '2024-12-02', 3, 4, 'Equipo2', 1),
(3, '2024-12-03', 2, 5, 'Equipo1', 2),
(4, '2024-12-04', 1, 4, 'Empate', 2),
(5, '2024-12-05', 5, 3, 'Equipo2', 1),
(6, '2024-12-06', 2, 3, 'Equipo1', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ranking`
--

CREATE TABLE `ranking` (
  `ID_Jugador` int(11) NOT NULL,
  `Puntuacion` int(11) NOT NULL,
  `Posicion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ranking`
--

INSERT INTO `ranking` (`ID_Jugador`, `Puntuacion`, `Posicion`) VALUES
(1, 150, 1),
(2, 800, 3),
(3, 950, 2),
(4, 1500, 1),
(5, 1800, 1);

-- --------------------------------------------------------

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `equipos`
--
ALTER TABLE `equipos`
  ADD PRIMARY KEY (`ID_Equipo`);

--
-- Indices de la tabla `inventario`
--
ALTER TABLE `inventario`
  ADD PRIMARY KEY (`ID_Inventario`),
  ADD KEY `ID_Jugador` (`ID_Jugador`);

--
-- Indices de la tabla `jugadores`
--
ALTER TABLE `jugadores`
  ADD PRIMARY KEY (`ID_Jugador`),
  ADD KEY `ID_Equipo` (`ID_Equipo`);

--
-- Indices de la tabla `mundos`
--
ALTER TABLE `mundos`
  ADD PRIMARY KEY (`ID_Mundo`);

--
-- Indices de la tabla `partidas`
--
ALTER TABLE `partidas`
  ADD PRIMARY KEY (`ID_Partida`),
  ADD KEY `Equipo1` (`Equipo1`),
  ADD KEY `Equipo2` (`Equipo2`),
  ADD KEY `ID_Mundo` (`ID_Mundo`);

--
-- Indices de la tabla `ranking`
--
ALTER TABLE `ranking`
  ADD PRIMARY KEY (`ID_Jugador`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `equipos`
--
ALTER TABLE `equipos`
  MODIFY `ID_Equipo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `inventario`
--
ALTER TABLE `inventario`
  MODIFY `ID_Inventario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `jugadores`
--
ALTER TABLE `jugadores`
  MODIFY `ID_Jugador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `mundos`
--
ALTER TABLE `mundos`
  MODIFY `ID_Mundo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `partidas`
--
ALTER TABLE `partidas`
  MODIFY `ID_Partida` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `inventario`
--
ALTER TABLE `inventario`
  ADD CONSTRAINT `inventario_ibfk_1` FOREIGN KEY (`ID_Jugador`) REFERENCES `jugadores` (`ID_Jugador`) ON DELETE CASCADE;

--
-- Filtros para la tabla `jugadores`
--
ALTER TABLE `jugadores`
  ADD CONSTRAINT `jugadores_ibfk_1` FOREIGN KEY (`ID_Equipo`) REFERENCES `equipos` (`ID_Equipo`) ON DELETE SET NULL;

--
-- Filtros para la tabla `partidas`
--
ALTER TABLE `partidas`
  ADD CONSTRAINT `partidas_ibfk_1` FOREIGN KEY (`Equipo1`) REFERENCES `equipos` (`ID_Equipo`),
  ADD CONSTRAINT `partidas_ibfk_2` FOREIGN KEY (`Equipo2`) REFERENCES `equipos` (`ID_Equipo`),
  ADD CONSTRAINT `partidas_ibfk_3` FOREIGN KEY (`ID_Mundo`) REFERENCES `mundos` (`ID_Mundo`) ON DELETE SET NULL;

--
-- Filtros para la tabla `ranking`
--
ALTER TABLE `ranking`
  ADD CONSTRAINT `ranking_ibfk_1` FOREIGN KEY (`ID_Jugador`) REFERENCES `jugadores` (`ID_Jugador`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
