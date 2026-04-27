from http.server import BaseHTTPRequestHandler
import json
from supabase import create_client

# Configuración de conexión
# IMPORTANTE: Reemplaza TU_SERVICE_ROLE_KEY con la llave que copiaste del dashboard
URL = "https://knnnemdkahzovufelowc.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imtubm5lbWRrYWh6b3Z1ZmVsb3djIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3NzI1NDEwMCwiZXhwIjoyMDkyODMwMTAwfQ.l4T0TGWQ79_lNDEuV8lCiwi4ZT9DGW3p_-weJvjC7XI" 

supabase = create_client(URL, KEY)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        
        try:
            # Con la llave service_role, las políticas RLS se saltan automáticamente
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
            self.wfile.write(json.dumps({"status": "exito"}).encode('utf-8'))
        except Exception as e:
            print(f"ERROR: {str(e)}")
            self.send_response(500)
            self.wfile.write(json.dumps({"status": "error", "detalle": str(e)}).encode('utf-8'))
            
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
