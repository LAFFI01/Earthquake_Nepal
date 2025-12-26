import pandas as pd
from bs4 import BeautifulSoup
import requests
from Config.setting import settings

#Scrapy
all_data = []
page = 1

while page <= 64:
    url = settings.BASE_URL + f"?page={page}"
    response = requests.get(url)
    if response.status_code != 200:
        break
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    if not table:
        break
    rows = table.find_all("tr")
    if len(rows) <= 1:
        break  # only header left → stop
    
    for row in rows[1:]:
        cols = row.find_all("td")
        if len(cols) > 0:
            date = cols[1].get_text(strip=True)
            time  = cols[2].get_text(strip=True)
            latitude = cols[3].get_text(strip=True)
            longitude = cols[4].get_text(strip=True)
            magnitude = cols[5].get_text(strip=True)
            epicenter = cols[6].get_text(strip=True)
            all_data.append([date,time,latitude,longitude,magnitude,epicenter])
    
    print(f"Scraped page {page}")
    page += 1  # move to next page

# Convert to DataFrame
df = pd.DataFrame(all_data, columns=['date','time','latitude','longitude','magnitude','epicenter'])



df.to_csv("earthquakes_nepal_Scraped.csv", index=False, encoding="utf-8")
print("Complete")