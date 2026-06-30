-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-06-2026 a las 13:54:40
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `rest_deseo_examen_2do_parcial`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_api_key`
--

CREATE TABLE `ab_api_key` (
  `id` int(11) NOT NULL,
  `uuid` varchar(36) NOT NULL,
  `name` varchar(256) NOT NULL,
  `key_hash` varchar(256) NOT NULL,
  `lookup_hash` varchar(256) DEFAULT NULL,
  `key_prefix` varchar(16) NOT NULL,
  `user_id` int(11) NOT NULL,
  `scopes` text DEFAULT NULL,
  `active` tinyint(1) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `expires_on` datetime DEFAULT NULL,
  `revoked_on` datetime DEFAULT NULL,
  `last_used_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_api_key_id_seq`
--

CREATE TABLE `ab_api_key_id_seq` (
  `next_not_cached_value` bigint(21) NOT NULL,
  `minimum_value` bigint(21) NOT NULL,
  `maximum_value` bigint(21) NOT NULL,
  `start_value` bigint(21) NOT NULL COMMENT 'start value when sequences is created or value if RESTART is used',
  `increment` bigint(21) NOT NULL COMMENT 'increment value',
  `cache_size` bigint(21) UNSIGNED NOT NULL,
  `cycle_option` tinyint(1) UNSIGNED NOT NULL COMMENT '0 if no cycles are allowed, 1 if the sequence should begin a new cycle when maximum_value is passed',
  `cycle_count` bigint(21) NOT NULL COMMENT 'How many cycles have been done'
) ENGINE=InnoDB;

--
-- Volcado de datos para la tabla `ab_api_key_id_seq`
--

INSERT INTO `ab_api_key_id_seq` (`next_not_cached_value`, `minimum_value`, `maximum_value`, `start_value`, `increment`, `cache_size`, `cycle_option`, `cycle_count`) VALUES
(1, 1, 9223372036854775806, 1, 1, 1000, 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_group`
--

CREATE TABLE `ab_group` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `label` varchar(150) DEFAULT NULL,
  `description` varchar(512) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_group_id_seq`
--

CREATE TABLE `ab_group_id_seq` (
  `next_not_cached_value` bigint(21) NOT NULL,
  `minimum_value` bigint(21) NOT NULL,
  `maximum_value` bigint(21) NOT NULL,
  `start_value` bigint(21) NOT NULL COMMENT 'start value when sequences is created or value if RESTART is used',
  `increment` bigint(21) NOT NULL COMMENT 'increment value',
  `cache_size` bigint(21) UNSIGNED NOT NULL,
  `cycle_option` tinyint(1) UNSIGNED NOT NULL COMMENT '0 if no cycles are allowed, 1 if the sequence should begin a new cycle when maximum_value is passed',
  `cycle_count` bigint(21) NOT NULL COMMENT 'How many cycles have been done'
) ENGINE=InnoDB;

--
-- Volcado de datos para la tabla `ab_group_id_seq`
--

INSERT INTO `ab_group_id_seq` (`next_not_cached_value`, `minimum_value`, `maximum_value`, `start_value`, `increment`, `cache_size`, `cycle_option`, `cycle_count`) VALUES
(1, 1, 9223372036854775806, 1, 1, 1000, 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_group_role`
--

CREATE TABLE `ab_group_role` (
  `id` int(11) NOT NULL,
  `group_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_group_role_id_seq`
--

CREATE TABLE `ab_group_role_id_seq` (
  `next_not_cached_value` bigint(21) NOT NULL,
  `minimum_value` bigint(21) NOT NULL,
  `maximum_value` bigint(21) NOT NULL,
  `start_value` bigint(21) NOT NULL COMMENT 'start value when sequences is created or value if RESTART is used',
  `increment` bigint(21) NOT NULL COMMENT 'increment value',
  `cache_size` bigint(21) UNSIGNED NOT NULL,
  `cycle_option` tinyint(1) UNSIGNED NOT NULL COMMENT '0 if no cycles are allowed, 1 if the sequence should begin a new cycle when maximum_value is passed',
  `cycle_count` bigint(21) NOT NULL COMMENT 'How many cycles have been done'
) ENGINE=InnoDB;

--
-- Volcado de datos para la tabla `ab_group_role_id_seq`
--

INSERT INTO `ab_group_role_id_seq` (`next_not_cached_value`, `minimum_value`, `maximum_value`, `start_value`, `increment`, `cache_size`, `cycle_option`, `cycle_count`) VALUES
(1, 1, 9223372036854775806, 1, 1, 1000, 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_permission`
--

CREATE TABLE `ab_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `ab_permission`
--

INSERT INTO `ab_permission` (`id`, `name`) VALUES
(26, 'can_actualizar_carrito_vivo'),
(3, 'can_add'),
(29, 'can_cambiar_imagen_plato'),
(25, 'can_carrito_vivo'),
(27, 'can_cerrar_venta'),
(15, 'can_chart'),
(24, 'can_cliente_nuevo'),
(6, 'can_delete'),
(9, 'can_download'),
(8, 'can_edit'),
(16, 'can_get'),
(22, 'can_index'),
(4, 'can_list'),
(17, 'can_panel'),
(28, 'can_pantalla_cliente'),
(21, 'can_platos_categoria'),
(18, 'can_pronosticos'),
(23, 'can_registrar_venta'),
(7, 'can_show'),
(2, 'can_this_form_get'),
(1, 'can_this_form_post'),
(19, 'can_top_platos'),
(5, 'can_userinfo'),
(20, 'can_ventas_mes'),
(14, 'copyrole'),
(13, 'menu_access'),
(10, 'resetmypassword'),
(11, 'resetpasswords'),
(12, 'userinfoedit');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_permission_id_seq`
--

CREATE TABLE `ab_permission_id_seq` (
  `next_not_cached_value` bigint(21) NOT NULL,
  `minimum_value` bigint(21) NOT NULL,
  `maximum_value` bigint(21) NOT NULL,
  `start_value` bigint(21) NOT NULL COMMENT 'start value when sequences is created or value if RESTART is used',
  `increment` bigint(21) NOT NULL COMMENT 'increment value',
  `cache_size` bigint(21) UNSIGNED NOT NULL,
  `cycle_option` tinyint(1) UNSIGNED NOT NULL COMMENT '0 if no cycles are allowed, 1 if the sequence should begin a new cycle when maximum_value is passed',
  `cycle_count` bigint(21) NOT NULL COMMENT 'How many cycles have been done'
) ENGINE=InnoDB;

--
-- Volcado de datos para la tabla `ab_permission_id_seq`
--

INSERT INTO `ab_permission_id_seq` (`next_not_cached_value`, `minimum_value`, `maximum_value`, `start_value`, `increment`, `cache_size`, `cycle_option`, `cycle_count`) VALUES
(1001, 1, 9223372036854775806, 1, 1, 1000, 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_permission_view`
--

CREATE TABLE `ab_permission_view` (
  `id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  `view_menu_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `ab_permission_view`
--

INSERT INTO `ab_permission_view` (`id`, `permission_id`, `view_menu_id`) VALUES
(1, 1, 6),
(3, 1, 7),
(5, 1, 8),
(2, 2, 6),
(4, 2, 7),
(6, 2, 8),
(7, 3, 10),
(19, 3, 13),
(27, 3, 15),
(47, 3, 28),
(55, 3, 31),
(62, 3, 33),
(69, 3, 35),
(76, 3, 37),
(83, 3, 39),
(8, 4, 10),
(20, 4, 13),
(28, 4, 15),
(36, 4, 19),
(40, 4, 21),
(42, 4, 23),
(44, 4, 25),
(48, 4, 28),
(56, 4, 31),
(63, 4, 33),
(70, 4, 35),
(77, 4, 37),
(84, 4, 39),
(90, 4, 41),
(93, 4, 44),
(95, 4, 46),
(97, 4, 48),
(100, 4, 51),
(102, 4, 53),
(9, 5, 10),
(10, 6, 10),
(21, 6, 13),
(29, 6, 15),
(38, 6, 19),
(49, 6, 28),
(57, 6, 31),
(64, 6, 33),
(71, 6, 35),
(78, 6, 37),
(85, 6, 39),
(11, 7, 10),
(22, 7, 13),
(30, 7, 15),
(37, 7, 19),
(50, 7, 28),
(58, 7, 31),
(65, 7, 33),
(72, 7, 35),
(79, 7, 37),
(86, 7, 39),
(12, 8, 10),
(23, 8, 13),
(31, 8, 15),
(51, 8, 28),
(59, 8, 31),
(66, 8, 33),
(73, 8, 35),
(80, 8, 37),
(87, 8, 39),
(13, 9, 10),
(24, 9, 13),
(32, 9, 15),
(52, 9, 28),
(60, 9, 31),
(67, 9, 33),
(74, 9, 35),
(81, 9, 37),
(88, 9, 39),
(14, 10, 10),
(15, 11, 10),
(16, 12, 10),
(17, 13, 11),
(18, 13, 12),
(26, 13, 14),
(33, 13, 16),
(35, 13, 18),
(39, 13, 20),
(41, 13, 22),
(43, 13, 24),
(45, 13, 26),
(53, 13, 29),
(54, 13, 30),
(61, 13, 32),
(68, 13, 34),
(75, 13, 36),
(82, 13, 38),
(89, 13, 40),
(91, 13, 42),
(92, 13, 43),
(94, 13, 45),
(96, 13, 47),
(98, 13, 49),
(99, 13, 50),
(101, 13, 52),
(103, 13, 54),
(25, 14, 13),
(34, 15, 17),
(46, 16, 27),
(104, 17, 1),
(110, 18, 48),
(105, 18, 51),
(106, 18, 53),
(107, 19, 55),
(108, 20, 55),
(109, 21, 55),
(111, 22, 56),
(112, 23, 56),
(113, 24, 56),
(114, 25, 56),
(115, 26, 56),
(116, 27, 56),
(117, 28, 56),
(118, 29, 56);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_permission_view_id_seq`
--

CREATE TABLE `ab_permission_view_id_seq` (
  `next_not_cached_value` bigint(21) NOT NULL,
  `minimum_value` bigint(21) NOT NULL,
  `maximum_value` bigint(21) NOT NULL,
  `start_value` bigint(21) NOT NULL COMMENT 'start value when sequences is created or value if RESTART is used',
  `increment` bigint(21) NOT NULL COMMENT 'increment value',
  `cache_size` bigint(21) UNSIGNED NOT NULL,
  `cycle_option` tinyint(1) UNSIGNED NOT NULL COMMENT '0 if no cycles are allowed, 1 if the sequence should begin a new cycle when maximum_value is passed',
  `cycle_count` bigint(21) NOT NULL COMMENT 'How many cycles have been done'
) ENGINE=InnoDB;

--
-- Volcado de datos para la tabla `ab_permission_view_id_seq`
--

INSERT INTO `ab_permission_view_id_seq` (`next_not_cached_value`, `minimum_value`, `maximum_value`, `start_value`, `increment`, `cache_size`, `cycle_option`, `cycle_count`) VALUES
(1001, 1, 9223372036854775806, 1, 1, 1000, 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_permission_view_role`
--

CREATE TABLE `ab_permission_view_role` (
  `id` int(11) NOT NULL,
  `permission_view_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `ab_permission_view_role`
--

INSERT INTO `ab_permission_view_role` (`id`, `permission_view_id`, `role_id`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 1),
(4, 4, 1),
(5, 5, 1),
(6, 6, 1),
(7, 7, 1),
(8, 8, 1),
(9, 9, 1),
(10, 10, 1),
(11, 11, 1),
(12, 12, 1),
(13, 13, 1),
(14, 14, 1),
(15, 15, 1),
(16, 16, 1),
(17, 17, 1),
(18, 18, 1),
(19, 19, 1),
(20, 20, 1),
(21, 21, 1),
(22, 22, 1),
(23, 23, 1),
(24, 24, 1),
(25, 25, 1),
(26, 26, 1),
(27, 27, 1),
(28, 28, 1),
(29, 29, 1),
(30, 30, 1),
(31, 31, 1),
(32, 32, 1),
(33, 33, 1),
(34, 34, 1),
(35, 35, 1),
(36, 36, 1),
(37, 37, 1),
(38, 38, 1),
(39, 39, 1),
(40, 40, 1),
(41, 41, 1),
(42, 42, 1),
(43, 43, 1),
(44, 44, 1),
(45, 45, 1),
(46, 46, 1),
(47, 47, 1),
(48, 48, 1),
(49, 49, 1),
(50, 50, 1),
(51, 51, 1),
(52, 52, 1),
(53, 53, 1),
(54, 54, 1),
(55, 55, 1),
(56, 56, 1),
(57, 57, 1),
(58, 58, 1),
(59, 59, 1),
(60, 60, 1),
(61, 61, 1),
(62, 62, 1),
(63, 63, 1),
(64, 64, 1),
(65, 65, 1),
(66, 66, 1),
(67, 67, 1),
(68, 68, 1),
(69, 69, 1),
(112, 69, 4),
(70, 70, 1),
(110, 70, 4),
(71, 71, 1),
(72, 72, 1),
(111, 72, 4),
(73, 73, 1),
(113, 73, 4),
(74, 74, 1),
(75, 75, 1),
(76, 76, 1),
(116, 76, 4),
(77, 77, 1),
(114, 77, 4),
(78, 78, 1),
(79, 79, 1),
(115, 79, 4),
(80, 80, 1),
(117, 80, 4),
(81, 81, 1),
(82, 82, 1),
(83, 83, 1),
(84, 84, 1),
(85, 85, 1),
(86, 86, 1),
(87, 87, 1),
(88, 88, 1),
(89, 89, 1),
(90, 90, 1),
(104, 90, 3),
(91, 91, 1),
(92, 92, 1),
(93, 93, 1),
(105, 93, 3),
(94, 94, 1),
(95, 95, 1),
(106, 95, 3),
(96, 96, 1),
(97, 97, 1),
(107, 97, 3),
(98, 98, 1),
(99, 99, 1),
(100, 100, 1),
(108, 100, 3),
(101, 101, 1),
(102, 102, 1),
(109, 102, 3),
(103, 103, 1),
(118, 104, 1),
(119, 104, 3),
(120, 104, 4),
(121, 105, 1),
(128, 105, 3),
(122, 106, 1),
(129, 106, 3),
(123, 107, 1),
(124, 108, 1),
(125, 109, 1),
(126, 110, 1),
(127, 110, 3),
(130, 111, 1),
(133, 111, 3),
(136, 111, 4),
(131, 112, 1),
(135, 112, 3),
(138, 112, 4),
(132, 113, 1),
(134, 113, 3),
(137, 113, 4),
(139, 114, 1),
(145, 114, 3),
(149, 114, 4),
(140, 115, 1),
(144, 115, 3),
(148, 115, 4),
(141, 116, 1),
(143, 116, 3),
(147, 116, 4),
(142, 117, 1),
(146, 117, 3),
(150, 117, 4),
(151, 118, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_permission_view_role_id_seq`
--

CREATE TABLE `ab_permission_view_role_id_seq` (
  `next_not_cached_value` bigint(21) NOT NULL,
  `minimum_value` bigint(21) NOT NULL,
  `maximum_value` bigint(21) NOT NULL,
  `start_value` bigint(21) NOT NULL COMMENT 'start value when sequences is created or value if RESTART is used',
  `increment` bigint(21) NOT NULL COMMENT 'increment value',
  `cache_size` bigint(21) UNSIGNED NOT NULL,
  `cycle_option` tinyint(1) UNSIGNED NOT NULL COMMENT '0 if no cycles are allowed, 1 if the sequence should begin a new cycle when maximum_value is passed',
  `cycle_count` bigint(21) NOT NULL COMMENT 'How many cycles have been done'
) ENGINE=InnoDB;

--
-- Volcado de datos para la tabla `ab_permission_view_role_id_seq`
--

INSERT INTO `ab_permission_view_role_id_seq` (`next_not_cached_value`, `minimum_value`, `maximum_value`, `start_value`, `increment`, `cache_size`, `cycle_option`, `cycle_count`) VALUES
(1001, 1, 9223372036854775806, 1, 1, 1000, 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_register_user`
--

CREATE TABLE `ab_register_user` (
  `id` int(11) NOT NULL,
  `first_name` varchar(64) NOT NULL,
  `last_name` varchar(64) NOT NULL,
  `username` varchar(128) NOT NULL,
  `password` varchar(256) DEFAULT NULL,
  `email` varchar(320) NOT NULL,
  `registration_date` datetime DEFAULT NULL,
  `registration_hash` varchar(256) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_register_user_id_seq`
--

CREATE TABLE `ab_register_user_id_seq` (
  `next_not_cached_value` bigint(21) NOT NULL,
  `minimum_value` bigint(21) NOT NULL,
  `maximum_value` bigint(21) NOT NULL,
  `start_value` bigint(21) NOT NULL COMMENT 'start value when sequences is created or value if RESTART is used',
  `increment` bigint(21) NOT NULL COMMENT 'increment value',
  `cache_size` bigint(21) UNSIGNED NOT NULL,
  `cycle_option` tinyint(1) UNSIGNED NOT NULL COMMENT '0 if no cycles are allowed, 1 if the sequence should begin a new cycle when maximum_value is passed',
  `cycle_count` bigint(21) NOT NULL COMMENT 'How many cycles have been done'
) ENGINE=InnoDB;

--
-- Volcado de datos para la tabla `ab_register_user_id_seq`
--

INSERT INTO `ab_register_user_id_seq` (`next_not_cached_value`, `minimum_value`, `maximum_value`, `start_value`, `increment`, `cache_size`, `cycle_option`, `cycle_count`) VALUES
(1, 1, 9223372036854775806, 1, 1, 1000, 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_role`
--

CREATE TABLE `ab_role` (
  `id` int(11) NOT NULL,
  `name` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `ab_role`
--

INSERT INTO `ab_role` (`id`, `name`) VALUES
(1, 'Admin'),
(2, 'Public'),
(3, 'Supervisor'),
(4, 'Usuario');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_role_id_seq`
--

CREATE TABLE `ab_role_id_seq` (
  `next_not_cached_value` bigint(21) NOT NULL,
  `minimum_value` bigint(21) NOT NULL,
  `maximum_value` bigint(21) NOT NULL,
  `start_value` bigint(21) NOT NULL COMMENT 'start value when sequences is created or value if RESTART is used',
  `increment` bigint(21) NOT NULL COMMENT 'increment value',
  `cache_size` bigint(21) UNSIGNED NOT NULL,
  `cycle_option` tinyint(1) UNSIGNED NOT NULL COMMENT '0 if no cycles are allowed, 1 if the sequence should begin a new cycle when maximum_value is passed',
  `cycle_count` bigint(21) NOT NULL COMMENT 'How many cycles have been done'
) ENGINE=InnoDB;

--
-- Volcado de datos para la tabla `ab_role_id_seq`
--

INSERT INTO `ab_role_id_seq` (`next_not_cached_value`, `minimum_value`, `maximum_value`, `start_value`, `increment`, `cache_size`, `cycle_option`, `cycle_count`) VALUES
(1001, 1, 9223372036854775806, 1, 1, 1000, 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_user`
--

CREATE TABLE `ab_user` (
  `id` int(11) NOT NULL,
  `first_name` varchar(64) NOT NULL,
  `last_name` varchar(64) NOT NULL,
  `username` varchar(128) NOT NULL,
  `password` varchar(256) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `email` varchar(320) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `login_count` int(11) DEFAULT NULL,
  `fail_login_count` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `changed_on` datetime DEFAULT NULL,
  `created_by_fk` int(11) DEFAULT NULL,
  `changed_by_fk` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `ab_user`
--

INSERT INTO `ab_user` (`id`, `first_name`, `last_name`, `username`, `password`, `active`, `email`, `last_login`, `login_count`, `fail_login_count`, `created_on`, `changed_on`, `created_by_fk`, `changed_by_fk`) VALUES
(1, 'admin', 'admin', 'admin', 'scrypt:32768:8:1$3ZpExQvflgzQ0gaM$654815990a8f5df0ff53baabce4b733bd0b6a9fd17cbbc87ac1cff43c9cc80f8adfab3ec644237012db501e5e5ac5bbe124a3156d9026a55ad0e667d10f51e96', 1, 'admin@admin.com', '2026-06-26 06:48:03', 36, 0, '2026-06-22 00:31:48', '2026-06-22 00:31:48', NULL, NULL),
(2, 'supervisor', 'supervisor', 'supervisor', 'scrypt:32768:8:1$z1bUkpp4TwI7Pick$9a96d8b7bd3b07f9e4223e74ec7bb142c965d41d6a7d1cef40eba38732a671776548855c6db581e8d430491453727c603cdd2b673432d14253e3e79e0c7b9139', 1, 'supervisor@supervisor.com', '2026-06-26 00:23:56', 14, 0, '2026-06-22 00:33:32', '2026-06-22 00:33:32', NULL, NULL),
(3, 'usuario', 'usuario', 'usuario', 'scrypt:32768:8:1$N4xL1UIIH3Bnfm1q$937306095a3815e142e8f44c54553fa0ab02fba6f9a4b2107d1fc2717443ce0e443b0946ff7de57fca01450403bfb430a2987e3d3d8484ca3518ebb14827e697', 1, 'usuario@usuario.com', '2026-06-26 00:24:47', 7, 0, '2026-06-22 00:36:32', '2026-06-22 00:36:32', NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_user_group`
--

CREATE TABLE `ab_user_group` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_user_group_id_seq`
--

CREATE TABLE `ab_user_group_id_seq` (
  `next_not_cached_value` bigint(21) NOT NULL,
  `minimum_value` bigint(21) NOT NULL,
  `maximum_value` bigint(21) NOT NULL,
  `start_value` bigint(21) NOT NULL COMMENT 'start value when sequences is created or value if RESTART is used',
  `increment` bigint(21) NOT NULL COMMENT 'increment value',
  `cache_size` bigint(21) UNSIGNED NOT NULL,
  `cycle_option` tinyint(1) UNSIGNED NOT NULL COMMENT '0 if no cycles are allowed, 1 if the sequence should begin a new cycle when maximum_value is passed',
  `cycle_count` bigint(21) NOT NULL COMMENT 'How many cycles have been done'
) ENGINE=InnoDB;

--
-- Volcado de datos para la tabla `ab_user_group_id_seq`
--

INSERT INTO `ab_user_group_id_seq` (`next_not_cached_value`, `minimum_value`, `maximum_value`, `start_value`, `increment`, `cache_size`, `cycle_option`, `cycle_count`) VALUES
(1, 1, 9223372036854775806, 1, 1, 1000, 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_user_id_seq`
--

CREATE TABLE `ab_user_id_seq` (
  `next_not_cached_value` bigint(21) NOT NULL,
  `minimum_value` bigint(21) NOT NULL,
  `maximum_value` bigint(21) NOT NULL,
  `start_value` bigint(21) NOT NULL COMMENT 'start value when sequences is created or value if RESTART is used',
  `increment` bigint(21) NOT NULL COMMENT 'increment value',
  `cache_size` bigint(21) UNSIGNED NOT NULL,
  `cycle_option` tinyint(1) UNSIGNED NOT NULL COMMENT '0 if no cycles are allowed, 1 if the sequence should begin a new cycle when maximum_value is passed',
  `cycle_count` bigint(21) NOT NULL COMMENT 'How many cycles have been done'
) ENGINE=InnoDB;

--
-- Volcado de datos para la tabla `ab_user_id_seq`
--

INSERT INTO `ab_user_id_seq` (`next_not_cached_value`, `minimum_value`, `maximum_value`, `start_value`, `increment`, `cache_size`, `cycle_option`, `cycle_count`) VALUES
(1001, 1, 9223372036854775806, 1, 1, 1000, 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_user_role`
--

CREATE TABLE `ab_user_role` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `ab_user_role`
--

INSERT INTO `ab_user_role` (`id`, `user_id`, `role_id`) VALUES
(1, 1, 1),
(2, 2, 3),
(3, 3, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_user_role_id_seq`
--

CREATE TABLE `ab_user_role_id_seq` (
  `next_not_cached_value` bigint(21) NOT NULL,
  `minimum_value` bigint(21) NOT NULL,
  `maximum_value` bigint(21) NOT NULL,
  `start_value` bigint(21) NOT NULL COMMENT 'start value when sequences is created or value if RESTART is used',
  `increment` bigint(21) NOT NULL COMMENT 'increment value',
  `cache_size` bigint(21) UNSIGNED NOT NULL,
  `cycle_option` tinyint(1) UNSIGNED NOT NULL COMMENT '0 if no cycles are allowed, 1 if the sequence should begin a new cycle when maximum_value is passed',
  `cycle_count` bigint(21) NOT NULL COMMENT 'How many cycles have been done'
) ENGINE=InnoDB;

--
-- Volcado de datos para la tabla `ab_user_role_id_seq`
--

INSERT INTO `ab_user_role_id_seq` (`next_not_cached_value`, `minimum_value`, `maximum_value`, `start_value`, `increment`, `cache_size`, `cycle_option`, `cycle_count`) VALUES
(1001, 1, 9223372036854775806, 1, 1, 1000, 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_view_menu`
--

CREATE TABLE `ab_view_menu` (
  `id` int(11) NOT NULL,
  `name` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `ab_view_menu`
--

INSERT INTO `ab_view_menu` (`id`, `name`) VALUES
(30, 'Administracion'),
(9, 'AuthDBView'),
(22, 'Base Permissions'),
(29, 'Categorías'),
(28, 'CategoriaView'),
(36, 'Clientes'),
(35, 'ClienteView'),
(40, 'Empleados'),
(39, 'EmpleadoView'),
(51, 'GraficaPlatosCategoriaView'),
(50, 'Gráficas'),
(53, 'GraficaTopPlatosView'),
(48, 'GraficaVentasMesView'),
(32, 'Ingredientes'),
(47, 'Ingredientes más usados'),
(31, 'IngredienteView'),
(16, 'List Groups'),
(14, 'List Roles'),
(11, 'List Users'),
(3, 'LocaleView'),
(27, 'MenuApi'),
(38, 'Mesas'),
(37, 'MesaView'),
(26, 'Permission on Views/Menus'),
(21, 'PermissionModelView'),
(25, 'PermissionViewModelView'),
(34, 'Platos'),
(45, 'Platos más vendidos'),
(52, 'Platos por categoría'),
(33, 'PlatoView'),
(56, 'PosView'),
(55, 'PronosticosAPI'),
(1, 'PublicView'),
(5, 'RegisterUserDBView'),
(19, 'RegisterUserModelView'),
(46, 'ReporteIngredientesUsadosView'),
(44, 'ReportePlatosPopularesView'),
(43, 'Reportes'),
(41, 'ReporteVentasView'),
(8, 'ResetMyPasswordView'),
(7, 'ResetPasswordView'),
(13, 'RoleModelView'),
(12, 'Security'),
(4, 'SecurityApi'),
(54, 'Top 5 platos'),
(20, 'User Registrations'),
(18, 'User\'s Statistics'),
(10, 'UserDBModelView'),
(15, 'UserGroupModelView'),
(6, 'UserInfoEditView'),
(17, 'UserStatsChartView'),
(2, 'UtilView'),
(49, 'Ventas por mes'),
(42, 'Ventas por período'),
(23, 'ViewMenuModelView'),
(24, 'Views/Menus');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ab_view_menu_id_seq`
--

CREATE TABLE `ab_view_menu_id_seq` (
  `next_not_cached_value` bigint(21) NOT NULL,
  `minimum_value` bigint(21) NOT NULL,
  `maximum_value` bigint(21) NOT NULL,
  `start_value` bigint(21) NOT NULL COMMENT 'start value when sequences is created or value if RESTART is used',
  `increment` bigint(21) NOT NULL COMMENT 'increment value',
  `cache_size` bigint(21) UNSIGNED NOT NULL,
  `cycle_option` tinyint(1) UNSIGNED NOT NULL COMMENT '0 if no cycles are allowed, 1 if the sequence should begin a new cycle when maximum_value is passed',
  `cycle_count` bigint(21) NOT NULL COMMENT 'How many cycles have been done'
) ENGINE=InnoDB;

--
-- Volcado de datos para la tabla `ab_view_menu_id_seq`
--

INSERT INTO `ab_view_menu_id_seq` (`next_not_cached_value`, `minimum_value`, `maximum_value`, `start_value`, `increment`, `cache_size`, `cycle_option`, `cycle_count`) VALUES
(1001, 1, 9223372036854775806, 1, 1, 1000, 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`id`, `nombre`, `descripcion`) VALUES
(1, 'Entradas', 'Platos para empezar'),
(2, 'Platos principales', 'Platos fuertes'),
(3, 'Postres', 'Dulces tentaciones'),
(4, 'Bebidas', 'Refrescos y jugos'),
(5, 'Ensaladas', 'Opciones saludables');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `fecha_registro` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`id`, `nombre`, `apellido`, `email`, `telefono`, `direccion`, `fecha_registro`) VALUES
(1, 'Ana', 'Gómez', 'ana@email.com', NULL, NULL, '2026-06-22 00:27:42'),
(2, 'Luis', 'Martínez', 'luis@email.com', NULL, NULL, '2026-06-22 00:27:42'),
(3, 'Sofía', 'Ramírez', 'sofia@email.com', NULL, NULL, '2026-06-22 00:27:42'),
(4, 'Ana Lucia', 'Claure', 'ana@gmail.com', '6547895', 'Av. Km7', '2026-06-25 17:05:44'),
(5, 'Jorge', 'Cadima', NULL, NULL, NULL, '2026-06-26 00:42:35'),
(6, 'Lalo', 'Rodrigues', NULL, NULL, NULL, '2026-06-26 01:13:05'),
(7, 'Rogelio', 'Sanchez', NULL, NULL, NULL, '2026-06-26 06:48:50'),
(8, 'Angel', 'Duran', NULL, NULL, NULL, '2026-06-26 06:50:23');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_pedido`
--

CREATE TABLE `detalle_pedido` (
  `id` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `subtotal` float NOT NULL,
  `pedido_id` int(11) NOT NULL,
  `plato_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `detalle_pedido`
--

INSERT INTO `detalle_pedido` (`id`, `cantidad`, `subtotal`, `pedido_id`, `plato_id`) VALUES
(1, 1, 45, 1, 1),
(2, 2, 100, 1, 2),
(3, 1, 50, 2, 2),
(4, 2, 70, 2, 3),
(5, 1, 35, 3, 3),
(6, 2, 80, 3, 4),
(7, 1, 40, 4, 4),
(8, 2, 50, 4, 5),
(9, 1, 25, 5, 5),
(10, 2, 90, 5, 1),
(11, 1, 35, 6, 3),
(12, 1, 40, 6, 4),
(13, 1, 25, 6, 5),
(14, 1, 35, 7, 3),
(15, 1, 40, 7, 4),
(16, 1, 25, 7, 5),
(17, 2, 90, 8, 1),
(18, 1, 25, 8, 5),
(19, 2, 100, 9, 2),
(20, 2, 100, 10, 2),
(21, 4, 200, 11, 2),
(22, 1, 45, 12, 1),
(23, 1, 50, 12, 2),
(24, 1, 35, 12, 3),
(25, 1, 40, 12, 4),
(26, 1, 25, 12, 5),
(27, 1, 45, 13, 1),
(28, 2, 100, 13, 2),
(29, 1, 35, 13, 3),
(30, 1, 40, 13, 4),
(31, 1, 25, 13, 5),
(32, 2, 100, 14, 2),
(33, 1, 45, 15, 1),
(34, 1, 50, 15, 2),
(35, 1, 45, 16, 1),
(36, 1, 50, 16, 2),
(37, 1, 45, 17, 1),
(38, 1, 50, 17, 2),
(39, 1, 45, 18, 1),
(40, 1, 35, 18, 3),
(41, 3, 120, 18, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `cargo` varchar(50) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `fecha_contratacion` datetime DEFAULT NULL,
  `activo` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`id`, `nombre`, `apellido`, `cargo`, `email`, `telefono`, `fecha_contratacion`, `activo`) VALUES
(1, 'Juan', 'Pérez', 'Administrador', 'juan@eldeseo.com', NULL, '2026-06-22 00:27:42', 1),
(2, 'María', 'López', 'Cajero', 'maria@eldeseo.com', NULL, '2026-06-22 00:27:42', 1),
(3, 'Carlos', 'García', 'Cocinero', 'carlos@eldeseo.com', NULL, '2026-06-22 00:27:42', 1),
(4, 'Samuel', 'Lopez', 'mesero', 'samuel@samuel.com', '76902677', '2026-06-22 16:04:04', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ingrediente`
--

CREATE TABLE `ingrediente` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `unidad` varchar(30) NOT NULL,
  `stock` float NOT NULL,
  `precio_unitario` float NOT NULL,
  `stock_minimo` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `ingrediente`
--

INSERT INTO `ingrediente` (`id`, `nombre`, `unidad`, `stock`, `precio_unitario`, `stock_minimo`) VALUES
(1, 'Harina', 'gramos', 5000, 2.5, 500),
(2, 'Huevo', 'unidades', 100, 1, 20),
(3, 'Leche', 'mililitros', 10000, 1.2, 1000),
(4, 'Aceite', 'mililitros', 5000, 3, 500),
(5, 'Sal', 'gramos', 1000, 0.5, 100),
(6, 'Azúcar', 'gramos', 2000, 1, 200),
(7, 'Carne', 'gramos', 3000, 15, 500),
(8, 'Pollo', 'gramos', 4000, 12, 500),
(9, 'Arroz', 'gramos', 5000, 2, 500),
(10, 'Tomate', 'unidades', 50, 1.5, 10),
(11, 'Cebolla', 'unidades', 30, 1, 10),
(12, 'Queso', 'gramos', 2000, 8, 200),
(13, 'Mantequilla', 'gramos', 1000, 5, 100),
(14, 'Ajo', 'dientes', 100, 0.5, 20),
(15, 'Papas', 'gramos', 5000, 2, 500),
(16, 'Pasta', 'gramos', 3000, 3, 300);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mesa`
--

CREATE TABLE `mesa` (
  `id` int(11) NOT NULL,
  `numero` int(11) NOT NULL,
  `capacidad` int(11) NOT NULL,
  `estado` varchar(20) NOT NULL,
  `ubicacion` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `mesa`
--

INSERT INTO `mesa` (`id`, `numero`, `capacidad`, `estado`, `ubicacion`) VALUES
(1, 1, 4, 'ocupada', NULL),
(2, 2, 4, 'disponible', NULL),
(3, 3, 4, 'ocupada', ''),
(4, 4, 4, 'ocupada', NULL),
(5, 5, 4, 'ocupada', NULL),
(6, 6, 4, 'disponible', NULL),
(7, 7, 4, 'disponible', NULL),
(8, 8, 4, 'ocupada', NULL),
(9, 9, 4, 'disponible', NULL),
(10, 10, 4, 'disponible', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedido`
--

CREATE TABLE `pedido` (
  `id` int(11) NOT NULL,
  `fecha` datetime DEFAULT NULL,
  `total` float NOT NULL,
  `estado` varchar(20) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `mesa_id` int(11) DEFAULT NULL,
  `empleado_id` int(11) NOT NULL,
  `para_llevar` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `pedido`
--

INSERT INTO `pedido` (`id`, `fecha`, `total`, `estado`, `cliente_id`, `mesa_id`, `empleado_id`, `para_llevar`) VALUES
(1, '2026-06-22 00:27:42', 145, 'entregado', 1, 1, 1, 0),
(2, '2026-06-20 00:27:42', 120, 'entregado', 2, 2, 2, 0),
(3, '2026-06-18 00:27:42', 115, 'entregado', 3, 3, 3, 0),
(4, '2026-06-16 00:27:42', 90, 'entregado', 1, 4, 1, 0),
(5, '2026-06-14 00:27:42', 115, 'entregado', 2, 5, 2, 0),
(6, '2026-06-25 06:06:34', 100, 'pendiente', 1, 4, 3, 0),
(7, '2026-06-25 06:07:41', 100, 'pendiente', 2, 3, 1, 0),
(8, '2026-06-25 06:21:53', 115, 'pendiente', 1, 3, 3, 0),
(9, '2026-06-25 06:22:01', 100, 'pendiente', 1, 3, 3, 0),
(10, '2026-06-25 06:23:21', 100, 'pendiente', 3, 4, 4, 0),
(11, '2026-06-25 06:31:07', 200, 'pendiente', 2, 8, 4, 0),
(12, '2026-06-25 17:06:40', 195, 'pendiente', 4, 1, 4, 0),
(13, '2026-06-26 00:42:51', 245, 'pendiente', 5, NULL, 3, 1),
(14, '2026-06-26 01:13:22', 100, 'pendiente', 6, 1, 4, 0),
(15, '2026-06-26 06:49:01', 95, 'pendiente', 7, NULL, 4, 1),
(16, '2026-06-26 06:50:00', 95, 'pendiente', 7, NULL, 4, 1),
(17, '2026-06-26 06:50:00', 95, 'pendiente', 7, NULL, 4, 1),
(18, '2026-06-26 06:51:10', 200, 'pendiente', 8, 5, 4, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `plato`
--

CREATE TABLE `plato` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(300) DEFAULT NULL,
  `precio` float NOT NULL,
  `disponible` tinyint(1) DEFAULT NULL,
  `tiempo_preparacion` int(11) DEFAULT NULL,
  `categoria_id` int(11) NOT NULL,
  `imagen_url` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `plato`
--

INSERT INTO `plato` (`id`, `nombre`, `descripcion`, `precio`, `disponible`, `tiempo_preparacion`, `categoria_id`, `imagen_url`) VALUES
(1, 'Milanesa con papas', 'Milanesa de carne con papas fritas', 45, 1, NULL, 2, 'https://foodit.lanacion.com.ar/resizer/v2/el-truco-para-hacer-milanesas-de-bajo-MJ6775DYBRF3FNKAWVJVB6KY5I.jpg?auth=d69225ae02a7ee3cb62de88ec89b27b6b480558bff97cc7342a6d7c7f2db9c35&width=880&height=586&quality=70&smart=true'),
(2, 'Pollo al horno', 'Pollo horneado con papas y especias', 50, 1, NULL, 2, 'https://recetasbolivia.com/wp-content/uploads/Pollo-al-horno-Boliviano.webp'),
(3, 'Ensalada César', 'Ensalada con pollo, queso y aderezo César', 35, 1, NULL, 5, 'https://www.divinacocina.es/wp-content/uploads/2017/04/ensalada-cesar-rapida-facil-v.jpg'),
(4, 'Arroz con pollo', 'Arroz con pollo y verduras', 40, 1, NULL, 2, 'https://imag.bonviveur.com/arroz-con-pollo.webp'),
(5, 'Torta de chocolate', 'Torta de chocolate con crema', 25, 1, NULL, 3, 'https://foodit.lanacion.com.ar/resizer/v2/torta-de-chocolate-JQGHGPRQSFC7TIXM66LTN5AEH4.png?auth=5e6289a4df4f58c582d16ce96426d3e80eaafc11fef06130ebabd0b20796018e&width=880&height=586&quality=70&smart=true'),
(6, 'Trucha', 'Pecado', 35, 1, 30, 2, '/static/uploads/platos/plato_6_73aa1937.png'),
(7, 'Ch\'anga de Pollo', 'Sopa de Pollo', 30, 1, 20, 2, '/static/uploads/platos/plato_7_a301b0a8.webp');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `plato_ingrediente`
--

CREATE TABLE `plato_ingrediente` (
  `plato_id` int(11) NOT NULL,
  `ingrediente_id` int(11) NOT NULL,
  `cantidad` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `plato_ingrediente`
--

INSERT INTO `plato_ingrediente` (`plato_id`, `ingrediente_id`, `cantidad`) VALUES
(1, 2, 2),
(1, 4, 50),
(1, 5, 5),
(1, 7, 200),
(1, 15, 300),
(2, 4, 30),
(2, 5, 5),
(2, 8, 300),
(2, 14, 3),
(2, 15, 200),
(3, 2, 1),
(3, 4, 20),
(3, 5, 3),
(3, 8, 150),
(3, 12, 50),
(4, 5, 5),
(4, 8, 200),
(4, 9, 200),
(4, 11, 1),
(4, 14, 2),
(5, 1, 200),
(5, 2, 3),
(5, 3, 100),
(5, 6, 150),
(5, 13, 100);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `ab_api_key`
--
ALTER TABLE `ab_api_key`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uuid` (`uuid`),
  ADD UNIQUE KEY `lookup_hash` (`lookup_hash`),
  ADD UNIQUE KEY `idx_api_key_lookup_hash` (`lookup_hash`),
  ADD KEY `idx_api_key_user_id` (`user_id`),
  ADD KEY `idx_api_key_prefix` (`key_prefix`);

--
-- Indices de la tabla `ab_group`
--
ALTER TABLE `ab_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `ab_group_role`
--
ALTER TABLE `ab_group_role`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `group_id` (`group_id`,`role_id`),
  ADD KEY `idx_group_id` (`group_id`),
  ADD KEY `idx_group_role_id` (`role_id`);

--
-- Indices de la tabla `ab_permission`
--
ALTER TABLE `ab_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `ab_permission_view`
--
ALTER TABLE `ab_permission_view`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `permission_id` (`permission_id`,`view_menu_id`),
  ADD KEY `idx_permission_id` (`permission_id`),
  ADD KEY `idx_view_menu_id` (`view_menu_id`);

--
-- Indices de la tabla `ab_permission_view_role`
--
ALTER TABLE `ab_permission_view_role`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `permission_view_id` (`permission_view_id`,`role_id`),
  ADD KEY `idx_permission_view_id` (`permission_view_id`),
  ADD KEY `idx_role_id` (`role_id`);

--
-- Indices de la tabla `ab_register_user`
--
ALTER TABLE `ab_register_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `ab_role`
--
ALTER TABLE `ab_role`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `ab_user`
--
ALTER TABLE `ab_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `created_by_fk` (`created_by_fk`),
  ADD KEY `changed_by_fk` (`changed_by_fk`);

--
-- Indices de la tabla `ab_user_group`
--
ALTER TABLE `ab_user_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`,`group_id`),
  ADD KEY `idx_user_id` (`user_id`),
  ADD KEY `idx_user_group_id` (`group_id`);

--
-- Indices de la tabla `ab_user_role`
--
ALTER TABLE `ab_user_role`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`,`role_id`),
  ADD KEY `role_id` (`role_id`);

--
-- Indices de la tabla `ab_view_menu`
--
ALTER TABLE `ab_view_menu`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `detalle_pedido`
--
ALTER TABLE `detalle_pedido`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pedido_id` (`pedido_id`),
  ADD KEY `plato_id` (`plato_id`);

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `ingrediente`
--
ALTER TABLE `ingrediente`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `mesa`
--
ALTER TABLE `mesa`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `numero` (`numero`);

--
-- Indices de la tabla `pedido`
--
ALTER TABLE `pedido`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cliente_id` (`cliente_id`),
  ADD KEY `mesa_id` (`mesa_id`),
  ADD KEY `empleado_id` (`empleado_id`);

--
-- Indices de la tabla `plato`
--
ALTER TABLE `plato`
  ADD PRIMARY KEY (`id`),
  ADD KEY `categoria_id` (`categoria_id`);

--
-- Indices de la tabla `plato_ingrediente`
--
ALTER TABLE `plato_ingrediente`
  ADD PRIMARY KEY (`plato_id`,`ingrediente_id`),
  ADD KEY `ingrediente_id` (`ingrediente_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `detalle_pedido`
--
ALTER TABLE `detalle_pedido`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT de la tabla `empleado`
--
ALTER TABLE `empleado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `ingrediente`
--
ALTER TABLE `ingrediente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `mesa`
--
ALTER TABLE `mesa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `pedido`
--
ALTER TABLE `pedido`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `plato`
--
ALTER TABLE `plato`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `ab_api_key`
--
ALTER TABLE `ab_api_key`
  ADD CONSTRAINT `ab_api_key_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `ab_user` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `ab_group_role`
--
ALTER TABLE `ab_group_role`
  ADD CONSTRAINT `ab_group_role_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `ab_group` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `ab_group_role_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `ab_role` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `ab_permission_view`
--
ALTER TABLE `ab_permission_view`
  ADD CONSTRAINT `ab_permission_view_ibfk_1` FOREIGN KEY (`permission_id`) REFERENCES `ab_permission` (`id`),
  ADD CONSTRAINT `ab_permission_view_ibfk_2` FOREIGN KEY (`view_menu_id`) REFERENCES `ab_view_menu` (`id`);

--
-- Filtros para la tabla `ab_permission_view_role`
--
ALTER TABLE `ab_permission_view_role`
  ADD CONSTRAINT `ab_permission_view_role_ibfk_1` FOREIGN KEY (`permission_view_id`) REFERENCES `ab_permission_view` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `ab_permission_view_role_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `ab_role` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `ab_user`
--
ALTER TABLE `ab_user`
  ADD CONSTRAINT `ab_user_ibfk_1` FOREIGN KEY (`created_by_fk`) REFERENCES `ab_user` (`id`),
  ADD CONSTRAINT `ab_user_ibfk_2` FOREIGN KEY (`changed_by_fk`) REFERENCES `ab_user` (`id`);

--
-- Filtros para la tabla `ab_user_group`
--
ALTER TABLE `ab_user_group`
  ADD CONSTRAINT `ab_user_group_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `ab_user` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `ab_user_group_ibfk_2` FOREIGN KEY (`group_id`) REFERENCES `ab_group` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `ab_user_role`
--
ALTER TABLE `ab_user_role`
  ADD CONSTRAINT `ab_user_role_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `ab_user` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `ab_user_role_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `ab_role` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `detalle_pedido`
--
ALTER TABLE `detalle_pedido`
  ADD CONSTRAINT `detalle_pedido_ibfk_1` FOREIGN KEY (`pedido_id`) REFERENCES `pedido` (`id`),
  ADD CONSTRAINT `detalle_pedido_ibfk_2` FOREIGN KEY (`plato_id`) REFERENCES `plato` (`id`);

--
-- Filtros para la tabla `pedido`
--
ALTER TABLE `pedido`
  ADD CONSTRAINT `pedido_ibfk_1` FOREIGN KEY (`cliente_id`) REFERENCES `cliente` (`id`),
  ADD CONSTRAINT `pedido_ibfk_2` FOREIGN KEY (`mesa_id`) REFERENCES `mesa` (`id`),
  ADD CONSTRAINT `pedido_ibfk_3` FOREIGN KEY (`empleado_id`) REFERENCES `empleado` (`id`);

--
-- Filtros para la tabla `plato`
--
ALTER TABLE `plato`
  ADD CONSTRAINT `plato_ibfk_1` FOREIGN KEY (`categoria_id`) REFERENCES `categoria` (`id`);

--
-- Filtros para la tabla `plato_ingrediente`
--
ALTER TABLE `plato_ingrediente`
  ADD CONSTRAINT `plato_ingrediente_ibfk_1` FOREIGN KEY (`plato_id`) REFERENCES `plato` (`id`),
  ADD CONSTRAINT `plato_ingrediente_ibfk_2` FOREIGN KEY (`ingrediente_id`) REFERENCES `ingrediente` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
