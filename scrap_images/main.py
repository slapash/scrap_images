import bs4 as bs 
import requests
import shutil
import os

path = "/Users/omarbenaidy/Desktop/scrap_images/"#emplacement du dossier contenant les images

def get_soup(url):
    page = requests.get(url)
    soup = bs.BeautifulSoup(page.content, 'html.parser')
    return soup

liens = ["https://www.elecfreaks.com/learn-en/microbitKit/ringbit_bricks_pack/ringbit_bricks_pack_case_01.html",
"https://www.elecfreaks.com/learn-en/microbitKit/ringbit_bricks_pack/ringbit_bricks_pack_case_02.html",
"https://www.elecfreaks.com/learn-en/microbitKit/ringbit_bricks_pack/ringbit_bricks_pack_case_03.html",
"https://www.elecfreaks.com/learn-en/microbitKit/ringbit_bricks_pack/ringbit_bricks_pack_case_04.html",
"https://www.elecfreaks.com/learn-en/microbitKit/ringbit_bricks_pack/ringbit_bricks_pack_case_05.html",
"https://www.elecfreaks.com/learn-en/microbitKit/ringbit_bricks_pack/ringbit_bricks_pack_case_06.html",
"https://www.elecfreaks.com/learn-en/microbitKit/ringbit_bricks_pack/ringbit_bricks_pack_case_07.html"]

def get_images(liens):
    global path
    images = get_soup(liens).find_all('img')
    os.mkdir(path + "case" + str(liens[-6]))#donner un nom au nouveau(x) dossier(s)
    directory = path + "case" + str(liens[-6]) +"/"#le nom du dossier qui va être créé
    for elem in range(len(images)):
        base_url = "https://www.elecfreaks.com/learn-en/"#url de base exemple https://www.exemple.com/images/
        url_ext = images[elem].attrs['src'].replace(r"../../", "")#extension d'url exemple /img01.jpg
        full_url = base_url + url_ext #url complet exemple https://www.exemple.com/images/img01.jpg
        request_image = requests.get(full_url, stream = True)
        print(request_image.status_code)
        if request_image.status_code == 200:                     #200 status code = OK
            with open(directory + f"img{elem}.jpg", 'wb') as f: 
                request_image.raw.decode_content = True
                shutil.copyfileobj(request_image.raw, f)
            
for elements in liens:
    get_images(elements)