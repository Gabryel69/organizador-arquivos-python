import os
import shutil

#Pasta onde vao estar os arquivos
PASTA_ORIGEM = "arquivos"

#Tipos de arquivos e suas pastas
EXTENSOES = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Musicas": [".mp3", ".wav"],
    "Compactados": [".zip", "rar"]
}

def criar_pastas():
    for pasta in EXTENSOES.keys():
        if not os.path.exists(pasta):
            os.mkdir(pasta)

def organizar():
    for arquivo in os.listdir(PASTA_ORIGEM):
        caminho_arquivo = os.path.join(PASTA_ORIGEM, arquivo)
        
        if os.path.isfile(caminho_arquivo):
            _, extensao = os.path.splitext(arquivo)
            
            for pasta, extensoes in EXTENSOES.items():
                if extensao.lower() in extensoes:
                    shutil.move(caminho_arquivo, pasta)
                    break

if __name__ == "__main__":
    criar_pastas()
    organizar()
    print("arquivos organizados com êxito!!")
    