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

        print( '{} : {} {}'.format(str(count).zfill(3), row[2], row[0]) )
        
        for entry in d.entries:
            date = entry.updated.split("T")[0].replace('-', '')
            time = entry.updated.split("T")[1].replace(':', '').split("+")[0]
            update = int(date + time)

            if(update <= threshold):
                break

            print("     ", entry.link, update, entry.title)
        count = count + 1

'''
            dict[update] = [entry.title, entry.link]
            Box.append(update)

        try:
            print("     ", dict[np.max(Box)][0], dict[np.max(Box)][1], np.max(Box))
        except ValueError:
            pass
'''