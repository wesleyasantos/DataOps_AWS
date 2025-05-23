from etl import extract

def test_extract():
    try:
        extract.extract()
    except Exception as e:
        assert False, f'Erro na extração: {e}'
