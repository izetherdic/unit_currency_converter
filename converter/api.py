import requests

BASE_URL = 'https://api.frankfurter.dev/v2'


# obtains the conversion rate from the first currency (str) to the second currency (str)
def get_rate(from_currency, to_currency):
    try:
        conversion_response = requests.get(
            BASE_URL + f'/rate/{from_currency.lower().strip()}/{to_currency.lower().strip()}', timeout=(5, 10))
    except requests.exceptions.RequestException:  # handles timeout errors and lost connection
        raise RuntimeError('Failed to reach service')

    conversion_json = conversion_response.json()

    if conversion_response.status_code == 200:  # handles invalid inputs eg. "abc"
        return conversion_json['rate']
    else:
        raise ValueError("Invalid currency(s)")

# next function takes an amount as an integer or float of an inital currency (currency_1) and converts it to currency_2


def convert_currency(amount, from_currency, to_currency):
    if not isinstance(amount, (int, float)):
        raise TypeError('Amount must be a number')
    elif amount < 0:
        raise ValueError('Amount can\'t be negative')

    currency_rate = get_rate(from_currency, to_currency)

    return round(amount * currency_rate, 2)
