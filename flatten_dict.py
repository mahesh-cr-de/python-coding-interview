def flatten_dict(d, parent_key="", sep="."):
    flattened = {}

    for key, value in d.items():

        new_key = f"{parent_key}{sep}{key}" if parent_key else key

        if isinstance(value, dict):
            flattened.update(flatten_dict(value, new_key, sep))
        elif isinstance(value, list):
            # flatten dicts inside lists too, e.g. "user.roles.0" -> "admin"
            for index, item in enumerate(value):
                list_key = f"{new_key}{sep}{index}"
                if isinstance(item, dict):
                    flattened.update(flatten_dict(item, list_key, sep))
                else:
                    flattened[list_key] = item
        else:
            flattened[new_key] = value

    return flattened


input_dict = {
    "user": {
        "id": 123,
        "personal_info": {
            "name": "Alex",
            "email": "alex@example.com"
        },
        "roles": ["admin", "editor"]
    },
    "status": "active"
}

result = flatten_dict(input_dict)

print(result)
# {'user.id': 123, 'user.personal_info.name': 'Alex',
#  'user.personal_info.email': 'alex@example.com',
#  'user.roles.0': 'admin', 'user.roles.1': 'editor', 'status': 'active'}
