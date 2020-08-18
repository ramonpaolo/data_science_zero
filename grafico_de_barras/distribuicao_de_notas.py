from matplotlib import pyplot as plt

#notas_dos_alunos = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
#qtd_alunos = [x for x in range(0, 13)]
#print(qtd_alunos)
notas = [87, 92, 95, 100, 56]
qtd_aluno = range(0, 5)

plt.title("Distribuição de notas")
plt.ylabel("# de Alunos")
plt.bar(qtd_aluno, notas, color="green")
plt.xticks(qtd_aluno)
#plt.bar(qtd_alunos, notas_dos_alunos, 0.8)
#plt.axis([-5, 105, 0, 5])
plt.show()