from forex_python.converter import *
c=CurrencyRates()
print(c.convert('USD','INR',20))
print(c.get_rate('USD','INR'))
