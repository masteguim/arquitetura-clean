from datetime import date
from unittest.mock import Mock
from Model.model import PessoaFisica, ContaPoupanca
from Service.depositar_usecase import DepositarUseCase


def test_depositar_usecase_com_dummy_stub_e_mock():
    # Dummy
    cliente_dummy = PessoaFisica(
        cpf="12345678900",
        nome="Cliente Dummy",
        data_nascimento=date.today(),
        endereco="Rua Teste"
    )

    # Stub
    conta_stub = ContaPoupanca(
        cliente=cliente_dummy,
        numero=1,
        agencia="0001"
    )
    conta_stub.depositar(100)

    # Mock
    repositorio_mock = Mock()
    usecase = DepositarUseCase(repositorio_mock)
    sucesso, mensagem = usecase.executar(conta_stub, 50)

    assert sucesso is True
    assert mensagem == "Depósito realizado com sucesso."
    assert conta_stub.saldo == 150
    assert conta_stub.historico.listar()[-1]["tipo"] == "Depósito"
    assert conta_stub.historico.listar()[-1]["valor"] == 50

    repositorio_mock.salvar.assert_called_once_with(conta_stub)