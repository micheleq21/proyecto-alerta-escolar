from http.server import BaseHTTPRequestHandler
import json
import os
from supabase import create_client, Client

# Configura tus credenciales (¡No las compartas!)
SUPABASE_URL = "TU_URL_AQUÍ" # Pega aquí la Project URL
SUPABASE_KEY = "TU_KEY_AQUÍ"  # Pega aquí la clave que encontraste en la captura

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        
        # Insertar en Supabase
        # Asegúrate de que los nombres de los campos coincidan exactamente con tu tabla
        try:
            supabase.table("alertas").insert({
                "nombre": data.get("nombre"),
                "escuela": data.get("escuela"),
                "dni": data.get("dni"),
                "cargo": data.get("cargo"),
                "telefono": data.get("telefono"),
                "latitud": data.get("ubicacion", {}).get("latitud"),
                "longitud": data.get("ubicacion", {}).get("longitud")
            }).execute()
            
            self.send_response(200)
        except Exception as e:
            print(f"Error: {e}")
            self.send_response(500)
            
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"status": "success"}).encode('utf-8'))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
