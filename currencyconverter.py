def get_exchange_rates():
    """Συναλαγματικές ισοτιμίες που ισχύουν σήμερα στις 19/12/2024 με βάση το ευρώ (EUR) από την Ευρωμαϊη Κεντρική Τράπεζα https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html """
    return{
        "EUR": 1.0,  # Το ευρώ είναι το βασικό νόμισμα
        "USD": 1.0395,
        "JPY": 163.07,
        "BGN": 1.9558,
        "CZK": 25.127,
        "DKK": 7.4613,
        "GBP": 0.82445,
        "HUF": 416.05,
        "PLN": 4.2500,
        "RON": 4.9760,
        "SEK": 11.4625,
        "CHF": 0.9319,
        "ISK": 144.70,
        "NOK": 11.8143,
        "TRY": 36.4565,
        "AUD": 1.6631,
        "BRL": 6.5335,
        "CAD": 1.4930,
        "CNY": 7.5858,
        "HKD": 8.0785,
        "IDR": 16957.88,
        "ILS": 3.7647,
        "INR": 88.4810,
        "KRW": 1505.30,
        "MXN": 21.1339,
        "MYR": 4.6835,
        "NZD": 1.8387,
        "PHP": 61.396,
        "SGD": 1.4131,
        "THB": 35.946,
        "ZAR": 19.0350
     }

def convert_currency(amount, from_currency, to_currency,rates):
     """Αν ο χρήστης δώσει ίδιο νόμισμα για μετατροπή τότε του επιστρέφει το αρχικό ποσό"""
     if from_currency == to_currency:
        return amount
    
     """Ελέγχει αν το νόμισμα προέλευσης, ή μετατροπής δεν υπάρχει στο λεξικό rates."""
     if from_currency not in rates or to_currency not in rates:
        return f"Μη έγκυροι κωδικοί νομισμάτων: {from_currency} ή {to_currency}"

     """Επειδή τα rates είναι με βάση το ευρώ το νόμισμα θα μετατραπεί πρώτα σε ευρώ και έπειτα θα μετατραπεί στο νόμισμα που ζητείται"""
     amount_in_euros = amount / rates [from_currency]
     converted_amount = amount_in_euros*rates[to_currency]
     return converted_amount 
  
def main():
     print("Καλωσήρθατε στον Μετατροπέα Νομισμάτων")
     rates = get_exchange_rates()
 
     try:
       amount = float(input("Εισάγετε το ποσό που θέλετε να μετατρέψετε:"))
       from_currency = input("Εισάγεται το νόμισμα από το οποίο θέλετε να μετατρέψετε (π.χ. EUR, USD, KRW κλπ.)")
       to_currency = input("Εισάγετε το νόμισμα στο οποίο θέλετε να μετατρέψετε (π.χ. CAD, MYR, ILS κλπ.)")

       result = convert_currency(amount,from_currency, to_currency, rates)

       """Ελέγχει αν το result είναι τύπου string"""
       if isinstance(result,str):
           print(result)
       else:
           print(f"Το ποσό μετατροπής είναι: {result:.2f} {to_currency}")

     except ValueError as e:
         print("Σφάλμα: Εισάγατε μη έγκυρα δεδομένα.")
     except Exception:
        print("Παρουσιάστηκε σφάλμα.")


        
