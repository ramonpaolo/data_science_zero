from matplotlib import pyplot as plt

idades = [20, 33, 17, 22]
rendas = [480.0, 1490.0, 0.0]

plt.title("A")
plt.plot(idades, rendas, color="red", marker="o", label="variavel")
plt.xticks(idades)
#plt.plot(rendas, idades, 'b:', label="Não variaveis")
#plt.xticks(rendas)
plt.ylabel("Renda das Pessoas")
plt.xlabel("Idade das Pessoas")
plt.legend(loc=9)
plt.show()