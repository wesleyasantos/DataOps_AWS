from etl import transform

def test_transform():
    try:
        transform.transform()
    except Exception as e:
        assert False, f'Erro na transformação: {e}'
