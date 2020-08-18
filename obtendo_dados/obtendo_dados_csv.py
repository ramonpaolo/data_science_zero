import re, csv
with open("obtendo_dados.txt", "r")as file:
    arquivo = file.read()

    if re.match("^opa", arquivo):
         print("Tem a palavra 'opa'")
        
    print("?")
    print(arquivo.replace("opa", "!"))

with open("obtendo_dados.csv", "rb") as f:
    arquivo = csv.DictReader(f)
    print(arquivo)