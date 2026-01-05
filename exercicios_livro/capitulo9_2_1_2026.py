from pathlib import Path
import shutil
import random

BASE_DIR = Path.cwd()

escritorio = BASE_DIR / "escritorio"
pasta_documentos = escritorio / "documentos"
pasta_fotos = escritorio / "fotos"
pasta_imagens = escritorio / "imagens"

escritorio.mkdir(parents=True, exist_ok=True)
pasta_documentos.mkdir(parents=True, exist_ok=True)
pasta_fotos.mkdir(parents=True, exist_ok=True)
pasta_imagens.mkdir(parents=True, exist_ok=True)


for arquivo in escritorio.iterdir():
    if arquivo.is_file():
        if arquivo.suffix == ".jpg":
            shutil.move(arquivo, pasta_fotos / arquivo.name)
        elif arquivo.suffix == ".txt":
            shutil.move(arquivo, pasta_documentos / arquivo.name)
        elif arquivo.suffix == ".png":
            shutil.move(arquivo, pasta_imagens / arquivo.name)
