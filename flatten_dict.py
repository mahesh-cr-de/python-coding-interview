def flatten_dict(d, parent_key=""):
    flattened = {}

    for key, value in d.items():

        new_key = f"{parent_key}.{key}" if parent_key else key

        if isinstance(value, dict):
            flattened.update(flatten_dict(value, new_key))
        else:
            flattened[new_key] = value

    return flattened


input_dict = {
    "user": {
        "id": 123,
        "personal_info": {
            "name": "Alex",
            "email": "alex@example.com"
        }
    },
    "status": "active"
}

result = flatten_dict(input_dict)

print(result)
