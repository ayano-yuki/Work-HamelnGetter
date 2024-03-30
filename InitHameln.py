from bs4 import BeautifulSoup
import requests
import csv, os
from main import main

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
cookies = {'over18': 'off'}
base_url = 'https://syosetu.org/novel/'

def InitHameln():
    records = []
    seen = set()

    # 既に取得済みの小説IDを読み込み
    if os.path.exists("Heaven'sMemoPad.csv"):
        with open("Heaven'sMemoPad.csv", 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            for record in reader:
                seen.add(record[1])

    while True:
        # 取得する小説のIDを入力
        id = input("Enter Novel ID (or q): ")
        if id == 'q':
            break
        if not id.isdigit():
            print("Please enter a valid ID")
            continue
        
        # IDから基本情報を取得
        url = 'https://syosetu.org/novel/' + id
        response = requests.get( url, headers=headers, cookies=cookies )
        if response.status_code != requests.codes.ok:
            print('通信に失敗しました。')
            continue
        soup = BeautifulSoup(response.text, 'html.parser')
        main_title = soup.find('title').get_text()
        print(main_title)

        # 重複しないようにフィルター
        if id not in seen:
            seen.add(id)
            records.append([main_title, id, '0'])

    # 新規小説情報をCSVに書き込み
    with open("Heaven'sMemoPad.csv", 'a', encoding="utf-8" ) as f:
        writer = csv.writer(f)
        writer.writerows(records)
        
if __name__ == '__main__':
    # 小説IDを入力してCSVに追加
    InitHameln()
    
    # 追加した小説をダウンロード
    main()