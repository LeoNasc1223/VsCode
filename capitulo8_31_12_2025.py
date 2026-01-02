from pathlib import Path

"""
onde_estou = Path.cwd()

print(onde_estou)

arquivo_do_banco = Path.cwd() / "meu_banco_de_dados.db"

print(f"Banco de dados salvo em {arquivo_do_banco}")
"""
"""
caminho_final = Path.cwd() / "Projetos" / "Banco_de_dados.db"

print(caminho_final)
"""
"""
arquivo_db = Path.cwd() / "Banco_dados.db"

if arquivo_db.exists():
    print(f"O caminho para o banco de dados é {arquivo_db}")
else:
    print(f"O arquivo não existe!")
    arquivo_db.touch()
"""
"""
pasta_mes = Path.cwd() / "Relatorio_do_Mes"

pasta_mes.mkdir(parents=True, exist_ok=True)

print(f"A pasta para o relatório do mês esta em {pasta_mes}")
"""
"""
BASE_DIR = Path.cwd()



pasta_notas = BASE_DIR / "minhas_senhas"

arquivo = pasta_notas / "PW.txt"

pasta_notas.mkdir(parents=True, exist_ok=True)

if not arquivo.exists():
    texto = input(("Digite a senha para salvar:"))
    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(texto)
    print("Senha cadastrada")



while True:
    senha_inserida = input("Digite sua senha:")
    with open(arquivo, "r", encoding="utf-8") as r:
        senha_no_arquivo = r.read()
    if senha_inserida == senha_no_arquivo:
        print("Acesso Liberado!")
        break
    else:
        print("Acesso Negado!")
"""
