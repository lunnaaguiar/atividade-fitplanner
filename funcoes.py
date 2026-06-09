import os


# variáveis de treino
pathTreinos = "files/treinos"
pathExercicios = "files/exercicios"
arquivoTreinos = "treinos.csv"

# inicializar arquivos
def inicializarArquivos():
    os.makedirs(pathTreinos, exist_ok=True)
    os.makedirs(pathExercicios, exist_ok=True)
    os.makedirs(pathMetas, exist_ok=True)
    os.makedirs("files/evolucao", exist_ok=True)

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
        print("6 - Calcular IMC")
        print("7 - Resetar dados")
        print("0 - Sair")
        print()
        opcao = int(input("Insira a opção desejada: "))
        if opcao < 0 or opcao > 7:
            print("Opção inválida")
            return None
        return opcao
    except ValueError:
        print()
        print("Entrada inválida.")
        print("Insira apeenas números.")
        print()
        return ""

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
        if opcao < 0 or opcao > 5:
            print("> > Opção inválida! Selecione um número entre 0-4.")
        print()
        return opcao
    except ValueError:
        print("Opção inválida.")
        print()
        return 0

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
        if opcao < 0 or opcao > 5:
            print("> > Opção inválida! Selecione um número entre 0-4.")
        print()
        return opcao
    except ValueError:
        print("Opção inválida.")
        print()
        return 0

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
        print()
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
            print("Opção inválida")
            print()
            return "invalido" # trocar por inválida
    except ValueError:
        print()
        print("Entrada inválida.")
        print("Tente novamente ou aperte '0 - Voltar'")
        print()
        return "invalido"


### Exercícios ###

def atualizarExercicios(path, categoria, listaExercicios):
    arquivo = open(f"{path}/{categoria}", "w", encoding='utf-8') # removi .txt

    for i in range(len(listaExercicios)):
        arquivo.write(f"{listaExercicios[i].strip()}\n") # precisa do .strip() pra apagar  aquebra de linha '\n' e adicionar de novo
    arquivo.close()

def editarExercicio(pathExercicio, categoria, exercicios):
    while True:
        try:
            print("(0 - Voltar)")
            print("Qual exercício deseja editar?")
            opcao = int(input("> Exercício nº: "))
        except ValueError:
            print("Entrada inválida.")
        if opcao <= len(exercicios) and opcao >0:
            indice = opcao-1
            novoExercicio = input("Novo texto: ").capitalize()
        elif opcao == 0:
            return ""
        else:
            print("Exercício não encontrado.")
        exercicios[indice] = novoExercicio
        if novoExercicio != "":
            arquivo = open(f"{pathExercicio}/{categoria}", "w", encoding='utf-8') # removi .txt
            for i in range(len(exercicios)):
                arquivo.write(f"{exercicios[i].strip()}\n") # precisa do .strip() pra apagar  aquebra de linha '\n' e adicionar de novo
            arquivo.close()    
        else:
            print("Escreva algo!")

def addExercicio(path, categoria, exercicios):
    try:
        exercicio = input("Nome: ").capitalize()
        print()
        if exercicio != "":
            print("(1 - Sim | 0 - Não)")
            confirmacao = int(input(f"> Deseja adicionar o exercício [{exercicio}]? "))
            print()
            if confirmacao == 1:
                exercicios.append(exercicio)
                arquivo = open(f"{path}/{categoria}", "w", encoding='utf-8') # removi .txt
                for i in range(len(exercicios)):
                    arquivo.write(f"{exercicios[i].strip()}\n") # precisa do .strip() pra apagar  aquebra de linha '\n' e adicionar de novo
                arquivo.close()
                print()
                print(f"[{exercicio}] foi adicionado!")
                print()
            elif confirmacao == 0:
                print("O exercício não foi adicionado à sua lista.")
                print()
        else:
            print()
            print("Escreva algo!")
            print()
    except ValueError:
        print("Entrada inválida.")

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
        print()
        return True
    else: 
        print("Sem exercícios cadastrados")
        print()
        return False

def excluirExercicio(pathExercicio, categoria, exercicios):
    while True:
        try:
            print("(0 - Voltar)")
            print("Qual exercício deseja apagar?")
            opcao = int(input("> Exercício nº: "))
            indice = opcao-1
            print()
            if opcao <= len(exercicios) and opcao > 0:
                indice = opcao-1
                break
            elif opcao == 0:
                return 0
            else:
                print("Exercício não encontrado.")
                print()
        except ValueError:
            print()
            print("Entrada inválida! Digite um número!")
            print()
    while True:
        try:
            print("(1 - Sim | 0 - Não)")
            confirmacao = int(input(f"Deseja apagar o exercício [{exercicios[indice].strip()}]? "))
            if confirmacao == 1:
                exercicioDeletado = exercicios[indice].strip()
                # deletar da lista
                exercicios.pop(indice)
                # reescrever os exercícios
                arquivo = open(f"{pathExercicio}/{categoria}", "w", encoding='utf-8') 
                for i in range(len(exercicios)):
                    arquivo.write(f"{exercicios[i].strip()}\n") 
                arquivo.close()
                print(f"Exercício '{exercicioDeletado}' deletado.")
                break
            elif confirmacao == 0:
                print("Cancelado!")
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print()
            print("Entrada inválida.")
            print()
            break           
    print("- "*16)
    print()
        
### Treinos ###

def listarTreinos(path, arquivo):

    # verificação
    if not os.path.exists(f"{path}/{arquivo}"):
        print("Nenhum treino encontrado.")
        return False

    arquivo = open(f"{path}/{arquivo}", "r", encoding='utf-8')
    colunas = arquivo.readline()
    linhas = arquivo.readlines()
    arquivo.close()

    if not linhas:
        print("Nenhum treino registrado!")
        print()
        return False
    else:
        # print
        print("Treinos")
        for i, linha in enumerate(linhas, start=1):
            categorias = linha.split(",")
            print(f"Treino {i} | {categorias[0]}")
        print()

def mostrarTreino(path,file, opcao):
    formatacao = ["Nome do treino:", "Tipo/Categoria:", "Duração:", "Objetivo:", "Observações:"]

    if not os.path.exists(f"{path}/{file}"):
        print("Arquivo de treinos não encontrado.")
        return ""

    arquivo = open(f"{path}/{file}", "r", encoding='utf-8')
    colunas = arquivo.readline()
    linhas = arquivo.readlines()
    arquivo.close()

    try:
        print(">>> 0 - Sair")
        opcao = int(input("Qual treino deseja visualizar? "))
        indiceTreino = opcao-1
        if opcao <= len(linhas) and opcao > 0:
            treino = linhas[indiceTreino].strip().split(",")
            print()
            print("- - - - - -")
            print(f"- Treino {opcao} -")

            for i in range(min(len(formatacao), len(treino))): # quantidade de elementos
                print(f"{formatacao[i]} {treino[i].strip()}")
            print()

            # imprimir exercícios
            if len(treino) > 5 and treino[5].strip() != "":
                listaExercicios = treino[5].split("|")
                print("Exercícios:")
                for exercicio in listaExercicios:
                    print(f"> {exercicio}")                
            else:
                print("Sem exercícios cadastrados.")
            print("- - - - - -")
            print()

        elif opcao == 0:
            return "break"
        else:
            print("\nTreino não encontrado!")
            print()
            return ""
    except ValueError:
        print("\nEntrada inválida.")
        print()
        return ""

def vincularExercicioTreino(pathExercicios):
    listaExercicios = []
    while True:
        try:
            print("(1 - Sim | 0 - Não)")
            addExercicio = int(input("Deseja adicionar exercícios ao seu treino? "))
            print()
            if addExercicio == 1:
                break
            elif addExercicio == 0:
                print("Nenhum exercício foi adicionado ao treino.")
                print()
                return ""
            else:
                print("Opção inválida!")
                continue
        except:
            print("Entrada inválida")    
            print()        
    while True:
        try:
            categoria = categoriaExercicio()
            if categoria == 0:
                if listaExercicios:
                    exercicios_string = "|".join(listaExercicios)
                    return exercicios_string
                else:
                    return ""
            elif categoria == "invalido":
                continue

            exercicios = abrirExercicios(pathExercicios, categoria)
            temExercicio = listarExercicios(exercicios, categoria)
            # print()
            if temExercicio == False:
                continue
            
            print(">>> 0 - Voltar")
            numeroExercicio = int(input("Qual exercício deseja adicionar? "))
            print()
            if numeroExercicio == 0:
                continue
            
            indiceExercicio = numeroExercicio-1
            if indiceExercicio < len(exercicios) and indiceExercicio >=0:

                exercicioLimpo = exercicios[indiceExercicio].strip() 
                if exercicioLimpo not in listaExercicios:
                    listaExercicios.append(exercicioLimpo)
                    print(f"'{exercicioLimpo}' foi adicionado ao seu treino.")
                    print()
                else:
                    print(f"{exercicioLimpo} já está no seu treino.")
                    print()
                    continue

                while True:
                    try:
                        print("(1 - Sim | 0 - Não)")
                        continuar = int(input("Deseja adicionar mais um exercício? "))
                        print()

                        if continuar in [0, 1]:
                            break
                        else:
                            print("Opção inválida! Digite 1 ou 0.")
                            print()
                    except ValueError:
                        print("Entrada inválida! Digite um número!")
                        # print("Entrada inválida! Digite apenas números (1 ou 0).")
                        print()

                if not listaExercicios:
                    print("Nenhum exercício adicionado.")
                else:
                    print("Exercícios adicionados:")
                    for exercicio in listaExercicios:
                        print(f"{exercicio} | ", end="")
                    print()
                    print()

                if continuar == 1:
                    continue
                elif continuar == 0:
                    exercicios_string = "|".join(listaExercicios)
                    return exercicios_string
            else:
                print("Opção inválida!")
                print()
                continue
        except ValueError:
            print("Entrada inválida.")
            print()
        
def salvarTreino(pathTreino, arquivoTreino, dicionarioTreino):
# adicionar no .csv
    dicionarioTreino["duracao"] = str(dicionarioTreino["duracao"]) # conversão float -> string // transforma a lista em string
    colunas = ",".join(list(dicionarioTreino.keys()))+"\n" # transforma a lista de chaves em uma string - separando por vírgulas + quebra de linha
    dados = ",".join(list(dicionarioTreino.values()))+"\n" # valores do dicionário -> string + quebra de linha 
    
    while True:
        try:
            print("(1 - Sim | 0 - Não)")
            confirmacao = int(input(f"Deseja salvar o treino '{dicionarioTreino["nome"]}'? "))
            print()
            if confirmacao == 1:
                break
            elif confirmacao == 0:
                print("Cancelado! O treino não foi salvo.")
                print()
                return None
            else:
                print("Por favor, insira 1 ou 0!")
                print()
        except ValueError:
            print("Ops! Opção inválida.")
            print()
            continue

    if os.path.exists(f"{pathTreino}/{arquivoTreino}"): # adiciona
        arquivo = open(f"{pathTreino}/{arquivoTreino}", "a", encoding='utf-8')
        arquivo.write(dados)
        arquivo.close()
    else: # not os.path.exists(f"{path}/{arquivoTreino}") # se não existe, cria (com etiquetas)
        arquivo = open(f"{pathTreino}/{arquivoTreino}", "w", encoding='utf-8')
        arquivo.write(colunas)
        arquivo.write(dados)
        arquivo.close()
    print("Treino salvo!")

def editarTreino(pathTreino, arquivoTreino):
    arquivo = open(f"{pathTreino}/{arquivoTreino}", "r", encoding='utf-8')
    colunas = arquivo.readline()
    linhas = arquivo.readlines()
    arquivo.close()
    while True:
        print()
        ## treino
        try:
            opcao = int(input("Qual treino deseja editar? "))
            if opcao <=(len(linhas)) and opcao >0:
                indiceTreino = opcao-1
                dadosTreino = linhas[indiceTreino].strip().split(",")
                formatacao = ["Nome do treino:", "Tipo/Categoria:", "Duração:", "Objetivo:", "Observações:"]
                for i in range(len(formatacao)):
                    print(f"{i+1} | {formatacao[i]} {dadosTreino[i]}")
                break
            elif opcao == 0:
                print("Voltando. :)")
                return 0
            else:
                print("Treino não encontrado")
                continue
        except ValueError:
            print("Entrada inválida! Digite um número!")    
            continue
    ## categoria
    while True:
        print()
        try:
            print(">>> 0 - Sair")
            itemEdicao = int(input("Qual categoria deseja editar? "))
    
            if itemEdicao <= len(dadosTreino) and itemEdicao > 0:
                indiceDado = itemEdicao-1
                if indiceDado == 2:
                    novaInformacao = int(input(f"- {formatacao[indiceDado]} "))    
                else:
                    novaInformacao = input(f"- {formatacao[indiceDado]} ")
                dadosTreino[indiceDado] = novaInformacao
                dadosTreinoTexto = ",".join(dadosTreino)
                linhas[indiceTreino] = dadosTreinoTexto + "\n"
                
                print()
                print("(1 - Sim | 0 - Não)")
                confirmacao = int(input("Você confirma as alterações? "))
                
                if confirmacao == 1:
                    arquivo = open(f"{pathTreino}/{arquivoTreino}", "w", encoding='utf-8')
                    arquivo.write(colunas)
                    for i in range(len(linhas)):
                        arquivo.write(linhas[i])   
                    arquivo.close()
                    print()
                    print("Edições aplicadas!")
                    print()
                    return ""
                elif confirmacao == 0:
                    print("Edições não aplicadas")
                    print()
                    return ""
            elif itemEdicao == 0:
                print("Voltando. :)")
                print()
                return ""
            else: 
                print("Opção inválida!")
                print()
                continue      
        except ValueError:
            print("Entrada inválida! Digite um número!")
            print()    
            return ""
        
def excluirTreino(pathTreino, arquivoTreino):
    arquivo = open(f"{pathTreino}/{arquivoTreino}", "r", encoding='utf-8')
    colunas = arquivo.readline()
    linhas = arquivo.readlines()
    arquivo.close() 
    while True:
        try:
            print(">>> 0 - Sair")
            opcao = int(input("Qual arquivo deseja excluir? "))
            indiceTreino = opcao-1
            formatacao = ["Nome do treino:", "Tipo/Categoria:", "Duração:", "Objetivo:", "Observações:"]
            if opcao <= len(linhas) and opcao > 0:
                treino = linhas[indiceTreino].split(",")
                print()
                print("- - -")
                for i in range(5): # quantidade de elementos
                    print(f"{formatacao[i]} {treino[i].strip()}")
                print("- - -")
                print()
                break
            elif opcao == 0:
                print()
                return 0
            else:
                print("Opção inválida")
                print()
                return ""        
        except ValueError:
            print("Entrada inválida! Digite um número!")
            print()
            continue
    ## confirmação
    while True:
        try:
            print("(1 - Sim | 0 - Não)")
            confirmacao = int(input(f"Tem certeza que deseja apagar o Treino {opcao}? "))
            print()
            if confirmacao == 1:
                linhas.pop(indiceTreino)
                
                arquivo = open(f"{pathTreino}/{arquivoTreino}", "w", encoding='utf-8')
                arquivo.write(colunas)
                for i in range(len(linhas)):
                    arquivo.write(linhas[i])
                arquivo.close()
                print("O treino foi deletado!")
                print()
                return ""
            elif confirmacao == 0:
                print("Cancelado!\nO treino não foi deletado!")
                print()
                return ""
            else:
                print("Opção inválida!")
                print()
                continue
        except ValueError:
            print("Entrada inválida! Digite um número!")
            print()

# Seção controle de metas  ============================================

# variáveis metas
pathMetas = "files/metas"
arquivoMetas = "metas.csv"
colunasMetas = "tipo,descricao,valorAlvo,valorAtual,unidade\n"

### Metas ###

def menuMeta():
    try:
        print("- - - - METAS - - - -")
        print("1 - Nova meta")
        print("2 - Ver metas")
        print("3 - Editar meta")
        print("4 - Excluir meta")
        print("5 - Atualizar minhas metas")
        print("0 - Voltar")
        print()
        opcao = int(input("> > Opção: "))
        if opcao < 0 or opcao > 5:
            print("> > Opção inválida! Selecione um número entre 0-5.")
        print()
        return opcao
    except ValueError:
        print("Opção inválida.")
        print()

def listarMetas(path, arquivo):

    # verificação
    if not os.path.exists(f"{path}/{arquivo}"):
        print("Nenhuma meta encontrada.")
        return False

    arquivo = open(f"{path}/{arquivo}", "r", encoding='utf-8')
    colunas = arquivo.readline()
    linhas = arquivo.readlines()
    arquivo.close()

    if not linhas:
        print("Nenhuma meta registrada!")
        print()
        return False
    else:
        # print
        print("Metas")
        for i, linha in enumerate(linhas, start=1):
            dados = linha.split(",")
            print(f"Meta {i} | {dados[1].strip()} ({dados[0].strip()})")
        print()

def mostrarMeta(path, arquivo):
    formatacao = ["Tipo:", "Descrição:", "Valor alvo:", "Valor atual:", "Unidade:"]

    arquivo = open(f"{path}/{arquivo}", "r", encoding='utf-8')
    colunas = arquivo.readline()
    linhas = arquivo.readlines()
    arquivo.close()

    try:
        print(">>> 0 - Sair")
        opcao = int(input("Qual meta deseja visualizar? "))
        if opcao <= len(linhas) and opcao > 0:
            meta = linhas[opcao-1].strip().split(",")
            print()
            print("- - - - - -")
            print(f"- Meta {opcao} -")
            for i in range(len(formatacao)):
                print(f"{formatacao[i]} {meta[i].strip()}")
            # barra de progresso
            tipo = meta[0].strip()
            valor_alvo = float(meta[2])
            valor_atual = float(meta[3])
            print(f"Progresso: {barraProgresso(valor_atual, valor_alvo, tipo)}")
            print("- - - - - -")
            print()
        elif opcao == 0:
            return "break"
        else:
            print()
            print("Meta não encontrada!")
            print()
            return ""
    except ValueError:
        print()
        print("Entrada inválida.")
        print()
        return ""

def tipoMeta():
    try:
        print("- - - Tipo de meta - - -")
        print("1 - Perder peso")
        print("2 - Ganhar massa muscular")
        print("3 - Melhorar condicionamento físico")
        print("4 - Outro")
        print("0 - Voltar")
        print()
        tipo = int(input("Selecione o tipo: "))
        print()
        tipos = {
            1: ("perder peso", "kg"),
            2: ("ganhar massa", "kg"),
            3: ("condicionamento", "treinos"),
            4: ("outro", "")
        }
        if tipo in tipos:
            return tipos[tipo]
        elif tipo == 0:
            return 0
        else:
            print("Opção inválida")
            print()
            return "invalido"
    except ValueError:
        print()
        print("Entrada inválida.")
        print("Tente novamente ou aperte '0 - Voltar'")
        print()
        return "invalido"

def salvarMeta(pathMeta, arquivoMeta, dicionarioMeta):
# adicionar no .csv
    dicionarioMeta["valorAlvo"] = str(dicionarioMeta["valorAlvo"]) # conversão float -> string
    dicionarioMeta["valorAtual"] = str(dicionarioMeta["valorAtual"]) # conversão float -> string
    colunas = ",".join(list(dicionarioMeta.keys()))+"\n" # transforma a lista de chaves em uma string
    dados = ",".join(list(dicionarioMeta.values()))+"\n" # valores do dicionário -> string

    while True:
        try:
            print("(1 - Sim | 0 - Não)")
            confirmacao = int(input(f"Deseja salvar a meta '{dicionarioMeta['descricao']}'? "))
            print()
            if confirmacao == 1:
                break
            elif confirmacao == 0:
                print("Cancelado! A meta não foi salva.")
                print()
                return None
            else:
                print("Por favor, insira 1 ou 0!")
                print()
        except ValueError:
            print("Ops! Opção inválida.")
            print()
            continue

    if os.path.exists(f"{pathMeta}/{arquivoMeta}"): # adiciona
        arquivo = open(f"{pathMeta}/{arquivoMeta}", "a", encoding='utf-8')
        arquivo.write(dados)
        arquivo.close()
    else: # se não existe, cria (com etiquetas)
        arquivo = open(f"{pathMeta}/{arquivoMeta}", "w", encoding='utf-8')
        arquivo.write(colunas)
        arquivo.write(dados)
        arquivo.close()
    print("Meta salva!")

def editarMeta(pathMeta, arquivoMeta):

    if not os.path.exists(f"{pathMeta}/{arquivoMeta}"):
        print("Nenhuma meta cadastrada.")
        return 0

    arquivo = open(f"{pathMeta}/{arquivoMeta}", "r", encoding='utf-8')
    colunas = arquivo.readline()
    linhas = arquivo.readlines()
    arquivo.close()

    if not linhas:
        print("Nenhuma meta cadastrada.")
        return 0

    while True:
        ## meta
        try:
            print(">>> 0 - Voltar")
            opcao = int(input("Qual meta deseja editar? "))
            if opcao == 0:
                return 0
            if opcao <=(len(linhas)) and opcao > 0:
                indiceMeta = opcao-1
                dadosMeta = linhas[indiceMeta].strip().split(",")
                formatacao = ["Tipo:", "Descrição:", "Valor alvo:", "Valor atual:", "Unidade:"]
                print("\nCampos editáveis:")
                for i in range(len(formatacao)):
                    print(f"{i+1} | {formatacao[i]} {dadosMeta[i].strip()}")
                break
            else:
                print("Meta não encontrada")
                continue
        except ValueError:
            print("Entrada inválida! Digite um número!")
            continue
    ## campo
    while True:
        print()
        try:
            print(">>> 0 - Sair")
            itemEdicao = int(input("Qual campo deseja editar? "))

            if itemEdicao == 0:
                print("Edição cancelada.\n")
                return ""
            
            if itemEdicao <= len(dadosMeta) and itemEdicao > 0:
                indiceDado = itemEdicao-1

                # bloquear campos fixos
                if indiceDado == 0:
                    print("Não é possível alterar o tipo da meta!")
                    # print()
                    continue
                elif indiceDado == 4:
                    print("Não é possível alterar unidades!")
                    # print()
                    continue

                
                if indiceDado in [2, 3]:  # valorAlvo ou valorAtual (float)
                    novaInformacao = float(input(f"- {formatacao[indiceDado]} "))
                    if novaInformacao < 0:
                        print("Valores numéricos não podem ser negativos!")
                        continue
                else:
                    novaInformacao = input(f"- {formatacao[indiceDado]} ").capitalize()

                # validações
                tipo = dadosMeta[0].strip()
                valor_alvo = novaInformacao if indiceDado == 2 else float(dadosMeta[2])
                valor_atual = novaInformacao if indiceDado == 3 else float(dadosMeta[3])

                if indiceDado == 2:  # editando valor alvo
                    if tipo == "perder peso" and  valor_atual < valor_alvo:
                            print("Erro")
                            print("O valor alvo não pode ser maior que o valor atual!")
                            print("(Para perder peso, a meta precisa estar abaixo do peso atual.)")
                            print()
                            continue
                    elif tipo == "ganhar massa" and valor_atual > valor_alvo:
                            print("Erro")
                            print("O valor alvo não pode ser menor que o valor atual!")
                            print("(Para ganhar massa, a meta precisa estar acima do peso atual.)")
                            print()
                            continue
                    
                dadosMeta[indiceDado] = str(novaInformacao)
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Entrada inválida! Digite o formato correto.")

    try:
        print()
        print("(1 - Sim | 0 - Não)")
        confirmacao = int(input("Você confirma as alterações? "))
        
        if confirmacao == 1:
            linhas[indiceMeta] = ",".join(dadosMeta) + "\n"
            arquivo = open(f"{pathMeta}/{arquivoMeta}", "w", encoding='utf-8')
            arquivo.write(colunas)
            for linha in linhas:
                arquivo.write(linha)
            arquivo.close()
            # print()
            print("Edições aplicadas com sucesso!")
        elif confirmacao == 0:
            print("Edições descartadas.")
    except ValueError:
        print("Entrada inválida!")
    print()
    return ""

def excluirMeta(pathMeta, arquivoMeta):
    arquivo = open(f"{pathMeta}/{arquivoMeta}", "r", encoding='utf-8')
    colunas = arquivo.readline()
    linhas = arquivo.readlines()
    arquivo.close()
    while True:
        try:
            print(">>> 0 - Sair")
            opcao = int(input("Qual meta deseja excluir? "))
            indiceMeta = opcao-1
            formatacao = ["Tipo:", "Descrição:", "Valor alvo:", "Valor atual:", "Unidade:"]
            if opcao <= len(linhas) and opcao > 0:
                meta = linhas[indiceMeta].split(",")
                print()
                print("- - -")
                for i in range(5): # quantidade de elementos
                    print(f"{formatacao[i]} {meta[i].strip()}")
                print("- - -")
                print()
                break
            elif opcao == 0:
                print()
                return 0
            else:
                print("Opção inválida")
                print()
                return ""
        except ValueError:
            print("Entrada inválida! Digite um número!")
            print()
            continue
    ## confirmação
    while True:
        try:
            print("(1 - Sim | 0 - Não)")
            confirmacao = int(input(f"Tem certeza que deseja apagar a Meta {opcao}? "))
            print()
            if confirmacao == 1:
                linhas.pop(indiceMeta)

                arquivo = open(f"{pathMeta}/{arquivoMeta}", "w", encoding='utf-8')
                arquivo.write(colunas)
                for i in range(len(linhas)):
                    arquivo.write(linhas[i])
                arquivo.close()
                print("A meta foi deletada!")
                print()
                return ""
            elif confirmacao == 0:
                print("Cancelado!\nA meta não foi deletada!")
                print()
                return ""
            else:
                print("Opção inválida!")
                print()
                continue
        except ValueError:
            print("Entrada inválida! Digite um número!")
            print()
        return True

def barraProgresso(atual, alvo, tipo, tamanho=20):
    # Calcula e exibe a barra de progresso conforme o tipo de meta.
    if tipo == "perder peso":
        # progresso = quanto já perdeu em relação ao quanto quer perder
        # valor_atual vai diminuindo
        progresso = alvo / atual if atual > 0 else 1
        progresso = min(progresso, 1.0)
    else:
        # metas de ganho: progresso = atual / alvo
        progresso = atual / alvo if alvo > 0 else 0
        progresso = min(progresso, 1.0)

    feito = int(progresso * tamanho)
    barra = "█" * feito + "░" * (tamanho - feito) # barrinha do progresso
    return f"[{barra}] {progresso*100:.1f}%"

def atualizarProgressoMeta(pathMeta, arquivoMeta):
    # verificação
    if not os.path.exists(f"{pathMeta}/{arquivoMeta}"):
        print("Nenhuma meta encontrada.")
        print()
        return

    arquivo = open(f"{pathMeta}/{arquivoMeta}", "r", encoding='utf-8')
    colunas = arquivo.readline()
    linhas = arquivo.readlines()
    arquivo.close()

    if not linhas:
        print("Nenhuma meta registrada!")
        print()
        return

    # exibe a lista
    print()
    print("\n--- Suas Metas ---")
    for i, linha in enumerate(linhas, start=1):
        dados = linha.split(",")
        print(f"{i} | {dados[1].strip()} ({dados[0].strip()}) - Atual: {dados[3].strip()} {dados[4].strip()} / Alvo: {dados[2].strip()} {dados[4].strip()}")
    print()

    while True:
        try:
            print(">>> 0 - Sair")
            opcao = int(input("Qual meta deseja atualizar o progresso rápido? "))

            if opcao == 0:
                return
            if 1 <= opcao <= len(linhas):
                indiceMeta = opcao - 1
                dadosMeta = linhas[indiceMeta].strip().split(",")

                tipo = dadosMeta[0].strip()
                descricao = dadosMeta[1].strip()
                valor_alvo = float(dadosMeta[2])
                unidade = dadosMeta[4].strip()

                novo_valor = float(input(f"Digite o NOVO valor atual para '{descricao}' ({unidade}): "))
                if novo_valor < 0:
                    print("O valor não pode ser negativo!")
                    continue

                if tipo == "perder peso" and novo_valor < valor_alvo:
                    print("Parabéns! Esse valor ultrapassa seu objetivo. Meta batida!")
                elif tipo == "ganhar massa" and novo_valor > valor_alvo:
                    print("Parabéns! Esse valor ultrapassa seu objetivo de ganho. Meta batida!")

                print("\n(1 - Confirmar | 0 - Cancelar)")
                conf = int(input("Confirmar atualização rápido? "))
                if conf == 1:
                    dadosMeta[3] = str(novo_valor)
                    linhas[indiceMeta] = ",".join(dadosMeta) + "\n"

                    arquivo = open(f"{pathMeta}/{arquivoMeta}", "w", encoding='utf-8')
                    arquivo.write(colunas)
                    for linha in linhas:
                        arquivo.write(linha)
                    arquivo.close()
                    print("Progresso atualizado com sucesso!\n")
                    return
                else:
                    print("Atualização cancelada.\n")
                    return
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

# ===============================================================
# Seção de Evolução (opção 4)

pathEvolucao = "files/evolucao"
arquivoEvolucao = "registros.csv"
colunasEvolucao = "data,treino,duracao\n"

def inicializarEvolucao():
    os.makedirs(pathEvolucao, exist_ok=True)
    caminho = f"{pathEvolucao}/{arquivoEvolucao}"
    if not os.path.exists(caminho):
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(colunasEvolucao)

def lerRegistros():
    caminho = f"{pathEvolucao}/{arquivoEvolucao}"
    if not os.path.exists(caminho):
        return []
    with open(caminho, "r", encoding="utf-8") as f:
        f.readline()
        linhas = f.readlines()
    registros = []
    for linha in linhas:
        partes = linha.strip().split(",")
        if len(partes) == 3:
            registros.append({
                "data":    partes[0],
                "treino":  partes[1],
                "duracao": float(partes[2])
            })
    return registros

def salvarRegistro(data, treino, duracao):
    inicializarEvolucao()
    caminho = f"{pathEvolucao}/{arquivoEvolucao}"
    with open(caminho, "a", encoding="utf-8") as f:
        f.write(f"{data},{treino},{duracao}\n")

def lerTreinos():
    caminho = f"{pathTreinos}/{arquivoTreinos}"
    if not os.path.exists(caminho):
        return []
    with open(caminho, "r", encoding="utf-8") as f:
        f.readline()
        linhas = f.readlines()
    treinos = []
    for linha in linhas:
        partes = linha.strip().split(",")
        if len(partes) >= 3:
            treinos.append({"nome": partes[0], "duracao": partes[2]})
    return treinos

def registrarTreino():
    from datetime import datetime
    print("\n  - Registrar treino realizado -")
    try:
        data_input = input("  Data (dd/mm/aaaa) ou Enter para hoje: ").strip()
        if data_input == "":
            data = datetime.today().strftime("%d/%m/%Y")
        else:
            datetime.strptime(data_input, "%d/%m/%Y")
            data = data_input

        treinos = lerTreinos()
        nome_treino = ""
        duracao = None

        if treinos:
            print("\n  Treinos cadastrados:")
            for i, t in enumerate(treinos, 1):
                print(f"  {i} | {t['nome']} ({t['duracao']} min)")
            print("  0 | Digitar nome manualmente")
            print()
            opcao = int(input("  Selecione o treino realizado: "))
            if opcao > 0 and opcao <= len(treinos):
                nome_treino = treinos[opcao - 1]["nome"]
                usar_duracao = input(f"  Usar duração padrão ({treinos[opcao-1]['duracao']} min)? [Enter = sim / outro valor]: ").strip()
                if usar_duracao == "":
                    duracao = float(treinos[opcao - 1]["duracao"])
                else:
                    duracao = float(usar_duracao)
            elif opcao == 0:
                nome_treino = input("  Nome do treino: ").capitalize()
            else:
                print("  Opção inválida.")
                return
        else:
            nome_treino = input("  Nome do treino realizado: ").capitalize()

        if duracao is None:
            duracao = float(input("  Duração (em minutos): "))

        salvarRegistro(data, nome_treino, duracao)
        print(f"\n  Treino '{nome_treino}' registrado em {data}!")
    except ValueError:
        print("  Entrada inválida. Tente novamente.")

def calcularFrequenciaSemanal(registros):
    """Retorna um dicionário {semana: quantidade_de_treinos}"""
    from datetime import datetime
    semanas = {}
    for r in registros:
        try:
            data = datetime.strptime(r["data"], "%d/%m/%Y")
            # semana no formato "Semana XX/AAAA"
            chave = f"Sem. {data.isocalendar()[1]:02d}/{data.year}"
            semanas[chave] = semanas.get(chave, 0) + 1
        except ValueError:
            continue
    return semanas

def verEvolucao():
    inicializarEvolucao()
    registros = lerRegistros()

    # ler metas diretamente do CSV (padrão Treinos)
    caminhoMetas = f"{pathMetas}/{arquivoMetas}"
    metas = []
    if os.path.exists(caminhoMetas):
        with open(caminhoMetas, "r", encoding='utf-8') as f:
            f.readline()  # pula cabeçalho
            for linha in f.readlines():
                partes = linha.strip().split(",")
                if len(partes) == 5:
                    metas.append({
                        "tipo":        partes[0],
                        "descricao":   partes[1],
                        "valor_alvo":  float(partes[2]),
                        "valor_atual": float(partes[3]),
                        "unidade":     partes[4]
                    })

    print(f"\n  {'='*40}")
    print("  EVOLUÇÃO")
    print(f"  {'='*40}")

    # Treinos realizados
    total = len(registros)
    print(f"\n  Total de treinos realizados: {total}")

    if registros:
        duracao_total = sum(r["duracao"] for r in registros)
        duracao_media = duracao_total / total
        print(f"  Duração total:  {duracao_total:.0f} min ({duracao_total/60:.1f} h)")
        print(f"  Duração média:  {duracao_media:.1f} min por treino")

        # Frequência semanal
        semanas = calcularFrequenciaSemanal(registros)
        if semanas:
            print(f"\n  Frequência semanal:")
            for semana, qtd in sorted(semanas.items()):
                barra = "█" * qtd
                print(f"    {semana}: {barra} ({qtd} treino{'s' if qtd > 1 else ''})")
            media_semanal = total / len(semanas)
            print(f"\n  Média: {media_semanal:.1f} treinos/semana")

        # Últimos 5 treinos
        print(f"\n  Últimos treinos:")
        for r in registros[-5:][::-1]:
            print(f"    {r['data']} | {r['treino']} | {r['duracao']:.0f} min")
    else:
        print("  Nenhum treino registrado ainda.")

    # Progresso nas metas
    if metas:
        print(f"\n  {'='*40}")
        print("  PROGRESSO NAS METAS")
        print(f"  {'='*40}")
        for i, m in enumerate(metas):
            print(f"\n  Meta {i+1}: {m['descricao']}")
            print(f"  {barraProgresso(m['valor_atual'], m['valor_alvo'], m['tipo'])}")
            print(f"  Atual: {m['valor_atual']} {m['unidade']} / Alvo: {m['valor_alvo']} {m['unidade']}")
    else:
        print("\n  Nenhuma meta cadastrada.")

    print()

def excluirRegistro():
    inicializarEvolucao()
    registros = lerRegistros()
    if not registros:
        print("  Nenhum treino registrado.")
        return

    print("\n  - Excluir registro de treino -")
    for i, r in enumerate(registros, 1):
        print(f"  {i} | {r['data']} | {r['treino']} | {r['duracao']:.0f} min")
    print("  0 | Voltar")
    print()
    try:
        opcao = int(input("  Qual registro deseja excluir? "))
        if opcao == 0:
            return
        if opcao < 1 or opcao > len(registros):
            print("  Opção inválida.")
            return

        r = registros[opcao - 1]
        print(f"\n  Tem certeza que deseja excluir '{r['treino']}' ({r['data']})?")
        print("  1 - Sim | 0 - Não")
        confirma = int(input("  [1/0]: "))
        if confirma == 1:
            registros.pop(opcao - 1)
            caminho = f"{pathEvolucao}/{arquivoEvolucao}"
            with open(caminho, "w", encoding="utf-8") as f:
                f.write(colunasEvolucao)
                for reg in registros:
                    f.write(f"{reg['data']},{reg['treino']},{reg['duracao']}\n")
            print("  Registro excluído!")
        else:
            print("  Cancelado.")
    except ValueError:
        print("  Entrada inválida.")

def menuEvolucao():
    while True:
        print("\n  - - - - EVOLUÇÃO - - - -")
        print("  1 - Ver evolução geral")
        print("  2 - Registrar treino realizado")
        print("  3 - Excluir registro")
        print("  0 - Voltar")
        print()
        try:
            opcao = int(input("  > > Opção: "))
            if opcao == 1:
                verEvolucao()
            elif opcao == 2:
                registrarTreino()
            elif opcao == 3:
                excluirRegistro()
            elif opcao == 0:
                break
            else:
                print("  Opção inválida.")
        except ValueError:
            print("  Opção inválida.")


# ===============================================================
# Seção de Sugestões Personalizadas (opção 5)

def menuSugestoes():
    while True:
        print("\n  - - - - SUGESTÕES - - - -")
        print("  1 - Sugestão de treino semanal")
        print("  2 - Sugestão de exercícios por objetivo")
        print("  3 - Dicas de descanso e recuperação")
        print("  4 - Dicas de alimentação")
        print("  0 - Voltar")
        print()
        try:
            opcao = int(input("  > > Opção: "))
            if opcao == 1:
                sugerirDivisaoSemanal()
            elif opcao == 2:
                sugerirExercicios()
            elif opcao == 3:
                dicasDescanso()
            elif opcao == 4:
                dicasAlimentacao()
            elif opcao == 0:
                break
            else:
                print("  Opção inválida.")
        except ValueError:
            print("  Opção inválida.")

def sugerirDivisaoSemanal():
    print("\n  - Sugestão de divisão semanal -")
    print("  Qual é o seu objetivo principal?")
    print("  1 - Perder peso / emagrecer")
    print("  2 - Ganhar massa muscular")
    print("  3 - Melhorar condicionamento físico")
    print("  4 - Manter saúde em geral")
    try:
        opcao = int(input("  > Opção: "))
    except ValueError:
        print("  Opção inválida.")
        return

    print("\n  Quantos dias por semana você pode treinar?")
    print("  1 - 2 dias   2 - 3 dias   3 - 4 dias   4 - 5+ dias")
    try:
        dias_opcao = int(input("  > Opção: "))
    except ValueError:
        print("  Opção inválida.")
        return

    planos = {
        # (objetivo, dias): plano
        (1, 1): [
            ("Seg", "Cardio + Força (corpo todo)"),
            ("Qua", "Descanso ativo / Caminhada"),
            ("Sex", "Cardio + Força (corpo todo)"),
        ],
        (1, 2): [
            ("Seg", "Cardio moderado (30-40 min)"),
            ("Ter", "Força: parte superior"),
            ("Qui", "Cardio intenso (HIIT 20 min)"),
            ("Sex", "Força: parte inferior"),
            ("Sáb", "Flexibilidade / alongamento"),
        ],
        (1, 3): [
            ("Seg", "Força: peito e tríceps"),
            ("Ter", "Cardio (corrida 30 min)"),
            ("Qua", "Força: costas e bíceps"),
            ("Qui", "Cardio (HIIT 20 min)"),
            ("Sex", "Força: pernas e ombros"),
            ("Sáb", "Flexibilidade + core"),
        ],
        (1, 4): [
            ("Seg", "Cardio + Força (corpo todo)"),
            ("Ter", "Cardio moderado"),
            ("Qua", "Força: parte superior"),
            ("Qui", "Cardio + core"),
            ("Sex", "Força: parte inferior"),
            ("Sáb", "Flexibilidade / alongamento"),
        ],
        (2, 1): [
            ("Seg", "Força: corpo todo (compostos)"),
            ("Qua", "Descanso ativo"),
            ("Sex", "Força: corpo todo (isolados)"),
        ],
        (2, 2): [
            ("Seg", "Força: peito e tríceps"),
            ("Qua", "Força: costas e bíceps"),
            ("Sex", "Força: pernas e ombros"),
        ],
        (2, 3): [
            ("Seg", "Força: peito e tríceps"),
            ("Ter", "Força: costas e bíceps"),
            ("Qui", "Força: pernas"),
            ("Sex", "Força: ombros e core"),
        ],
        (2, 4): [
            ("Seg", "Força: peito e tríceps"),
            ("Ter", "Força: costas e bíceps"),
            ("Qua", "Descanso ativo"),
            ("Qui", "Força: pernas"),
            ("Sex", "Força: ombros"),
            ("Sáb", "Core + flexibilidade"),
        ],
        (3, 1): [
            ("Ter", "Cardio moderado (40 min)"),
            ("Qui", "Descanso ativo"),
            ("Sáb", "Cardio + força leve"),
        ],
        (3, 2): [
            ("Seg", "Cardio longo (corrida 40 min)"),
            ("Qua", "Força funcional + core"),
            ("Sex", "Cardio intervalado (HIIT)"),
        ],
        (3, 3): [
            ("Seg", "Cardio (corrida 40 min)"),
            ("Ter", "Força funcional"),
            ("Qui", "Cardio (ciclismo ou natação)"),
            ("Sex", "Força + core"),
        ],
        (3, 4): [
            ("Seg", "Corrida 5 km"),
            ("Ter", "Força: corpo todo"),
            ("Qua", "Cardio leve (caminhada 45 min)"),
            ("Qui", "Força: core e funcional"),
            ("Sex", "Cardio intenso (HIIT)"),
            ("Sáb", "Flexibilidade + recuperação"),
        ],
        (4, 1): [
            ("Ter", "Caminhada/corrida 30 min + alongamento"),
            ("Qui", "Força leve: corpo todo"),
            ("Sáb", "Atividade ao ar livre (bike, natação)"),
        ],
        (4, 2): [
            ("Seg", "Força: parte superior"),
            ("Qua", "Cardio moderado (30 min)"),
            ("Sex", "Força: parte inferior + core"),
        ],
        (4, 3): [
            ("Seg", "Força: corpo todo"),
            ("Ter", "Cardio (30 min)"),
            ("Qui", "Força: core e funcional"),
            ("Sex", "Cardio + flexibilidade"),
        ],
        (4, 4): [
            ("Seg", "Força: parte superior"),
            ("Ter", "Cardio moderado"),
            ("Qua", "Força: parte inferior"),
            ("Qui", "Cardio leve + core"),
            ("Sex", "Força: corpo todo"),
            ("Sáb", "Flexibilidade + alongamento"),
        ],
    }

    chave = (opcao, dias_opcao)
    plano = planos.get(chave)

    objetivos = {1: "Perder peso", 2: "Ganhar massa", 3: "Condicionamento", 4: "Saúde geral"}
    dias_str = {1: "2 dias", 2: "3-4 dias (ABC)", 3: "4 dias", 4: "5-6 dias"}

    print(f"\n  {'='*40}")
    print(f"  Objetivo: {objetivos.get(opcao, '?')} | {dias_str.get(dias_opcao, '?')}")
    print(f"  {'='*40}")

    if plano:
        for dia, atividade in plano:
            print(f"    {dia:<5}: {atividade}")
        print(f"\n  Dias de descanso: não listados acima.")
    else:
        print("  Sugestão não encontrada para essa combinação.")
    print()

def sugerirExercicios():
    print("\n  - Sugestão de exercícios por objetivo -")
    print("  Qual grupo muscular / objetivo?")
    print("  1 - Cardio / emagrecimento")
    print("  2 - Força: parte superior")
    print("  3 - Força: parte inferior")
    print("  4 - Core e equilíbrio")
    print("  5 - Flexibilidade e mobilidade")
    try:
        opcao = int(input("  > Opção: "))
    except ValueError:
        print("  Opção inválida.")
        return

    sugestoes = {
        1: [
            "Corrida (20-40 min, ritmo moderado)",
            "HIIT: 20 min (30s esforço / 30s descanso)",
            "Pular corda: 3 séries de 3 min",
            "Ciclismo: 45 min em ritmo constante",
            "Caminhada acelerada: 45 min",
            "Burpees: 4 séries de 10 repetições",
        ],
        2: [
            "Supino reto: 4x10",
            "Remada curvada: 4x10",
            "Desenvolvimento de ombros: 3x12",
            "Rosca direta (bíceps): 3x12",
            "Tríceps pulley: 3x12",
            "Flexão de braço: 3x15",
        ],
        3: [
            "Agachamento livre: 4x10",
            "Leg press: 4x12",
            "Afundo (passada): 3x12 cada perna",
            "Stiff (posterior de coxa): 3x12",
            "Elevação de panturrilha: 4x15",
            "Agachamento sumô: 3x12",
        ],
        4: [
            "Prancha frontal: 3x30-60s",
            "Abdominal remador: 3x15",
            "Bird-dog: 3x10 cada lado",
            "Dead bug: 3x10",
            "Prancha lateral: 3x20s cada lado",
            "Equilíbrio em uma perna: 3x30s cada lado",
        ],
        5: [
            "Alongamento de isquiotibiais: 3x30s cada perna",
            "Postura da criança (yoga): 3x30s",
            "Rotação de quadril: 2x10 cada lado",
            "Mobilidade de ombros com bastão: 3x10",
            "Alongamento de psoas: 3x30s cada lado",
            "Gato-vaca (mobilidade de coluna): 3x10",
        ],
    }

    titulos = {1: "Cardio", 2: "Força - Superior", 3: "Força - Inferior", 4: "Core e Equilíbrio", 5: "Flexibilidade"}
    lista = sugestoes.get(opcao)

    if lista:
        print(f"\n  Exercícios sugeridos — {titulos[opcao]}:")
        for i, ex in enumerate(lista, 1):
            print(f"    {i}. {ex}")
    else:
        print("  Opção inválida.")
    print()

def dicasDescanso():
    print(f"\n  {'='*40}")
    print("  DICAS DE DESCANSO E RECUPERAÇÃO")
    print(f"  {'='*40}")
    dicas = [
        ("Sono", "Durma entre 7 e 9 horas por noite. O músculo cresce durante o repouso."),
        ("Descanso ativo", "Nos dias de folga, prefira caminhadas leves ou alongamento no lugar de ficar completamente parado."),
        ("Grupos musculares", "Evite treinar o mesmo grupo muscular em dias consecutivos. Dê ao menos 48h de descanso."),
        ("Hidratação", "Beba pelo menos 35 ml de água por kg de peso corporal ao dia (ex: 70 kg → ~2,5 litros)."),
        ("Alongamento pós-treino", "Sempre alongue os músculos trabalhados por 5-10 minutos ao final do treino."),
        ("Semana de deload", "A cada 4-6 semanas, reduza a intensidade dos treinos em ~50% por uma semana para recuperação profunda."),
        ("Sinais de excesso", "Dor persistente, queda de desempenho e cansaço extremo são sinais de overtraining — descanse mais."),
    ]
    for titulo, dica in dicas:
        print(f"\n  • {titulo}:")
        print(f"    {dica}")
    print()

def dicasAlimentacao():
    print(f"\n  {'='*40}")
    print("  DICAS DE ALIMENTAÇÃO")
    print(f"  {'='*40}")

    print("\n  Qual o seu objetivo?")
    print("  1 - Perder peso")
    print("  2 - Ganhar massa muscular")
    print("  3 - Saúde geral")
    try:
        opcao = int(input("  > Opção: "))
    except ValueError:
        print("  Opção inválida.")
        return

    dicas = {
        1: [
            ("Déficit calórico", "Consuma ~300-500 kcal a menos do que seu gasto diário. Evite cortes extremos."),
            ("Proteína", "Mantenha a ingestão de proteínas alta (1,8-2,2 g/kg). Preserva a massa muscular."),
            ("Carboidratos", "Prefira carboidratos complexos (aveia, batata-doce, arroz integral). Evite açúcar simples."),
            ("Refeições", "Faça 4-5 refeições ao dia em horários regulares para controlar a fome."),
            ("Alimentos a evitar", "Refrigerantes, fast food, frituras e ultraprocessados dificultam a perda de peso."),
        ],
        2: [
            ("Superávit calórico", "Consuma ~200-400 kcal a mais do que seu gasto diário para criar massa."),
            ("Proteína", "Ingira 2,0-2,5 g de proteína por kg corporal. Priorize frango, ovos, atum e leguminosas."),
            ("Pré-treino", "Consuma carboidratos + proteína 1-2h antes do treino (ex: arroz + frango)."),
            ("Pós-treino", "Logo após o treino, ingira proteína de rápida absorção (ex: whey, ovos, atum)."),
            ("Carboidratos", "Carboidratos são aliados: fornecem energia para treinar pesado. Não os elimine."),
        ],
        3: [
            ("Variedade", "Inclua todos os grupos alimentares: proteínas, carboidratos, gorduras boas, fibras e vitaminas."),
            ("Água", "Hidrate-se bem ao longo do dia, especialmente antes, durante e após exercícios."),
            ("Frutas e vegetais", "Consuma pelo menos 5 porções de frutas e vegetais por dia."),
            ("Gorduras boas", "Inclua abacate, azeite, castanhas e peixes na dieta. São essenciais para o organismo."),
            ("Processados", "Reduza o consumo de alimentos ultraprocessados, embutidos e fast food."),
        ],
    }

    titulos = {1: "Perda de peso", 2: "Ganho de massa", 3: "Saúde geral"}
    lista = dicas.get(opcao)

    if lista:
        print(f"\n  Dicas para: {titulos[opcao]}")
        for titulo, dica in lista:
            print(f"\n  • {titulo}:")
            print(f"    {dica}")
    else:
        print("  Opção inválida.")
    print()

def excluirMeta():
    metas = lerMetas()
    if not metas:
        print("  Nenhuma meta cadastrada.")
        return
 
    print("\n  - Excluir meta -")
    for i, m in enumerate(metas):
        print(f"  {i+1} | {m['descricao']} ({m['tipo']})")
 
    try:
        opcao = int(input("\n  Qual meta deseja excluir? (0 para voltar): "))
        if opcao == 0:
            return
        if opcao < 1 or opcao > len(metas):
            print("  Opção inválida.")
            return
 
        meta_removida = metas[opcao - 1]
        print(f"\n  Tem certeza que deseja excluir '{meta_removida['descricao']}'?")
        print("  1 - Sim | 0 - Não")
        confirma = int(input("  [1/0]: "))
 
        if confirma == 1:
            metas.pop(opcao - 1)
            salvarMetas(metas)
            print("  Meta excluída com sucesso!")
        else:
            print("  Cancelado!")
 
    except ValueError:
        print("  Entrada inválida.")

# ===============================================================
# Seção IMC (opção 6)

def calcularIMC():
    print(f"\n  {'='*40}")
    print("  CALCULADORA DE IMC")
    print(f"  {'='*40}")
    try:
        peso = float(input("\n  Seu peso atual (kg): "))
        altura = float(input("  Sua altura (ex: 1.75): "))
        if peso <= 0 or altura <= 0:
            print("  Valores inválidos.")
            return

        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
            dica = "Considere aumentar a ingestão calórica com alimentos nutritivos."
        elif imc < 25.0:
            classificacao = "Peso normal"
            dica = "Parabéns! Mantenha hábitos saudáveis de exercício e alimentação."
        elif imc < 30.0:
            classificacao = "Sobrepeso"
            dica = "Atividade física regular e dieta equilibrada podem ajudar."
        elif imc < 35.0:
            classificacao = "Obesidade grau I"
            dica = "Recomenda-se acompanhamento médico e atividade física regular."
        elif imc < 40.0:
            classificacao = "Obesidade grau II"
            dica = "Busque orientação médica e nutricional."
        else:
            classificacao = "Obesidade grau III"
            dica = "Procure acompanhamento médico especializado."

        print(f"\n  IMC calculado: {imc:.2f}")
        print(f"  Classificação: {classificacao}")
        print(f"\n  Tabela de referência (OMS):")
        faixas = [
            ("< 18.5",      "Abaixo do peso"),
            ("18.5 – 24.9", "Peso normal    "),
            ("25.0 – 29.9", "Sobrepeso      "),
            ("30.0 – 34.9", "Obesidade I    "),
            ("35.0 – 39.9", "Obesidade II   "),
            (">= 40.0",     "Obesidade III  "),
        ]
        for faixa, nome in faixas:
            marcador = " <<" if nome.strip().lower() in classificacao.lower() else "   "
            print(f"    {faixa:<14} {nome}{marcador}")
        print(f"\n  Dica: {dica}")
    except ValueError:
        print("  Entrada inválida. Use ponto como separador decimal (ex: 1.75).")
    print()


# ===============================================================
# Seção Reset (opção 7)

def resetarDados():
    print(f"\n  {'='*40}")
    print("  RESETAR TODOS OS DADOS")
    print(f"  {'='*40}")
    print("\n  ATENÇÃO: esta ação apaga permanentemente:")
    print("    - Todos os treinos")
    print("    - Todos os exercícios de todas as categorias")
    print("    - Todas as metas")
    print("    - Todo o histórico de evolução")
    print("\n  Essa ação NÃO pode ser desfeita!")
    print()
    try:
        confirmacao1 = input("  Digite RESETAR para confirmar (ou Enter para cancelar): ").strip()
        if confirmacao1.upper() != "RESETAR":
            return

        confirma2 = int(input("  Tem absoluta certeza? (1 - Sim | 0 - Não): "))
        if confirma2 != 1:
            print("  Cancelado. Nenhum dado foi apagado.")
            return

        # Apagar treinos
        caminho_treinos = f"{pathTreinos}/{arquivoTreinos}"
        if os.path.exists(caminho_treinos):
            with open(caminho_treinos, "w", encoding="utf-8") as f:
                f.write("nome,tipo,duracao,objetivo,observacao,exercicios\n")

        # Apagar exercícios
        for cat in ["cardio.txt", "forca.txt", "flexibilidade.txt", "equilibrio.txt"]:
            caminho_cat = f"{pathExercicios}/{cat}"
            if os.path.exists(caminho_cat):
                open(caminho_cat, "w", encoding="utf-8").close()

        # Apagar metas
        caminho_metas = f"{pathMetas}/{arquivoMetas}"
        if os.path.exists(caminho_metas):
            with open(caminho_metas, "w", encoding="utf-8") as f:
                f.write(colunasMetas)

        # Apagar evolução
        caminho_evolucao = f"{pathEvolucao}/{arquivoEvolucao}"
        if os.path.exists(caminho_evolucao):
            with open(caminho_evolucao, "w", encoding="utf-8") as f:
                f.write(colunasEvolucao)

        print("\n  Todos os dados foram apagados. O sistema foi resetado.")
    except ValueError:
        print(" Entrada inválida. Reset cancelado.")
    print()
