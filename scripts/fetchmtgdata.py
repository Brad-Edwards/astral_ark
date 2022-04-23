#!/usr/local/bin/python3

# Fetches MtG card data from Scryfall, saves all data in one file, and
# Planechase card data in another.l

import json
import urllib.request

# Every Planechase card has a "type_line" of "Plane - <plane>"
TYPE_LINE_FRAGMENT = "Plane — "

url = "https://api.scryfall.com/bulk-data/oracle_cards"
response = urllib.request.urlopen(url)
url = json.load(response)["download_uri"]

f = urllib.request.urlopen(url)
data = json.load(f)

planechase_cards = [card for card in data if TYPE_LINE_FRAGMENT in card["type_line"]]

with open("../data/planechase-cards.json", "w", encoding="utf-8") as g:
    json.dump(planechase_cards, g, ensure_ascii=False, indent=4)

with open("../data/oracle-cards.json", "w", encoding="utf-8") as g:
    json.dump(data, g, ensure_ascii=False, indent=4)

f.close()
