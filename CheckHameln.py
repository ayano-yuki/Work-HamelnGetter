import feedparser
import csv

def check_hameln():
    novels = []
    updated = []
    with open( "Heaven'sMemoPad.csv", 'r', encoding="utf-8" ) as f:
        reader = csv.reader(f)
        count = 1
        for row in reader:

            RSS_URL = "https://rss.syosetu.org/?nid=" + row[1]
            d = feedparser.parse(RSS_URL)
            threshold = int(row[2])

            print( '{} : {} {}'.format(str(count).zfill(3), row[2], row[0]) )
            
            last_updated = 0
            for entry in d.entries:
                date = entry.updated.split("T")[0].replace('-', '')
                time = entry.updated.split("T")[1].replace(':', '').split("+")[0]
                update = int(date + time)

                if last_updated < update:
                    last_updated = update
                if update <= threshold:
                    continue

                print("     ", entry.link, update, entry.title, row[0])
                novels.append([entry.link, update, entry.title, row[0]])
            updated.append([row[0], row[1], last_updated])
            count += 1

    # 更新情報をCSVに書き込み
    with open("Heaven'sMemoPad.csv", 'w', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(updated)
    
    return novels
        
if __name__ == '__main__':
    novels = check_hameln()
    
    # ダウンロードキューをCSVに書き込み
    with open('Rasiel.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(novels)