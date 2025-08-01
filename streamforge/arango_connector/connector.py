import asyncio
from typing import Any, Dict


class ArangoConnector:
    """A simplified asynchronous connector mock for ArangoDB."""

    def __init__(self, url: str, username: str, password: str) -> None:
        self.url = url
        self.username = username
        self.password = password
        self._db: Dict[str, Dict[str, Any]] = {}
        self.connected = False

    async def connect(self) -> None:
        """Simulate an asynchronous connection setup."""
        await asyncio.sleep(0)  # no-op for example purposes
        self.connected = True

    async def insert_document(self, collection: str, key: str, document: Dict[str, Any]) -> None:
        self._ensure_connected()
        self._db.setdefault(collection, {})[key] = document

    async def get_document(self, collection: str, key: str) -> Dict[str, Any]:
        self._ensure_connected()
        return self._db.get(collection, {}).get(key)

    async def update_document(self, collection: str, key: str, document: Dict[str, Any]) -> None:
        self._ensure_connected()
        if collection in self._db and key in self._db[collection]:
            self._db[collection][key].update(document)
        else:
            raise KeyError(key)

    async def delete_document(self, collection: str, key: str) -> None:
        self._ensure_connected()
        if collection in self._db:
            self._db[collection].pop(key, None)

    def _ensure_connected(self) -> None:
        if not self.connected:
            raise RuntimeError("Connector not connected")
