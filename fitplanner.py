import os
os.system('cls' if os.name == 'nt' else 'clear')

## agente
# from agente import falar_com_agente
##

from funcoes import *

# criar arquivos importantes! // exercícios - - -
inicializarArquivos()

pathTreino = "files/treinos"
arquivoTreino = "treinos.csv"
pathExercicios = "files/exercicios"

while True:
    opcao = menu()

    # - - - - > TREINOS
    if opcao == 1:
        while True:
            opcaoTreino = menuTreino()

            if opcaoTreino == 1: # add
                dicionarioTreino = {}

                print("- Adicionar novo treino -")
                try:
                    # print("Aperte Enter para pular")
                    dicionarioTreino = {
                    'nome':       input("- Nome: ").capitalize(),
                    'tipo':       input("- Tipo [categoria]: ").capitalize(),
                    'duracao':    float(input("- Duração (em minutos): ")),
                    'objetivo':   input("- Objetivo: ").capitalize(),
                    'observacao': input("- Observações: ").capitalize(),
                    'exercicios': ""
                    }
                    print()
                except ValueError:
                    print("Entrada inválida. Tente novamente.")
                    print()
                    continue

                dicionarioTreino["exercicios"] = vincularExercicioTreino(pathExercicios)  
                salvarTreino(pathTreino, arquivoTreino, dicionarioTreino)

            elif opcaoTreino == 2: # mostrar
                while True:
                    # os.system('cls' if os.name == 'nt' else 'clear')
                    print("- Ver treinos -")
                    
                    treinos = listarTreinos(pathTreino,arquivoTreino)
                    if treinos == False: # não existe
                        break
                    treino = mostrarTreino(pathTreino, arquivoTreino, opcao)
                    if treino == "break":
                        print()
                        break
                    # continuar = input("Aperte enter para continuar...")

            elif opcaoTreino == 3: # editar
                while True: 
                    print("- Editar treinos - ")

                    treinos = listarTreinos(pathTreino,arquivoTreino)
                    if treinos == False:
                        break
                    edicao = editarTreino(pathTreino, arquivoTreino)
                    if edicao == 0:
                        break
                    
            elif opcaoTreino == 4: # excluir
                while True:
                    print("- Excluir arquivo -")
                
                    treinos = listarTreinos(pathTreino,arquivoTreino)
                    if treinos == False: # não existe
                        break

                    deletar = excluirTreino(pathTreino, arquivoTreino)
                    if deletar == 0:
                        break

            elif opcaoTreino == 0: # sair
                break

    # - - - - > EXERCÍCIOS
    elif opcao == 2: # exercício
        while True:
            opcaoExercicio = menuExercicio() # MENU

            if opcaoExercicio == 1: # adicionar exercícios
                while True:
                    print("- Adicionar exercício novo -")
                    categoria = categoriaExercicio()

                    if categoria == 0:
                        print()
                        break
                    elif categoria == "invalido":
                        print("Tente novamente ou aperte '0 - Voltar'")
                        continue # pula o print, reinicia o loop

                    exercicios = abrirExercicios(pathExercicios, categoria)
                    addExercicio(pathExercicios, categoria, exercicios)

            elif opcaoExercicio == 2: # listar exercícios
                while True:
                    print("- Ver exercícios -")
                    categoria = categoriaExercicio() # retorna o nome do arquivo: "categoria.txt" 

                    if categoria == 0:
                        break
                    elif categoria == "invalido":
                        continue # pula o print, reinicia o loop

                    exercicios = abrirExercicios(pathExercicios, categoria)
                    listarExercicios(exercicios, categoria)

            elif opcaoExercicio == 3: # editar exercícios
                while True:
                    print("- Editar exercícios -")
                    print("- Selecione a categoria do exercício que deseja editar -")
                    categoria = categoriaExercicio() # retorna o arquivo: "categoria.txt" 

                    if categoria == 0:
                        break
                    elif categoria == "invalido":
                        print("Tente novamente ou aperte '0 - Voltar'")
                        continue # pula o print, reinicia o loop

                    exercicios = abrirExercicios(pathExercicios, categoria)
                    editarExercicio(pathExercicios, categoria, exercicios)
                    print()
                    
            elif opcaoExercicio == 4: # excluir exercícios
                print("- Excluir exercícios -")

                while True:
                    categoria = categoriaExercicio() # retorna o arquivo: "categoria.txt" 

                    if categoria == 0:
                        break
                    elif categoria == "invalido":
                        print("Tente novamente ou aperte '0 - Voltar'")
                        continue # pula o print, reinicia o loop

                    exercicios = abrirExercicios(pathExercicios, categoria)
                    temExercicio = listarExercicios(exercicios, categoria)
                    if temExercicio == True:
                        excluirExercicio(pathExercicios, categoria, exercicios)

            elif opcaoExercicio == 0: # sair
                break
    
    ######
    # - - - - > METAS
    elif opcao == 3:
        while True:
            print("----Controle de metas----")
            print("1 - Ver metas")
            print("2 - Adicionar meta")
            print("3 - Editar meta")
            print("4 - Excluir meta")
            print("0 - Voltar")
            print()

            opcaoMeta = int(input("> > Opção: "))
            print()

            if opcaoMeta == 1:
                visualizarMetas()
            elif opcaoMeta == 2:
                adicionarMeta()
            elif opcaoMeta == 3:
                editarMeta()
            elif opcaoMeta == 4:
                excluirMeta()
            elif opcaoMeta == 0:
                break

# --> EVOLUÇÃO
    elif opcao == 4:
        menuEvolucao()

# -- > SUGESTÕES
    elif opcao == 5:
        menuSugestoes()

# -- > IMC
    elif opcao == 6:
        calcularIMC()

# -- > RESET
    elif opcao == 7:
        resetarDados()