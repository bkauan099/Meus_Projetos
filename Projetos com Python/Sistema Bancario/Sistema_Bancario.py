class SistemaBancario:
    def __init__(self):
        self.conta_bancaria = 0
        self.historico = []

    def depositar(self):
        deposito = float(input("Digite o valor a ser depositado: "))
        self.conta_bancaria += deposito
        self.historico.append(f"Deposito de R$ {deposito}")
        print(f"R$ {deposito:.2f} foram Adicionados a sua conta. Saldo atual: R$ {self.conta_bancaria:.2f} ")
    
    def sacar(self):
        saque = float(input("Digite o valor a ser sacado: "))
        if saque < self.conta_bancaria:
            self.conta_bancaria -= saque
            self.historico.append(f"Saque de R$ {saque}")
            print(f"O seguinte valor foi sacado R$ {saque:.2f}. Saldo atual: R$ {self.conta_bancaria:.2f}")
        else:
            print("Saldo insuficiente na conta. Não foi possivel realizar o saque desejado")
            
    def extrato(self):
        print("Extro Bancario (do mais antigo ao mais recente):\n")
        print(f"Saldo atual da conta: {self.conta_bancaria:.2f}")
        for valores in self.historico:
            print(valores)
        
          
def main(): 
    sistema = SistemaBancario()
    while True:
        print("="*16)
        print("Sistema Bancário")
        print("="*16)
        print("1 - Realizar um deposito")
        print("2 - Realizar um Saque")
        print("3 - Verificar Extrato")
        print("4 - Finalizar Sistema")
        valor =  int(input("Escolha uma opção: "))

        if valor == 1:
            sistema.depositar()
        elif valor == 2:
            sistema.sacar()
        elif valor == 3:
            sistema.extrato()
        elif valor == 4:
            break
        else:
            print("Valor invalido Digitado.Tente Novamente")
    
    print("Sistema financeiro finalizado")
    
if __name__ == '__main__':
    main()       