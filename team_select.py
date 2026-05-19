from team import Team


def escolher_time(players):

    print("\n================")
    print("MONTE SUA EQUIPE")
    print("================")

    for i, p in enumerate(players):

        print(
            f"[{i}] {p.nome}"
        )

    time = Team("Seu Time")

    while len(time.membros) < 5:

        try:

            escolha = int(
                input("\nEscolha: ")
            )

            escolhido = players[escolha]

            if escolhido in time.membros:

                print("Já escolhido")

                continue

            time.adicionar_membro(
                escolhido
            )

            print(
                f"✅ {escolhido.nome}"
            )
        except KeyboardInterrupt:
          print("\n\nEncerrando jogo...")
          exit()
        
        except:

            print("Inválido")

    return time