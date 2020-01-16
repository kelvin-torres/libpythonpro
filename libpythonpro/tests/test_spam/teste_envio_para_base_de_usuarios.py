from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.test_enviador_de_email import Enviador


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'kelvinlgtorres@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
