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
        # print("6 - API TEST")
        # print("7 - Configurações") // deletar tudo
        print("0 - Sair")
        print()
        opcao = int(input("Insira a opção desejada: "))
        if opcao < 0 or opcao > 5:
            print("Opção inválida")
        print()
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
            print("Entrada inválida!")
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

    arquivo = open(f"{path}/{file}", "r", encoding='utf-8')
    colunas = arquivo.readline()
    linhas = arquivo.readlines()
    arquivo.close()

    try:
        print(">>> 0 - Sair")
        opcao = int(input("Qual treino deseja visualizar? "))
        if opcao <= len(linhas) and opcao > 0:
            treino = linhas[opcao-1].strip().split(",")
            print()
            print("- - - - - -")
            print(f"- Treino {opcao} -")
            for i in range(len(formatacao)): # quantidade de elementos
                print(f"{formatacao[i]} {treino[i].strip()}")
            print()
        elif opcao == 0:
            return "break"
        else:
            print()
            print("Treino não encontrado!")
            print()
            return ""
    except ValueError:
        print()
        print("Entrada inválida.")
        print()
        return ""


    ## imprimir exercicios
    exerciciosTreino = treino[5]
    if exerciciosTreino != "":
        listaExercicios = exerciciosTreino.split("|")
        # print
        print("Exercícios:")
        for exercicio in listaExercicios:
            print(f"> {exercicio}")
    else:
        print("Sem exercícios cadastrados.")
    print("- - - - - -")
    print()

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
                        print("Entrada inválida!")
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
            print("Entrada inválida!")    
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
            print("Entrada inválida!")
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
            print("Entrada inválida!")
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
            print("Entrada inválida!")
            print()
        return True
    else: 
        print("Sem exercícios cadastrados")
        return False

# Seção controle de metas  ============================================

# variáveis metas
pathMetas = "files/metas"
arquivoMetas = "metas.csv"
colunasMetas = "tipo,descricao,valorAlvo,valorAtual,unidade\n"

# Inicializar arquivos
def inicializarMetas():
    os.makedirs(pathMetas, exist_ok=True)
    caminho = f"{pathMetas}/{arquivoMetas}"
    if not os.path.exists(caminho):
        with open(caminho, "w", encoding='utf-8') as f:
            f.write(colunasMetas)

# ======================================================================

def lerMetas():
    caminho = f"{pathMetas}/{arquivoMetas}"
    if not os.path.exists(caminho):
        return []
    with open(caminho, "r", encoding='utf-8') as f:
        f.readline()  # pula o cabeçalho
        linhas = f.readlines()
    metas = []
    for linha in linhas:
        partes = linha.strip().split(",")
        if len(partes) == 5:
            metas.append({
                "tipo":        partes[0],
                "descricao":   partes[1],
                "valor_alvo":  float(partes[2]),
                "valor_atual": float(partes[3]),
                "unidade":     partes[4]
            })
    return metas
 
def salvarMetas(metas):
    caminho = f"{pathMetas}/{arquivoMetas}"
    with open(caminho, "w", encoding='utf-8') as f:
        f.write(colunasMetas)
        for m in metas:
            linha = f"{m['tipo']},{m['descricao']},{m['valor_alvo']},{m['valor_atual']},{m['unidade']}\n"
            f.write(linha)

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

# manipulação e inputs
 
def exibirMeta(i, dicionario):
    print(f"\n  Meta {i+1}")
    print(f"  Tipo:      {dicionario['tipo'].capitalize()}")
    print(f"  Descrição: {dicionario['descricao']}")
    print(f"  Alvo:      {dicionario['valor_alvo']} {dicionario['unidade']}")
    print(f"  Atual:     {dicionario['valor_atual']} {dicionario['unidade']}")
    print(f"  Progresso: {barraProgresso(dicionario['valor_atual'], dicionario['valor_alvo'], dicionario['tipo'])}")
 
def menuTipoMeta():
    print(" Tipo de meta:")
    print(" 1 - Perder peso")
    print(" 2 - Ganhar massa muscular")
    print(" 3 - Melhorar condicionamento físico")
    print(" 4 - Outro")
    opcao = int(input("> Opção: "))
    print()
    tipos = {
        1: ("perder peso", "kg"),
        2: ("ganhar massa", "kg"),
        3: ("condicionamento", "treinos"),
        4: ("outro", "")
    }
    if opcao in tipos:
        return tipos[opcao]
    return ("outro", "")

# ===============================================================
# REVISAR

def visualizarMetas():
    metas = lerMetas()
    if not metas:
        print("Nenhuma meta cadastrada.")
        return
    print(f"\n  {'='*40}")
    print("  SUAS METAS")
    print(f"  {'='*40}")
    for i, m in enumerate(metas):
        exibirMeta(i, m)
    print()
 
def adicionarMeta():
    print("\n  - Adicionar nova meta -")
    print()
    try:
        tipo, unidade_padrao = menuTipoMeta()
        descricao = input("  Descrição da meta: ").capitalize()
        valor_alvo = float(input(f"  Valor alvo ({unidade_padrao if unidade_padrao else 'unidade'}): "))
        valor_atual = float(input(f"  Valor atual ({unidade_padrao if unidade_padrao else 'unidade'}): "))
        print()
        if tipo == "perder peso":
            if valor_atual < valor_alvo:
                print("  Valores incorretos.")
                print()
                return ""
        elif tipo == "ganhar massa":
            if valor_atual > valor_alvo:
                print("  Valores incorretos.")
                print()
                return ""

        if not unidade_padrao:
            unidade = input("Unidade (ex: kg, km, min): ")
        else:
            unidade = unidade_padrao
 
        nova_meta = {
            "tipo":        tipo,
            "descricao":   descricao,
            "valor_alvo":  valor_alvo,
            "valor_atual": valor_atual,
            "unidade":     unidade
        }
 
        metas = lerMetas()
        metas.append(nova_meta)
        salvarMetas(metas)
        print("\nMeta adicionada com sucesso!")
        exibirMeta(len(metas)-1, nova_meta)
 
    except ValueError:
        print()
        print("Entrada inválida. Tente novamente.")
        print()
def editarMeta():
    metas = lerMetas()
    if not metas:
        print("Nenhuma meta cadastrada.")
        return
 
    print("\n  - Editar meta - ")
    for i, m in enumerate(metas):
        exibirMeta(i, m)
 
    try:
        opcao = int(input("\n  Qual meta deseja editar? (0 para voltar): "))
        if opcao == 0:
            return
        if opcao < 1 or opcao > len(metas):
            print("  Opção inválida.")
            return
 
        m = metas[opcao - 1]
        print(f"\n  Editando: {m['descricao']}")
        print("  1 - Atualizar valor atual (registrar progresso)")
        print("  2 - Editar valor alvo")
        print("  3 - Editar descrição")
        print("  0 - Voltar")
 
        sub = int(input("  > Opção: "))
 
        if sub == 1:
            novo = float(input(f"  Novo valor atual ({m['unidade']}): "))
            metas[opcao - 1]["valor_atual"] = novo
            salvarMetas(metas)
            print("\n  Progresso atualizado!")
            exibirMeta(opcao - 1, metas[opcao - 1])
 
        elif sub == 2:
            novo = float(input(f"  Novo valor alvo ({m['unidade']}): "))
            metas[opcao - 1]["valor_alvo"] = novo
            salvarMetas(metas)
            print("  Valor alvo atualizado!")
 
        elif sub == 3:
            nova = input("  Nova descrição: ").capitalize()
            metas[opcao - 1]["descricao"] = nova
            salvarMetas(metas)
            print("  Descrição atualizada!")
 
    except ValueError:
        print("  Entrada inválida.")
 
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
