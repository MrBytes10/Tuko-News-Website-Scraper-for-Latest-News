# Tuko News webscraper
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# Requesting the website data
URL="https://www.tuko.co.ke/"
response= requests.get(URL)
"""print("the response code is:", response)"""
# Parse the HTML Document
soup= BeautifulSoup(response.content, "html.parser")
"""print(soup)""" # This would print the whole html document for tuko news

# Extract the news articles headlines from the HTML Document
articles = soup.find_all('article')
# Lists to store data
data = []

# Extracting details from each article
for article in articles:
    headline_tag = article.find('a', class_='c-article-card-with-badges__headline')
    time_tag = article.find('time', class_='c-article-info__time--clock')
    
    if headline_tag and time_tag:
        headline = headline_tag.text.strip()
        time_posted = time_tag['datetime']
        link = headline_tag['href']
        
        data.append([time_posted, headline, link])
# Create a DataFrame
df = pd.DataFrame(data, columns=["time posted", "article headline", "article link"])

# Convert the time posted column to datetime and remove timezone info
df["time posted"] = pd.to_datetime(df["time posted"]).dt.tz_localize(None)

# Sort the DataFrame by the time posted in descending order
df = df.sort_values(by="time posted", ascending=False)

# Save the DataFrame to an Excel file
df.to_excel("tuko_news.xlsx", index=False)

print("Data has been saved to tuko_news.xlsx")



