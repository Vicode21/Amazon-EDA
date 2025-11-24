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

## Conclusioni finali

✅ Conclusioni dell’Analisi del Dataset Amazon

Dopo aver esplorato, pulito e analizzato il dataset relativo ai prodotti Amazon, emergono diversi punti chiave:

⸻

1. Qualità dei dati
	•	Il dataset contiene 1.465 righe e 16 colonne.
	•	Non sono presenti valori nulli rilevanti, tranne rating_count con 2 celle vuote, facilmente sistemate.
	•	Molte colonne numeriche erano salvate come stringhe con simboli (“₹”, “%”, virgole), perciò è stato necessario un importante lavoro di cleaning.

⸻

2. Prezzi dei prodotti
	•	I prezzi originali e scontati mostrano una forte variabilità: ci sono prodotti molto economici e altri con prezzi più alti.
	•	Dopo il cleaning, la distribuzione dei prezzi mostra una concentrazione di prodotti nella fascia bassa, con pochi prodotti premium.

📊 I grafici delle distribuzioni evidenziano:
	•	una curva decrescente: pochi prodotti molto costosi
	•	molti prodotti tra le fasce ₹100 – ₹1.000

⸻

3. Politiche di sconto
	•	Le percentuali di sconto variano molto, con molti prodotti che hanno sconti tra il 20% e il 60%.
	•	Alcune categorie presentano differenze significative tra prezzo originale e scontato.

💡 Questo può indicare strategie di marketing aggressive per attirare gli utenti.

⸻

4. Rating e recensioni

Analizzando la distribuzione dei rating emerge che:
	•	La maggior parte dei prodotti ha una valutazione tra 3.8 e 4.4 stelle
	•	Il picco maggiore è tra 4.0 e 4.3
	•	I rating molto bassi (sotto 3) sono rari

📌 Conclusione importante:

Le valutazioni sono mediamente alte, probabilmente perché Amazon tende a promuovere prodotti con recensioni positive o perché gli utenti comprano di più prodotti con rating elevati.

Inoltre:
	•	I rating_count (numero di recensioni) variano moltissimo: alcuni prodotti hanno pochissime recensioni, altri centinaia.

⸻

5. Analisi per categoria

La media dei prezzi per categoria mostra che:
	•	alcune categorie hanno prezzi nettamente più alti
	•	altre sono molto più economiche e densamente popolate

Le Top 10 Categorie per prezzo medio aiutano a capire quali prodotti sono premium.

⸻

🧾 Sintesi Finale

In conclusione:

✔️ Il dataset è ricco e ben strutturato
✔️ È stato possibile pulirlo eliminando formati errati e trasformando le colonne numeriche
✔️ Le analisi mostrano:
	•	forte variabilità nei prezzi
	•	molte categorie diverse
	•	rating tendenzialmente positivi
	•	politiche di sconto significative
	•	categorie premium con prezzi più alti

L’insieme dei risultati dà una buona panoramica della struttura e delle dinamiche di vendita dei prodotti su Amazon.



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