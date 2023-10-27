-- Inserindo dados na tabela USER_
INSERT INTO USER_ (FIST_NAME, LAST_NAME, DATE_BIRTH, WEIGHT, HEIGTH) 
VALUES ('João', 'Silva', '1990-01-01', 70.5, 1.75),
       ('Maria', 'Santos', '1988-05-12', 65.2, 1.68),
       ('Pedro', 'Almeida', '1995-11-30', 80.1, 1.80),
       ('Ana', 'Oliveira', '1992-03-15', 55.7, 1.60),
       ('Carlos', 'Souza', '1998-07-20', 73.4, 1.76),
       ('Mariana', 'Ribeiro', '1993-09-25', 68.9, 1.72),
       ('Lucas', 'Cunha', '1991-02-18', 75.0, 1.78),
       ('Fernanda', 'Machado', '1989-06-06', 60.3, 1.65),
       ('Gustavo', 'Barros', '1997-04-10', 82.5, 1.85),
       ('Sandra', 'Ferreira', '1994-08-28', 58.0, 1.63);

-- Inserindo dados na tabela LOGIN
INSERT INTO LOGIN (EMAIL, PASSWORD) 
VALUES ('joao.silva@example.com', 'senha123'),
       ('maria.santos@example.com', 'senha456'),
       ('pedro.almeida@example.com', 'senha789'),
       ('ana.oliveira@example.com', 'senhaabc'),
       ('carlos.souza@example.com', 'senhadef'),
       ('mariana.ribeiro@example.com', 'senhaghi'),
       ('lucas.cunha@example.com', 'senhajkl'),
       ('fernanda.machado@example.com', 'senhamno'),
       ('gustavo.barros@example.com', 'senhapqr'),
       ('sandra.ferreira@example.com', 'senhastu');

-- Inserindo dados na tabela EXERCISE
INSERT INTO EXERCISE (NAME, MUSCLE_GROUP, MUSCLE_PART, EQUIPMENT, WEIGHT_USED, DATE, HOUR, REPETITIONS, USER_ID) 
VALUES ('Agachamento', 'Pernas', 'Quadríceps', 'Barra', 50.0, '2023-10-01', '14:00', 10, 1),
       ('Supino', 'Peitoral', 'Peitoral Maior', 'Barra', 30.0, '2023-10-02', '15:30', 12, 2),
       ('Desenvolvimento', 'Ombros', 'Deltoides', 'Halteres', 15.0, '2023-10-03', '16:45', 8, 3),
       ('Levantamento Terra', 'Costas', 'Eretores da Espinha', 'Barra', 70.0, '2023-10-04', '17:15', 6, 4),
       ('Flexão de Braço', 'Braços', 'Tríceps e Peitoral', 'Peso Corporal', 0.0, '2023-10-05', '18:00', 15, 5),
       ('Rosca Direta', 'Braços', 'Bíceps', 'Barra', 20.0, '2023-10-06', '19:20', 10, 6),
       ('Leg Press', 'Pernas', 'Glúteos', 'Máquina', 80.0, '2023-10-07', '14:30', 12, 7),
       ('Puxada Alta', 'Costas', 'Latíssimo do Dorso', 'Barra', 35.0, '2023-10-08', '15:45', 8, 8),
       ('Abdominal', 'Abdômen', 'Retos Abdominais', 'Peso Corporal', 0.0, '2023-10-09', '16:20', 20, 9),
       ('Caminhada', 'Cardio', 'Corpo Inteiro', NULL, 0.0, '2023-10-10', '17:00', 30, 10);
