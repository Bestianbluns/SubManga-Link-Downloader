import requests, os
from bs4 import BeautifulSoup


def find_images_submanga(data:str):
    splited = data.split(" ")
    links = []
    for word in splited:
        if word.startswith("https://submanga.io/uploads/manga/"):
            links.append(word)
    return links

def find_name(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    data = soup.title.text.strip()
    name_split = []
    for word in data.split(" "):
        if word == "Capitulo":
            break
        name_split.append(word)
    return " ".join(name_split)

def find_chapter(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    data = soup.title.text.strip()
    name_split = []
    flag = False
    for word in data.split(" "):
        if word == "Manga":
            break
        if flag:
            name_split.append(word)
        if word == "Capitulo":
            flag = True
    return " ".join(name_split)

def get_page(link):
    end = link.split("/")[-1]
    return end.split(".")[0]

def get_extension(link):
    return link.split(".")[-1]


def download(link_fixed):
    page = requests.get(link_fixed)
    soup = BeautifulSoup(page.text, 'html.parser')
    images = soup.find_all("img", class_="img-responsive")
    save_data = str(images[0])
    links = find_images_submanga(save_data)
    print(links[0])

    name = find_name(link_fixed)
    chapter = find_chapter(link_fixed)


    for link in links:
        page = get_page(link)
        extension = get_extension(link)
        os.makedirs('Downloads/' + name + "/" + chapter + "/", exist_ok=True)
        full_path = 'Downloads/' + name + "/" + chapter + "/" + page + '.' + extension

        print(f"Downloading {name} {chapter} {page}")

        response = requests.get(link)
        file = open(full_path, "wb")
        file.write(response.content)
        file.close()

