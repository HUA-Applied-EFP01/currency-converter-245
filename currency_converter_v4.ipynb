# Λίστα συναλλαγματικών ισοτιμιών
exchange_rates = {
    "USD": 1.0,      # Βασικό νόμισμα: USD
    "EUR": 0.92,     # 1 USD = 0.92 EUR
    "GBP": 0.81,     # 1 USD = 0.81 GBP
    "JPY": 133.0,    # 1 USD = 133.0 JPY
    "CHF": 0.94,     # 1 USD = 0.94 CHF
}


# Συνάρτηση για τη μετατροπή νομισμάτων
def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return f"Λάθος νόμισμα. Τα διαθέσιμα νομίσματα είναι: {', '.join(exchange_rates.keys())}"
   
    # Υπολογισμός της μετατροπής
    usd_amount = amount / exchange_rates[from_currency]
    converted_amount = usd_amount * exchange_rates[to_currency]
    return round(converted_amount, 2)


# Συνάρτηση για την αλληλεπίδραση με τον χρήστη
def user_input():
    print("Καλώς ήρθατε στον μετατροπέα νομισμάτων!")
    print(f"Διαθέσιμα νομίσματα: {', '.join(exchange_rates.keys())}")
    
    while True:
        # Λήψη ποσού
        try:
            amount = float(input("Εισάγετε το ποσό που θέλετε να μετατρέψετε: "))
        except ValueError:
            print("Παρακαλώ εισάγετε ένα έγκυρο ποσό.")
            continue
        
        # Λήψη νομισμάτων
        from_currency = input("Εισάγετε το νόμισμα από το οποίο θέλετε να μετατρέψετε (π.χ. USD): ").upper()
        to_currency = input("Εισάγετε το νόμισμα στο οποίο θέλετε να μετατρέψετε (π.χ. EUR): ").upper()

        # Κλήση της συνάρτησης μετατροπής
        result = convert_currency(amount, from_currency, to_currency)
       
        # Εμφάνιση αποτελέσματος
        if isinstance(result, str):
            print(result)  # Μήνυμα λάθους
        else:
            print(f"Το ποσό των {amount} {from_currency} ισούται με {result} {to_currency}.")
        
        # Ρώτα τον χρήστη αν θέλει να συνεχίσει
        again = input("Θέλετε να κάνετε άλλη μετατροπή; (ναι/όχι): ").lower()
        if again != "ναι":
            print("Ευχαριστούμε που χρησιμοποιήσατε τον μετατροπέα νομισμάτων!")
            break


# Κλήση της συνάρτησης για αλληλεπίδραση με τον χρήστη
user_input()
