import requests

def convert(amount, from_currency, to_currency):
    url = f'http://data.fixer.io/api/latest?access_key=YOUR_API_KEY&symbols={from_currency},{to_currency}'
    response = requests.get(url)
    data = response.json()
    from_rate = data['rates'][from_currency]
    to_rate = data['rates'][to_currency]
    return (amount * to_rate) / from_rate

print(convert(100, 'USD', 'EUR'))
print(convert(100, 'USD', 'JPY'))
print(convert(100, 'USD', 'GBP'))
print(convert(100, 'USD', 'CNY'))
print(convert(100, 'USD', 'CHF'))
print(convert(100, 'USD', 'CAD'))
print(convert(100, 'USD', 'AUD'))
print(convert(100, 'USD', 'AED'))
print(convert(100, 'USD', 'INR'))
print(convert(100, 'USD', 'BRL'))
