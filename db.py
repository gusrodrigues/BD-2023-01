import psycopg2

# Iniciar conexão com banco de dados
def connect():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password="12345")

    # Abrir conexão com banco de dados
    return conn

# Encerrar conexão com banco de dados
def close(cur, conn):
    # Encerrar cursor
    cur.close()

    # Encerrar conexão
    conn.close()

# Inserir informações no banco
def inserir(cursor, tabela, colunas, valores):
    # Inserir novo valor
    print(('INSERT INTO public.'+ str(tabela) +' ('+ str(colunas) +') VALUES'+ str(valores) +';'))
    cursor.execute('INSERT INTO public.'+ str(tabela) +' ('+ str(colunas) +') VALUES'+ str(valores) +';')

def view():
    pass

def update():
    pass

def selectAll(cursor, tabela):
    cursor.execute("SELECT * FROM public."+ tabela +";")
    return cursor.fetchall()

def select():
    pass
# cur.execute("SELECT * FROM public.estudantes;")
# print(cur.fetchall())