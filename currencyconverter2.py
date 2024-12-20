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
    # Ελέγχουμε αν τα νομίσματα είναι έγκυρα
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Λάθος νόμισμα. Παρακαλώ εισάγετε έγκυρα νομίσματα (π.χ. USD, EUR, GBP)."
   
    # Υπολογισμός της μετατροπής
    usd_amount = amount / exchange_rates[from_currency]  # Μετατροπή σε USD
    converted_amount = usd_amount * exchange_rates[to_currency]  # Μετατροπή στο τελικό νόμισμα
    return round(converted_amount, 2)


# Συνάρτηση για την αλληλεπίδραση με τον χρήστη
def user_input():
    print("Καλώς ήρθατε στον μετατροπέα νομισμάτων!")
   
    # Λήψη ποσού
    try:
        amount = float(input("Εισάγετε το ποσό που θέλετε να μετατρέψετε: "))
    except ValueError:
        return "Παρακαλώ εισάγετε ένα έγκυρο ποσό."
   
    # Λήψη νομισμάτων
    from_currency = input("Εισάγετε το νόμισμα από το οποίο θέλετε να μετατρέψετε (π.χ. USD): ").upper()
    to_currency = input("Εισάγετε το νόμισμα στο οποίο θέλετε να μετατρέψετε (π.χ. EUR): ").upper()


    # Κλήση της συνάρτησης μετατροπής
    result = convert_currency(amount, from_currency, to_currency)
   
    # Εμφάνιση αποτελέσματος
    if isinstance(result, str):
        print(result)  # Αν είναι μήνυμα λάθους
    else:
        print(f"Το ποσό των {amount} {from_currency} ισούται με {result} {to_currency}.")


# Κλήση της συνάρτησης για αλληλεπίδραση με τον χρήστη
user_input()
