import os

# inicializar arquivos

# variáveis de treino
pathTreinos = "files/treinos"
pathExercicios = "files/exercicios"
arquivoTreinos = "treinos.csv"

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

# Seção controle de metas  ============================================

# variáveis metas
pathMetas = "files/metas"
arquivoMetas = "metas.csv"
colunasMetas = "tipo,descricao,valor_alvo,valor_atual,unidade\n"

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
    barra = "█" * feito + "░" * (tamanho - feito)
    return f"[{barra}] {progresso*100:.1f}%"

# manipulação e inputs
 
def exibirMeta(i, m):
    print(f"\n  Meta {i+1}")
    print(f"  Tipo:      {m['tipo'].capitalize()}")
    print(f"  Descrição: {m['descricao']}")
    print(f"  Alvo:      {m['valor_alvo']} {m['unidade']}")
    print(f"  Atual:     {m['valor_atual']} {m['unidade']}")
    print(f"  Progresso: {barraProgresso(m['valor_atual'], m['valor_alvo'], m['tipo'])}")
 
def menuTipoMeta():
    print("  Tipo de meta:")
    print("  1 - Perder peso")
    print("  2 - Ganhar massa muscular")
    print("  3 - Melhorar condicionamento físico")
    print("  4 - Outro")
    opcao = int(input("  > Opção: "))
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
# Parte de Pedro

def viewGoals():
    metas = lerMetas()
    if not metas:
        print("  Nenhuma meta cadastrada.")
        return
    print(f"\n  {'='*40}")
    print("  SUAS METAS")
    print(f"  {'='*40}")
    for i, m in enumerate(metas):
        exibirMeta(i, m)
    print()
 
def addGoal():
    print("\n  - Adicionar nova meta -")
    try:
        tipo, unidade_padrao = menuTipoMeta()
        descricao = input("  Descrição da meta: ").capitalize()
        valor_alvo = float(input(f"  Valor alvo ({unidade_padrao if unidade_padrao else 'unidade'}): "))
        valor_atual = float(input(f"  Valor atual ({unidade_padrao if unidade_padrao else 'unidade'}): "))
 
        if not unidade_padrao:
            unidade = input("  Unidade (ex: kg, km, min): ")
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
        print("\n  Meta adicionada com sucesso!")
        exibirMeta(len(metas)-1, nova_meta)
 
    except ValueError:
        print("  Entrada inválida. Tente novamente.")
 
def editGoal():
    metas = lerMetas()
    if not metas:
        print("  Nenhuma meta cadastrada.")
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
 
def removeGoal():
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
