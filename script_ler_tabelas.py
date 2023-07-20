from pathlib import Path
import csv
import re
import db
import os

conexao = db.connect()

local_path = os.path.dirname(os.path.abspath(__file__)) + "/bd_files"

def lista_arquivos_csv():
    arquivos_csv = []
    for p, _, files in os.walk(os.path.abspath(local_path)):
        for file in files:
            if re.search('.csv$', file):
                arquivos_csv.append(os.path.join(p, file))

    return arquivos_csv

def ler_arquivo_csv(arquivo):
    with open(arquivo, newline='') as csvFile:
        linhas = csv.reader(csvFile, delimiter=',')
        for idx, linha in enumerate(linhas):
            if re.search('departamentos', arquivo):
                if idx != 0:
                    #cod,nome
                    colunas = '"cod", "nome"'
                    cursor = conexao.cursor()
                    valores = (linha[0], linha[1])
                    db.inserir(cursor, "departamentos", colunas, valores)

            elif re.search('disciplinas', arquivo):
                #cod,nome,cod_depto
                if idx != 0:
                    colunas = '"cod", "nome", "cod_depto"'
                    cursor = conexao.cursor()
                    valores = (linha[0], linha[1], linha[2])
                    db.inserir(cursor, "disciplinas", colunas, valores)

            elif re.search('turmas', arquivo):
               #turma,periodo,professor,horario,vagas_ocupadas,total_vagas,local,cod_disciplina,cod_depto
                if idx != 0:
                    colunas = '"turma", "periodo", "professor", "horario", "vagas_ocupadas", "total_vagas", "local", "cod_disciplina", "cod_depto"'
                    cursor = conexao.cursor()
                    valores = (linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8])
                    db.inserir(cursor, "turmas", colunas, valores)

if __name__ == "__main__":

    arquivos_csv = lista_arquivos_csv()

    for arquivo in arquivos_csv:
        ler_arquivo_csv(arquivo)

    conexao.commit()
    db.close(conexao.cursor(), conexao)