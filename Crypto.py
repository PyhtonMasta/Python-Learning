import time
crypto = ["ADA", "BTC", "MENB", "GHT"]
print("Tieto crptomeny ponúkane \n" + str(crypto))
choice = input("Vyber si zo zonamu: ")
if choice in crypto:
    print("Dobre takže si chceš kúpiť: " + choice)
else:
    print("Zlý výber")
budget = int(input("Za kolko chceš investovať ?: "))
if budget > 0:
    print("Chceš si kúpiť: " + choice + " za " + str(budget) + "€")
else:
    print("Zlá čiastka")
choice_1 = input("Potrvdzujete objednávku: ")
if choice_1 == "ANO":
    print("0bjednávka sa spracovavá...")
    time.sleep(2.5)
    print("Objednávka úspešne dokončena.")
elif choice_1 == "NIE":
    print("Objednávka zlyhala")
retry = input("Chceš to zopakovať ?: ")
if retry == "ANO":
    print("Opakujem transkaciu...")
    time.sleep(2.5)
    print("Transakcia prebehla uspešne")
else:
    print("Transakcia zlyhala")

