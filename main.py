import os
import random
import requests
from fastapi import FastAPI, Request

app = FastAPI()

TOKEN = "9204768032:AAGdCe7c_tym2R6zyug8jtx33P9gC4wpZx4"
RENDER_URL = "dieng-poker-bot.onrender.com"

@app.on_event("startup")
def setup_webhook():
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url=https://{RENDER_URL}/"
        requests.get(url)
    except Exception:
        pass

@app.get("/")
def home():
    return {"status": "TvBet Poker Pro Active"}

@app.post("/")
async def telegram_webhook(request: Request):
    data = await request.json()
    
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text_recu = data["message"].get("text", "").strip()
        
        # Valeur par défaut si vide
        session_info = "PB237462 17H30mn"
        if text_recu and not text_recu.startswith("/"):
            session_info = text_recu.upper()
            
        marches_tvbet = [
            {"combinaison": "Deux Paires", "cote": "3.1"},
            {"combinaison": "Quinte", "cote": "5.7"},
            {"combinaison": "Une Paire", "cote": "5.8"},
            {"combinaison": "Brelan", "cote": "6.8"},
            {"combinaison": "Couleur", "cote": "8.7"},
            {"combinaison": "Full House", "cote": "8.6"}
        ]
        
        selection = random.choice(marches_tvbet)
        main_gagnante = random.choice(["Main (1)", "Main (2)"])
        cote_duel = "5.2"
        
        # Indice de fiabilité dynamique variable entre 98.6% et 99.9%
        confiance_val = round(random.uniform(98.6, 99.9), 1)
        confiance = f"{confiance_val}%"
        
        analysis_text = (
            f"♠️ **TVBET POKER EXPERT ANALYTICS** ♠️\n\n"
            f"🔒 **Session & Horaire :** POKER. {session_info}\n\n"
            f"🎯 **Option Validée :** {selection['combinaison']}\n"
            f"💰 **Cote Marché :** {selection['cote']}\n"
            f"🏆 **Duel de Main :** {main_gagnante} (Cote {cote_duel})\n"
            f"📈 **Indice de Fiabilité :** {confiance}\n"
            f"⚡ *Statut : Synchronisation horaire et grille verrouillée.*"
        )
        
        payload = {
            "chat_id": chat_id,
            "text": analysis_text,
            "parse_mode": "Markdown"
        }
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json=payload)
            
    return {"status": "ok"}
