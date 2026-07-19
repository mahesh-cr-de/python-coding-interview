# Python Interview Questions

This repository contains solutions to common Python interview questions explained in my YouTube series.
https://www.youtube.com/@DataEngWithMahesh

## Table of Contents

1. [Reverse a String](#1-reverse-a-string)
2. [Flatten a Nested Dictionary](#2-flatten-a-nested-dictionary)
3. [Calculate Total Sales by Department](#3-calculate-total-sales-by-department)
4. [Most Watched Movies](#4-most-watched-movies)

Each problem includes a problem statement, a Python solution, and a short explanation.

---

## 1. Reverse a String

**File:** [reverse_string.py](reverse_string.py)

Reverse a string without using `str.reverse()` (strings are immutable in Python, so it doesn't exist).

**Approaches covered:**
- Slicing (`s[::-1]`) - most idiomatic, O(n)
- Prepending characters in a loop - O(n²) due to repeated string concatenation
- Walking the index backwards
- `"".join(reversed(s))` - O(n), avoids repeated concatenation

## 2. Flatten a Nested Dictionary

**File:** [flatten_dict.py](flatten_dict.py)

Given an arbitrarily nested dictionary (including lists of values/dicts), produce a single-level
dictionary whose keys are dot-separated paths to each leaf value.

```python
input_dict = {
    "user": {
        "id": 123,
        "personal_info": {"name": "Alex", "email": "alex@example.com"},
        "roles": ["admin", "editor"]
    },
    "status": "active"
}
# -> {'user.id': 123, 'user.personal_info.name': 'Alex',
#     'user.personal_info.email': 'alex@example.com',
#     'user.roles.0': 'admin', 'user.roles.1': 'editor', 'status': 'active'}
```

Solved recursively; list items are indexed by position, and dicts nested inside lists are
flattened too.

## 3. Calculate Total Sales by Department

Given a list of sale records (`{"dept": ..., "amount": ...}`), sum the amount per department.
This question is walked through in three stages, each in its own file:

| File | Approach |
|---|---|
| [calculate_sales.py](calculate_sales.py) | Plain dict with an `if dept in result` check |
| [KeyError_test.py](KeyError_test.py) | Why `result[dept] += amount` alone raises `KeyError`, caught and explained |
| [calculate_sales_using_defaultdict.py](calculate_sales_using_defaultdict.py) | Clean fix using `collections.defaultdict(int)` |

All three produce `{'electronics': 350, 'clothing': 125, 'home': 100}`.

## 4. Most Watched Movies

**File:** [most_watched_movies.py](most_watched_movies.py)

Given a dictionary mapping user IDs to the list of movies each user watched, return the
movie(s) watched by the highest number of *distinct* users. A movie should only count once
per user, even if that user watched it multiple times.

```python
watch_history = {
    "user1": ["Inception", "Interstellar", "Inception"],  # rewatch - still counts once
    "user2": ["Avatar", "Inception", "Titanic"],
    "user3": ["Avatar", "Interstellar", "Inception"],
    "user4": ["Inception", "Avatar"],
    "user5": ["Avatar", "Titanic"],
}
# -> ['Inception', 'Avatar']  (tie: both watched by 4 distinct users)
```

Includes two implementations: one using `collections.Counter`, and a plain-dict version with
no imports.

---

## YouTube Series

Channel: Data Engineering with Mahesh (https://www.youtube.com/@DataEngWithMahesh)

This series covers:
- Python interview questions
- Data engineering concepts
- Coding interview preparation
