-- ATIVIDADE: Crie uma nova tabela chamada 'professores", com a mesma quantidade de características de 'alunos', fazendo ao menos duas injeções de dados e uma consulta.

CREATE TABLE professor (
  id_professor INTEGER PRIMARY KEY,
  nome_professor TEXT NOT NULL,
  qualificacao TEXT NOT NULL
);
-- injeção de dados-teste
INSERT INTO professor VALUES (1, 'Matheus', 'Formação técnica');
INSERT INTO professor VALUES (2, 'Joana', 'Formação licenciatura');
INSERT INTO professor VALUES (3, 'Pedro', 'Formação licenciatura');



-- consultando as injeçoes realizadas
SELECT * FROM professor WHERE professor= 1;
SELECT * FROM professor WHERE professor= 2;
SELECT * FROM professor WHERE professor= 3;