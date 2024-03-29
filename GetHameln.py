from bs4 import BeautifulSoup
import requests
import csv
import re
import os

def get_hameln(novel):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    cookies = {'over18': 'off'}
    base_dir = 'contents'

    if (len(novel) == 0):
        print("Finish Prog")
        exit()

    url = novel[0]
    main_title = novel[3]

    dir = os.path.join(base_dir, main_title)
    if not os.path.isdir(dir):
        os.makedirs( dir )

        FileName =  os.path.join( base_dir, main_title, '000__index.txt')
        f_index = open(FileName, 'a', encoding='UTF-8')
        f_index.write(main_title + "\n\n")
        f_index.close()
        
    response = requests.get( url , headers=headers, cookies=cookies)
    
    if response.status_code != requests.codes.ok:
        print('通信に失敗しました。')
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    match = re.search(r'https://syosetu.org/novel/\d+/(\d+).html', url)
    storyNumber = match.group(1) if match else 0

    page_title = soup.find('title').get_text()
    page_related = soup.find(id="honbun")

    FileName = os.path.join( base_dir, main_title, str(storyNumber).zfill(3) + "__" + page_title +".txt")
    f = open(FileName, 'a', encoding='UTF-8')

    for page_element in page_related.find_all("p"):
        string = str( page_element )
        string = string.replace("</p>", "")
        string = string.replace("\"", "", 2)
        string = string.replace("<p id=", "")
        string = string.replace(">", "")
        string = string.split()
        string = str( string[1:] )
        string = string.replace("'", "", 10)
        string = string.replace("[", "")
        string = string.replace("]", "")
        f.write(string + "\n")
    f.close()
    print(f'{page_title} downloaded')

if __name__ == '__main__':
    with open("Rasiel.csv", 'r', encoding='UTF-8') as LINK:
        novels = csv.reader(LINK)
        for novel in novels:
            get_hameln(novel)