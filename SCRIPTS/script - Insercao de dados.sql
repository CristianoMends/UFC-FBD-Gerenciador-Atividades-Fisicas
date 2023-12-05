-- Povoamento da tabela USUARIO
INSERT INTO USUARIO (NOME, SOBRENOME, DATA_NASCIMENTO, PESO, ALTURA)
VALUES
    ('João', 'Silva', '1990-01-01', 70.5, 1.75),
    ('Maria', 'Santos', '1988-05-12', 65.2, 1.68),
    ('Pedro', 'Almeida', '1995-11-30', 80.1, 1.80),
    ('Ana', 'Oliveira', '1992-03-15', 55.7, 1.60),
    ('Carlos', 'Souza', '1998-07-20', 73.4, 1.76),
    ('Mariana', 'Ribeiro', '1993-09-25', 68.9, 1.72),
    ('Lucas', 'Cunha', '1991-02-18', 75.0, 1.78),
    ('Fernanda', 'Machado', '1989-06-06', 60.3, 1.65),
    ('Gustavo', 'Barros', '1997-04-10', 82.5, 1.85),
    ('Sandra', 'Ferreira', '1994-08-28', 58.0, 1.63);

-- Povoamento da tabela LOGIN
INSERT INTO LOGIN (USUARIO, SENHA)
VALUES
    ('e', 'senha123'),
    ('maria.santos', 'senha456'),
    ('pedro.almeida', 'senha789'),
    ('ana.oliveira', 'senhaabc'),
    ('carlos.souza', 'senhadef'),
    ('mariana.ribeiro', 'senhaghi'),
    ('lucas.cunha', 'senhajkl'),
    ('fernanda.machado', 'senhamno'),
    ('gustavo.barros', 'senhapqr'),
    ('sandra.ferreira', 'senhastu');

INSERT INTO EXERCICIO (NOME, GRUPO_MUSCULAR, PARTE_MUSCULAR, EQUIPAMENTO, PESO_UTILIZADO, DATA, HORA, REPETICOES, USUARIO_ID)
VALUES
    ('Leg Press', 'Pernas', 'Quadríceps', 'Leg Press', 80.0, '2023-10-01', '14:00', 10, 1),
    ('Supino na Máquina', 'Peitoral', 'Peitoral Maior', 'Chest Press', 30.0, '2023-10-02', '15:30', 12, 2),
    ('Desenvolvimento na Máquina', 'Ombros', 'Deltoides', 'Shoulder Press', 15.0, '2023-10-03', '16:45', 8, 3),
    ('Pulldown', 'Costas', 'Latíssimo do Dorso', 'Lat Pulldown', 70.0, '2023-10-04', '17:15', 6, 4),
    ('Prensa de Pernas', 'Pernas', 'Glúteos', 'Leg Press', 80.0, '2023-10-05', '18:00', 15, 5),
    ('Rosca Direta na Máquina', 'Braços', 'Bíceps', 'Biceps Curl', 20.0, '2023-10-06', '19:20', 10, 6),
    ('Puxada Alta na Máquina', 'Costas', 'Latíssimo do Dorso', 'Lat Pulldown', 35.0, '2023-10-07', '14:30', 12, 7),
    ('Prensa de Peito', 'Peitoral', 'Peitoral Maior', 'Chest Press', 45.0, '2023-10-08', '15:45', 8, 8),
    ('Extensão de Pernas', 'Pernas', 'Quadríceps', 'Leg Extension', 60.0, '2023-10-09', '16:20', 20, 9);