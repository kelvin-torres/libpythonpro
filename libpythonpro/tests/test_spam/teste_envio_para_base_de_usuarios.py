import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.test_enviador_de_email import Enviador
from libpythonpro.tests.test_spam.test_usuarios import Usuario


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


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
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'kelvinlgtorres@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Kelvin', email='kelvinlgtorres@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'lcaguimaraes@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
    assert enviador.parametros_de_envio == (
        'lcaguimaraes@gmail.com',
        'kelvinlgtorres@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
