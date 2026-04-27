try:
            # Imprimimos lo que recibimos para verlo en los logs de Vercel
            print(f"DATOS RECIBIDOS: {data}")
            
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
            # Esto es lo más importante: imprimirá el error real en Vercel
            print(f"ERROR DE SUPABASE: {str(e)}")
            self.send_response(500)
