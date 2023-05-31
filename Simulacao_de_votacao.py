class Candidato:
    def __init__(self, nome, numero, partido, cargo):
        self.nome = nome
        self.numero = numero
        self.partido = partido
        self.cargo = cargo

class Eleitor:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class UrnaEletronica:
    def __init__(self):
        self.candidatos_presidente = []
        self.candidatos_governador = []
        self.candidatos_prefeito = []
        self.eleitores = []
        self.votos_prefeito = []
        self.votos_governador = []
        self.votos_presidente = []

    def cadastrar_candidatos(self):
        while True:
            nome = input("Digite o nome do candidato: ")
            numero = input("Digite o número do candidato: ")
            partido = input("Digite o partido do candidato: ")
            cargo = input("Digite o cargo que o candidato disputa: ")

            candidato = Candidato(nome, numero, partido, cargo)

            if cargo.lower() == "presidente":
                self.candidatos_presidente.append(candidato)
            elif cargo.lower() == "governador":
                self.candidatos_governador.append(candidato)
            elif cargo.lower() == "prefeito":
                self.candidatos_prefeito.append(candidato)

            resposta = input("Deseja cadastrar outro candidato? (S/N): ")
            if resposta.lower() == "n" or resposta.lower() == "nao":
                break

    def cadastrar_eleitores(self):
        while True:
            nome = input("Digite o nome do eleitor: ")
            cpf = input("Digite o CPF do eleitor: ")

            eleitor = Eleitor(nome, cpf)
            self.eleitores.append(eleitor)

            resposta = input("Deseja cadastrar outro eleitor? (S/N): ")
            if resposta.lower() == "n" or resposta.lower() == "nao":
                break

    def votar(self):
        print("\nVotação")
        print("-------")

        for cargo, candidatos in [("Prefeito", self.candidatos_prefeito),
                                  ("Governador", self.candidatos_governador),
                                  ("Presidente", self.candidatos_presidente)]:
            print(f"\nVotação para {cargo}:")
            for candidato in candidatos:
                print(f"Número: {candidato.numero}")
                print(f"Nome: {candidato.nome}")
                print(f"Partido: {candidato.partido}")
                print("")

            voto = input(f"Digite o número do candidato para {cargo}: ")
            confirmacao = None

            if voto == "1":
                confirmacao = input("Confirma voto em branco? (S/N): ")
            elif voto == "2":
                confirmacao = input("Confirma voto nulo? (S/N): ")
            elif any(c.numero == voto for c in candidatos):
                candidato = next(c for c in candidatos if c.numero == voto)
                confirmacao = input(f"Confirma voto para {candidato.nome}? (S/N): ")

            if confirmacao and confirmacao.lower() == "s":
                if cargo.lower() == "prefeito":
                    self.votos_prefeito.append(voto)
                elif cargo.lower() == "governador":
                    self.votos_governador.append(voto)
                elif cargo.lower() == "presidente":
                    self.votos_presidente.append(voto)
                print("Voto registrado.")
            else:
                print("Voto não registrado.")

    def apurar_resultados(self):
        # Apuração dos votos para prefeito
        contador_prefeito = {}
        for voto in self.votos_prefeito:
            if voto == 1:
                candidato = "Branco"
            elif voto == 2:
                candidato = "Nulo"
            else:
                candidato = next((c for c in self.candidatos_prefeito if c.numero == voto), None)
            if candidato:
                contador_prefeito[candidato] = contador_prefeito.get(candidato, 0) + 1
        ranking_prefeito = sorted(contador_prefeito.items(), key=lambda x: x[1], reverse=True)

        # Apuração dos votos para governador
        contador_governador = {}
        for voto in self.votos_governador:
            if voto == 1:
                candidato = "Branco"
            elif voto == 2:
                candidato = "Nulo"
            else:
                candidato = next((c for c in self.candidatos_governador if c.numero == voto), None)
            if candidato:
                contador_governador[candidato] = contador_governador.get(candidato, 0) + 1
        ranking_governador = sorted(contador_governador.items(), key=lambda x: x[1], reverse=True)

        # Apuração dos votos para presidente
        contador_presidente = {}
        for voto in self.votos_presidente:
            if voto == 1:
                candidato = "Branco"
            elif voto == 2:
                candidato = "Nulo"
            else:
                candidato = next((c for c in self.candidatos_presidente if c.numero == voto), None)
            if candidato:
                contador_presidente[candidato] = contador_presidente.get(candidato, 0) + 1
        ranking_presidente = sorted(contador_presidente.items(), key=lambda x: x[1], reverse=True)

        # Exibição dos resultados
        print("---------------------------------------------------")
        print("\nRANKING DO RESULTADO PARA PREFEITO")
        print("---------------------------------------------------")
        for candidato, votos in ranking_prefeito:
            print(f"|{candidato.nome} ({candidato.partido}): {votos} votos")
        total_votos_prefeito = sum(contador_prefeito.values())
        percentual_validos_prefeito = (total_votos_prefeito - contador_prefeito.get("Branco", 0) - contador_prefeito.get("Nulo", 0)) / total_votos_prefeito * 100
        percentual_brancos_prefeito = contador_prefeito.get("Branco", 0) / total_votos_prefeito * 100
        percentual_nulos_prefeito = contador_prefeito.get("Nulo", 0) / total_votos_prefeito * 100
        print("---------------------------------------------------")
        print(f"| Total de votos válidos: {total_votos_prefeito}"+'|')
        print("---------------------------------------------------")
        print(f"| Percentual de votos válidos: {percentual_validos_prefeito:.2f}%"+'|')
        print("---------------------------------------------------")
        print(f"| Total de votos em branco: {contador_prefeito.get('Branco', 0)}"+'|')
        print("---------------------------------------------------")
        print(f"| Percentual de votos em branco: {percentual_brancos_prefeito:.2f}%"+'|')
        print("---------------------------------------------------")
        print(f"| Total de votos nulos: {contador_prefeito.get('Nulo', 0)}"+'|')
        print("---------------------------------------------------")
        print(f"| Percentual de votos nulos: {percentual_nulos_prefeito:.2f}%"+'|')
        print("---------------------------------------------------")

        print("---------------------------------------------------")
        print("\nRANKING DO RESULTADO PARA GOVERNADOR:")
        print("---------------------------------------------------")
        for candidato, votos in ranking_governador:
            print(f"|{candidato.nome} ({candidato.partido}): {votos} votos" +'|')
        total_votos_governador = sum(contador_governador.values())
        percentual_validos_governador = (total_votos_governador - contador_governador.get("Branco", 0) - contador_governador.get("Nulo", 0)) / total_votos_governador * 100
        percentual_brancos_governador = contador_governador.get("Branco", 0) / total_votos_governador * 100
        percentual_nulos_governador = contador_governador.get("Nulo", 0) / total_votos_governador * 100
        print("---------------------")
        print(f"|Total de votos válidos: {total_votos_governador}" +'|')
        print(f"|Percentual de votos válidos: {percentual_validos_governador:.2f}%"+'|')
        print(f"|Total de votos em branco: {contador_governador.get('Branco', 0)}"+'|')
        print(f"|Percentual de votos em branco: {percentual_brancos_governador:.2f}%"+'|')
        print(f"|Total de votos nulos: {contador_governador.get('Nulo', 0)}")
        print(f"|Percentual de votos nulos: {percentual_nulos_governador:.2f}%"+'|')

        print("--------------------------------------------------")
        print("\nRANKING DO RESULTADO PARA PRESIDENTE"+'|')
        print("---------------------------------------------------")
        for candidato, votos in ranking_presidente:
            print(f"|{candidato.nome} ({candidato.partido}): {votos} votos"+'|')
        total_votos_presidente = sum(contador_presidente.values())
        percentual_validos_presidente = (total_votos_presidente - contador_presidente.get("Branco", 0) - contador_presidente.get("Nulo", 0)) / total_votos_presidente * 100
        percentual_brancos_presidente = contador_presidente.get("Branco", 0) / total_votos_presidente * 100
        percentual_nulos_presidente = contador_presidente.get("Nulo", 0) / total_votos_presidente * 100
        print("---------------------------------------------------")
        print(f"Total de votos válidos: {total_votos_presidente}"+'|')
        print("---------------------------------------------------")
        print(f"Percentual de votos válidos: {percentual_validos_presidente:.2f}%"+'|')
        print("---------------------------------------------------")
        print(f"Total de votos em branco: {contador_presidente.get('Branco', 0)}"+'|')
        print("---------------------------------------------------")
        print(f"Percentual de votos em branco: {percentual_brancos_presidente:.2f}%"+'|')
        print("---------------------------------------------------")
        print(f"Total de votos nulos: {contador_presidente.get('Nulo', 0)}"+'|')
        print("---------------------------------------------------")
        print(f"Percentual de votos nulos: {percentual_nulos_presidente:.2f}%"+ '|')
        print("---------------------------------------------------")

    def relatorio_estatisticas(self):
        print("---------------------------------------------------")
        print("\nRelatório e Estatísticas")
        print("---------------------------------------------------")

        print("\nLista de eleitores que votaram:")
        print("---------------------------------------------------")
        for eleitor in self.eleitores:
            print(f"Nome: {eleitor.nome} - CPF: {eleitor.cpf}")

        total_eleitores = len(self.eleitores)
        total_votos_prefeito = len(self.votos_prefeito)
        total_votos_governador = len(self.votos_governador)
        total_votos_presidente = len(self.votos_presidente)

        print("---------------------------------------------------")
        print("\nVerificação de quantidade de eleitores e votos por cargo:")
        print("---------------------------------------------------")
        print(f"Total de eleitores: {total_eleitores}")
        print("---------------------------------------------------")
        print(f"Total de votos para Prefeito: {total_votos_prefeito}")
        print("---------------------------------------------------")
        print(f"Total de votos para Governador: {total_votos_governador}")
        print("---------------------------------------------------")
        print(f"Total de votos para Presidente: {total_votos_presidente}")
        print("---------------------------------------------------")

        total_votos_validos_prefeito = total_votos_prefeito - self.votos_prefeito.count("1") - self.votos_prefeito.count("2")
        total_votos_validos_governador = total_votos_governador - self.votos_governador.count("1") - self.votos_governador.count("2")
        total_votos_validos_presidente = total_votos_presidente - self.votos_presidente.count("1") - self.votos_presidente.count("2")

        porcentagem_votos_validos_prefeito = (total_votos_validos_prefeito / total_votos_prefeito) * 100 if total_votos_prefeito > 0 else 0
        porcentagem_votos_validos_governador = (total_votos_validos_governador / total_votos_governador) * 100 if total_votos_governador > 0 else 0
        porcentagem_votos_validos_presidente = (total_votos_validos_presidente / total_votos_presidente) * 100 if total_votos_presidente > 0 else 0

        total_votos_brancos_prefeito = self.votos_prefeito.count("1")
        total_votos_brancos_governador = self.votos_governador.count("1")
        total_votos_brancos_presidente = self.votos_presidente.count("1")

        porcentagem_votos_brancos_prefeito = (total_votos_brancos_prefeito / total_votos_prefeito) * 100 if total_votos_prefeito > 0 else 0
        porcentagem_votos_brancos_governador = (total_votos_brancos_governador / total_votos_governador) * 100 if total_votos_governador > 0 else 0
        porcentagem_votos_brancos_presidente = (total_votos_brancos_presidente / total_votos_presidente) * 100 if total_votos_presidente > 0 else 0

        total_votos_nulos_prefeito = self.votos_prefeito.count("2")
        total_votos_nulos_governador = self.votos_governador.count("2")
        total_votos_nulos_presidente = self.votos_presidente.count("2")

        porcentagem_votos_nulos_prefeito = (total_votos_nulos_prefeito / total_votos_prefeito) * 100 if total_votos_prefeito > 0 else 0
        porcentagem_votos_nulos_governador = (total_votos_nulos_governador / total_votos_governador) * 100 if total_votos_governador > 0 else 0
        porcentagem_votos_nulos_presidente = (total_votos_nulos_presidente / total_votos_presidente) * 100 if total_votos_presidente > 0 else 0

        print("\nDados estatísticos por cargo:")
        print(f"Total de votos válidos para Prefeito: {total_votos_validos_prefeito} ({porcentagem_votos_validos_prefeito:.2f}%)")
        print(f"Total de votos em branco para Prefeito: {total_votos_brancos_prefeito} ({porcentagem_votos_brancos_prefeito:.2f}%)")
        print(f"Total de votos nulos para Prefeito: {total_votos_nulos_prefeito} ({porcentagem_votos_nulos_prefeito:.2f}%)")

        print(f"\nTotal de votos válidos para Governador: {total_votos_validos_governador} ({porcentagem_votos_validos_governador:.2f}%)")
        print(f"Total de votos em branco para Governador: {total_votos_brancos_governador} ({porcentagem_votos_brancos_governador:.2f}%)")
        print(f"Total de votos nulos para Governador: {total_votos_nulos_governador} ({porcentagem_votos_nulos_governador:.2f}%)")

        print(f"\nTotal de votos válidos para Presidente: {total_votos_validos_presidente} ({porcentagem_votos_validos_presidente:.2f}%)")
        print(f"Total de votos em branco para Presidente: {total_votos_brancos_presidente} ({porcentagem_votos_brancos_presidente:.2f}%)")
        print(f"Total de votos nulos para Presidente: {total_votos_nulos_presidente} ({porcentagem_votos_nulos_presidente:.2f}%)")

    def menu_principal(self):
        while True:
            print("---------------------------------------")
            print("|  Simulador de Votação                |")
            print("---------------------------------------")
            print("|  1. Cadastrar Candidatos  " + "           |")
            print("|  2. Cadastrar Eleitores              " + "|")
            print("|  3. Votar                            " + "|")
            print("|  4. Apurar Resultados                " + "|")
            print("|  5. Relatório e Estatísticas         " + "|")
            print("|  6. Encerrar                         " + "|")
            print("---------------------------------------")

            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                self.cadastrar_candidatos()
            elif opcao == "2":
                self.cadastrar_eleitores()
            elif opcao == "3":
                self.votar()
            elif opcao == "4":
                self.apurar_resultados()
            elif opcao == "5":
                self.relatorio_estatisticas()
            elif opcao == "6":
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    urna = UrnaEletronica()
    urna.menu_principal()
