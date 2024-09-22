from typing import List, Dict, Callable

def aggregate_data(data: List[Dict], key: str, aggregator: Callable):
    grouped_data = {}
    
    # Group dictionaries by the provided key
    for item in data:
        group_key = item[key]
        if group_key not in grouped_data:
            grouped_data[group_key] = []
        grouped_data[group_key].append(item)
    
    # Apply the aggregator function to each group
    aggregated_result = {group: aggregator(group_items) for group, group_items in grouped_data.items()}
    
    return aggregated_result

# Example of using the function
data = [
    {'category': 'fruits', 'quantity': 10},
    {'category': 'vegetables', 'quantity': 15},
    {'category': 'fruits', 'quantity': 20},
    {'category': 'vegetables', 'quantity': 10},
    {'category': 'fruits', 'quantity': 5}
]

# Aggregator function that sums the 'quantity' values
def sum_quantities(items):
    return sum(item['quantity'] for item in items)

# Aggregating data by 'category' using the sum_quantities function
result = aggregate_data(data, 'category', sum_quantities)

print(result)
