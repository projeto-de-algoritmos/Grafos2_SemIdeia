from desenho import desenhar_grafo
from grafos import Grafo


grafo = Grafo()

grafo.adicionar_predio("S1", (1,1))
grafo.adicionar_predio("S2", (2,1))
grafo.adicionar_predio("S3", (3,1))
grafo.adicionar_predio("S4", (4,1))
grafo.adicionar_predio("S5", (5,1))
grafo.adicionar_predio("S6", (6,1))
grafo.adicionar_predio("S7", (7,1))
grafo.adicionar_predio("S8", (8,1))
grafo.adicionar_predio("S9", (9,1))
grafo.adicionar_predio("S10", (10,1))

grafo.adicionar_predio("I1", (1,2))
grafo.adicionar_predio("I2", (2,2))
grafo.adicionar_predio("I3", (3,2))
grafo.adicionar_predio("I4", (4,2))
grafo.adicionar_predio("I5", (5,2))
grafo.adicionar_predio("I6", (6,2))
grafo.adicionar_predio("I7", (7,2))
grafo.adicionar_predio("I8", (8,2))
grafo.adicionar_predio("I9", (9,2))
grafo.adicionar_predio("I10", (10,2))

grafo.adicionar_predio("Mocap", (1,4))
grafo.adicionar_predio("Lab SS", (2,4))
grafo.adicionar_predio("Lab NEI", (3,4))
grafo.adicionar_predio("Lab Fisica", (4,4))
grafo.adicionar_predio("Lab Quimica", (5,4))

grafo.adicionar_predio("Direção", (1,5))
grafo.adicionar_predio("Salas dos professores", (2,5))

grafo.adicionar_conexao("S1", "S2", 1)
grafo.adicionar_conexao("S2", "S3", 1)
grafo.adicionar_conexao("S3", "S4", 1)
grafo.adicionar_conexao("S4", "S5", 1)
grafo.adicionar_conexao("S5", "S6", 1)
grafo.adicionar_conexao("S6", "S7", 1)
grafo.adicionar_conexao("S7", "S8", 1)
grafo.adicionar_conexao("S8", "S9", 1)
grafo.adicionar_conexao("S9", "S10", 1)

grafo.adicionar_conexao("I1", "I2", 1)
grafo.adicionar_conexao("I2", "I3", 1)
grafo.adicionar_conexao("I3", "I4", 1)
grafo.adicionar_conexao("I4", "I5", 1)
grafo.adicionar_conexao("I5", "I6", 1)
grafo.adicionar_conexao("I6", "I7", 1)
grafo.adicionar_conexao("I7", "I8", 1)
grafo.adicionar_conexao("I8", "I9", 1)
grafo.adicionar_conexao("I9", "I10", 1)

grafo.adicionar_conexao("I1", "S1", 5)
grafo.adicionar_conexao("I10", "S10", 5)

grafo.adicionar_conexao("I1", "Mocap",10)
grafo.adicionar_conexao("I1", "Lab SS",10)
grafo.adicionar_conexao("I1", "Lab NEI",10)
grafo.adicionar_conexao("I1", "Lab Fisica",10)
grafo.adicionar_conexao("I1", "Lab Quimica",10)


grafo.adicionar_conexao("Lab SS", "Mocap",1)
grafo.adicionar_conexao("Lab NEI", "Lab SS",1)
grafo.adicionar_conexao("Lab Fisica", "Lab NEI",1)

grafo.adicionar_conexao("Direção", "Lab Fisica",5)
grafo.adicionar_conexao("Direção", "Lab Quimica",5)
grafo.adicionar_conexao("Direção", "Mocap",5)
grafo.adicionar_conexao("Direção", "Lab SS",5)
grafo.adicionar_conexao("Direção", "Lab NEI",5)

grafo.adicionar_conexao("Direção", "Salas dos professores",1)









desenhar_grafo(grafo)