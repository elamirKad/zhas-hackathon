import sqlite3, csv

conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()


with open('cosmetics_cleaned.csv','r') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['Label'], i['Brand'], i['Name'], i['Price'], i['Rank'], i['Ingredients'], i['Combination'], i['Dry'], i['Normal'], i['Oily'], i['Sensitive']) for i in dr]

c.executemany("INSERT OR REPLACE INTO recommend_cosmetics (id, label, brand, name, price, rank, ingridients, combination, dry, normal, oily, sensitive) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", to_db)
conn.commit()
conn.close()