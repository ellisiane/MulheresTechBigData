-- ATIVIDADE: Crie uma nova tabela chamada 'professores", com a mesma quantidade de características de 'alunos', fazendo ao menos duas injeções de dados e uma consulta.

CREATE TABLE id_professor (
  id_professor INTEGER PRIMARY KEY,
  nome_professor TEXT NOT NULL,
  qualificacao TEXT NOT NULL
);
-- injeção de dados-teste
INSERT INTO id_professor VALUES (1, 'Matheus', 'Formação técnica');
INSERT INTO id_professor VALUES (2, 'Joana', 'Formação licenciatura');
INSERT INTO id_professor VALUES (3, 'Pedro', 'Formação licenciatura');



-- consultando as injeçoes realizadas
SELECT * FROM id_professor WHERE id_professor= 1;
SELECT * FROM id_professor WHERE id_professor= 2;
SELECT * FROM id_professor WHERE id_professor= 3;