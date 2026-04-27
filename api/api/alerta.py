from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Aquí puedes poner la lógica que hace tu botón (ej. enviar email, guardar en DB)
        # Por ahora, responderemos con un mensaje de éxito
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        respuesta = {"mensaje": "Alerta recibida correctamente"}
        self.wfile.write(json.dumps(respuesta).encode('utf-8'))
        return

    def do_OPTIONS(self):
        # Esto es necesario para evitar errores de CORS (permisos de conexión)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
