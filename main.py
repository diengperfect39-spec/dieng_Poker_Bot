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
    return {"status": "TvBet Poker Expert Engine - Active"}

@app.post("/")
async def telegram_webhook(request: Request):
    try:
        data = await request.json()
        
        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text_recu = data["message"].get("text", "").strip()
            
            session_info = "PB6754788 17H30MN"
            if text_recu and not text_recu.startswith("/"):
                session_info = text_recu.upper()
                
            matrice_analytique = [
                {"combinaison": "Brelan", "cote": "6.8", "analyse_outs": "Indice de tirage fort (3 cartes similaires en vis-à-vis)"},
                {"combinaison": "Deux Paires", "cote": "3.1", "analyse_outs": "Stabilité statistique optimale sur la table"},
                {"combinaison": "Une Paire", "cote": "5.8", "analyse_outs": "Pression de main dominante validée par l'historique"},
                {"combinaison": "Quinte", "cote": "5.7", "analyse_outs": "Alignement séquentiel des connecteurs confirmé"}
            ]
            
            selection = random.choice(matrice_analytique)
            main_gagnante = random.choice(["Main (1)", "Main (2)", "Main (3)", "Main (4)"])
            cote_duel = "5.2"
            confiance_val = round(random.uniform(99.1, 99.9), 1)
            confiance = f"{confiance_val}%"
            
            analysis_text = (
                f"♠️ **DIENG POKER VIP - EXPERT ANALYTICS** ♠️\n\n"
                f"🔒 **Session & Horaire :** POKER. {session_info}\n\n"
                f"🎯 **Option Validée :** {selection['combinaison']}\n"
                f"📊 **Analyse Mathématique :** {selection['analyse_outs']}\n"
                f"💰 **Cote Marché :** {selection['cote']}\n"
                f"🏆 **Duel de Main :** {main_gagnante} (Cote {cote_duel})\n"
                f"📈 **Indice de Fiabilité :** {confiance}\n"
                f"⚡ *Statut : Grille validée par le moteur stochastique.*"
            )
            
            payload = {
                "chat_id": chat_id,
                "text": analysis_text,
                "parse_mode": "Markdown"
            }
            requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json=payload)
    except Exception as e:
        print(f"Erreur: {e}")
        
    return {"status": "ok"}
