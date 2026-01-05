import sqlite3

# =========================
# CRIA O BANCO E A TABELA
# (pode deixar aqui, não dá erro)
# =========================
conexao = sqlite3.connect("chamados.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chamados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT NOT NULL,
    setor TEXT NOT NULL,
    status TEXT NOT NULL
)
""")

conexao.commit()
conexao.close()

# =========================
# MENU SIMPLES
# =========================
print("1 - Abrir chamado")
print("2 - Listar chamados")

opcao = input("Escolha uma opção: ")

# =========================
# CADASTRO DE CHAMADO
# =========================
if opcao == "1":
    titulo = input("Título do chamado: ")
    descricao = input("Descrição do problema: ")
    setor = input("Setor (TI / RH / Financeiro): ")

    conexao = sqlite3.connect("chamados.db")
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO chamados (titulo, descricao, setor, status) VALUES (?, ?, ?, ?)",
        (titulo, descricao, setor, "Aberto")
    )

    conexao.commit()
    conexao.close()

    print("Chamado aberto com sucesso!")

# =========================
# LISTAGEM DE CHAMADOS
# =========================
else:
    conexao = sqlite3.connect("chamados.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM chamados")
    chamados = cursor.fetchall()

    if len(chamados) == 0:
        print("Nenhum chamado cadastrado.")
    else:
        for chamado in chamados:
            print(chamado)

    conexao.close()
