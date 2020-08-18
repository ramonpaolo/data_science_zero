import matplotlib.pyplot as plt

idades = [16, 17, 23, 18, 19]
tp_sexos = ["M", "F", "F", "F", "M"]
nomes = ["Ramon", "Maria", "Eduarda", "Braatz", "Dudu"]

plt.title("A")
plt.scatter(tp_sexos, idades, edgecolors="green", marker="o")
for nome, idade, tp_sexo in zip(nomes, idades, tp_sexos):
    plt.annotate(nome, xy=(tp_sexo, idade))
#plt.annotate(nome, xy=idades)
plt.show()