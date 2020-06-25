async def test_create_new(cli, db_and_tables):
    await cli.post('/api/v1/bread', json={'name': 'pie'})
    response = await cli.get('/api/v1/bread')
    assert len(await response.json()) == 1


async def test_fresh_database(cli, db_and_tables):
    # Database should be cleared
    response = await cli.get('/api/v1/bread')
    assert len(await response.json()) == 0
