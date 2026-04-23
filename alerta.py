from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Leer el contenido que envía el botón
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        # Aquí es donde verás los datos en el servidor
        print(f"ALERTA RECIBIDA: {data}")

        # Responder al celular para que sepa que llegó bien
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"status": "recibido"}).encode())