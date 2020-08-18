height_weight_age = [
                70,
                170,
                40
]

grades = [95,
          80,
          75,
          62]

lista = []


def vetor_add(v, w):
    lista = [v_i + w_i for v_i, w_i in zip(v, w)]

vetor_add(2, 5)
print(lista)