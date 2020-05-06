async def test_health_check(web_client, logs):
    """ Checks: Health check is available to request """
    resp = await web_client.get('/health')
    assert resp.status == 200
    assert await resp.text() == 'App is working'
