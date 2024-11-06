--criando meu primeiro banco de dados
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
SELECT * FROM alunos WHERE matricula=1


-- ATIVIDADE: Crie uma nova tabela chamada 'professores", com a mesma quantidade de características de 'alunos'


