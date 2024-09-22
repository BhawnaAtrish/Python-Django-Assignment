def find_duplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    
    while True:
        tortoise = nums[tortoise]  # Move tortoise by 1 step
        hare = nums[nums[hare]]    # Move hare by 2 steps
        if tortoise == hare:       # They meet at the cycle
            break
    
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]  # Move both pointers by 1 step
        hare = nums[hare]
    
    return hare  

# Example usage:
nums = [1, 3, 4, 2, 3]
duplicate = find_duplicate(nums)
print(duplicate)  # Output: 3
