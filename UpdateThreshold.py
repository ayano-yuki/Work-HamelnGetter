import feedparser
import numpy as np
import csv

count = 1
with open( "Heaven'sMemoPad.csv", 'r', encoding="utf-8" ) as f:
    reader = csv.reader(f)
    for row in reader:

        RSS_URL = "https://rss.syosetu.org/?nid=" + row[1]
        d = feedparser.parse(RSS_URL)
        threshold = int(row[2])
        dict = {}
        Box =[]
        
        for entry in d.entries:
            date = entry.updated.split("T")[0].replace('-', '')
            time = entry.updated.split("T")[1].replace(':', '').split("+")[0]
            update = int(date + time)

            if(update < threshold-1):
                break

            dict[update] = [entry.title, entry.link]
            Box.append(update)

        try:
            print(np.max(Box))
        except ValueError:
            print("     更新あるいは、小説がありません")