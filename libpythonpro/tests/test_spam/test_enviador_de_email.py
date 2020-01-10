from libpythonpro.spam.test_enviador_de_email import Enviador, EmailInvalido

import pytest


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['kelvinlgtorres@gmail.com', 'foo@bar.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'kelvin_lucas10@hotmail.com',
        'Teste assunto',
        'teste corpo email'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'testando']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'kelvin_lucas10@hotmail.com',
            'Teste assunto',
            'teste corpo email'
        )
