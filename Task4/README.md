# Python Rate Limiter

This project implements a simple **rate limiter** in Python. The rate limiter restricts the number of requests a user can make within a defined time window. Specifically, each user is allowed to make up to **5 requests per minute**.

## Features

- Limits the number of requests a user can make within a specific time window (1 minute).
- Handles multiple users with individual rate limits.
- Designed to work in a **concurrent environment** using thread locks for safety.
- Configurable **request limit** and **time window**.

## Requirements

- Python 3.x

## Usage
This rate limiter is primarily designed for **offline Python scripts** where requests are controlled locally, for example, a script making API calls.

### Installation

Clone the repository or copy the script to your local machine.

### Running the Script

You can run the rate limiter using Python:

```bash
python rate_limiter.py
```

## API

### `RateLimiter` Class

#### `__init__(self, max_requests=5, time_window=60)`

- **max_requests**: The maximum number of requests a user can make within the time window. Defaults to 5.
- **time_window**: The time window in seconds during which the rate limit applies. Defaults to 60 seconds (1 minute).

#### `allow_request(self, user_id)`

- **user_id**: A string representing the ID of the user making the request.
- Returns `True` if the user is allowed to make a request, otherwise returns `False`.

### Concurrency Handling

- The rate limiter is designed to work in a highly concurrent environment.
- It uses a **threading lock** (`threading.Lock()`) to ensure that requests from multiple threads or processes are handled safely.

## Configuration

The rate limiter can be configured with custom limits by passing arguments to the `RateLimiter` constructor:

```python
rate_limiter = RateLimiter(max_requests=10, time_window=120)  # 10 requests per 2 minutes
```
## Adapting for an Online Django Application

If you need to implement this rate limiting mechanism in an online Django application, you will need to account for the web environment where requests are made by multiple users over the network. Here’s how you can adapt this for Django:

1. **Use Django Middleware**:  
   To apply rate limiting globally or to specific views, you can create a custom middleware that uses similar logic as this rate limiter. In the middleware, track requests based on user IDs or IP addresses, and store request data in Django's caching framework (e.g., using Redis, Memcached, etc.).

2. **Store Request Data in Cache**:  
   Unlike local scripts where request timestamps are stored in memory, in a Django application you would need to store the request data in a shared cache like Redis. This ensures that rate limiting works across multiple web server instances.

3. **Integrating with Views**:  
   You can implement rate limiting at the view level by adding logic in views or using Django decorators. If the limit is exceeded, you can return a `429 Too Many Requests` response.

### Example for Django View:
```python
from django.core.cache import cache
from django.http import JsonResponse

def rate_limiter(request, user_id, max_requests=5, time_window=60):
    request_count = cache.get(user_id, 0)
    
    if request_count >= max_requests:
        return JsonResponse({"error": "Too many requests"}, status=429)
    
    cache.set(user_id, request_count + 1, timeout=time_window)
    return None  # Proceed with the request

# Usage in a view
def my_view(request):
    user_id = request.user.id if request.user.is_authenticated else request.META['REMOTE_ADDR']
    
    rate_limit_response = rate_limiter(request, user_id)
    if rate_limit_response:
        return rate_limit_response  # Return 429 if rate limit exceeded

    return JsonResponse({"message": "Request processed successfully!"})
```
