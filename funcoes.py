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
    barra = "█" * feito + "░" * (tamanho - feito) # barrinha do progresso
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
    metas = lerMetas()

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