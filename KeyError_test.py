sales = [ {"dept": "electronics", "amount": 200}, 
         {"dept": "clothing", "amount": 50}, 
         {"dept": "electronics", "amount": 150}, 
         {"dept": "home", "amount": 100}, 
         {"dept": "clothing", "amount": 75} ]

result = {}
#this will throw KeyError. To avoid this we have to use defaultdict module
for record in sales:
    result[record["dept"]] += record["amount"]
print(result)
