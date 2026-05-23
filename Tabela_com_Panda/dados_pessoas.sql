CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    localizacao VARCHAR(100),
    salario DECIMAL(10, 2),
    genero VARCHAR(20)
);

INSERT INTO funcionarios (nome, localizacao, salario, genero) VALUES
('Ana Silva', 'São Paulo, SP', 4500.5, 'Feminino'),
('Bruno Santos', 'Rio de Janeiro, RJ', 3200.0, 'Masculino'),
('Carla Oliveira', 'Belo Horizonte, MG', 5800.75, 'Feminino'),
('Diego Costa', 'Curitiba, PR', 4100.0, 'Masculino'),
('Eduarda Lima', 'Salvador, BA', 2900.0, 'Feminino'),
('Fernando Souza', 'Porto Alegre, RS', 7200.4, 'Masculino'),
('Gabriela Rocha', 'Brasília, DF', 5100.25, 'Feminino'),
('Henrique Almeida', 'Fortaleza, CE', 3600.0, 'Masculino'),
('Isabela Martins', 'Recife, PE', 6300.9, 'Feminino'),
('João Pereira', 'Manaus, AM', 4800.0, 'Masculino');