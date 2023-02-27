-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-02-2023 a las 20:15:27
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bookiegames`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros`
--

CREATE TABLE `libros` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `nota` int(2) UNSIGNED NOT NULL,
  `imagen` varchar(400) NOT NULL DEFAULT 'https://ewr9gftwh9h.exactdn.com/wp-content/uploads/2018/01/Question-Mark.png?strip=all&lossy=1&resize=195%2C195	'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `libros`
--

INSERT INTO `libros` (`id`, `nombre`, `nota`, `imagen`) VALUES
(4, 'El Camino de Los Reyes', 9, 'https://m.media-amazon.com/images/I/51Qh9KpS2CL.jpg'),
(5, 'Mistborn I: El Imperio Final', 8, 'https://m.media-amazon.com/images/I/91a4czYsaJL.jpg'),
(6, 'Harry Potter y la Piedra Filosofal', 3, 'https://m.media-amazon.com/images/I/91R1AixEiLL.jpg'),
(7, 'Palabras Radiantes', 10, 'https://m.media-amazon.com/images/I/81LBim3i3HL.jpg'),
(8, 'Harry Potter y el Prisionero de Azkaban', 8, 'https://imagessl0.casadellibro.com/a/l/t5/30/9788498383430.jpg'),
(9, 'El Heroe de las Eras', 9, 'https://m.media-amazon.com/images/I/51h10D+bP1L.jpg'),
(10, 'Juramentada', 8, 'https://m.media-amazon.com/images/I/91aS6KfXULL.jpg'),
(11, 'El Ritmo de la Guerra', 8, 'https://m.media-amazon.com/images/I/51OdFl1fGAL.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `videojuegos`
--

CREATE TABLE `videojuegos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `nota` int(2) UNSIGNED DEFAULT 5,
  `imagen` varchar(400) NOT NULL DEFAULT 'https://ewr9gftwh9h.exactdn.com/wp-content/uploads/2018/01/Question-Mark.png?strip=all&lossy=1&resize=195%2C195'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `videojuegos`
--

INSERT INTO `videojuegos` (`id`, `nombre`, `nota`, `imagen`) VALUES
(56, 'Hotline Miami', 8, 'https://s3.gaming-cdn.com/images/products/5207/orig/hotline-miami-pc-juego-steam-cover.jpg?v=1656601950'),
(57, 'Dead Cells', 8, 'https://fs-prod-cdn.nintendo-europe.com/media/images/10_share_images/games_15/nintendo_switch_4/H2x1_NSwitch_DeadCells.jpg'),
(59, 'Hollow Knight', 10, 'https://s3.gaming-cdn.com/images/products/2198/orig/hollow-knight-pc-mac-juego-steam-cover.jpg?v=1649252899'),
(60, 'Monster Hunter: World', 8, 'https://cdn-ext.fanatical.com/production/product/1280x720/7f6e4bbc-69a4-4910-a424-8b4f14100c12.jpeg'),
(61, 'DOOM', 7, 'https://cdn.akamai.steamstatic.com/steam/apps/379720/capsule_616x353.jpg?t=1593395083'),
(62, 'DOOM Eternal', 9, 'https://s3.gaming-cdn.com/images/products/2669/616x353/doom-eternal-pc-juego-steam-europe-cover.jpg?v=1663058455'),
(63, 'Stardew Valley', 9, 'https://hb.imgix.net/35e1689e7634e948baab56601cd8879f5b06dd7b.jpeg?auto=compress,format&fit=crop&h=353&w=616&s=8a74e6a49b712d241d1dfb99415c4e0a'),
(64, 'Atomic Heart', 10, 'https://i.ytimg.com/vi/1YYRb0F_fqE/maxresdefault.jpg'),
(65, 'Dying Light', 7, 'https://cdn.dlcompare.com/game_tetiere/upload/gameimage/file/dying-light-file-538736b7.jpeg'),
(66, 'Horizon Zero Dawn', 7, 'https://cdn1.epicgames.com/3328b08ac1c14540aa265a1a85c07839/offer/hzd_wide-2560x1440-bd312be05c49cf339097777c493cb899.jpg'),
(67, 'Hi-Fi Rush', 8, 'https://portal.33bits.net/wp-content/uploads/2023/01/Hi-Fi-RUSH.jpg'),
(68, 'FIFA 23', 4, 'https://cdn1.epicgames.com/offer/f5deacee017b4b109476933f7dd2edbd/EGS_EASPORTSFIFA23StandardEdition_EACanada_S1_2560x1440-aaf9c5273c27a485f2cce8cb7e804f5c');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `libros`
--
ALTER TABLE `libros`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `videojuegos`
--
ALTER TABLE `videojuegos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `libros`
--
ALTER TABLE `libros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `videojuegos`
--
ALTER TABLE `videojuegos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
