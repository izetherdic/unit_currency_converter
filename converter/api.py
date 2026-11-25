import requests

BASE_URL = 'https://api.frankfurter.dev/v2'

def get_rate(currency_1, currency_2): #obtains the conversion rate from the first currency (str) to the second currency (str)
    try:
        conversion_response = requests.get(BASE_URL + f'/rate/{currency_1.lower()}/{currency_2.lower()}', timeout=(5,10))
    except requests.exceptions.RequestException: # handles timeout errors and lost connection
        raise RuntimeError('Failed to reach service') 

    conversion_json = conversion_response.json()

    if conversion_response.status_code == 200: #handles invalid inputs eg. "abc"
        return conversion_json['rate']
    else:
        raise ValueError("Invalid currency(s)")

#next function takes an amount as an integer or float of an inital currency (currency_1) and converts it to currency_2

def convert_amount(amount, currency_1, currency_2):
    if not isinstance(amount, (int, float)):
        raise TypeError('Amount must be a number')
    elif amount < 0:
        raise ValueError('Amount can\'t be negative')

    currency_rate = get_rate(currency_1, currency_2) 
    
    return round(amount * currency_rate, 2)

print(convert_amount(-1, 'usd', 'eur'))