import pandas as pd
import matplotlib.pyplot as plt


df= pd.read_csv("amazon.csv")

# capire cosa c'è nel dataset
df = pd.read_csv("amazon.csv")
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())
print(df.nunique())


# controllo e pulizia dei dati
df["rating_count"].fillna(0, inplace=True)
print("\nValori mancanri per colonna")
print(df.isna().sum())

# Rimuovi simboli e converte in numeri
df["actual_price"] = df["actual_price"].replace("[₹,]", "", regex=True).astype(float)
df["discounted_price"] = df["discounted_price"].replace("[₹,]", "", regex=True).astype(float)

# creazione dataset pulito
df.to_csv("amazon_clean.csv", index=False)
print("\nDataset pulito e aggiornato salvato come amazon_clean")

# --- DISTRIBUZIONE DEI PREZZI ---
plt.figure(figsize=(8,5))
plt.hist(df["actual_price"], bins=30, edgecolor="black")
plt.title("Distribuzione dei prezzi originali dei prodotti")
plt.xlabel("Prezzo (€)")
plt.ylabel("Numero di prodotti")
plt.show()

# --- DISTRIBUZIONE DEI PREZZI SCONTATI ---
plt.figure(figsize=(8,5))
plt.hist(df["discounted_price"], bins=30, color="orange", edgecolor="black")
plt.title("Distribuzione dei prezzi scontati dei prodotti")
plt.xlabel("Prezzo scontato (€)")
plt.ylabel("Numero di prodotti")
plt.show()

# --- DISTRIBUZIONE DELLE PERCENTUALI DI SCONTO ---
plt.figure(figsize=(8,5))
plt.hist(df["discount_percentage"], bins=30, color="green", edgecolor="black")
plt.title("Distribuzione delle percentuali di sconto")
plt.xlabel("Sconto (%)")
plt.ylabel("Numero di prodotti")
plt.show()


# Calcola il prezzo medio e sconto medio per categoria
categoria_media_sconti = (
    df.groupby("category")[["actual_price", "discounted_price"]]
    .mean()
    .sort_values(by="actual_price", ascending=False)
)

print("\nAnalisi categoria per prezzi e sconti")
print(categoria_media_sconti)

# Mostra solo le prime 10 categorie
top10 = categoria_media_sconti.head(10)

top10.plot(kind="bar", figsize=(10,5))
plt.title("Top 10 categorie per prezzo medio")
plt.ylabel("Prezzo medio (₹)")
plt.xlabel("Categoria")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# visualizzazione di alcune info di base
print("\nStatistiche sul rating:")
print(df["rating"].describe()) 

# conta quante recensioni ci sono per ogni valore di rating
rating_counts = df["rating"].value_counts().sort_index()

print("\nDistribuzione delle valutazioni:")
print(rating_counts)

# visualizzazione grafica
plt.figure(figsize=(8,5))
rating_counts.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Distribuzione delle valutazioni dei prodotti")
plt.xlabel("Valutazioni (stelle)")
plt.ylabel("Numero di recensioni")
plt.show()

