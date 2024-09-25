numero_placa = input("digite o numero final placa de veiculo: ")

match numero_placa:
    case "1" | "2": print("rodizio na segunda_feira")
    case "3" | "4": print("rodizio na terça-feira")
    case "5" | "6": print("rodizio na quarta-feira")
    case "7" | "8": print("rodizio na quinta-feira")
    case "9" | "0": print("rodizio na sexta-feira")
    case _: print("final de placa invalido")