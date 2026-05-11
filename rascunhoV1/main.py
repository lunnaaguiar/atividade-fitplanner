import os
os.system('cls' if os.name == 'nt' else 'clear')
# - - - - - - - - - - - - - - -

def menu():
  print("1 - Treinos")
  print("2 - Exercícios")
  print("3 - Metas")
  print("4 - Evolução")
  print("5 - Sugestões")
  print("0 - Sair")
  print()
  opcao = int(input("Insira a opção desejada: "))
  print()
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

def salvarArquivoTreino(dicionario):
    textos = ["Nome: ", "Tipo [categoria]: ", "Duração (em minutos): ", "Objetivo: ", "Observações: "]
    numeroArquivo = len((os.listdir("files/treinos")))
    
    arquivo = open(f"files/treinos/dados_{numeroArquivo+1}.txt", "w", encoding="utf-8")
    for texto, valor in zip(textos, dicionario.values()):
        arquivo.write(f"{texto}{valor}\n")
    arquivo.close()
    return arquivo

def salvarArquivo(caminho, dicionario, textos): #função geral TESTAR
    numeroArquivo = len((os.listdir(caminho)))
    
    arquivo = open(f"{caminho}/dados_{numeroArquivo+1}.txt", "w", encoding="utf-8")
    for texto, valor in zip(textos, dicionario.values()):
        arquivo.write(f"{texto}{valor}\n")
    arquivo.close()
    return arquivo

def renomearArquivo(caminho):
    arquivos = sorted(os.listdir(caminho))
    for i, arquivo in enumerate(arquivos, start=1):
        os.rename(f"{caminho}/{arquivo}", f"{caminho}/dados_{i}.txt")
        
def mostrarArquivos(caminho, tipo): # treinos e exercícios
    arquivos = sorted(os.listdir(caminho))
    
    for i in range(len(arquivos)):
        arquivo = open(f"{caminho}/dados_{i+1}.txt", "r")
        nome = arquivo.readline().split()
        print(f"{tipo} {i+1} |", *nome[1:])

def mostrarArquivo(caminho, numArquivo):
    arquivo = open(f"{caminho}/dados_{numArquivo}.txt", "r")
    conteudo = arquivo.read()
    print("- - - - - - - - - - - -")
    print(conteudo.strip())
    print("- - - - - - - - - - - -")

def editarArquivo(caminho, numArquivo, textos):
    arquivo = open(f"{caminho}/dados_{numArquivo}.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()

    print("- - - - -")
    for i, linha in enumerate(linhas, start=1):
        print(f"[{i}] {linha.strip()}")
    print("- - - - -")

    editar = int(input(f"Qual linha deseja editar? [1-{len(linhas)}] "))
    novaLinha = input("Novo texto: ")
    linhas[editar-1] = textos[editar-1]+novaLinha+"\n"

    arquivo = open(f"{caminho}/dados_{numArquivo}.txt", "w")
    arquivo.writelines(linhas)
    arquivo.close()
    
    print("Editado com sucesso!")    
    return arquivo

def apagarArquivo(caminho, numArquivo):
    os.remove(f"{caminho}/dados_{numArquivo}.txt")


while True:
    opcao = menu()

    # - - - - > TREINOS
    if opcao == 1:
        while True:
            textos = ["Nome: ", "Tipo [categoria]: ", "Duração (em minutos): ", "Objetivo: ", "Observações: "]
            path = "files/treinos"
            opcaoTreino = menuTreino()
            renomearArquivo(path)

            if opcaoTreino == 1: # add
                treinoDicionario = {}

                print("- Adicionar treino novo -")
                # print("(Digite 0 a qualquer momento para cancelar)\n") # Adicionar isso aqui

                treinoDicionario = {
                'nome':       input("Nome: "),
                'tipo':       input("Tipo (categoria): "),
                'duracao':    float(input("Duração (minutos): ")),
                'objetivo':   input("Objetivo: "),
                'observacao': input("Observações: ")
                }

                treinoTag = ["Nome: ", "Tipo [categoria]: ", "Duração (em minutos): ", "Objetivo: ", "Observações: "]
                salvarArquivo(path, treinoDicionario, treinoTag) # criar .txt
                print("Treino salvo!")

            elif opcaoTreino == 2: # mostrar
                while True:
                    print("- Ver treinos -")
                    mostrarArquivos(path, "Treino")
                    print(">>> 0 - Sair")
                    opcao = int(input("Qual treino deseja visualizar? "))
                    if opcao <= len((os.listdir(path))) and opcao > 0:
                        mostrarArquivo(path, opcao)
                    elif opcao == 0:
                        break
                    else: 
                        print("Opção inválida.\n")
            elif opcaoTreino == 3: # editar
                while True: 
                    print("- Editar treinos - ")
                    mostrarArquivos(path, "Treinos")
                    print("\n0 - Sair")
                    numArquivo = int(input("Selecione o número do arquivo: "))
                    if numArquivo == 0: # ??
                        break
                    editarArquivo(path, numArquivo, textos)

            elif opcaoTreino == 4: # excluir
                print("- Excluir arquivo -")
                mostrarArquivos(path, "Treino")
                numArquivo = int(input("Qual arquivo deseja excluir? "))
                mostrarArquivo(path, numArquivo)
                print(f"Tem certeza que deseja apagar o Treino {numArquivo}")
                print("1 - Sim | 0 - Não")
                delete = int(input("[1/0]: "))
                if delete == 1:
                    apagarArquivo(path, numArquivo)
                    print("O Treino foi deletado.")
                elif delete == 0:
                    print("Cancelado! O arquivo não foi deletado.")


            elif opcaoTreino == 0:
                break

    # - - - - > EXERCÍCIOS
    elif opcao == 2:
        aa = "em construção"   
        break