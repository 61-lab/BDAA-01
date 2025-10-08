# Loģistikas piegādes izmaksu un CO₂ kalkulators
# Izmanto sarakstus, vārdnīcas, ciklus un nosacījumus

# Tarifi un emisijas dažādiem transporta veidiem (eiro un CO₂ par kg·km)
tarifi = {"kravas_auto": 0.05, "vilciens": 0.03, "kuģis": 0.02}
emisijas = {"kravas_auto": 0.08, "vilciens": 0.04, "kuģis": 0.02}

# Saraksts, kur tiks glabāti visu kravu dati
kravas = []

print("=== LOĢISTIKAS PIEGĀDES KALKULATORS ===")

# Lietotājs ievada, cik kravas jārēķina
n = int(input("Cik kravas jāaprēķina? "))

# Cikls, lai ievadītu katras kravas datus
for i in range(n):
    print(f"\nKrava #{i+1}")
    nosaukums = input("Nosaukums: ")
    attalums = float(input("Attālums (km): "))
    svars = float(input("Svars (kg): "))

    # Pārbauda transporta veidu un prasa atkārtoti, ja nepareizs
    while True:
        veids = input("Transporta veids (kravas_auto/vilciens/kuģis): ").lower()
        if veids in tarifi:
            break
        print("❌ Nepareizs transporta veids! Mēģini vēlreiz.")

    # Aprēķina kopējās izmaksas un CO₂ izmešus
    cena = attalums * svars * tarifi[veids]
    co2 = attalums * svars * emisijas[veids]

    # Nosaka, cik videi draudzīga ir piegāde
    if co2 < 1000:
        efekts = "Videi draudzīgs"
    elif co2 < 3000:
        efekts = "Vidēji efektīvs"
    else:
        efekts = "Liels CO₂ piesārņojums"

    # Saglabā kravas datus vārdnīcā un pievieno sarakstam
    kravas.append({
        "nosaukums": nosaukums,
        "veids": veids,
        "cena": cena,
        "co2": co2,
        "efekts": efekts
    })

# Izvada rezultātus par visām kravām
print("\n=== REZULTĀTI ===")
for k in kravas:
    print(f"{k['nosaukums']} ({k['veids']}): €{k['cena']:.2f}; "
          f"CO₂: {k['co2']:.1f} kg → {k['efekts']}")

# Atrod lētāko piegādi
letaka = min(kravas, key=lambda x: x["cena"])

# Izvada secinājumu par lētāko piegādi
print(f"\nLētākā piegāde ir '{letaka['nosaukums']}' ar {letaka['veids']}.")
print("Secinājums: Šis maršruts ir", letaka["efekts"].lower())
