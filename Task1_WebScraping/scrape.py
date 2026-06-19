import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

countries = []
capitals = []
populations = []

for country in soup.find_all("div", class_="country"):
    countries.append(country.find("h3", class_="country-name").text.strip())
    capitals.append(country.find("span", class_="country-capital").text.strip())
    populations.append(country.find("span", class_="country-population").text.strip())

df = pd.DataFrame({
    "Country": countries,
    "Capital": capitals,
    "Population": populations
})

print(df.head())

df.to_csv("countries.csv", index=False)

print("Dataset created successfully!")