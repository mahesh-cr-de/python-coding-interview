sales = [ {"dept": "electronics", "amount": 200}, 
         {"dept": "clothing", "amount": 50}, 
         {"dept": "electronics", "amount": 150}, 
         {"dept": "home", "amount": 100}, 
         {"dept": "clothing", "amount": 75} ]

result = {}

#defaultdict is a special type of dictionary from Python’s collections module.
from collections import defaultdict 

def calculate_sales(sales):
    #Here we are creating a dictionary where every new key automatically gets a default value.
    result = defaultdict(int) 

    for record in sales:
        result[record["dept"]] += record["amount"]
    return dict(result)

print(calculate_sales(sales))
