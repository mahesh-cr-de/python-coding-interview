# Calculate total sales per department using a plain dict.
# See KeyError_test.py for why `result[dept] += amount` alone isn't safe,
# and calculate_sales_using_defaultdict.py for a cleaner fix.

sales = [
    {"dept": "electronics", "amount": 200},
    {"dept": "clothing", "amount": 50},
    {"dept": "electronics", "amount": 150},
    {"dept": "home", "amount": 100},
    {"dept": "clothing", "amount": 75},
]


def calculate_sales(sales):
    result = {}

    for record in sales:
        if record["dept"] in result:
            result[record["dept"]] += record["amount"]
        else:
            result[record["dept"]] = record["amount"]

    return result


print(calculate_sales(sales))
# {'electronics': 350, 'clothing': 125, 'home': 100}
