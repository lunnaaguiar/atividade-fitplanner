import os

# inicializar arquivos

# variáveis de treino
pathTreinos = "files/treinos"
pathExercicios = "files/exercicios"
arquivoTreinos = "treinos.csv"

def inicializarArquivos():
    os.makedirs(pathTreinos, exist_ok=True)
    os.makedirs(pathExercicios, exist_ok=True)
    for nome in ["cardio.txt", "forca.txt", "flexibilidade.txt", "equilibrio.txt"]:
        caminho = f"{pathExercicios}/{nome}"
        if not os.path.exists(caminho):
            open(caminho, "w", encoding='utf-8').close()

####
 
def menu():
    try:
        print("1 - Treinos")
        print("2 - Exercícios")
        print("3 - Metas")
        print("4 - Evolução")
        print("5 - Sugestões")
        print("0 - Sair")
        print()
        opcao = int(input("Insira a opção desejada: "))
        return opcao
    except ValueError:
        print("Opção inválida.")
        print()


def menuTreino():
    try:
        print("- - - - TREINOS - - - -")
        print("1 - Novo treino")
        print("2 - Ver treinos")
        print("3 - Editar treino")
        print("4 - Excluir treino")
        print("0 - Voltar")
        print()
        opcao = int(input("> > Opção: "))
        print()
        return opcao
    except ValueError:
        print("Opção inválida.")
        print()

def menuExercicio():
    try:
        print("- - - - EXERCÍCIOS - - - -")
        print("1 - Adicionar exercício novo")
        print("2 - Ver exercícios")
        print("3 - Editar")
        print("4 - Excluir exercício")
        print("0 - Voltar")
        print()
        opcao = int(input("> > Opção: "))
        print()
        return opcao
    except ValueError:
        print("Opção inválida.")
        print()

def categoriaExercicio():
    try:
        print("- - - Categorias - - -")
        print("1 - Aeróbicos (cardio)")
        print("2 - Força (resistência)")
        print("3 - Flexibilidade/alongamento")
        print("4 - Equilíbrio")
        print("0 - Voltar")
        print()
        categoria = int(input("Selecione uma categoria: "))
        # return categoria
        if categoria == 1:
            return "cardio.txt"
        elif categoria == 2:
            return "forca.txt"
        elif categoria == 3:
            return "flexibilidade.txt"
        elif categoria == 4:
            return "equilibrio.txt"
        elif categoria == 0:
            return 0
        else:
            print("\n- Opção inválida -")
            return "invalido" # trocar por inválida
    except ValueError:
        print("Opção inválida.")
        print()

### Exercícios ###

def atualizarExercicios(path, categoria, listaExercicios):
    arquivo = open(f"{path}/{categoria}", "w", encoding='utf-8') # removi .txt

    for i in range(len(listaExercicios)):
        arquivo.write(f"{listaExercicios[i].strip()}\n") # precisa do .strip() pra apagar  aquebra de linha '\n' e adicionar de novo
    arquivo.close()

def addExercicio(path, categoria, exercicios, exercicio):
    if exercicio == '0':
        return None
    
    exercicios.append(exercicio)
    arquivo = open(f"{path}/{categoria}", "w", encoding='utf-8') # removi .txt
    for i in range(len(exercicios)):
        arquivo.write(f"{exercicios[i].strip()}\n") # precisa do .strip() pra apagar  aquebra de linha '\n' e adicionar de novo
    arquivo.close()
    print()
    print(f"[{exercicio}] foi adicionado!")

def abrirExercicios(path, categoria):
    arquivo = open(f"{path}/{categoria}", "r", encoding='utf-8') # removi .txt
    exercicios = arquivo.readlines()
    arquivo.close()

    return exercicios

def listarExercicios(exercicios, categoria):
    # título
    if categoria == "cardio.txt":
        print(" > Aeróbicos <")
    elif categoria == "forca.txt":
        print(" > Força <")
    elif categoria == "flexibilidade.txt":
        print(" > Flexibilidade <")
    elif categoria == "equilibrio.txt":
        print(" > Equilíbrio <")
    
    # lisa dos exercícios
    if len(exercicios) > 0:
        for i in range(len(exercicios)):
            print(f"{i+1} | {exercicios[i].strip()}") # print de cada linha do arquivo
        return True
    else: 
        print("Sem exercícios cadastrados")
        return False

# def addListaExercicio(categoria, listaExercicios):
#     exercicios = abrirExercicios("files/exercicios", categoria)
#     numeroExercicio = int(input("Qual exercício deseja adicionar?"))
#     indiceExercicio = numeroExercicio-1
#     listaExercicios.append(exercicios[indiceExercicio])
#     print(f"'{exercicios[indiceExercicio]}' foi adicionado ao treino!")
#     for i in range(len(listaExercicios)):
#         listaExercicios[i] = listaExercicios[i].strip()
#     exerciciosTreino = "-".join(listaExercicios)
#     # dicionarioTreino["exercicios"] = exerciciosTreino
#     return exerciciosTreino

#Seção controle de metas

def viewGoals():
    with open("files/goals.txt", "r", encoding='utf-8') as file:
        fileList = file.readlines()

        if fileList == []:
            print("Nenhuma meta cadastrada")
            return

        for i in range(len(fileList)):
            print(f"{i+1} | {fileList[i].strip()}")


def addGoal():
    goal = input("Qual a meta?")
    with open("files/goals.txt", "a", encoding='utf-8') as file:
        file.write(f"{goal}\n")

def editGoal():
    with open("files/goals.txt", "r", encoding='utf-8') as file:
        fileList = file.readlines()

        if fileList == []:
            print("Nenhuma meta cadastrada")
            return

        for i in range(len(fileList)):
            print(f"{i+1} | {fileList[i].strip()}")

        opcao = int(input("Qual meta deseja editar? "))
        goal = input("Qual a nova meta?")
        fileList[opcao-1] = goal

        with open("files/goals.txt", "w", encoding='utf-8') as file:
            for i in range(len(fileList)):
                file.write(f"{fileList[i].strip()}\n")

    print("Meta editada com sucesso!")

def removeGoal():
    with open("files/goals.txt", "r", encoding='utf-8') as file:
        fileList = file.readlines()

        if fileList == []:
            print("Nenhuma meta cadastrada")
            return

        for i in range(len(fileList)):
            print(f"{i+1} | {fileList[i].strip()}")

        opcao = int(input("Qual meta deseja excluir? "))
        fileList.pop(opcao-1)

        with open("files/goals.txt", "w", encoding='utf-8') as file:
            for i in range(len(fileList)):
                file.write(f"{fileList[i].strip()}\n")

    print("Meta excluida com sucesso!")
