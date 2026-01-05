from pathlib import Path
import random

palavras = ["teste", "casa", "carro", "estrada", "python", "programacao", "desafio", "codigo", "arquivo", "sistema"]

BASE_DIR = Path.cwd()

pasta_provas = BASE_DIR / "provas"

pasta_provas.mkdir(parents=True, exist_ok=True)

for i in range(5):
    arquivo_alunos = pasta_provas / f"prova_aluno{i + 1}.txt"
    with open(arquivo_alunos, "w", encoding="utf-8") as a:
        a.write(random.choice(palavras))

        