"""
main.py – Centro Analisi Mediche
Ogni paziente accumula più misurazioni dello stesso tipo nel tempo.
Le statistiche raggruppano i risultati per tipo con NumPy.
"""

import numpy as np

from paziente import Paziente
from medico   import Medico
from analisi  import Analisi

# PARTE 1 

nome1, cognome1, cf1 = "Mario",    "Rossi",    "RSSMRA80A01F205X"
eta1, peso1          = 45,          78.5
analisi1             = ["emocromo", "glicemia", "colesterolo"]

nome2, cognome2, cf2 = "Laura",    "Bianchi",  "BNCLRA92B41H501Y"
eta2, peso2          = 32,          62.0
analisi2             = ["glicemia", "trigliceridi", "creatinina"]

nome3, cognome3, cf3 = "Giovanni", "Verdi",    "VRDGNN55C15L219Z"
eta3, peso3          = 60,          90.3
analisi3             = ["colesterolo", "creatinina", "emocromo"]

print(f"Paziente 1: {nome1} {cognome1}, {eta1} anni, {peso1} kg → {analisi1}")
print(f"Paziente 2: {nome2} {cognome2}, {eta2} anni, {peso2} kg → {analisi2}")
print(f"Paziente 3: {nome3} {cognome3}, {eta3} anni, {peso3} kg → {analisi3}")

# PARTE 2 

# 3 Medici
medico_ferrari = Medico("Carlo",     "Ferrari",   "Medicina Interna")
medico_conti   = Medico("Francesca", "Conti",     "Ematologia")
medico_marino  = Medico("Roberto",   "Marino",    "Endocrinologia")

medici = [medico_ferrari, medico_conti, medico_marino]

# 5 Pazienti
mario    = Paziente("Mario",    "Rossi",    "RSSMRA80A01F205X", 45, 78.5)
laura    = Paziente("Laura",    "Bianchi",  "BNCLRA92B41H501Y", 32, 62.0)
giovanni = Paziente("Giovanni", "Verdi",    "VRDGNN55C15L219Z", 60, 90.3)
sofia    = Paziente("Sofia",    "Greco",    "GRCSFN88D52H501W", 36, 55.8)
luca     = Paziente("Luca",     "Esposito", "SPSLCU75H10A087V", 50, 83.2)

pazienti = [mario, laura, giovanni, sofia, luca]

# Mario – 3 glicemie, 3 colesteroli, 3 emocromi
mario.aggiungi_analisi(Analisi("glicemia",    95))   
mario.aggiungi_analisi(Analisi("colesterolo", 210))
mario.aggiungi_analisi(Analisi("emocromo",    7.2))
mario.aggiungi_analisi(Analisi("glicemia",    102))  
mario.aggiungi_analisi(Analisi("colesterolo", 198))
mario.aggiungi_analisi(Analisi("emocromo",    6.8))
mario.aggiungi_analisi(Analisi("glicemia",    98))   
mario.aggiungi_analisi(Analisi("colesterolo", 205))
mario.aggiungi_analisi(Analisi("emocromo",    7.5))

# Laura – 3 glicemie, 3 trigliceridi, 3 creatinine
laura.aggiungi_analisi(Analisi("glicemia",     88))  
laura.aggiungi_analisi(Analisi("trigliceridi", 170))
laura.aggiungi_analisi(Analisi("creatinina",   0.9))
laura.aggiungi_analisi(Analisi("glicemia",     91))  
laura.aggiungi_analisi(Analisi("trigliceridi", 160))
laura.aggiungi_analisi(Analisi("creatinina",   1.0))
laura.aggiungi_analisi(Analisi("glicemia",     85))  
laura.aggiungi_analisi(Analisi("trigliceridi", 180))
laura.aggiungi_analisi(Analisi("creatinina",   0.85))

# Giovanni – 3 colesteroli, 3 creatinine, 3 emocromi
giovanni.aggiungi_analisi(Analisi("colesterolo", 230))  
giovanni.aggiungi_analisi(Analisi("creatinina",  1.5))
giovanni.aggiungi_analisi(Analisi("emocromo",    5.0))
giovanni.aggiungi_analisi(Analisi("colesterolo", 245))  
giovanni.aggiungi_analisi(Analisi("creatinina",  1.6))
giovanni.aggiungi_analisi(Analisi("emocromo",    4.8))
giovanni.aggiungi_analisi(Analisi("colesterolo", 220))  
giovanni.aggiungi_analisi(Analisi("creatinina",  1.4))
giovanni.aggiungi_analisi(Analisi("emocromo",    5.2))

# Sofia – 3 glicemie, 3 colesteroli, 3 trigliceridi
sofia.aggiungi_analisi(Analisi("glicemia",     72))   
sofia.aggiungi_analisi(Analisi("colesterolo",  185))
sofia.aggiungi_analisi(Analisi("trigliceridi", 130))
sofia.aggiungi_analisi(Analisi("glicemia",     68))   
sofia.aggiungi_analisi(Analisi("colesterolo",  190))
sofia.aggiungi_analisi(Analisi("trigliceridi", 125))
sofia.aggiungi_analisi(Analisi("glicemia",     75))   
sofia.aggiungi_analisi(Analisi("colesterolo",  178))
sofia.aggiungi_analisi(Analisi("trigliceridi", 140))

# Luca – 3 creatinine, 3 emocromi, 3 glicemie
luca.aggiungi_analisi(Analisi("creatinina", 0.7))   
luca.aggiungi_analisi(Analisi("emocromo",   3.8))
luca.aggiungi_analisi(Analisi("glicemia",   115))
luca.aggiungi_analisi(Analisi("creatinina", 0.8))   
luca.aggiungi_analisi(Analisi("emocromo",   4.0))
luca.aggiungi_analisi(Analisi("glicemia",   120))
luca.aggiungi_analisi(Analisi("creatinina", 0.75))  
luca.aggiungi_analisi(Analisi("emocromo",   3.9))
luca.aggiungi_analisi(Analisi("glicemia",   118))

# Stampa schede e valutazione di ogni singola misurazione
for p in pazienti:
    print(p.scheda_personale())
    for a in p.lista_analisi:
        print(a.valuta())

# PARTE 3 
print("\n" + ("="*50))

rng = np.random.default_rng(seed=42)
valori_glicemia = np.round(rng.normal(100, 15, 100).astype(np.float32),2)

print(f"Valori:        {valori_glicemia}")
print(f"Media:         {np.mean(valori_glicemia):.2f}")
print(f"Massimo:       {np.max(valori_glicemia):.2f}")
print(f"Minimo:        {np.min(valori_glicemia):.2f}")
print(f"Dev. standard: {np.std(valori_glicemia):.2f}")

# PARTE 4 e 5 

for p in pazienti:
    print(p.statistiche_analisi())

medico_ferrari.visita_paziente(mario)
medico_conti.visita_paziente(laura)
medico_marino.visita_paziente(giovanni)
medico_ferrari.visita_paziente(sofia)
medico_conti.visita_paziente(luca)

