# Amazon Data Analysis

Analisi esplorativa dei dati di vendita Amazon.  
Questo progetto mira a comprendere il dataset dei prodotti Amazon, pulire i dati, analizzare prezzi e sconti, visualizzare pattern e comprendere le recensioni dei clienti.

---

## Obiettivi del progetto

1. **Pulizia dei dati**  
   - Gestire valori mancanti
   - Convertire i prezzi in formato numerico
   - Standardizzare le colonne

2. **Analisi descrittiva**  
   - Distribuzione dei prezzi e dei prezzi scontati
   - Distribuzione delle percentuali di sconto
   - Analisi dei rating e del numero di recensioni

3. **Visualizzazione**  
   - Grafici per prezzi, sconti e valutazioni
   - Confronti tra categorie di prodotti

4. **Rilevazione pattern e insight**  
   - Categorie con prezzi medi più alti
   - Prodotti più recensiti
   - Eventuali anomalie nei dati

---

## Task principali

- [x] Esplorazione iniziale del dataset
- [x] Pulizia e trasformazione dei dati
- [x] Salvataggio dataset pulito (`amazon_clean.csv`)
- [x] Analisi statistica dei prezzi e sconti
- [x] Visualizzazione grafica
- [x] Analisi dei rating dei prodotti
- [ ] Analisi avanzata e correlazioni tra colonne
- [ ] Possibile creazione di modelli predittivi (opzionale)

---

## Struttura del progetto
amazon_analysis/
├── data/                 # Dataset originale e pulito
│   ├── amazon.csv
│   └── amazon_clean.csv
├── notebooks/            # Notebook per analisi esplorativa
│   └── 01_data_exploration.ipynb
├── src/                  # Funzioni Python riutilizzabili
├── main.py               # Script principale
├── requirements.txt      # Librerie necessarie
└── README.md             # Documentazione del progetto

---

## Librerie utilizzate

- `pandas` per la manipolazione dei dati  
- `numpy` per calcoli numerici  
- `matplotlib` per la visualizzazione dei dati  

Puoi installare tutte le librerie con:

```bash
pip install -r requirements.txt

Esempi di grafici
	•	Distribuzione dei prezzi dei prodotti
	•	Distribuzione dei prezzi scontati
	•	Percentuali di sconto
	•	Distribuzione dei rating dei prodotti

Contatti

Creato da ["Vincenzo Ciavarrella"]