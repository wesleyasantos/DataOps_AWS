from analytics import data_quality

def test_data_quality():
    try:
        data_quality.check_quality()
    except Exception as e:
        assert False, f'Erro na checagem de qualidade: {e}'
