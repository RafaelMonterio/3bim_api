-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 24/08/2026 às 20:55
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `loja`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `petsdb`
--

CREATE TABLE `petsdb` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `especie` varchar(100) NOT NULL,
  `raca` varchar(100) NOT NULL,
  `idade` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `petsdb`
--

INSERT INTO `petsdb` (`id`, `nome`, `especie`, `raca`, `idade`) VALUES
(2, 'string', 'string', 'string', 0),
(3, 'thechoices', 'cachorro', 'beagle', 67),
(4, 'thechoices', 'gato', 'shrondiguer', 75),
(5, 'barney', 'coelho', 'branco', 6),
(6, 'eduardo', 'cachorro', 'dalmata', 0);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `petsdb`
--
ALTER TABLE `petsdb`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_PetsDB_id` (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `petsdb`
--
ALTER TABLE `petsdb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
