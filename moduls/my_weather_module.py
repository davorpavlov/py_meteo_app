import requests
from bs4 import BeautifulSoup



url = "https://meteo.hr/prognoze.php?section=prognoze_metp&param=zgdanas"
def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    forecast = soup.find("div", class_="fd-l-col--12 fd-l-md-col--8 fd-u-display--none fd-u-md-display--block").text
    return forecast
