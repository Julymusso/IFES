-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 31, 2021 at 03:15 PM
-- Server version: 10.3.16-MariaDB
-- PHP Version: 7.3.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `id16352844_petshop`
--

-- --------------------------------------------------------

--
-- Table structure for table `agendamento`
--

CREATE TABLE `agendamento` (
  `id` int(11) NOT NULL,
  `idCliente` int(10) NOT NULL,
  `idPet` int(11) NOT NULL,
  `nome` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `tipoServico` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `data` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `horario` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `queixa` varchar(240) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `agendamento`
--

INSERT INTO `agendamento` (`id`, `idCliente`, `idPet`, `nome`, `tipoServico`, `data`, `horario`, `queixa`) VALUES
(1, 10, 3, 'Amora', 'Exame/Hemograma', '23/04/2021', '10:00', ''),
(2, 10, 6, 'Homer', 'Exame/Ultrassonografia', '2/4/2021', '10:30', ''),
(3, 10, 2, 'felix', 'Consulta/Saúde Bucal', '6/4/2021', '15:30', ''),
(4, 10, 1, 'Dog', 'Consulta/Veterinário', '30/4/2021', '15:00', 'Pelos caindo'),
(6, 13, 7, 'Snake', 'Estética/Hidratação', '3/6/2021', '14:00', ''),
(7, 13, 7, 'Snake', 'Exame/Hemograma', '30/4/2021', '14:30', 'cega');

-- --------------------------------------------------------

--
-- Table structure for table `animal`
--

CREATE TABLE `animal` (
  `id` int(10) NOT NULL,
  `idCliente` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `nome` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `sobrenome` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `rga` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `especie` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `raca` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `sexo` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `nascimento` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `observacao` varchar(200) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `animal`
--

INSERT INTO `animal` (`id`, `idCliente`, `nome`, `sobrenome`, `rga`, `especie`, `raca`, `sexo`, `nascimento`, `observacao`) VALUES
(1, '10', 'Dog', 'Silva', '356728', 'Cachorro', 'Pastor Alemão', 'M', '03/05/2008', ''),
(2, '10', 'felix', 'Felício', '276389', 'Gato', 'Siamês', 'M', '01/12/2019', ''),
(3, '10', 'Amora', 'Silva', '987345', 'Cachorro', 'Pitbul', 'F', '27/03/2011', ''),
(6, '13', 'Homer', 'Silva', '236748', 'Peixe', 'Salmão', 'M', '09/03/2008', ''),
(7, '13', 'Snake', 'Sheike', '9287451', 'Cobra', 'Sucuri', 'F', '24/08/2002', ''),
(12, '10', 'Bilu', '', '983765', 'Cachorro', 'Bulldog', 'F', '09/03/2018', '');

-- --------------------------------------------------------

--
-- Table structure for table `cliente`
--

CREATE TABLE `cliente` (
  `id` int(10) NOT NULL,
  `nome` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `sobrenome` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `cpf` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `rua` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `bairro` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `num` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `estado` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cidade` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cep` varchar(8) COLLATE utf8_unicode_ci DEFAULT NULL,
  `telefone` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `senha` varchar(15) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `cliente`
--

INSERT INTO `cliente` (`id`, `nome`, `sobrenome`, `cpf`, `rua`, `bairro`, `num`, `estado`, `cidade`, `cep`, `telefone`, `email`, `senha`) VALUES
(1, 'abacate', 'manga', 'pera', 'uva', 'salada', 'alaface', 'tomate', 'repolho', 'pepino', 'morango', 'cebola', 'alho'),
(2, 'abacaxi', 'cenoura', '123456', 'palito', 'churros', '01', 'goiaba', 'uva', '789456', '546731298', 'tirulipa@senado.com', 'cabrito'),
(10, 'Juliana', 'Musso', '11122233300', '', '', '', '', '', '', '27999349215', 'julianamusso@hotmail.com', '123abc'),
(13, 'Sergio', 'Musso', '12345698700', '', '', '', '', '', '', '27999999999', 'samusso@gmail.com', 'asd'),
(14, 'angela', 'musso', '637337', '', '', '', '', '', '', 'yeurur', 'angela', 'ahg'),
(15, 'agdhd', 'gshshs', 'bdhshdd', '', '', '', '', '', '', 'gshdhd', 'hdbxhd', 'bdbsbdbd');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `agendamento`
--
ALTER TABLE `agendamento`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `animal`
--
ALTER TABLE `animal`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `agendamento`
--
ALTER TABLE `agendamento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `animal`
--
ALTER TABLE `animal`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
