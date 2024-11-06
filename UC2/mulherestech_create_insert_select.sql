 -- criando meu primeiro banco de dados
CREATE DATABASE senac_copacabana;

-- criando minha primeira tabela/entidade
CREATE TABLE alunos (
  matricula INTEGER PRIMARY KEY,
  nome_aluno TEXT NOT NULL,
  genero TEXT NOT NULL
);
-- injeção de dados-teste
INSERT INTO alunos VALUES (1, 'Marian', 'F');
INSERT INTO alunos VALUES (2, 'Joana', 'F');

-- consultando as injeçoes realizadas
SELECT * FROM alunos WHERE matricula=1;


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
SELECT * FROM id_professor WHERE id_professor= 1;
SELECT * FROM id_professor WHERE id_professor= 2;
SELECT * FROM id_professor WHERE id_professor= 3;


CREATE TABLE turno (
id INT AUTO_INCREMENT PRIMARY KEY,
    nome_turno VARCHAR(100),
    horario_inicio TIME,
    horario_fim TIME
    );






