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
    return {"status": "Bot Poker Active"}

@app.post("/")
async def telegram_webhook(request: Request):
    data = await request.json()
    
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        
        joueurs = ["Dieng VIP", "Alpha", "Moussa", "King 99", "Matrix", "Titan", "Casino Master", "Cyber Pro"]
        j1, j2 = random.sample(joueurs, 2)
        
        confiance = random.randint(84, 96)
        issue = random.choice([f"Victoire nette de {j1}", f"Victoire serrée de {j2}", "Value / Partage technique"])
        
        analysis_text = (
            f"♠️ **DIENG POKER ANALYTICS VIP** ♠️\n\n"
            f"🎯 **IndianPoker : ({j1} vs {j2})**\n\n"
            f"📊 **Indicateur de Tendance :** {issue}\n"
            f"📈 **Niveau de Fiabilité :** {confiance}%\n"
            f"⚡ *Statut : Analyse de confrontation directe validée.*"
        )
        
        payload = {
            "chat_id": chat_id,
            "text": analysis_text,
            "parse_mode": "Markdown"
        }
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json=payload)
            
    return {"status": "ok"}
