import os
import random
import requests
from fastapi import FastAPI, Request

app = FastAPI()

TOKEN = "9204768032:AAGdCe7c_tym2R6zyug8jtx33P9gC4wpZx4"
RENDER_URL = "dieng-poker-bot.onrender.com"  # Ton URL Render exacte

@app.on_event("startup")
def setup_webhook():
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url=https://{RENDER_URL}/"
        requests.get(url)
    except Exception:
        pass

@app.get("/")
def home():
    return {"status": "TvBet Poker Bot Active"}

@app.post("/")
async def telegram_webhook(request: Request):
    data = await request.json()
    
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        
        # Liste des joueurs et des combinaisons TvBet Poker avec leurs cotes
        joueurs = ["Dieng VIP", "Alpha", "Moussa", "King 99", "Matrix", "Titan", "Casino Master", "Cyber Pro"]
        j1, j2 = random.sample(joueurs, 2)
        
        combinaisons_tvbet = [
            {"nom": "Carte Haute / Paire Simple", "cote": "1.85"},
            {"nom": "Deux Paires", "cote": "3.1"},[span_1](start_span)[span_1](end_span)
            {"nom": "Brelan", "cote": "4.5"},
            {"nom": "Quinte", "cote": "5.7"},[span_2](start_span)[span_2](end_span)
            {"nom": "Couleur (Flush)", "cote": "8.5"},
            {"nom": "Full", "cote": "12.0"},
            {"nom": "Carré", "cote": "25.0"},
            {"nom": "Quinte Flush Royale", "cote": "500.0"}[span_3](start_span)[span_3](end_span)
        ]
        
        choix_combinaiso = random.choice(combinaisons_tvbet)
        gagnant_main = random.choice([j1, j2])
        confiance = random.randint(85, 98)
        
        analysis_text = (
            f"♠️ **TVBET POKER ANALYTICS VIP** ♠️\n\n"
            f"📺 **TvBet POKER : ({j1} vs {j2})**\n\n"
            f"🎯 **Option Recommandée :** {choix_combinaiso['nom']}\n"
            f"💰 **Cote Estimée :** {choix_combinaiso['cote']}\n"
            f"🏆 **Avantage Tactique :** {gagnant_main}\n"
            f"📈 **Niveau de Fiabilité :** {confiance}%\n"
            f"⚡ *Statut : Analyse de pari direct validée.*"
        )
        
        payload = {
            "chat_id": chat_id,
            "text": analysis_text,
            "parse_mode": "Markdown"
        }
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json=payload)
            
    return {"status": "ok"}
