import downloader

if __name__ == '__main__':
    print("https://submanga.io/")
    link = input("Ingresa el link del capitulo: ")
    downloader.download(link)
    print("Descarga completa")
