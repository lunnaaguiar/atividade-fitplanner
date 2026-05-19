import os
os.system('cls' if os.name == 'nt' else 'clear')
# make it work  make it right  make it fast

# >> testar essas funcionalidades:
# criar arquivos importantes! // exercícios - - -

# arquivos = ["cardio.txt", "forca.txt", "flexibilidade.txt", "equilibrio.txt"]
# path = "file/exercicios"
# for nome in arquivos:
#     if not os.path.exists(f"{path}/{nome}"):
#         open(f"{path}/{nome}", "w").close()
# - - - - - - - - - - - - - - -

# [ importante ]
# - ajeitar os 'print()' pra quebra de linha 
# - criar funções da manipulação de arquivos .csv
# - colocar verificação se o arquivo existe ou está vazio
# - falta colocar a visualização e edição dos exercícios // mas eles estão salvos


def menu():
  print("1 - Treinos")
  print("2 - Exercícios")
  print("3 - Metas")
  print("4 - Evolução")
  print("5 - Sugestões")
  print("0 - Sair")
  print()
  opcao = int(input("Insira a opção desejada: "))
  return opcao

def menuTreino():
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

def menuExercicio():
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

def categoriaExercicio():
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

### Exercícios ###

def atualizarExercicios(path, categoria, listaExercicios):
    arquivo = open(f"{path}/{categoria}", "w") # removi .txt

    for i in range(len(listaExercicios)):
        arquivo.write(f"{listaExercicios[i].strip()}\n") # precisa do .strip() pra apagar  aquebra de linha '\n' e adicionar de novo
    arquivo.close()

def addExercicio(path, categoria, exercicios, exercicio):
    exercicios.append(exercicio)
    arquivo = open(f"{path}/{categoria}", "w") # removi .txt
    for i in range(len(exercicios)):
        arquivo.write(f"{exercicios[i].strip()}\n") # precisa do .strip() pra apagar  aquebra de linha '\n' e adicionar de novo
    arquivo.close()
    print()
    print(f"[{exercicio}] foi adicionado!")

def abrirExercicios(path, categoria):
    arquivo = open(f"{path}/{categoria}", "r") # removi .txt
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
    else: 
        print("Sem exercícios cadastrados")



while True:
    opcao = menu()

    if opcao == 1:
        # consertar esse path // está no modelo antigo do.txt 
        path = "files/treinos"
        arquivoTreinos = "treinos.csv"
    elif opcao == 2:
        path = "files/exercicios"

    # - - - - > TREINOS
    if opcao == 1:
        while True:
            opcaoTreino = menuTreino()

            if opcaoTreino == 1: # add
                dicionarioTreino = {}

                print("- Adicionar treino novo -")
                # print("(Digite 0 a qualquer momento para cancelar)\n") # Adicionar isso aqui

                dicionarioTreino = {
                'nome':       input("Nome: "),
                'tipo':       input("Tipo [categoria]: "),
                'duracao':    float(input("Duração (em minutos): ")),
                'objetivo':   input("Objetivo: "),
                'observacao': input("Observações: "),
                'exercicios': ""
                }
                
                print("1 - Sim | 0 - Não")
                opcaoExercicios = int(input("Deseja adicionar exercícios ao seu treino?"))
                if opcaoExercicios == 1:
                    listaExercicios = []
                    while True:
                        tipoExercicio = categoriaExercicio()
                        exercicios = abrirExercicios("files/exercicios", tipoExercicio)
                        listarExercicios(exercicios, tipoExercicio)
                        numeroExercicio = int(input("Qual exercício deseja adicionar?"))
                        indiceExercicio = numeroExercicio-1
                        listaExercicios.append(exercicios[indiceExercicio])
                        print(f"'{exercicios[indiceExercicio]}' foi adicionado ao treino!")

                        print("1 - Sim | 0 - Não")
                        continuar = int(input("Deseja adicionar mais um exercício?"))
                        if continuar == 1:
                            continue
                        elif continuar == 0:
                            break
                        
                    for i in range(len(listaExercicios)):
                        listaExercicios[i] = listaExercicios[i].strip()
                    exerciciosTreino = "-".join(listaExercicios)
                    dicionarioTreino["exercicios"] = exerciciosTreino
                        
                        
                
                # adicionar no .csv
                dicionarioTreino["duracao"] = str(dicionarioTreino["duracao"]) # conversão float -> string // transforma a lista em string
                colunas = ",".join(list(dicionarioTreino.keys()))+"\n" # transforma a lista de chaves em uma string - separando por vírgulas + quebra de linha
                dados = ",".join(list(dicionarioTreino.values()))+"\n" # valores do dicionário -> string + quebra de linha 
                
                print(f"{path}/{arquivoTreinos}")
                if os.path.exists(f"{path}/{arquivoTreinos}"): # adiciona
                    arquivo = open(f"{path}/{arquivoTreinos}", "a")
                    arquivo.write(dados)
                    arquivo.close()
                else: # not os.path.exists(f"{path}/{arquivoTreinos}") # se não existe, cria (com etiquetas)
                    arquivo = open(f"{path}/{arquivoTreinos}", "w")
                    arquivo.write(colunas)
                    arquivo.write(dados)
                    arquivo.close()


                print("Treino salvo!")

            elif opcaoTreino == 2: # mostrar
                while True:
                    print("- Ver treinos -")

                    if not os.path.exists(f"{path}/{arquivoTreinos}"):
                        print("Nenhum treino encontrado.")
                        break
                    
                    # transformar isso em função e corrigir os path!!!
                    # mostrar arquivos // falta incluir se não existir nenhum treino ou arquivo (.csv)    
                    arquivo = open(f"{path}/{arquivoTreinos}", "r")
                    colunas = arquivo.readline()
                    linhas = arquivo.readlines()
                    arquivo.close()

                    if not linhas:
                        print("Nenhum treino encontrado.")
                        break

                    # print
                    print("Treinos")
                    for i, linha in enumerate(linhas, start=1):
                        categorias = linha.split(",")
                        print(f"Treino {i} | {categorias[0]}")

                    print(">>> 0 - Sair")

                    formatacao = ["Nome do treino:", "Tipo/Categoria:", "Duração:", "Objetivo:", "Observações:"]
                    opcao = int(input("Qual treino deseja visualizar? "))

                    if opcao <= len(linhas) and opcao > 0:
                        linha = linhas[opcao-1].split(",")
                        print(f"- Treino {opcao} -")
                        for i in range(len(formatacao)): # quantidade de elementos
                            print(f"{formatacao[i]} {linha[i].strip()}")
                    elif opcao == 0:
                        break
                    else: 
                        print("Opção inválida.\n")
              
            elif opcaoTreino == 3: # editar
                while True: 
                    print("- Editar treinos - ")
                    if not os.path.exists(f"{path}/{arquivoTreinos}"):
                        print("Nenhum treino encontrado.")
                        break
                        
                    arquivo = open(f"{path}/{arquivoTreinos}", "r")
                    colunas = arquivo.readline()
                    linhas = arquivo.readlines()
                    arquivo.close()

                    if not linhas:
                        print("Nenhum treino encontrado.")
                        break
                    
                    # listar arquivos [ vai virar função ]
                    print("Treinos")
                    for i, linha in enumerate(linhas, start=1):
                        categorias = linha.split(",")
                        print(f"Treino {i} | {categorias[0]}")
                        
                    # organizar essa parte: 
                    opcao = int(input("Qual treino deseja editar? "))
                    if opcao <= len(linhas) and opcao > 0:
                        indiceTreino = opcao-1
                        categorias = linhas[indiceTreino].strip().split(",")
                        formatacao = ["Nome do treino:", "Tipo/Categoria:", "Duração:", "Objetivo:", "Observações:"]
                        for i in range(len(formatacao)):
                            print(f"{i+1} | {formatacao[i]} {categorias[i]}")
                            
                        print(">>> 0 - Sair")
                        opcaoCategoria = int(input("Qual categoria deseja editar?"))
                        
                        if opcaoCategoria <= len(categorias) and opcaoCategoria > 0:
                            indiceCategoria = opcaoCategoria-1
                            novoTexto = input(f"{formatacao[indiceCategoria]} ")
                            categorias[indiceCategoria] = novoTexto
                            # confirmacao = int(input(""))
                            categoria_str = ",".join(categorias)
                            linhas[indiceTreino] = categoria_str + "\n"
                            
                            arquivo = open(f"{path}/{arquivoTreinos}", "w")
                            arquivo.write(colunas)
                            for i in range(len(linhas)):
                                arquivo.write(linhas[i])   
                            arquivo.close()      
                        elif opcaoCategoria == 0:
                            break
                        else:
                           print("Opção inválida") 
                            
                    elif opcao == 0:
                        break
                    else: 
                        print("Opção inválida.\n")    
                    

            elif opcaoTreino == 4: # excluir
                while True:
                    print("- Excluir arquivo -")
                
                    if not os.path.exists(f"{path}/{arquivoTreinos}"):
                        print("Nenhum treino encontrado.")
                        break
                        
                    arquivo = open(f"{path}/{arquivoTreinos}", "r")
                    colunas = arquivo.readline()
                    linhas = arquivo.readlines()
                    arquivo.close()

                    if not linhas:
                        print("Nenhum treino encontrado.")
                        break
                    # listar arquivos
                    print("Treinos")
                    for i, linha in enumerate(linhas, start=1):
                        categorias = linha.split(",")
                        print(f"Treino {i} | {categorias[0]}")
                    opcao = int(input("Qual arquivo deseja excluir? "))
                                            
                    # mostrar arquivo
                    print(">>> 0 - Sair")

                    formatacao = ["Nome do treino:", "Tipo/Categoria:", "Duração:", "Objetivo:", "Observações:"]
                    if opcao <= len(linhas) and opcao > 0:
                        linha = linhas[opcao-1].split(",")
                        print(f"- Treino {opcao} -")
                        for i in range(5): # quantidade de elementos
                            print(f"{formatacao[i]} {linha[i].strip()}")
                    elif opcao == 0:
                        break
                    else: 
                        print("Opção inválida.\n")
                    
                    
                    print(f"Tem certeza que deseja apagar o Treino {opcao}")
                    print("1 - Sim | 0 - Não")
                    delete = int(input("[1/0]: "))
                    if delete == 1:
                        indice = opcao-1
                        linhas.pop(indice)
                        arquivo = open(f"{path}/{arquivoTreinos}", "w")
                        arquivo.write(colunas)
                        for i in range(len(linhas)):
                            arquivo.write(linhas[i]) 
                        arquivo.close()                       
                        print("O Treino foi deletado.")
                    elif delete == 0:
                        print("Cancelado! O arquivo não foi deletado.")
                    
                    else:
                        print("Opção inválida!")


            elif opcaoTreino == 0:
                break

    # - - - - > EXERCÍCIOS
    elif opcao == 2:
        while True:
            opcaoExercicio = menuExercicio() # MENU

            # OPÇÕES
            if opcaoExercicio == 1: # adicionar exercícios
                while True:
                    print("- Adicionar exercício novo -")
                    categoria = categoriaExercicio()

                    if categoria == 0:
                        break
                    elif categoria == "invalido":
                        print("Tente novamente ou aperte '0 - Voltar'")
                        continue # pula o print, reinicia o loop
                    
                    print() # pular linha

                    exercicio = input("Nome: ").capitalize() # primeira letra maiuscula
                    exercicios = abrirExercicios(path, categoria)
                    addExercicio(path, categoria, exercicios, exercicio)

            elif opcaoExercicio == 2: # listar exercícios
                while True:
                    print("- Ver exercícios -")
                    categoria = categoriaExercicio() # retorna o arquivo: "categoria.txt" 

                    if categoria == 0:
                        break
                    elif categoria == "invalido":
                        print("Tente novamente ou aperte '0 - Voltar'")
                        continue # pula o print, reinicia o loop

                    exercicios = abrirExercicios(path, categoria)
                    listarExercicios(exercicios, categoria)

            elif opcaoExercicio == 3: # editar exercícios
                while True:
                    print("- Editar exercícios -")
                    print("Qual a categoria do exercício que você deseja editar?")
                    categoria = categoriaExercicio() # retorna o arquivo: "categoria.txt" 

                    if categoria == 0:
                        break
                    elif categoria == "invalido":
                        print("Tente novamente ou aperte '0 - Voltar'")
                        continue # pula o print, reinicia o loop

                    exercicios = abrirExercicios(path, categoria)
                    print("Qual exercício deseja editar?")
                    listarExercicios(exercicios, categoria)
                    print()
                    indice = int(input("Exercício nº: "))-1
                    novoExercicio = input("Novo texto: ").capitalize() # editar
                    print(exercicios[indice])
                    exercicios[indice] = novoExercicio

                    atualizarExercicios(path, categoria, exercicios)
                    
                    

            elif opcaoExercicio == 4: # excluir exercícios
                print("- Excluir exercícios -")

                while True:
                    # print("Qual categoria de exercício você deseja editar?")
                    categoria = categoriaExercicio() # retorna o arquivo: "categoria.txt" 

                    if categoria == 0:
                        break
                    elif categoria == "invalido":
                        print("Tente novamente ou aperte '0 - Voltar'")
                        continue # pula o print, reinicia o loop

                    exercicios = abrirExercicios(path, categoria)
                    # deletar
                    print("Qual exercício deseja deletar?")
                    listarExercicios(exercicios, categoria)
                    print()
                    indice = int(input("Exercício nº: "))-1

                    # confirmação
                    while True:
                        print(f"Deseja apagar exercício [{exercicios[indice].strip()}]?")
                        confirmacao = int(input("1 - Sim / 0 - Não: "))

                        if confirmacao == 1: # sim
                            exercicios.pop(indice) # deletar
                            atualizarExercicios(path, categoria, exercicios)
                            print("Exercício deletado!")
                            break
                        elif confirmacao == 0: # não
                            print("Cancelado!")
                            break
                        else:
                            print("Opção inválida!")
                            continue


            elif opcaoExercicio == 0: # fim
                print("break")
                break


