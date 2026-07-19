# Calculate total sales per department using collections.defaultdict.
# defaultdict(int) gives every new key an automatic starting value of 0,
# so `result[dept] += amount` is safe even the first time `dept` is seen -
# no KeyError (see KeyError_test.py) and no `if dept in result` check
# (see calculate_sales.py).

from collections import defaultdict

sales = [
    {"dept": "electronics", "amount": 200},
    {"dept": "clothing", "amount": 50},
    {"dept": "electronics", "amount": 150},
    {"dept": "home", "amount": 100},
    {"dept": "clothing", "amount": 75},
]


def calculate_sales(sales):
    result = defaultdict(int)

    for record in sales:
        result[record["dept"]] += record["amount"]

    return dict(result)


print(calculate_sales(sales))
# {'electronics': 350, 'clothing': 125, 'home': 100}
