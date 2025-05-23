from etl import load

def test_load():
    try:
        load.load()
    except Exception as e:
        assert False, f'Erro na carga: {e}'
