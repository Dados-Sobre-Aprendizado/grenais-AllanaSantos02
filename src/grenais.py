def main():
    inter_vitoria = 0
    gremio_vitoria = 0
    empate = 0
    total_grenais = 0
    opcao = 1

    while opcao == 1:
        gols_inter, gols_gremio = map(int, input().split())
        total_grenais += 1

        if gols_inter > gols_gremio:
            inter_vitoria += 1
        elif gols_gremio > gols_inter:
            gremio_vitoria += 1
        else:
            empate += 1

        print("Novo grenal (1-sim 2-nao)")
        opcao = int(input( ))

    print(f"{total_grenais} grenais")
    print(f"Inter:{inter_vitoria}")
    print(f"Gremio:{gremio_vitoria}")
    print(f"Empates:{empate}")

    if inter_vitoria > gremio_vitoria:
        print("Inter venceu mais")
    elif gremio_vitoria > inter_vitoria:
        print("Gremio venceu mais")
    else:
        print("Não houve vencedor")

if __name__ == "__main__":
    main()
