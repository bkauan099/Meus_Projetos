class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.historico = []
        self.limite_diario = 3
        self.cont_diario = 0
        self.limite_saque = 500
        self.usuarios = []
        self.conta = []
        self.cpf = []

    def CriarUsuario(self):
        cpf = input("Digite o número do seu CPF: ")

        if cpf in self.cpf:
            print("CPF já cadastrado.")
            return

        nome = input("Digite o seu nome: ")
        data_nascimento = input("Digite a sua data de nascimento: ")
        endereco = input("Digite o seu endereço (logradouro, nro - bairro - cidade/sigla estado ): ")
        self.usuarios.append({"Nome": nome, "CPF": cpf, "Data de Nascimento": data_nascimento, "Endereço": endereco})
        self.cpf.append(cpf)
        print("Usuário criado com sucesso!")

    def FiltrarUsuario(self, cpf):
        # Busca o usuário pelo CPF na lista de usuários
        usuarios_filtrados = [usuario for usuario in self.usuarios if usuario["CPF"] == cpf]
        return usuarios_filtrados[0] if usuarios_filtrados else None

    def CriarConta(self):
        cpf = input("Informe o CPF do usuário: ")
        usuario = self.FiltrarUsuario(cpf)
        if usuario:
            print("Conta criada com sucesso!")
            self.conta.append({"Agência": "0001", "Número da conta": len(self.conta) + 1, "Usuário": usuario})
        else:
            print("Usuário não encontrado, fluxo de criação de conta encerrado!")

    def listar_contas(self):
        if self.conta:
            print("Listagem de Contas:")
            for conta in self.conta:
                print(f"\nAgência: {conta['Agência']}, Número da conta: {conta['Número da conta']}, Usuário: {conta['Usuário']['Nome']}")
        else:
            print("Nenhuma conta adicionada.")

    def depositar(self):
        deposito = float(input("Digite o valor a ser depositado: "))
        self.saldo += deposito
        self.historico.append(f"Depósito de R$ {deposito}")
        print(f"R$ {deposito} foram adicionados à sua conta. Saldo atual: R$ {self.saldo}")

    def sacar(self):
        if self.cont_diario >= self.limite_diario:
            print("Limite de saques diários atingido. Tente novamente amanhã.")
            return

        saque = float(input("Digite o valor a ser sacado: "))

        if saque > self.saldo:
            print("Saldo insuficiente na conta. Não foi possível realizar o saque desejado.")
        elif saque > self.limite_saque:
            print(f"O valor solicitado excede o limite de saque permitido de R$ {self.limite_saque}.")
        else:
            self.saldo -= saque
            self.cont_diario += 1
            self.historico.append(f"Saque de R$ {saque}")
            print(f"O valor de R$ {saque} foi sacado. Saldo atual: R$ {self.saldo}")

    def extrato(self):
        print("Extrato Bancário (do mais antigo ao mais recente):\n")
        print(f"Saldo atual da conta: R$ {self.saldo}")
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
        print("4 - Criar Usuário")
        print("5 - Criar Conta")
        print("6 - Listar contas")
        print("7 - Finalizar Sistema")
        valor = int(input("Escolha uma opção: "))

        if valor == 1:
            sistema.depositar()
        elif valor == 2:
            sistema.sacar()
        elif valor == 3:
            sistema.extrato()
        elif valor == 4:
            sistema.CriarUsuario()
        elif valor == 5:
            sistema.CriarConta()
        elif valor == 6:
            sistema.listar_contas()
        elif valor == 7:
            if not sistema.finalizar():
                break
        else:
            print("Valor inválido. Tente novamente.")
    
if __name__ == '__main__':
    main()