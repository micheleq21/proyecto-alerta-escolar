from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Aquí es donde ocurre la magia cuando presionas el botón
        # Por ahora, enviamos una respuesta de éxito al navegador
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        respuesta = {"status": "success", "message": "Alerta enviada correctamente"}
        self.wfile.write(json.dumps(respuesta).encode('utf-8'))
        return

    def do_OPTIONS(self):
        # Necesario para que el navegador permita la conexión
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
