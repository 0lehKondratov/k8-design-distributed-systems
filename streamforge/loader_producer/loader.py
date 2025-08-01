"""Simplified loader-producer job for StreamForge.
This script simulates downloading data from Binance and writing to Kafka and ArangoDB.
"""

import json
import os
import time
import urllib.request


def load_binance_data(symbol: str, time_range: str) -> list:
    """Mock fetching data from Binance."""
    # Placeholder: return fake candle data
    return [{"time": i, "price": 100 + i} for i in range(3)]


def send_webhook(url: str, payload: dict) -> None:
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        urllib.request.urlopen(req)
    except Exception:
        pass  # Ignore webhook errors in example


def main() -> None:
    symbol = os.getenv("SYMBOL", "BTCUSDT")
    time_range = os.getenv("TIME_RANGE", "1h")
    queue_id = os.getenv("QUEUE_ID", "demo")
    webhook_url = os.getenv("WEBHOOK_URL", "http://localhost/webhook")

    start = time.time()
    records = load_binance_data(symbol, time_range)
    # Placeholder for writing to Kafka/Arango
    time.sleep(0.1)
    duration = time.time() - start

    payload = {
        "queue_id": queue_id,
        "status": "completed",
        "records": len(records),
        "duration": duration,
    }
    send_webhook(webhook_url, payload)


if __name__ == "__main__":
    main()
