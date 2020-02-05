from libpythonpro import github_api


def teste_buscar_avatar():
    url = github_api.buscar_avatar('kelvin-torres')
    assert 'https://avatars3.githubusercontent.com/u/57693050?v=4' == url
