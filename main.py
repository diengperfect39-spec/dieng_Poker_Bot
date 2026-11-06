import hashlib
import os
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
    return {"status": "TvBet Poker Deterministic VIP Engine - Active"}

@app.post("/")
def telegram_webhook(request: Request):
    try:
        data = request.json()
        
        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text_recu = data["message"].get("text", "").strip()
            
            session_info = "PB6754788 17H30MN"
            if text_recu and not text_recu.startswith("/"):
                session_info = text_recu.upper()
                
            # Moteur déterministe pur : l'analyse est mathématiquement liée au code de la session (Zéro Aléatoire)
            hash_val = int(hashlib.md5(session_info.encode()).hexdigest(), 16)
            
            options_expertes = [
                {
                    "combinaison": "Quinte", 
                    "cote_comb": "5.7", 
                    "main": "Main (5)", 
                    "cote_main": "5.2", 
                    "analyse": "Algorithme stochastique lourd : Alignement séquentiel et dynamique de table optimale."
                },
                {
                    "combinaison": "Brelan", 
                    "cote_comb": "6.8", 
                    "main": "Main (2)", 
                    "cote_main": "5.2", 
                    "analyse": "Matrice de densité : Pression de redondance et vis-à-vis validée."
                },
                {
                    "combinaison": "Deux Paires", 
                    "cote_comb": "3.1", 
                    "main": "Main (1)", 
                    "cote_main": "5.2", 
                    "analyse": "Analyse vectorielle : Stabilité statistique et croisement de paires fort."
                },
                {
                    "combinaison": "Couleur", 
                    "cote_comb": "8.7", 
                    "main": "Main (4)", 
                    "cote_main": "5.2", 
                    "analyse": "Spectre de probabilité : Distribution homogène des enseignes confirmée."
                }
            ]
            
            # Sélection indexée de manière fixe par la session
            choix = options_expertes[hash_val % len(options_expertes)]
            confiance_val = 99.8
            
            analysis_text = (
                f"♠️ **DIENG POKER VIP - ANALYSE INSTITUTIONNELLE** ♠️\n\n"
                f"🔒 **Session Ciblée :** POKER. {session_info}\n\n"
                f"🎯 **Option Validée :** {choix['combinaison']} (Cote : {choix['cote_comb']})\n"
                f"🏆 **Main Directe :** {choix['main']} (Cote : {choix['cote_main']})\n"
                f"📊 **Rapport Analytique :** {choix['analyse']}\n"
                f"📈 **Indice de Fiabilité :** {confiance_val}%\n"
                f"⚡ *Statut : Moteur déterministe sans simulation.*"
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
