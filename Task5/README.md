# aggregate_data Function - README

## Overview

The `aggregate_data` function allows you to group a list of dictionaries based on a specified key and apply an aggregator function to the grouped data. This can be useful for summarizing or manipulating data in various ways (e.g., summing values, averaging, counting occurrences, etc.) without using external libraries like `itertools`.

## Function Signature

```python
def aggregate_data(data: List[Dict], key: str, aggregator: Callable):
```

- `data`: A list of dictionaries that contain the data to be aggregated.
- `key`: The dictionary key by which the data will be grouped.
- `aggregator`: A function that processes the grouped data and returns an aggregated result.

## Key Features

- **Custom Grouping**: You can group data by any key present in the dictionaries.
- **Flexible Aggregation**: You can pass any aggregation function that suits your use case (e.g., summing, counting, finding max/min).
- **No External Libraries**: The implementation does not rely on external libraries, such as `itertools`, making it lightweight and adaptable.

## Example Use Case

### Sample Data

```python
data = [
    {'category': 'fruits', 'quantity': 10},
    {'category': 'vegetables', 'quantity': 15},
    {'category': 'fruits', 'quantity': 20},
    {'category': 'vegetables', 'quantity': 10},
    {'category': 'fruits', 'quantity': 5}
]
```

### Aggregator Function

The example aggregator function `sum_quantities` sums up the 'quantity' field from the grouped dictionaries:

```python
def sum_quantities(items):
    return sum(item['quantity'] for item in items)
```

### Aggregating the Data

You can group and aggregate the data by the 'category' key, summing up the 'quantity' for each category:

```python
result = aggregate_data(data, 'category', sum_quantities)
```

### Output

The output will be:

```python
{'fruits': 35, 'vegetables': 25}
```

This indicates that the total quantity of fruits is 35 and the total quantity of vegetables is 25.

## How It Works

1. **Grouping by Key**: The function loops through each dictionary in the input data, using the provided key to group dictionaries into a `grouped_data` dictionary.
2. **Applying the Aggregator**: For each group, the aggregator function is applied to the items, and the results are stored in the final `aggregated_result` dictionary.

## How to Run

1. Define your dataset as a list of dictionaries.
2. Create a custom aggregation function that fits your use case.
3. Call the `aggregate_data` function with your data, the key to group by, and the aggregator function.

```python
# Example usage
print(result)  # Outputs: {'fruits': 35, 'vegetables': 25}
```


