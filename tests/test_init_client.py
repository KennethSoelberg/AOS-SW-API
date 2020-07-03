import aos_sw_api


def test_client(settings):
    client = aos_sw_api.Client(**settings)


def test_async_client(settings):
    client = aos_sw_api.AsyncClient(**settings)
