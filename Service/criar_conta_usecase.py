from datetime import date
from Model.model import PessoaFisica, ContaPoupanca, ContaCorrente


class CriarContaUseCase:
    def __init__(self, repository):
        self.repository = repository

    def executar(self, nome, cpf, saldo_inicial, numero):
        cliente = PessoaFisica(
            cpf=cpf,
            nome=nome,
            data_nascimento=date.today(),
            endereco="Não informado"
        )

        conta = ContaPoupanca(
            cliente=cliente,
            numero=numero,
            agencia="0001",
            rendimento=0.005
        )

        if saldo_inicial > 0:
            conta.depositar(saldo_inicial)
            conta.historico.adicionar_transacao("Depósito Inicial", saldo_inicial)

        self.repository.salvar(conta)
        return conta