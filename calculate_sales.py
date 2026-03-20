sales = [ {"dept": "electronics", "amount": 200}, 
         {"dept": "clothing", "amount": 50}, 
         {"dept": "electronics", "amount": 150}, 
         {"dept": "home", "amount": 100}, 
         {"dept": "clothing", "amount": 75} ]

result = {}

for record in sales:
    if record["dept"] in result:
        result[record["dept"]] += record["amount"]
    else:
        result[record["dept"]] = record["amount"]
print(result)
