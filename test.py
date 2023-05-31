candidatos_presidente = []
candidatos_governador = []
candidatos_prefeito = []
eleitores = []

def cadastrar_candidato():
    while True:
        nome = input("Digite o nome do candidato: ")
        numero = input("Digite o número do candidato: ")
        partido = input("Digite o partido do candidato: ")
        cargo = input("Digite o cargo que o candidato disputa: ")

        if cargo.lower() == "presidente":
            candidatos_presidente.append({"nome": nome, "numero": numero, "partido": partido})
        elif cargo.lower() == "governador":
            candidatos_governador.append({"nome": nome, "numero": numero, "partido": partido})
        elif cargo.lower() == "prefeito":
            candidatos_prefeito.append({"nome": nome, "numero": numero, "partido": partido})
        else:
            print("Cargo inválido!")

        opcao = input("Deseja cadastrar outro candidato? (Sim/Não): ")
        if opcao.lower() == "não":
            break

def cadastrar_eleitor():
    while True:
        nome = input("Digite o nome do eleitor: ")
        cpf = input("Digite o CPF do eleitor: ")
        eleitores.append({"nome": nome, "cpf": cpf})

        opcao = input("Deseja cadastrar outro eleitor? (Sim/Não): ")
        if opcao.lower() == "não":
            break

def votar():
    # Etapa Prefeito
    print("----- Etapa Prefeito -----")
    for candidato in candidatos_prefeito:
        print(f"| Número: {candidato['numero']} | Nome: {candidato['nome']} | Partido: {candidato['partido']} |")
    voto_prefeito = input("Digite o número do candidato para prefeito (ou -1 para voto em branco, -2 para voto nulo): ")
    # Registrar voto na lista de candidatos

    # Etapa Governador
    print("----- Etapa Governador -----")
    for candidato in candidatos_governador:
        print(f"| Número: {candidato['numero']} | Nome: {candidato['nome']} | Partido: {candidato['partido']} |")
    voto_governador = input("Digite o número do candidato para governador (ou -1 para voto em branco, -2 para voto nulo): ")
    # Registrar voto na lista de candidatos

    # Etapa Presidente
    print("----- Etapa Presidente -----")
    for candidato in candidatos_presidente:
        print(f"| Número: {candidato['numero']} | Nome: {candidato['nome']} | Partido: {candidato['partido']} |")
    voto_presidente = input("Digite o número do candidato para presidente (ou -1 para voto em branco, -2 para voto nulo): ")
    # Registrar voto na lista de candidatos

def apurar_resultados():
    # Implementar lógica de apuração de votos e exibição dos resultados
    pass

def relatorio_estatisticas():
    # Implementar lógica de exibição do relatório e estatísticas
    pass

def exibir_menu():
    print("-----------------------------")
    print("|  Simulador de Votação     |")
    print("-----------------------------")
    print("|  1. Cadastrar Candidatos |")
    print("|  2. Cadastrar Eleitores  |")
    print("|  3. Votar                |")
    print("|  4. Apurar Resultados    |")
    print("|  5. Relatório e Estatísticas |")
    print("|  6. Encerrar             |")
    print("-----------------------------")

def main():
    while True:
        exibir_menu()
        opcao = input("Digite o número da operação desejada: ")

        if opcao == "1":
            cadastrar_candidato()
        elif opcao == "2":
            cadastrar_eleitor()
        elif opcao == "3":
            votar()
        elif opcao == "4":
            apurar_resultados()
        elif opcao == "5":
            relatorio_estatisticas()
        elif opcao == "6":
            break
        else:
            print("Opção inválida! Digite novamente.")

if __name__ == "__main__":
    main()
