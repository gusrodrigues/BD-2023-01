# Criar tabela de estudantes
CREATE TABLE public.estudantes (
	nome varchar NOT NULL,
	matricula varchar NOT NULL,
	curso varchar NOT NULL,
	"admin" boolean NOT NULL,
	senha varchar NOT NULL
);

# Criar tabela professores
CREATE TABLE public.professores (
	nome varchar NOT NULL,
	matricula varchar NOT NULL,
	"admin" boolean NOT NULL
);

# Criar tabela Disciplinas
CREATE TABLE public.disciplinas (
	nome varchar NULL,
	cod varchar NULL,
	cod_depto varchar NULL
);

# Criar tabela Turmas
CREATE TABLE public.turmas (
	professor varchar NULL,
	horario varchar NULL,
	vagas_ocupadas varchar NULL,
	turma varchar NULL,
	periodo varchar NULL,
	total_vagas varchar NULL,
	"local" varchar NULL,
	cod_disciplina varchar NULL,
	cod_depto varchar NULL
);

# Criar tabela Departamentos
CREATE TABLE public.departamentos (
	nome varchar NULL,
	cod varchar NULL
);

# Criar tabela Avaliações
CREATE TABLE public.avaliacoes (
	turma varchar NULL,
	professor varchar NULL,
	avaliacao varchar NULL
);

# Criar tabela Denuncias
CREATE TABLE public.denuncias (
	denunciar varchar NULL,
	denuncia varchar NULL
);