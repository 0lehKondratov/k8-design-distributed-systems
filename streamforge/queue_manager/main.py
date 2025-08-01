"""Simplified queue manager service for StreamForge.
This is a placeholder that mimics key API endpoints without external dependencies.
"""

import json
import uuid
from http.server import BaseHTTPRequestHandler, HTTPServer


QUEUES = {}


class QueueHandler(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path == "/queue/start":
            queue_id = str(uuid.uuid4())
            QUEUES[queue_id] = {"status": "running"}
            self._send_json({"queue_id": queue_id})
        elif self.path == "/queue/stop":
            length = int(self.headers.get("Content-Length", 0))
            data = json.loads(self.rfile.read(length) or b"{}")
            queue_id = data.get("queue_id")
            if queue_id in QUEUES:
                QUEUES[queue_id]["status"] = "stopped"
                self._send_json({"queue_id": queue_id, "status": "stopped"})
            else:
                self._send_json({"error": "not found"}, status=404)
        else:
            self._send_json({"error": "unknown endpoint"}, status=404)

    def do_GET(self):
        if self.path.startswith("/queue/status"):
            parts = self.path.split("?")
            if len(parts) > 1:
                params = dict(p.split("=") for p in parts[1].split("&") if "=" in p)
                queue_id = params.get("queue_id")
                if queue_id in QUEUES:
                    self._send_json({"queue_id": queue_id, **QUEUES[queue_id]})
                    return
        self._send_json({"error": "not found"}, status=404)


def run(port: int = 8000) -> None:
    server = HTTPServer(("0.0.0.0", port), QueueHandler)
    print(f"queue-manager listening on {port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
