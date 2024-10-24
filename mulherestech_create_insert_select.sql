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


CREATE TABLE cursos (
  id_curso INTEGER PRIMARY KEY,
  nome_curso TEXT NOT NULL,
  duracao INTEGER NOT NULL,  -- duração em meses
  nivel TEXT NOT NULL,       -- nível do curso (básico, intermediário, avançado)
  area TEXT NOT NULL,        -- área do curso (Ex: Tecnologia, Administração)
  descricao TEXT             -- descrição do curso
);

-- Injeção de dados
INSERT INTO cursos VALUES (1, 'Desenvolvimento Web', 6, 'Intermediário', 'Tecnologia', 'Curso de desenvolvimento de sites e aplicações web.');
INSERT INTO cursos VALUES (2, 'Marketing Digital', 4, 'Básico', 'Administração', 'Curso de estratégias de marketing em plataformas digitais.');
INSERT INTO cursos VALUES (3, 'Gestão de Projetos', 8, 'Avançado', 'Administração', 'Curso sobre práticas de gerenciamento de projetos.');
INSERT INTO cursos VALUES (4, 'Data Science', 12, 'Avançado', 'Tecnologia', 'Curso de ciência de dados e análise de big data.');
INSERT INTO cursos VALUES (5, 'Design Gráfico', 5, 'Intermediário', 'Arte', 'Curso de técnicas e ferramentas de design gráfico.');
INSERT INTO cursos VALUES (6, 'Finanças Pessoais', 3, 'Básico', 'Finanças', 'Curso sobre gerenciamento de finanças pessoais.');
INSERT INTO cursos VALUES (7, 'Programação em Python', 4, 'Intermediário', 'Tecnologia', 'Curso de programação utilizando a linguagem Python.');
INSERT INTO cursos VALUES (8, 'Comunicação Empresarial', 6, 'Intermediário', 'Comunicação', 'Curso de técnicas de comunicação no ambiente corporativo.');
INSERT INTO cursos VALUES (9, 'Inteligência Artificial', 10, 'Avançado', 'Tecnologia', 'Curso sobre conceitos e aplicações de inteligência artificial.');
INSERT INTO cursos VALUES (10, 'Recursos Humanos', 7, 'Intermediário', 'Administração', 'Curso de práticas e estratégias de gestão de recursos humanos.');

-- Consulta
SELECT * FROM cursos WHERE id_curso = 1;

CREATE TABLE filiais (
  id_filial INTEGER PRIMARY KEY,
  nome_filial TEXT NOT NULL,
  endereco TEXT NOT NULL,
  cidade TEXT NOT NULL,
  estado TEXT NOT NULL,
  telefone TEXT NOT NULL,
  email TEXT NOT NULL
);

-- Injeção de dados
INSERT INTO filiais VALUES (1, 'Filial Centro', 'Rua das Flores, 123', 'São Paulo', 'SP', '(11) 1234-5678', 'centro@empresa.com');
INSERT INTO filiais VALUES (2, 'Filial Norte', 'Av. Amazonas, 456', 'Manaus', 'AM', '(92) 8765-4321', 'norte@empresa.com');
INSERT INTO filiais VALUES (3, 'Filial Sul', 'Rua Paraná, 789', 'Curitiba', 'PR', '(41) 1122-3344', 'sul@empresa.com');
INSERT INTO filiais VALUES (4, 'Filial Leste', 'Av. Rio Branco, 101', 'Rio de Janeiro', 'RJ', '(21) 5566-7788', 'leste@empresa.com');
INSERT INTO filiais VALUES (5, 'Filial Oeste', 'Rua São João, 202', 'Porto Alegre', 'RS', '(51) 9988-7766', 'oeste@empresa.com');
INSERT INTO filiais VALUES (6, 'Filial Nordeste', 'Av. Boa Viagem, 303', 'Recife', 'PE', '(81) 2233-4455', 'nordeste@empresa.com');
INSERT INTO filiais VALUES (7, 'Filial Sudeste', 'Rua Libertador, 404', 'Belo Horizonte', 'MG', '(31) 3344-5566', 'sudeste@empresa.com');
INSERT INTO filiais VALUES (8, 'Filial Centro-Oeste', 'Av. Brasília, 505', 'Goiânia', 'GO', '(62) 5566-7788', 'centrooeste@empresa.com');
INSERT INTO filiais VALUES (9, 'Filial Noroeste', 'Rua Tocantins, 606', 'Palmas', 'TO', '(63) 6677-8899', 'noroeste@empresa.com');
INSERT INTO filiais VALUES (10, 'Filial Sudoeste', 'Av. Independência, 707', 'Campo Grande', 'MS', '(67) 7788-9900', 'sudoeste@empresa.com');

-- Consulta
SELECT * FROM filiais WHERE id_filial = 1;
    






