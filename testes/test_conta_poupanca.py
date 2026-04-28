from datetime import date
from Model.model import PessoaFisica, ContaPoupanca


def test_aplicar_rendimento_poupanca():
    cliente = PessoaFisica(
        cpf="12345678900",
        nome="Lucas",
        data_nascimento=date.today(),
        endereco="Não informado"
    )

    conta = ContaPoupanca(
        cliente=cliente,
        numero=1,
        agencia="0001",
        rendimento=0.005
    )

    conta.depositar(1000)

    resultado = conta.aplicar_rendimento()

    assert resultado is True
    assert conta.saldo == 1005
    assert conta.historico.listar()[-1]["tipo"] == "Rendimento"
    assert conta.historico.listar()[-1]["valor"] == 5