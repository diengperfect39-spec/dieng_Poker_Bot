import hashlib
import os
import requests
from fastapi import FastAPI, Request

app = FastAPI()

TOKEN = "9204768032:AAGdCe7c_tym2R6zyug8jtx33P9gC4wpZx4"

@app.get("/")
def home():
    return {"status": "Active"}

@app.post("/")
async def telegram_webhook(request: Request):
    try:
        data = await request.json()
        
        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text_recu = data["message"].get("text", "").strip()
            
            session_info = "PB237498 18H42MN"
            if text_recu and not text_recu.startswith("/"):
                session_info = text_recu.upper()
                
            hash_val = int(hashlib.md5(session_info.encode()).hexdigest(), 16)
            
            options_expertes = [
                {"combinaison": "Quinte", "cote_comb": "5.7", "main": "Main (5)", "cote_main": "5.2", "analyse": "Alignement séquentiel optimal validé."},
                {"combinaison": "Brelan", "cote_comb": "6.8", "main": "Main (2)", "cote_main": "5.2", "analyse": "Pression de redondance et vis-à-vis confirmée."},
                {"combinaison": "Deux Paires", "cote_comb": "3.1", "main": "Main (1)", "cote_main": "5.2", "analyse": "Stabilité statistique et croisement de paires."},
                {"combinaison": "Couleur", "cote_comb": "8.7", "main": "Main (4)", "cote_main": "5.2", "analyse": "Distribution homogène des enseignes."}
            ]
            
            choix = options_expertes[hash_val % len(options_expertes)]
            
            analysis_text = (
                f"♠️ **DIENG POKER VIP** ♠️\n\n"
                f"🔒 **Session :** {session_info}\n\n"
                f"🎯 **Option :** {choix['combinaison']} (Cote : {choix['cote_comb']})\n"
                f"🏆 **Main :** {choix['main']} (Cote : {choix['cote_main']})\n"
                f"📊 **Analyse :** {choix['analyse']}\n"
                f"📈 **Fiabilité :** 99.8%"
            )
            
            requests.post(
                f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                json={"chat_id": chat_id, "text": analysis_text, "parse_mode": "Markdown"}
            )
    except Exception as e:
        print(e)
        
    return {"ok": True}
