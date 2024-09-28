meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            }
parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")
if parola in meme_dict.keys():
    print(meme_dict["CRINGE"])
else:
    print("La parola non è presente nel dizionario, prova con un'altra...")
