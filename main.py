"""
	Pregunta 1
	Dada la lista de notas [15,20,18] y la lista de alumnos ["Marcelo", "José", "Juan"] Imprimirlos de la siguiente forma:

	Marcelo : 15

	José : 20

	Juan : 18
"""

scores = [15, 20, 18]
students = ["Marcelo", "José", "Juan"]


def zipStudents(scores, students): return zip(students, scores)


def questionOne():
    for name, score in zipStudents(scores, students):
        print(f"{name}: {score}")


"""
Pregunta 2
Dada la siguiente lista ['Hola', True, 5, 6.04]

Imprimir los valores e índices sin utilizar un contador o range.

0 -> Hola
1 -> True
2 -> 5
3 -> 6.04
"""


def questionTwo():
    mylist = ['Hola', True, 5, 6.04]
    for cont, value in enumerate(mylist):
        print(f"{cont} -> {value}")


"""
Pregunta 3
Dada la lista de notas [15,20,18] y la lista de alumnos ["Marcelo", "José", "Juan"], imprimirlos de la siguiente forma:

1 -> Jose : 20

2 -> Juan : 18

3 -> Marcelo : 15
No usar range, ni comparadores. Hint: usar sorted
"""


def questionThree():
    listsorted = sorted(list(zipStudents(scores, students)))
    for cont, (name, value) in enumerate(listsorted):
        print(f"{cont} -> {name}: {value}")


"""
Pregunta 4
Escriba un generador que permita contar las letras de las palabras de una lista.

Ejemplos:

Para "humanidad": {'h': 1, 'u': 1, 'm': 1, 'a': 2, 'n': 1, 'i': 1, 'd': 2}

Para "humano": {'h': 1, 'u': 1, 'm': 1, 'a': 1, 'n': 1, 'o': 1}
"""


def generator(word):
    for w in word:
        yield w, word.count(w)


def questionFour():
    word = "humanidad"
    print(dict(generator(word)))


"""
Pregunta 5
Teniéndos los siguientes criterios:

Desaprobado: nota < 11
Destacado: nota > 16
Aprobado: para el resto de casos
notas = [15, 20 18, 11, 4, 7, 14, 13 ,1 ,9, 10]
alumnos = ["Marcelo", "Jose", "Juan", "Marco", "María",
    "Ricardo", "Liz", "Diego", "Roberto", "Martin", "Álvaro"]
alumnos_notas = zip(alumnos, notas)

def registrar_aprobados(l):
    pass
Implementar registrar_aprobados como generador y que su único parametro de entrada sea alumnos_notas Posteriormente utilizar un bucle y enumerate para obtener la siguiente salida.

1 -> Marcelo : 15 (Aprobado)
2 -> Jose : 20 (Destacado)
3 -> Juan : 18 (Destacado)
4 -> Marco : 11 (Aprobado)
5 -> María : 4 (Desaprobado)
6 -> Ricardo : 7 (Desaprobado)
7 -> Liz : 14 (Aprobado)
8 -> Diego : 13 (Aprobado)
9 -> Roberto : 1 (Desaprobado)
10 -> Martin : 9 (Desaprobado)
11 -> Álvaro : 10 (Desaprobado)
"""

def register(scoresOfStudens):

    for name, score in scoresOfStudens:
        _h = "a" if score > 16 else "b" if score >= 11 else "c"
        yield name, score, {"a": "Destacado", "b": "Aprobado", "c": "Desaprobado"}[_h]


scores2 = [15, 20, 18, 11, 4, 7, 14, 13, 1, 9, 10]
students2 = ["Marcelo", "Jose", "Juan", "Marco", "María", "Ricardo", "Liz", "Diego", "Roberto", "Martin", "Álvaro"]

def questionFive():
    for cont, (name, score, helper) in enumerate(register(zip(students2, scores2))):
        print(f"{cont} -> {name}: {score} ({helper})")


def run():
    questionOne()
    questionTwo()
    questionThree()
    questionFour()
    questionFive()


if __name__ == "__main__":
    run()
