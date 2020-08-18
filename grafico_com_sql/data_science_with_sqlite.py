from matplotlib import pyplot as plt
import sqlite3 as sql
import time

conexao = sql.connect("./database/analise.db")
add = conexao.cursor()


def create_table():
    """Docstring hehe"""
    add.execute("""
        CREATE TABLE usuarios(
        nome varchar(50) not null,
        idade int(2) not null,
        renda float not null
        );
    """)
    conexao.commit()


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda: "))


def insert_db():
    add.execute("""
    
    INSERT INTO usuarios(
    nome, idade, renda
    ) VALUES(?, ?, ?);
    
    """, (nome, idade, renda))
    print(nome)

    conexao.commit()


rendas = []
idades = []


def selecionar_todos():

    add.execute("""
    SELECT * FROM usuarios;
    """)
    for linha in add.fetchall():
        print(linha)
        idades.append(linha[1])
        rendas.append(linha[2])


def criar_plot():
    plt.title("Idade dos Usuários e seus salários")
    plt.ylabel("Idade")
    # X(horizonte), Y(vertical)
    plt.plot(rendas, idades, marker="o", color="green")
    plt.show()


#def criar_grafico_de_barra():
#    plt.title("Idade dos usuários")
#   plt.ylabel("Idade")
#    plt.bar(rendas, idades)
#    plt.show()


#create_table()
#time.sleep(1)


insert_db()
time.sleep(1)

selecionar_todos()
time.sleep(1)

#criar_grafico_de_barra()
criar_plot()
time.sleep(1)

conexao.close()