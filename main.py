import os
import random
import requests
from fastapi import FastAPI, Request
import telegram

app = FastAPI()

TOKEN = "9204768032:AAGhyVmAdpbtJtk91-BLsCt7UHeZTPrEmGk"
bot = telegram.Bot(token=TOKEN)

# URL de ton service sur Render (mets la tienne ici sans les https:// au début)
RENDER_URL = "dieng-poker-bot.onrender.com"

@app.on_event("startup")
async def startup_event():
    # Configuration automatique du webhook au démarrage du serveur
    webhook_url = f"https://{RENDER_URL}/webhook-poker"
    url = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={webhook_url}"
    try:
        requests.get(url)
    except Exception as e:
        print(f"Erreur webhook: {e}")

def analyze_indian_poker():
    joueurs = ["Dieng VIP", "Alpha", "Moussa", "King 99", "Matrix", "Titan", "Casino Master", "Cyber Pro"]
    j1, j2 = random.sample(joueurs, 2)
    
    confiance = random.randint(84, 96)
    issue = random.choice([f"Victoire net de {j1}", f"Victoire serrée de {j2}", "Value / Partage technique"])
    
    analysis_text = (
        f"♠️ **DIENG POKER ANALYTICS VIP** ♠️\n\n"
        f"🎯 **IndianPoker : ({j1} vs {j2})**\n\n"
        f"📊 **Indicateur de Tendance :** {issue}\n"
        f"📈 **Niveau de Fiabilité :** {confiance}%\n"
        f"⚡ *Statut : Analyse de confrontation directe validée.*"
    )
    return analysis_text

@app.post("/webhook-poker")
async def telegram_webhook(request: Request):
    data = await request.json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        
        if text.startswith("/poker") or text.startswith("/cyber") or text.startswith("/start"):
            analysis = analyze_indian_poker()
            await bot.send_message(chat_id=chat_id, text=analysis, parse_mode="Markdown")
            
    return {"status": "ok"}
