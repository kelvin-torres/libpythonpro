from unittest.mock import Mock

import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.tests.test_spam.test_usuarios import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Kelvin', email='kelvinlgtorres@gmail.com'),
            Usuario(nome='Lucas', email='lcaguimaraes@gmail.com')
        ],
        [
            Usuario(nome='Kelvin', email='kelvinlgtorres@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'kelvinlgtorres@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Kelvin', email='kelvinlgtorres@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'lcaguimaraes@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
    enviador.enviar.assert_called_once_with(
        'lcaguimaraes@gmail.com',
        'kelvinlgtorres@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
