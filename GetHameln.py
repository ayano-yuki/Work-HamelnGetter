from bs4 import BeautifulSoup
import requests
import csv
import re
import os


with open("Heaven'sMemoPad.csv", 'r') as LINK:
    csv.reader(LINK)
    for main_url in csv.reader(LINK):
        if (len(main_url) == 0):
            print("Finish Prog")
            exit()

        main_url = main_url[0]
        response = requests.get( main_url )
        soup = BeautifulSoup(response.text, 'html.parser')
        main_title = soup.find('title').get_text()
        os.mkdir( main_title )
        print( main_title )

        FileName = main_title + "//" + "000__index.txt"
        f_index = open(FileName, 'a', encoding='UTF-8')
        f_index.write(main_title + "\n\n")


        storyNumber = 1
        related = soup.find(id="maind")
        for elements in related.find_all(class_="ss"):
            for element in elements.find_all("a"):
                page_url = element.get("href")
                if ( re.search("^./[0-9]+.html",page_url) != None ):
                    url = main_url + page_url[2:]
                    page_response = requests.get( url )
                    page_soup = BeautifulSoup(page_response.text, 'html.parser')
                    page_title = page_soup.find('title').get_text()
                    page_related = page_soup.find(id="honbun")

                    FileName = main_title + "//" + str(  str(storyNumber).zfill(3) ) + "__" + page_title +".txt"
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
                    storyNumber = storyNumber + 1