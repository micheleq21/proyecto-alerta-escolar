from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. Leer el contenido que envía el celular
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # 2. Convertir ese contenido a formato legible (JSON)
        data = json.loads(post_data.decode('utf-8'))
        
        # 3. IMPRIMIR los datos en los logs de Vercel (aquí verás la magia)
        print("--- NUEVA ALERTA RECIBIDA ---")
        print(json.dumps(data, indent=2)) 
        
        # Respuesta al navegador
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        respuesta = {"status": "success", "message": "Datos recibidos"}
        self.wfile.write(json.dumps(respuesta).encode('utf-8'))
        return

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
