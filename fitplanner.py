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
            opcaoMeta = menuMeta()

            if opcaoMeta == 1: # add
                dicionarioMeta = {}

                print("- Adicionar nova meta -")
                resultado = tipoMeta()
                if resultado == 0:
                    continue
                elif resultado == "invalido":
                    continue
                tipo, unidadePadrao = resultado

                try:
                    descricao = input("- Descrição: ").capitalize()
                    valorAlvo = float(input(f"- Valor alvo ({unidadePadrao if unidadePadrao else 'unidade'}): "))
                    valorAtual = float(input(f"- Valor atual ({unidadePadrao if unidadePadrao else 'unidade'}): "))
                    print()

                    # validação de sentido dos valores
                    if tipo == "perder peso":
                        if valorAtual < valorAlvo:
                            print("Valores incorretos.")
                            print()
                            continue
                    elif tipo == "ganhar massa":
                        if valorAtual > valorAlvo:
                            print("Valores incorretos.")
                            print()
                            continue

                    if not unidadePadrao:
                        unidade = input("- Unidade (ex: kg, km, min): ")
                    else:
                        unidade = unidadePadrao

                    dicionarioMeta = {
                        'tipo':        tipo,
                        'descricao':   descricao,
                        'valorAlvo':   valorAlvo,
                        'valorAtual':  valorAtual,
                        'unidade':     unidade
                    }
                except ValueError:
                    print("Entrada inválida. Tente novamente.")
                    print()
                    continue

                salvarMeta(pathMetas, arquivoMetas, dicionarioMeta)

            elif opcaoMeta == 2: # mostrar
                while True:
                    # os.system('cls' if os.name == 'nt' else 'clear')
                    print("- Ver metas -")

                    metas = listarMetas(pathMetas, arquivoMetas)
                    if metas == False: # não existe
                        break
                    meta = mostrarMeta(pathMetas, arquivoMetas)
                    if meta == "break":
                        print()
                        break

            elif opcaoMeta == 3: # editar
                while True:
                    print("- Editar metas - ")

                    metas = listarMetas(pathMetas,arquivoMetas)
                    if metas == False:
                        break
                    edicao = editarMeta(pathMetas, arquivoMetas)
                    if edicao == 0:
                        break

            elif opcaoMeta == 4: # excluir
                while True:
                    print("- Excluir meta -")

                    metas = listarMetas(pathMetas,arquivoMetas)
                    if metas == False: # não existe
                        break

                    deletar = excluirMeta(pathMetas, arquivoMetas)
                    if deletar == 0:
                        break
            elif opcaoMeta == 5:
                atualizarProgressoMeta(pathMetas, arquivoMetas)
                
            elif opcaoMeta == 0: # sair
                break

# --> EVOLUÇÃO
    elif opcao == 4:
        menuEvolucao()

# -- > SUGESTÕES
    elif opcao == 5:
        menuSugestoes()
## break ##    
    elif opcao == 0:
        print("Programa encerrado.")
        break
