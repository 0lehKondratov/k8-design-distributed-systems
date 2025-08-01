import asyncio
from streamforge.arango_connector import ArangoConnector


async def run_connector_ops():
    connector = ArangoConnector(url="http://localhost:8529", username="root", password="")
    await connector.connect()
    await connector.insert_document("test", "1", {"value": 1})
    doc = await connector.get_document("test", "1")
    assert doc == {"value": 1}
    await connector.update_document("test", "1", {"value": 2})
    doc = await connector.get_document("test", "1")
    assert doc == {"value": 2}
    await connector.delete_document("test", "1")
    doc = await connector.get_document("test", "1")
    assert doc is None


def test_connector():
    asyncio.run(run_connector_ops())
