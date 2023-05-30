class Candidato:
    def __init__(self, nome, numero, partido, cargo):
        self.nome = nome
        self.numero = numero
        self.partido = partido
        self.cargo = cargo
        self.votos = 0

class Eleitor:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

def cadastrar_candidatos():
    candidatos_presidente = []
    candidatos_governador = []
    candidatos_prefeito = []

    while True:
        print("\nCadastro de Candidatos")
        nome = input("Digite o nome do candidato: ")
        numero = input("Digite o número do candidato: ")
        partido = input("Digite o partido do candidato: ")
        cargo = input("Digite o cargo que o candidato disputa: ")

        candidato = Candidato(nome, numero, partido, cargo)

        if cargo.lower() == "presidente":
            candidatos_presidente.append(candidato)
        elif cargo.lower() == "governador":
            candidatos_governador.append(candidato)
        elif cargo.lower() == "prefeito":
            candidatos_prefeito.append(candidato)
        else:
            print("Cargo inválido!")

        opcao = input("Deseja cadastrar outro candidato? (Digite SIM ou NÃO): ")
        if opcao.lower() == "nao" or opcao.lower() == "não":
            break

    return candidatos_presidente, candidatos_governador, candidatos_prefeito

def cadastrar_eleitores():
    eleitores = []

    while True:
        print("\nCadastro de Eleitores")
        nome = input("Digite o nome do eleitor: ")
        cpf = input("Digite o CPF do eleitor: ")

        eleitor = Eleitor(nome, cpf)
        eleitores.append(eleitor)

        opcao = input("Deseja cadastrar outro eleitor? (Digite SIM ou NÃO): ")
        if opcao.lower() == "nao" or opcao.lower() == "não":
            break

    return eleitores

def confirmar_voto(candidato):
    print("\nConfirmação de Voto:")
    print(f"Nome: {candidato.nome}")
    print(f"Partido: {candidato.partido}")
    opcao = input("Confirma o voto? (Digite SIM ou NÃO): ")

    return opcao.lower() == "sim"

def registrar_voto(candidato):
    candidato.votos += 1

def exibir_opcoes(candidatos):
    for candidato in candidatos:
        print(f"Número: {candidato.numero}")
        print(f"Nome: {candidato.nome}")
        print(f"Partido: {candidato.partido}")

def votar(candidatos_prefeito, candidatos_governador, candidatos_presidente, eleitores):
    print("\nVotação para Prefeito:")
    exibir_opcoes(candidatos_prefeito)
    voto_prefeito = input("Digite o número do candidato ou -1 para voto branco, -2 para voto nulo: ")
    if voto_prefeito == "-1":
        print("Voto branco confirmado!")
    elif voto_prefeito == "-2":
        print("Voto nulo confirmado!")
    else:
        candidato = next((c for c in candidatos_prefeito if c.numero == voto_prefeito), None)
        if candidato:
            if confirmar_voto(candidato):
                registrar_voto(candidato)
                print("Voto registrado com sucesso!")
            else:
                print("Voto cancelado!")
        else:
            print("Candidato não encontrado!")

    print("\nVotação para Governador:")
    exibir_opcoes(candidatos_governador)
    voto_governador = input("Digite o número do candidato ou -1 para voto branco, -2 para voto nulo: ")
    if voto_governador == "-1":
        print("Voto branco confirmado!")
    elif voto_governador == "-2":
        print("Voto nulo confirmado!")
    else:
        candidato = next((c for c in candidatos_governador if c.numero == voto_governador), None)
        if candidato:
            if confirmar_voto(candidato):
                registrar_voto(candidato)
                print("Voto registrado com sucesso!")
            else:
                print("Voto cancelado!")
        else:
            print("Candidato não encontrado!")

    print("\nVotação para Presidente:")
    exibir_opcoes(candidatos_presidente)
    voto_presidente = input("Digite o número do candidato ou -1 para voto branco, -2 para voto nulo: ")
    if voto_presidente == "-1":
        print("Voto branco confirmado!")
    elif voto_presidente == "-2":
        print("Voto nulo confirmado!")
    else:
        candidato = next((c for c in candidatos_presidente if c.numero == voto_presidente), None)
        if candidato:
            if confirmar_voto(candidato):
                registrar_voto(candidato)
                print("Voto registrado com sucesso!")
            else:
                print("Voto cancelado!")
        else:
            print("Candidato não encontrado!")

def apurar_resultados(candidatos):
    candidatos.sort(key=lambda x: x.votos, reverse=True)

    print("\nResultados da Eleição:")
    print("Candidatos Vencedores por Cargo:")
    vencedores_presidente = [candidato for candidato in candidatos if candidato.cargo.lower() == "presidente" and candidato.votos > 0]
    if vencedores_presidente:
        print(f"\nVencedor para Presidente: {vencedores_presidente[0].nome} - Votos: {vencedores_presidente[0].votos}")
    else:
        print("\nNenhum candidato para Presidente recebeu votos!")

    vencedores_governador = [candidato for candidato in candidatos if candidato.cargo.lower() == "governador" and candidato.votos > 0]
    if vencedores_governador:
        print(f"Vencedor para Governador: {vencedores_governador[0].nome} - Votos: {vencedores_governador[0].votos}")
    else:
        print("Nenhum candidato para Governador recebeu votos!")

    vencedores_prefeito = [candidato for candidato in candidatos if candidato.cargo.lower() == "prefeito" and candidato.votos > 0]
    if vencedores_prefeito:
        print(f"Vencedor para Prefeito: {vencedores_prefeito[0].nome} - Votos: {vencedores_prefeito[0].votos}")
    else:
        print("Nenhum candidato para Prefeito recebeu votos!")

    print("\nRanking Geral dos Candidatos:")
    for candidato in candidatos:
        print(f"\nNome: {candidato.nome}")
        print(f"Partido: {candidato.partido}")
        print(f"Votos: {candidato.votos}")

def exibir_relatorio_e_estatisticas(eleitores, candidatos):
    print("\nRelatório e Estatísticas:")
    print("\nLista de Eleitores:")
    eleitores.sort(key=lambda x: x.nome)
    for eleitor in eleitores:
        print(f"Nome: {eleitor.nome}")
        print(f"CPF: {eleitor.cpf}")

    total_eleitores = len(eleitores)
    total_votos = sum(candidato.votos for candidato in candidatos)
    print(f"\nQuantidade de Eleitores: {total_eleitores}")
    print(f"Total de Votos Registrados: {total_votos}")

    partidos = {}
    for candidato in candidatos:
        if candidato.partido in partidos:
            partidos[candidato.partido] += 1
        else:
            partidos[candidato.partido] = 1

    partido_mais_eleitos = max(partidos, key=partidos.get)
    partido_menos_eleitos = min(partidos, key=partidos.get)

    print(f"\nPartido com Mais Candidatos Eleitos: {partido_mais_eleitos}")
    print(f"Partido com Menos Candidatos Eleitos: {partido_menos_eleitos}")

# Menu principal
while True:
    print("\n--- Simulador de Votação ---")
    print("1. Cadastrar Candidatos")
    print("2. Cadastrar Eleitores")
    print("3. Votar")
    print("4. Apurar Resultados")
    print("5. Relatório e Estatísticas")
    print("6. Encerrar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        candidatos_presidente, candidatos_governador, candidatos_prefeito = cadastrar_candidatos()
        candidatos = candidatos_presidente + candidatos_governador + candidatos_prefeito
    elif opcao == "2":
        eleitores = cadastrar_eleitores()
    elif opcao == "3":
        if not candidatos:
            print("Erro: É necessário cadastrar candidatos antes de iniciar a votação!")
            continue
        if not eleitores:
            print("Erro: É necessário cadastrar eleitores antes de iniciar a votação!")
            continue
        votar(candidatos_prefeito, candidatos_governador, candidatos_presidente, eleitores)
    elif opcao == "4":
        if not candidatos:
            print("Erro: É necessário cadastrar candidatos antes de apurar os resultados!")
            continue
        apurar_resultados(candidatos)
    elif opcao == "5":
        if not eleitores or not candidatos:
            print("Erro: É necessário cadastrar eleitores e candidatos antes de exibir o relatório e estatísticas!")
            continue
        exibir_relatorio_e_estatisticas(eleitores, candidatos)
    elif opcao == "6":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida! Escolha uma opção válida.")

