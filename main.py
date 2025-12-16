import http.server
import socketserver
import webbrowser
import urllib.request
import os

DUCKDNS_DOMAIN = "stlckmacsterluke"
DUCKDNS_TOKEN = os.getenv("TOKEN")
PORT = 8000

if not DUCKDNS_TOKEN:
    raise ValueError("No TOKEN!")

url = f"https://www.duckdns.org/update?domains={DUCKDNS_DOMAIN}&token={DUCKDNS_TOKEN}&ip="
with urllib.request.urlopen(url) as response:
    print("DuckDNS response:", response.read().decode())

socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler).serve_forever()
