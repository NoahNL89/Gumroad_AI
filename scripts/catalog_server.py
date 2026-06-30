#!/usr/bin/env python3
"""Tiny authenticated HTTP server for the Pinterest catalog CSV."""
import base64
import os
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = Path(os.environ.get("CATALOG_FILE", ROOT / "output" / "pinterest_catalog.csv"))
USERNAME = os.environ.get("CATALOG_BASIC_USER", "")
PASSWORD = os.environ.get("CATALOG_BASIC_PASSWORD", "")
HOST = os.environ.get("CATALOG_HOST", "0.0.0.0")
PORT = int(os.environ.get("CATALOG_PORT", "9000"))


class Handler(BaseHTTPRequestHandler):
    server_version = "SchepCatalog/1.0"

    def log_message(self, fmt, *args):
        print(f"{self.address_string()} - {fmt % args}")

    def unauthorized(self):
        self.send_response(HTTPStatus.UNAUTHORIZED)
        self.send_header("WWW-Authenticate", 'Basic realm="Pinterest Catalog"')
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Authentication required\n")

    def authenticated(self):
        if not USERNAME and not PASSWORD:
            return True
        header = self.headers.get("Authorization", "")
        if not header.startswith("Basic "):
            return False
        try:
            raw = base64.b64decode(header.split(" ", 1)[1]).decode()
        except Exception:
            return False
        user, sep, password = raw.partition(":")
        return sep == ":" and user == USERNAME and password == PASSWORD

    def do_GET(self):
        self.handle_request(send_body=True)

    def do_HEAD(self):
        self.handle_request(send_body=False)

    def handle_request(self, send_body):
        if self.path == "/healthz":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            if send_body:
                self.wfile.write(b"ok\n")
            return

        if self.path.split("?", 1)[0] != "/pinterest_catalog.csv":
            self.send_error(HTTPStatus.NOT_FOUND, "Not found")
            return

        if not self.authenticated():
            self.unauthorized()
            return

        if not CATALOG_PATH.exists():
            self.send_error(HTTPStatus.NOT_FOUND, f"Catalog not found: {CATALOG_PATH}")
            return

        body = CATALOG_PATH.read_bytes()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "text/csv; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        if send_body:
            self.wfile.write(body)


def main():
    print(f"Serving {CATALOG_PATH} on http://{HOST}:{PORT}/pinterest_catalog.csv")
    if USERNAME or PASSWORD:
        print("Basic Auth: enabled")
    else:
        print("Basic Auth: disabled")
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()


if __name__ == "__main__":
    main()
