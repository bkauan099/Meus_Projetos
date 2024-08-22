class SistemaBancario:
    def __init__(self):
        self.conta_bancaria = 0
        self.historico = []
        self.limite_diario = 3
        self.cont_diario = 0
        self.limite_saque = 500

    def depositar(self):
        deposito = float(input("Digite o valor a ser depositado: "))
        self.conta_bancaria += deposito
        self.historico.append(f"Depósito de R$ {deposito}")
        print(f"R$ {deposito} foram adicionados à sua conta. Saldo atual: R$ {self.conta_bancaria} ")

    def sacar(self):
        if self.cont_diario >= self.limite_diario:
            print("Limite de saques diários atingido. Tente novamente amanhã.")
            return

        saque = float(input("Digite o valor a ser sacado: "))

        if saque > self.conta_bancaria:
            print("Saldo insuficiente na conta. Não foi possível realizar o saque desejado.")
        elif saque > self.limite_saque:
            print(f"O valor solicitado excede o limite de saque permitido de R$ {self.limite_saque}.")
        else:
            self.conta_bancaria -= saque
            self.cont_diario += 1
            self.historico.append(f"Saque de R$ {saque}")
            print(f"O valor de R$ {saque} foi sacado. Saldo atual: R$ {self.conta_bancaria}")

    def extrato(self):
        print("Extrato Bancário (do mais antigo ao mais recente):\n")
        print(f"Saldo atual da conta: R$ {self.conta_bancaria}")
        for i, valores in enumerate(self.historico):
            print(f"{i+1}ª Transação: {valores}")
    
    def finalizar(self):
        print("Sistema financeiro finalizado.")
        return False

def main():
    sistema = SistemaBancario()
    while True:
        print("="*16)
        print("Sistema Bancário")
        print("="*16)
        print("1 - Realizar um depósito")
        print("2 - Realizar um saque")
        print("3 - Verificar extrato")
        print("4 - Finalizar sistema")
        valor = int(input("Escolha uma opção: "))

        if valor == 1:
            sistema.depositar()
        elif valor == 2:
            sistema.sacar()
        elif valor == 3:
            sistema.extrato()
        elif valor == 4:
            if not sistema.finalizar():
                break
        else:
            print("Valor inválido. Tente novamente.")
    
if __name__ == '__main__':
    main()