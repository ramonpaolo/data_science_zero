from bs4 import BeautifulSoup
import requests

html = requests.get("https://zepikeno16.github.io").text
soup = BeautifulSoup(html, features="html.parser")

#todos_img = soup.find_all("img")

primeiro_h1 = soup.find("h1")
print(primeiro_h1)
print(primeiro_h1.text.startswith("Data"))

#extrair atributos
primeiro_h1 = soup.h1["class"]
print(primeiro_h1)
primeiro_h1 = soup.h1.get("class")
print(primeiro_h1)

all_figcaption = soup.find_all("figcaption")
#all_figcaption = soup("h1") equivale ao find_all
print(all_figcaption)

#Procura com a class especifica
h1_class_especific = soup.find_all("h1", {"class": "text-center"})
print(h1_class_especific)

url = "http://amazon.com.br/gp"