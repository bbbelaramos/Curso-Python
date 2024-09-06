import random
alunos = ["ana","lucas","luis","josé"]

random.shuffle(alunos)

for i in range (0,len(alunos)):
    print(alunos[i],end = ",")