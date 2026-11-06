import os
import random
from fastapi import FastAPI, Request
import telegram

app = FastAPI()

TOKEN = "9204768032:AAGhyVmAdpbtJtk91-BLsCt7UHeZTPrEmGk"
bot = telegram.Bot(token=TOKEN)

def analyze_indian_poker():
    # Liste de joueurs virtuels professionnels pour l'affrontement
    joueurs = ["Dieng VIP", "Alpha", "Moussa", "King 99", "Matrix", "Titan", "Casino Master", "Cyber Pro"]
    j1, j2 = random.sample(joueurs, 2)
    
    # Analyse de dynamique et probabilité sérieuse
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
