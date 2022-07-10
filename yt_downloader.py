from pytube import YouTube

link = input("Digite a URL do vídeo que deseja baixar: ")
path = input("Digite o caminho onde deseja salvar o vídeo: ")

yt = YouTube(link)

result = {
    "Título": yt.title,
    "Número de views": yt.views,
    "Tamanho do vídeo": yt.length,
    "Avaliação do vídeo": yt.rating
}

print(result)

ys = yt.streams.get_highest_resolution()

print("Baixando...")

ys.download(path)
print("Download concluído com sucesso!")

