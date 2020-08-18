from matplotlib import pyplot as plt
#from state.states import plot_state_borders

cidades = [([-122.3, 47.53], "Python"),([-96.85, 32.85], "Java"),([-89.33, 43.13], "R")]

plots = {"Java": ([], []), "Python": ([], []), "R": ([], [])}

markers = {"Java": "o", "Python": "s", "R": "^"}
colors = {"Java": "r", "Python": "b", "R": "g"}

for (longitude, latitude), linguagem in cidades:
    print(longitude, latitude)
    plots[linguagem][0].append(longitude)
    plots[linguagem][1].append(latitude)

for linguagem, (x, y) in plots.items():
    plt.scatter(x, y, color=colors[linguagem], marker=markers[linguagem], label=linguagem, zorder=10)
#plot_state_borders(plt)

plt.legend(loc=0)
plt.axis([-130, -60, 20, 55])

plt.title("Linguagens de Programação Preferidas")
plt.show()