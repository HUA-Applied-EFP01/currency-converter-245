def get_exchange_rates():
    """"Συναλλαγματικές ισοτιμίες που ισχύουν σήμερα στις 27/01/2025 με βάση το ευρώ (EUR) από την Ευρωπαϊκή Κεντρική Τράπεζα. """
    return {
        "EUR": 1.0,  # Το ευρώ είναι το βασικό νόμισμα
        "USD": 1.0530,
        "JPY": 162.21,
        "BGN": 1.9558,
        "CZK": 25.102,
        "DKK": 7.4625,
        "GBP": 0.84106,
        "HUF": 408.78,
        "PLN": 4.2193,
        "RON": 4.9750,
        "SEK": 11.4960,
        "CHF": 0.9453,
        "ISK": 146.30,
        "NOK": 11.8095,
        "TRY": 37.6265,
        "AUD": 1.6700,
        "BRL": 6.2375,
        "CAD": 1.5096,
        "CNY": 7.6306,
        "HKD": 8.1987,
        "IDR": 17007.37,
        "ILS": 3.8064,
        "INR": 90.8800,
        "KRW": 1507.97,
        "MXN": 21.5878,
        "MYR": 4.6106,
        "NZD": 1.8464,
        "PHP": 61.408,
        "SGD": 1.4134,
        "THB": 35.402,
        "ZAR": 19.6537
    }

def convert_currency(amount, from_currency, to_currency, rates):
    """Αν ο χρήστης δώσει ίδιο νόμισμα για μετατροπή τότε του επιστρέφει το αρχικό ποσό"""
    if from_currency == to_currency:
        return amount

    """Ελέγχει αν το νόμισμα προέλευσης ή μετατροπής δεν υπάρχει στο λεξικό rates."""
    if from_currency not in rates or to_currency not in rates:
        return f"Μη έγκυροι κωδικοί νομισμάτων: {from_currency} ή {to_currency}"

    """Επειδή τα rates είναι με βάση το ευρώ, το νόμισμα θα μετατραπεί πρώτα σε ευρώ και έπειτα θα μετατραπεί στο νόμισμα που ζητείται"""
    amount_in_euros = amount / rates[from_currency]
    converted_amount = amount_in_euros * rates[to_currency]
    return converted_amount

def user_input():
    print("Καλωσήρθατε στον Μετατροπέα Νομισμάτων")
    rates = get_exchange_rates()

    try:
        amount = float(input("Εισάγετε το ποσό που θέλετε να μετατρέψετε: "))
        from_currency = input("Εισάγετε το νόμισμα από το οποίο θέλετε να μετατρέψετε (π.χ. EUR, USD, KRW κλπ.): ").upper()
        to_currency = input("Εισάγετε το νόμισμα στο οποίο θέλετε να μετατρέψετε (π.χ. CAD, MYR, ILS κλπ.): ").upper()

        result = convert_currency(amount, from_currency, to_currency, rates)

        """Ελέγχει αν το result είναι τύπου string"""
        if isinstance(result, str):
            print(result)
        else:
            print(f"Το ποσό μετατροπής είναι: {result:.2f} {to_currency}")

    except ValueError as e:
        print("Σφάλμα: Εισάγατε μη έγκυρα δεδομένα.")
    except Exception:
        print("Παρουσιάστηκε σφάλμα.")

if __name__ == "__main__":
    user_input()
