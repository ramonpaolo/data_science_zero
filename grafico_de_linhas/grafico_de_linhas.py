from matplotlib import pyplot as plt
anos = [2010, 2011, 2012, 2013]
dinheiro = [96889.0, 127098.1, 130001.7, 119986.2]

# cria um gráfico de linha, anos no eixo x, gdp no eixo y

plt.plot(anos, dinheiro, color="green", marker="o")
# adiciona um título
plt.title("GDP Nominal")
# adiciona um selo no eixo y
plt.ylabel("Bilhões de $")
plt.show()