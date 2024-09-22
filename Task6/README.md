# Find Duplicate Number

This script implements a function to find a duplicate number in a list of integers. The solution uses the Floyd's Tortoise and Hare (Cycle Detection) algorithm to efficiently identify the duplicate.

## Functionality

- `find_duplicate(nums)`: This function takes a list of integers and returns the duplicate number.

## Example Usage

```python
nums = [1, 3, 4, 2, 3]
duplicate = find_duplicate(nums)
print(duplicate)  # Output: 3
