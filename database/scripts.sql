create schema Lanchonete;

CREATE USER 'dono_lanchonete'@'localhost' IDENTIFIED BY 'uma_senha_forte';
GRANT SELECT, INSERT, UPDATE, DELETE ON lanchonete.* TO 'dono_lanchonete'@'localhost';

CREATE TABLE prato(
    id_prato INT(5) NOT NULL,
    nome_prato VARCHAR(60) NOT NULL,
    preco DECIMAL(5,2) NULL,
    validade int (3) not null,
    peso varchar (15) not null,
    
    primary key(id_prato)
);
 
CREATE TABLE pizza(
    id_prato INT(5) NOT NULL,
    molho VARCHAR(20) NOT NULL,
    recheio JSON,
    borda VARCHAR(20) NOT NULL,
    
    foreign key(id_prato) references prato(id_prato)
);

create table lanche(
	id_prato INT(5) NOT NULL,
	pao varchar(20) not null,
	recheio JSON,
	molhos JSON,
    
    foreign key(id_prato) references prato(id_prato)
);

create table salgado(
	id_prato INT(5) NOT NULL,
	recheio JSON,
	massa varchar(20) not null,
    
    foreign key(id_prato) references prato(id_prato)
);

CREATE TABLE cliente(
    id_cliente INT(5) NOT NULL,
    nome_cliente VARCHAR(60) NOT NULL,
    telefone VARCHAR(15) NOT NULL,
    rua VARCHAR(60) NOT NULL,
    cidade VARCHAR(60) NOT NULL,
    cod_Postal VARCHAR(60) NOT NULL,
    historico_pedidos JSON NOT NULL,
    
    primary key(id_cliente)
);

CREATE TABLE pedido(
    id_pedido INT(5) NOT NULL,
    id_cliente INT(5) NOT NULL,
    taxa_servico DECIMAL(5,2) NULL,
    
    primary key(id_pedido)
);

CREATE TABLE item_pedido(
	id_pedido INT(5) NOT NULL,
    id_prato INT(5) NOT NULL,
    quantidade INT(5) NOT NULL,
    
    foreign key(id_prato) references prato(id_prato),
    foreign key(id_pedido) references pedido(id_pedido)
);

INSERT INTO prato (id_prato, nome_prato, preco, validade, peso) VALUES
(1, 'Pizza de Calabresa com Queijo e Cebola', 32.90, 7, '800g'),
(2, 'Pizza de Frango com Bacon e Cebola', 35.90, 7, '850g'),
(3, 'Pizza de Muçarela com Tomate e Manjericão', 30.90, 7, '750g'),
(4, 'Pizza de Frango com Tomate Seco e Muçarela', 37.90, 7, '900g'),
(5, 'Pizza de Palmito com Cebola e Muçarela', 29.90, 7, '700g'),
(6, 'Pizza de Presunto com Palmito e Azeitona', 34.90, 7, '800g'),
(7, 'Pizza de Atum com Cebola e Azeitona', 33.90, 7, '800g'),
(8, 'Pizza de Calabresa com Cebola e Pimenta', 31.90, 7, '750g'),
(9, 'Sanduíche de Filé Mignon com Cheddar', 17.90, 3, '200g'),
(10, 'Hambúrguer de Carne com Queijo Prato', 12.90, 3, '150g'),
(11, 'Sanduíche de Peito de Peru com Mussarela', 14.90, 3, '180g'),
(12, 'Sanduíche de Frango Desfiado com Queijo Prato', 11.90, 3, '150g'),
(13, 'Sanduíche de Lombo Canadense com Mussarela', 9.90, 3, '150g'),
(14, 'Salgado de Carne com Queijo Prato', 3.50, 1, '50g'),
(15, 'Salgado de Frango com Catupiry', 3.50, 1, '50g'),
(16, 'Salgado de Presunto e Queijo com Tomate', 3.00, 1, '50g'),
(17, 'Salgado de Pizza com Muçarela, Calabresa e Cebola', 3.50, 1, '50g'),
(18, 'Coxinha de Frango', 3.00, 1, '50g'),
(19, 'Kibe de Carne', 3.00, 1, '50g'),
(20, 'Rissole de Camarão', 4.00, 1, '50g'),
(21, 'Empada de Palmito', 3.50, 1, '50g'),
(22, 'Enroladinho de Salsicha', 3.00, 1, '50g');


INSERT INTO pizza (id_prato, molho, recheio, borda) VALUES
(1, 'tomate', '{"sabores": ["calabresa", "queijo", "cebola"]}', 'catupiry'),
(2, 'barbecue', '{"sabores": ["frango", "bacon", "cebola"]}', 'cheddar'),
(3, 'tomate', '{"sabores": ["muçarela", "tomate", "manjericão"]}', 'tradicional'),
(4, 'pesto', '{"sabores": ["frango", "tomate seco", "muçarela"]}', 'catupiry'),
(5, 'tomate', '{"sabores": ["palmito", "cebola", "muçarela"]}', 'tradicional'),
(6, 'molho branco', '{"sabores": ["presunto", "palmito", "azeitona"]}', 'catupiry'),
(7, 'tomate', '{"sabores": ["atum", "cebola", "azeitona"]}', 'tradicional'),
(8, 'molho barbecue', '{"sabores": ["calabresa", "cebola", "pimenta"]}', 'chocolate');

INSERT INTO lanche (id_prato, pao, recheio, molhos) VALUES
(9, 'Pão Francês', '{"tipo": "Filé Mignon", "queijo": "Cheddar"}', '{"mostarda": true, "ketchup": true}'),
(10, 'Pão de Hambúrguer', '{"tipo": "Hambúrguer", "queijo": "Prato", "vegetais": ["alface", "tomate"]}', '{"maionese": true, "catchup": true}'),
(11, 'Pão Sírio', '{"tipo": "Peito de Peru", "queijo": "Mussarela", "vegetais": ["alface", "tomate", "cebola"]}', '{"barbecue": true, "mostarda": true}'),
(12, 'Pão Integral', '{"tipo": "Frango Desfiado", "queijo": "Prato", "vegetais": ["alface", "tomate", "cenoura"]}', '{"mostarda": true, "maionese": true}'),
(13, 'Baguete', '{"tipo": "Lombo Canadense", "queijo": "Mussarela", "vegetais": ["alface", "cebola"]}', '{"barbecue": true, "mostarda": true}');

INSERT INTO salgado (id_prato, recheio, massa) VALUES
(14, '{"tipo": "Carne", "queijo": "Prato", "vegetais": ["cebola", "tomate"]}', 'Folhado'),
(15, '{"tipo": "Frango", "queijo": "Catupiry"}', 'Massa Podre'),
(16, '{"tipo": "Presunto e Queijo", "vegetais": ["tomate"]}', 'Folhado'),
(17, '{"tipo": "Pizza", "recheio": ["muçarela", "calabresa", "cebola"]}', 'Massa de Pastel'),
(18, '{"tipo": "Coxinha", "recheio": "Frango"}', 'Massa de Batata'),
(19, '{"tipo": "Kibe", "recheio": "Carne"}', 'Massa de Trigo'),
(20, '{"tipo": "Rissole", "recheio": "Camarão"}', 'Massa Podre'),
(21, '{"tipo": "Empada", "recheio": "Palmito"}', 'Massa Podre'),
(22, '{"tipo": "Enroladinho", "recheio": "Salsicha"}', 'Massa de Pastel');


INSERT INTO cliente (id_cliente, nome_cliente, telefone, rua, cidade, cod_Postal, historico_pedidos)
VALUES
(1, 'João', '99999-1111', 'Rua A', 'São Paulo', '01234-567', '{"pedidos": []}'),
(2, 'Maria', '99999-2222', 'Rua B', 'Rio de Janeiro', '98765-432', '{"pedidos": []}'),
(3, 'Pedro', '99999-3333', 'Rua C', 'Belo Horizonte', '45678-901', '{"pedidos": []}'),
(4, 'Julia', '99999-4444', 'Rua D', 'Curitiba', '76543-210', '{"pedidos": []}'),
(5, 'Lucas', '99999-5555', 'Rua E', 'Salvador', '23456-789', '{"pedidos": []}'),
(6, 'Ana', '99999-6666', 'Rua F', 'Porto Alegre', '98765-432', '{"pedidos": []}'),
(7, 'Luiz', '99999-7777', 'Rua G', 'Recife', '54321-098', '{"pedidos": []}'),
(8, 'Carla', '99999-8888', 'Rua H', 'Florianópolis', '87654-321', '{"pedidos": []}'),
(9, 'Gabriel', '99999-9999', 'Rua I', 'Belém', '34567-890', '{"pedidos": []}');


INSERT INTO pedido (id_pedido, id_cliente, pratos_consumidos, taxa_servico)
VALUES (1, 2, '[{"id_prato": "7", "quantidade": 2}, {"id_prato": "9", "quantidade": 1}]', 10.00);

INSERT INTO pedido (id_pedido, id_cliente, pratos_consumidos, taxa_servico)
VALUES (2, 3, '[{"id_prato": "22", "quantidade": 1}, {"id_prato": "3", "quantidade": 10}]', 7.50);

INSERT INTO pedido (id_pedido, id_cliente, pratos_consumidos, taxa_servico)
VALUES (3, 1, '[{"id_prato": "13", "quantidade": 3}]', 12.00);

INSERT INTO pedido (id_pedido, id_cliente, pratos_consumidos, taxa_servico)
VALUES (4, 4, '[{"id_prato": "15", "quantidade": 1}, {"id_prato": "19", "quantidade": 15}]', 8.75);

ALTER TABLE salgado ADD tipo_salgado ENUM('Frito', 'Assado') NOT NULL;

UPDATE salgado SET tipo_salgado = 'Frito' WHERE id_prato IN (14, 16, 17, 18, 19, 22);
UPDATE salgado SET tipo_salgado = 'Assado' WHERE id_prato IN (15, 20, 21);

select * from pedido;

DELETE FROM pedido
WHERE id_pedido < 5;

ALTER TABLE pedido
DROP COLUMN pratos_consumidos;

INSERT INTO pedido (id_pedido, id_cliente, taxa_servico)
VALUES
    (1, 10, 2.50),
    (2, 12, 3.00),
    (3, 15, 4.20),
    (4, 20, 1.50),
    (5, 8, 5.75);

INSERT INTO item_pedido (id_pedido, id_prato, quantidade) VALUES
(1, 1, 2),
(1, 5, 1),
(1, 7, 3),
(2, 2, 1),
(2, 9, 2),
(2, 12, 1),
(3, 4, 4),
(4, 16, 2),
(5, 19, 3);

INSERT INTO cliente (id_cliente, nome_cliente, telefone, rua, cidade, cod_Postal, historico_pedidos)
VALUES 
(10, 'Joana Silva', '(11) 99999-1111', 'Rua das Flores, 123', 'São Paulo', '01234-567', '{"pedidos": []}'),
(11, 'Pedro Oliveira', '(21) 99999-2222', 'Rua dos Passarinhos, 456', 'Rio de Janeiro', '01234-567', '{"pedidos": []}'),
(12, 'Leticia Santos', '(11) 99999-3333', 'Av. Paulista, 1234', 'São Paulo', '01234-567', '{"pedidos": []}'),
(13, 'Lucas Souza', '(19) 99999-4444', 'Rua dos Girassóis, 789', 'Campinas', '01234-567', '{"pedidos": []}'),
(14, 'Fernanda Alves', '(11) 99999-5555', 'Rua das Margaridas, 456', 'São Paulo', '01234-567', '{"pedidos": []}'),
(15, 'Rafael Lima', '(31) 99999-6666', 'Av. Afonso Pena, 567', 'Belo Horizonte', '01234-567', '{"pedidos": []}'),
(16, 'Gabriela Ferreira', '(11) 99999-7777', 'Rua dos Cravos, 890', 'São Paulo', '01234-567', '{"pedidos": []}'),
(17, 'Mauricio Oliveira', '(11) 99999-8888', 'Rua das Orquídeas, 123', 'São Paulo', '01234-567', '{"pedidos": []}'),
(18, 'Carla Santos', '(11) 99999-9999', 'Rua das Tulipas, 456', 'São Paulo', '01234-567', '{"pedidos": []}'),
(19, 'Gustavo Souza', '(21) 99999-0000', 'Rua dos Jasmins, 789', 'Rio de Janeiro', '01234-567', '{"pedidos": []}'),
(20, 'Julia Alves', '(11) 99999-1111', 'Av. Brigadeiro Faria Lima, 1234', 'São Paulo', '01234-567', '{"pedidos": []}'),
(21, 'Thiago Lima', '(19) 99999-2222', 'Rua dos Lírios, 456', 'Campinas', '01234-567', '{"pedidos": []}'),
(22, 'Ana Santos', '(11) 99999-3333', 'Rua dos Antúrios, 789', 'São Paulo', '01234-567', '{"pedidos": []}'),
(23, 'Bruno Souza', '(31) 99999-4444', 'Rua dos Crisântemos, 123', 'Belo Horizonte', '01234-567', '{"pedidos": []}'),
(24, 'Renata Ferreira', '(11) 99999-5555', 'Rua das Camélias, 456', 'São Paulo', '01234-567', '{"pedidos": []}'),
(25, 'Fabio Oliveira', '(11) 99999-6666', 'Av. Paulista, 567', 'São Paulo', '01234-567', '{"pedidos": []}');


INSERT INTO pedido (id_pedido, id_cliente, taxa_servico)
VALUES
    (11, 10, 2.50),
    (12, 12, 3.00),
    (13, 15, 4.20),
    (14, 20, 1.50),
    (15, 8, 5.75),
    (6, 10, 1.50),
    (7, 15, 2.75),
    (8, 20, 3.25),
    (9, 12, 4.00),
    (10, 10, 5.50);

INSERT INTO item_pedido (id_item, id_pedido, id_prato, quantidade) VALUES
	(1, 1, 1, 2),
	(2, 1, 5, 1),
	(3, 1, 7, 3),
	(4, 2, 2, 1),
	(5, 2, 9, 2),
	(6, 2, 12, 1),
	(7, 3, 4, 4),
	(8, 4, 16, 2),
	(9, 5, 19, 3),
    (10, 6, 1, 2),
    (11, 6, 5, 1),
    (12, 6, 7, 3),
    (13, 7, 2, 1),
    (14, 7, 9, 2),
    (15, 7, 12, 1),
    (16, 8, 4, 4),
    (17, 9, 16, 2),
    (18, 10, 19, 3),
    (19, 11, 3, 2),
    (20, 12, 8, 1),
    (21, 12, 15, 2),
    (22, 13, 6, 1),
    (23, 13, 10, 1),
    (24, 13, 13, 3),
    (25, 14, 17, 2),
    (26, 14, 20, 2),
    (27, 14, 22, 1),
    (28, 15, 11, 3),
    (29, 15, 14, 1),
    (30, 15, 18, 2),
    (31, 1, 2, 2),
    (32, 3, 5, 1),
    (33, 8, 9, 1);
    

SELECT
    pedido.id_pedido,
    cliente.id_cliente,
    cliente.nome_cliente, 
    prato.id_prato, 
    prato.nome_prato, 
    prato.preco,
    item_pedido.quantidade,
    pedido.taxa_servico
FROM prato
JOIN item_pedido ON prato.id_prato = item_pedido.id_prato
JOIN pedido      ON item_pedido.id_pedido = pedido.id_pedido
JOIN cliente     ON pedido.id_cliente = cliente.id_cliente;

ALTER TABLE item_pedido
ADD COLUMN id INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;

ALTER TABLE item_pedido
ADD CONSTRAINT fk_item_pedido_pedido FOREIGN KEY (id_pedido) REFERENCES pedido (id_pedido),
ADD CONSTRAINT fk_item_pedido_prato FOREIGN KEY (id_prato) REFERENCES prato (id_prato);

ALTER TABLE item_pedido CHANGE id id_item INT NOT NULL;

SELECT
	prato.id_prato,
    prato.nome_prato,
    prato.preco,
    lanche.pao,
    lanche.recheio,
    lanche.molhos
FROM prato
JOIN lanche ON prato.id_prato = lanche.id_prato;


SELECT
	prato.id_prato,
    prato.nome_prato,
    prato.preco,
    pizza.molho,
    pizza.recheio,
    pizza.borda  
FROM prato
JOIN pizza ON prato.id_prato = pizza.id_prato;

SELECT
	prato.id_prato,
    prato.nome_prato,
    prato.preco,
    salgado.recheio,
    salgado.massa,
    salgado.tipo_salgado
FROM prato
JOIN salgado ON prato.id_prato = salgado.id_prato;


SELECT
	pedido.id_pedido,
    pedido.status,
    item_pedido.id_item,
    item_pedido.quantidade,
    prato.id_prato,
    prato.nome_prato,
    prato.preco,
    cliente.id_cliente,
    cliente.nome_cliente,
    pedido.taxa_servico
FROM pedido
JOIN item_pedido ON pedido.id_pedido = item_pedido.id_prato
JOIN prato ON item_pedido.id_prato = prato.id_prato
JOIN cliente ON pedido.id_cliente = cliente.id_cliente;

SELECT *
FROM item_pedido;
   

SELECT
	prato.id_prato,
    prato.nome_prato,
    prato.preco,
    lanche.pao,
    lanche.recheio,
    lanche.molhos,
    pizza.molho,
    pizza.recheio,
    pizza.borda,
    salgado.recheio,
    salgado.massa,
    salgado.tipo_salgado
  
FROM prato
LEFT JOIN salgado ON prato.id_prato = salgado.id_prato
LEFT JOIN lanche      ON prato.id_prato = lanche.id_prato
LEFT JOIN pizza     ON prato.id_prato = pizza.id_prato;

ALTER TABLE Pedido
ADD COLUMN status VARCHAR(50) DEFAULT 'pendente' NOT NULL;

Select * from pedido;

SET FOREIGN_KEY_CHECKS=0;

ALTER TABLE pedido
MODIFY COLUMN id_pedido INT AUTO_INCREMENT;
ALTER TABLE pedido AUTO_INCREMENT = 16;

ALTER TABLE item_pedido
ADD CONSTRAINT fk_id_pedido FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido);

SET FOREIGN_KEY_CHECKS=1;

INSERT INTO pedido (id_cliente)
VALUES (1);

select * from salgado;

SELECT  item_pedido.id_item,
        item_pedido.id_pedido,
		item_pedido.id_prato,
        prato.nome_prato,
        prato.preco,
		item_pedido.quantidade
FROM pedido
JOIN item_pedido ON item_pedido.id_pedido = pedido.id_pedido
JOIN prato ON item_pedido.id_prato = prato.id_prato
WHERE item_pedido.id_pedido = 1; 

       
        """