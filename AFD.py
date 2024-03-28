class AFD:
    # O construtor da classe inicializa uma nova instancia do AFD
    def __init__(self, estados: list, alfabeto: list, estado_inicial: str, estados_finais: list):
        self.estados = estados  # Lista de todos os estados possíveis
        self.alfabeto = alfabeto  # Lista dos símbolos do alfabeto aceitos
        self.estado_inicial = estado_inicial  # Estado inicial do AFD
        self.estados_finais = estados_finais  # Lista de estados que são considerados finais/aceitos
        self.transicoes = {}  # Dicionário para armazenar as transições

    # Método para definir uma transição de um estado para outro dado um símbolo
    def define_transicao(self, estado: str, simbolo: str, proximo_estado: str):
        self.transicoes[(estado, simbolo)] = proximo_estado

    # Método que verifica se uma dada sequência de entrada é aceita pela máquina
    def verifica_transicoes(self, entrada: str) -> None:
        proximo_estado = self.estado_inicial  # Começa no estado inicial
        for letra in entrada:  # Itera sobre cada letra da entrada
            # Verifica se a transição atual (estado atual + letra) está definida
            if (proximo_estado, letra) in self.transicoes:
                proximo_estado = self.transicoes[(proximo_estado, letra)]  # Atualiza o estado atual
                if proximo_estado is None:  # Se o próximo estado é None, a entrada é recusada
                    print("Recusado")
                    return
            else:
                print("Recusado")
                return
        # Se o loop terminar e o estado atual estiver entre os estados finais, a entrada é aceita
        if proximo_estado in self.estados_finais:
            print("Aceito")
        else:
            print("Recusado")

def main():
    # Solicita ao usuário os componentes do AFD e cria uma instância
    estados = input("Digite os estados da máquina: ").split()
    alfabeto = input("Digite o alfabeto: ").split()
    estado_inicial = input("Digite o estado inicial: ")
    estados_finais = input("Digite os estados finais: ").split()

    # Instancia o AFD com os dados fornecidos
    maquina = AFD(estados, alfabeto, estado_inicial, estados_finais)

    # Solicita ao usuário as transições e as define para o AFD
    print("Lendo transições, caso a transição não exista, digite 'nulo':")
    for estado in estados:
        for simbolo in alfabeto:
            print(f"Lendo {simbolo}")
            print(f"{estado} ---> ", end="")
            proximo_estado = input()
            # Se o usuário digitar 'nulo', a transição é definida como None
            if proximo_estado == "nulo":
                maquina.define_transicao(estado, simbolo, None)
            else:
                maquina.define_transicao(estado, simbolo, proximo_estado)

    # Solicita ao usuário uma sequência de entrada para testar no AFD
    entrada = input("Digite a sequência de entrada: ")
    maquina.verifica_transicoes(entrada)


main()
