"""Tiny web app for the OpenShift labs. Standard library only."""
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

VERSION = os.environ.get("APP_VERSION", "unknown")
PORT = 8080


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, content_type):
        data = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == "/healthz":
            self._send(200, "ok\n", "text/plain")
        elif self.path == "/":
            body = json.dumps({"app": "webapp", "version": VERSION})
            self._send(200, body + "\n", "application/json")
        else:
            self._send(404, "not found\n", "text/plain")


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
