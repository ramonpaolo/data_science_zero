from matplotlib import pyplot as plt

filmes = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# Barras possuem o tamanho padrão de 0.8, então adicionaremos 0.1 ás
# Cordenadas á esquerda para que cada barra seja centralizada
xs = [i + 0.1 for i, _ in enumerate(filmes)] #Não precisa

#As barras do gráfico com as coordenadas x á esquerda [xs], alturas [num_oscars]
plt.bar(filmes, num_oscars)

plt.ylabel("# de Premiações")
plt.title("Meus Filmes Favoritos")

#Nomeia o eixo x com nomes de filmes na barra central
plt.xticks(xs, filmes) #Não precisa

plt.show()