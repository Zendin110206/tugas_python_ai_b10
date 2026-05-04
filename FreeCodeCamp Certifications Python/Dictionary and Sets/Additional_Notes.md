# Python Collection Types Reference

This note compares the four collection types used most often in beginner Python
programs: `list`, `tuple`, `set`, and `dict`. The goal is to make the basic
differences easy to review before choosing the right data structure for a task.

## Comparison Table

| Feature | `list` | `tuple` | `set` | `dict` |
| :--- | :--- | :--- | :--- | :--- |
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` | `{"key": "value"}` |
| Mutable | Yes | No | Yes | Yes |
| Ordered | Yes | Yes | No | Yes, since Python 3.7 |
| Allows duplicates | Yes | Yes | No | Keys: no; values: yes |
| Access style | By index | By index | By membership check | By key |
| Common use | Flexible sequence of values | Fixed sequence of values | Unique values and set operations | Paired key-value data |

## `list`

A `list` is a mutable ordered collection. It is useful when the data needs to
keep its order and may change over time.

```python
fruits = ["apple", "mango", "orange", "apple"]
```

Lists allow duplicates, so `"apple"` can appear more than once.

Common list operations:

| Operation | Example | Purpose |
| :--- | :--- | :--- |
| Add one item at the end | `fruits.append("banana")` | Add a new value after the last item. |
| Insert at a specific index | `fruits.insert(1, "grape")` | Place a value before the current item at that index. |
| Add multiple items | `fruits.extend(["melon", "kiwi"])` | Append every item from another iterable. |
| Remove by value | `fruits.remove("apple")` | Remove the first matching value. |
| Remove by index | `fruits.pop(2)` | Remove and return the item at index `2`. |
| Remove the last item | `fruits.pop()` | Remove and return the final item. |
| Clear all items | `fruits.clear()` | Empty the list. |
| Sort items | `fruits.sort()` | Sort the list in place. |
| Reverse items | `fruits.reverse()` | Reverse the list in place. |
| Count occurrences | `fruits.count("apple")` | Count how many times a value appears. |

Use a list when:

- the order matters
- duplicate values are acceptable
- values need to be added, removed, or updated

## `tuple`

A `tuple` is an immutable ordered collection. It is similar to a list, but once
created, its contents cannot be changed.

```python
coordinates = (10.5, 20.7, 10.5)
```

Tuples are useful when the data should stay fixed, such as coordinates,
constant configuration values, or records that should not be modified.

Common tuple operations:

| Operation | Example | Purpose |
| :--- | :--- | :--- |
| Count occurrences | `coordinates.count(10.5)` | Count how many times a value appears. |
| Find index | `coordinates.index(20.7)` | Return the index of the first matching value. |

Tuples do not support methods such as `.append()`, `.remove()`, or `.sort()`
because those operations would change the data.

If a tuple must be changed, convert it to a list first, modify the list, and
convert it back:

```python
coordinates_list = list(coordinates)
coordinates_list.append(30.2)
coordinates = tuple(coordinates_list)
```

Use a tuple when:

- the order matters
- the values should not be modified
- the data represents a fixed record or pair of related values

## `set`

A `set` is a mutable collection of unique values. It does not preserve a
position-based order, so values cannot be accessed by index.

```python
unique_numbers = {1, 2, 3, 3, 3, 4}
print(unique_numbers)
```

The duplicate `3` values are stored only once.

Common set operations:

| Operation | Example | Purpose |
| :--- | :--- | :--- |
| Add one item | `unique_numbers.add(5)` | Add a single value. |
| Add multiple items | `unique_numbers.update([6, 7, 8])` | Add values from another iterable. |
| Remove existing item | `unique_numbers.remove(3)` | Remove a value and raise an error if it does not exist. |
| Remove item safely | `unique_numbers.discard(10)` | Remove a value if it exists; do nothing if it does not. |
| Remove arbitrary item | `unique_numbers.pop()` | Remove and return an unspecified item. |
| Union | `a.union(b)` | Return all unique values from both sets. |
| Intersection | `a.intersection(b)` | Return values that exist in both sets. |
| Difference | `a.difference(b)` | Return values in `a` that are not in `b`. |

Use a set when:

- only unique values should be stored
- membership checking is important
- mathematical set operations are needed

Example:

```python
registered_users = {"andi", "budi", "citra"}
if "budi" in registered_users:
    print("User found")
```

## `dict`

A `dict` stores data as key-value pairs. Each key must be unique, but values can
be repeated.

```python
profile = {
    "name": "Budi",
    "age": 20,
    "hobby": "Coding",
}
```

Common dictionary operations:

| Operation | Example | Purpose |
| :--- | :--- | :--- |
| Access by key | `profile["name"]` | Return the value for an existing key. |
| Safe access | `profile.get("name")` | Return the value, or `None` if the key does not exist. |
| Add a new pair | `profile["city"] = "Jakarta"` | Add a new key-value pair. |
| Update an existing value | `profile["age"] = 21` | Replace the value for an existing key. |
| Update multiple pairs | `profile.update({"height": 170, "weight": 65})` | Add or update multiple key-value pairs. |
| Remove by key | `profile.pop("hobby")` | Remove a key-value pair and return its value. |
| Remove last inserted pair | `profile.popitem()` | Remove and return the most recently inserted pair. |
| Get all keys | `profile.keys()` | Return a view of all keys. |
| Get all values | `profile.values()` | Return a view of all values. |
| Get all pairs | `profile.items()` | Return a view of key-value pairs. |

Use a dictionary when:

- each value needs a clear label
- data should be accessed by name rather than by position
- the structure represents an object-like record

Example:

```python
for key, value in profile.items():
    print(f"{key}: {value}")
```

## Choosing the Right Collection

| Situation | Recommended type | Reason |
| :--- | :--- | :--- |
| Store a changeable ordered sequence | `list` | The values can be added, removed, sorted, or updated. |
| Store a fixed ordered sequence | `tuple` | The values should remain unchanged. |
| Store unique values only | `set` | Duplicate values are automatically removed. |
| Store labeled information | `dict` | Each value can be accessed through a meaningful key. |

The most important decision is whether the data needs order, uniqueness,
mutability, or named access. Once that requirement is clear, the correct
collection type is usually straightforward.
