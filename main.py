import os
import random
from fastapi import FastAPI, Request
import telegram

app = FastAPI()

TOKEN = "9204768032:AAGhyVmAdpbtJtk91-BLsCt7UHeZTPrEmGk"
bot = telegram.Bot(token=TOKEN)

def analyze_cyber_poker():
    hands_probabilities = {
        "Carte haute": {"prob": 0.35, "avg_cote": 2.5},
        "Une Paire": {"prob": 0.40, "avg_cote": 2.7},
        "Deux Paires": {"prob": 0.15, "avg_cote": 3.5},
        "Brelan": {"prob": 0.06, "avg_cote": 15.0},
        "Quinte / Couleur": {"prob": 0.04, "avg_cote": 12.0}
    }
    
    match_id = random.randint(900, 999)
    selected_hand = random.choices(
        list(hands_probabilities.keys()), 
        weights=[data["prob"] for data in hands_probabilities.values()]
    )[0]
    
    cote_estimee = hands_probabilities[selected_hand]["avg_cote"]
    
    prediction_text = (
        f"♠️ **DIENG POKER PREDICT VIP** ♠️\n\n"
        f"📊 **Analyse Match Virtuel n°{match_id}**\n"
        f"🎯 **Tendance Principale :** {selected_hand}\n"
        f"📈 **Cote estimée / value :** ~{cote_estimee}\n"
        f"⚡ *Recommandation : Gestion de bankroll stricte sur les marchés de mains combinées.*"
    )
    return prediction_text

@app.post("/webhook-poker")
async def telegram_webhook(request: Request):
    data = await request.json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        
        if text.startswith("/poker") or text.startswith("/cyber"):
            analysis = analyze_cyber_poker()
            await bot.send_message(chat_id=chat_id, text=analysis, parse_mode="Markdown")
            
    return {"status": "ok"}
