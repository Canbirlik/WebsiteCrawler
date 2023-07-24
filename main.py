import requests
from bs4 import BeautifulSoup

# html parsing

target_url = "https://www.canbirlik.com"
foundLinks = []

def make_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def crawler(url):
    links = make_request(url)
    for link in links.find_all("a"):
       found_link = link.get("href")
       if found_link[0] == "#" or found_link[0:4] == "tel:":
           continue
       if found_link[-5:] == ".html" or found_link[0] == "/":
           found_link = target_url + "/" + found_link
       if target_url in found_link and found_link not in foundLinks:
            foundLinks.append(found_link)
            print(found_link)
            # Recursive:
            crawler(found_link)

crawler(target_url)


