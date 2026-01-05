import sqlite3

# =========================================
# CRIA O BANCO DE DADOS E A TABELA
# =========================================
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

# =========================================
# MENU PRINCIPAL
# =========================================
print("\n📌 SISTEMA DE CHAMADOS INTERNOS")
print("Escolha uma opção abaixo:")
print("1 - Abrir um novo chamado")
print("2 - Ver chamados cadastrados")

opcao = input("\nDigite o número da opção desejada: ")

# =========================================
# ABERTURA DE CHAMADO
# =========================================
if opcao == "1":
    print("\n📝 ABERTURA DE CHAMADO")

    titulo = input("Título do chamado: ")
    descricao = input("Descreva o problema: ")
    setor = input("Setor responsável (TI / RH / Financeiro): ")

    conexao = sqlite3.connect("chamados.db")
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO chamados (titulo, descricao, setor, status) VALUES (?, ?, ?, ?)",
        (titulo, descricao, setor, "Aberto")
    )

    conexao.commit()
    conexao.close()

    print("\n✅ Chamado aberto com sucesso!")

# =========================================
# LISTAGEM DE CHAMADOS
# =========================================
else:
    print("\n📂 LISTA DE CHAMADOS")

    conexao = sqlite3.connect("chamados.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM chamados")
    chamados = cursor.fetchall()

    if len(chamados) == 0:
        print("Nenhum chamado encontrado no momento.")
    else:
        for chamado in chamados:
            print(
                f"\nID: {chamado[0]}"
                f"\nTítulo: {chamado[1]}"
                f"\nDescrição: {chamado[2]}"
                f"\nSetor: {chamado[3]}"
                f"\nStatus: {chamado[4]}"
                f"\n---------------------------"
            )

    conexao.close()


