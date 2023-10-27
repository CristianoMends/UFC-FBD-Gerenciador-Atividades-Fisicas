Selecione o e-mail e a senha do login para o usuário com ID 1 da tabela LOGIN:

SELECT EMAIL, PASSWORD
FROM LOGIN WHERE USER_ID = 1;

Selecione todos os exercícios realizados pelo usuário com ID 1 da tabela EXERCISE:

SELECT *
FROM EXERCISE WHERE USER_ID = 1;

Selecione os exercícios realizados pelo usuário com ID 1 na data '2023-10-05' da tabela EXERCISE:

SELECT *
FROM EXERCISE
WHERE USER_ID = 1 AND
      DATE = '2023-10-05';

Selecione os exercícios realizados pelo usuário com ID 1 com mais de 10 repetições da tabela EXERCISE:

SELECT *
FROM EXERCISE
WHERE USER_ID = 1 AND
      REPETITIONS > 10;

selecione IMC do usuario ID = 1

SELECT FIST_NAME, LAST_NAME, WEIGHT, HEIGTH, 
    (WEIGHT / (HEIGTH * HEIGTH)) as IMC
FROM USER_
WHERE USER_ID = 1;

selecione o nome do exercicio mais executado

SELECT NAME, COUNT(*) AS TOTAL_EXECUTADO
FROM EXERCISE
WHERE USER_ID = 1
GROUP BY NAME
ORDER BY TOTAL_EXECUTADO DESC
LIMIT 1;

Maior peso registrado nos exercícios do usuário com ID 1:

SELECT MAX(WEIGHT_USED) AS MAIOR_PESO
FROM EXERCISE
WHERE USER_ID = 1;

Número total de exercícios registrados pelo usuário com ID 1:

SELECT COUNT(*) AS TOTAL_EXERCICIOS
FROM EXERCISE
WHERE USER_ID = 1;



