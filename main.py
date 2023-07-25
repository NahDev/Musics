import os
import shutil


def mover_arquivos_mp3(origem, destino):
    if not os.path.isdir(origem):
        print(f"Erro: O caminho '{origem}' não é um diretório válido.")
        return

    if not os.path.isdir(destino):
        print(f"Erro: O caminho '{destino}' não é um diretório válido.")
        return

    arquivos = os.listdir(origem)

    arquivos_mp3 = [arquivo for arquivo in arquivos if arquivo.endswith(".mp3")]

    for arquivo_mp3 in arquivos_mp3:
        origem_arquivo = os.path.join(origem, arquivo_mp3)
        destino_arquivo = os.path.join(destino, arquivo_mp3)
        shutil.move(origem_arquivo, destino_arquivo)
        print(f"Arquivo '{arquivo_mp3}' movido para '{destino}'.")


