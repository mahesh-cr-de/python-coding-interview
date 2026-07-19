# Common pitfall: `result[dept] += amount` throws a KeyError the first time
# `dept` is seen, because `result[dept]` doesn't exist yet and += needs to
# read it before it can write to it. Fix it with `.get()` (calculate_sales.py)
# or `collections.defaultdict` (calculate_sales_using_defaultdict.py).

sales = [
    {"dept": "electronics", "amount": 200},
    {"dept": "clothing", "amount": 50},
    {"dept": "electronics", "amount": 150},
    {"dept": "home", "amount": 100},
    {"dept": "clothing", "amount": 75},
]

result = {}

try:
    for record in sales:
        result[record["dept"]] += record["amount"]
    print(result)
except KeyError as e:
    print(f"KeyError raised for missing key: {e}")
    print("Fix: use result.get(dept, 0) + amount, or collections.defaultdict(int)")
