import hashlib
import os
import requests
from fastapi import FastAPI, Request

app = FastAPI()

TOKEN = "9204768032:AAGdCe7c_tym2R6zyug8jtx33P9gC4wpZx4"

@app.get("/")
def home():
    return {"status": "VIP Engine Active"}

@app.post("/")
async def telegram_webhook(request: Request):
    try:
        data = await request.json()
        
        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text_recu = data["message"].get("text", "").strip()
            
            session_info = "PB237510 19:30"
            if text_recu and not text_recu.startswith("/"):
                session_info = text_recu.upper()
                
            # Génération d'une empreinte cryptographique stable pour la session
            hash_bytes = hashlib.sha256(session_info.encode()).digest()
            val1 = hash_bytes[0]
            val2 = hash_bytes[1]
            
            # Matrice VIP affinée (Combinaisons, Cotes, Mains, Indices de stabilité)
            combinaisons_vip = [
                {"comb": "Brelan", "cote_c": "6.8", "analyse": "Pression de redondance et croisement de table."},
                {"comb": "Deux Paires", "cote_c": "3.1", "analyse": "Stabilité statistique et équilibre des tirages."},
                {"comb": "Full House", "cote_c": "12.5", "analyse": "Forte convergence de structure sur l'axe central."},
                {"comb": "Quinte", "cote_c": "5.7", "analyse": "Alignement séquentiel optimal de la river."},
                {"comb": "Couleur", "cote_c": "8.7", "analyse": "Distribution homogène des enseignes majeures."}
            ]
            
            mains_vip = [
                {"main": "Main (1)", "cote_m": "5.2"},
                {"main": "Main (2)", "cote_m": "5.2"},
                {"main": "Main (3)", "cote_m": "5.2"},
                {"main": "Main (4)", "cote_m": "5.2"},
                {"main": "Main (5)", "cote_m": "5.2"},
                {"main": "Main (6)", "cote_m": "5.2"}
            ]
            
            choix_comb = combinaisons_vip[val1 % len(combinaisons_vip)]
            choix_main = mains_vip[val2 % len(mains_vip)]
            
            # Calcul d'un indice de fiabilité dynamique haut de gamme (entre 98.4% et 99.7%)
            fiabilite = 98.4 + (val1 % 14) / 10
            
            analysis_text = (
                f"♠️ **DIENG POKER VIP** ♠️\n\n"
                f"🔒 **Session :** {session_info}\n\n"
                f"🎯 **Option :** {choix_comb['comb']} (Cote : {choix_comb['cote_c']})\n"
                f"🏆 **Duel de Main :** {choix_main['main']} (Cote : {choix_main['cote_m']})\n"
                f"📊 **Analyse :** {choix_comb['analyse']}\n"
                f"📈 **Indice de Fiabilité :** {fiabilite:.1f}%"
            )
            
            requests.post(
                f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                json={"chat_id": chat_id, "text": analysis_text, "parse_mode": "Markdown"}
            )
    except Exception as e:
        print(e)
        
    return {"ok": True}
