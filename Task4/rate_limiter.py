import time
import threading

class RateLimiter:
    def __init__(self, max_requests=5, time_window=60):
        self.max_requests = max_requests    # Maximum number of requests allowed in the time window
        self.time_window = time_window      # Time window for counting requests (in seconds)
        self.user_requests = {}             # Dictionary to store request timestamps for each user
        self.lock = threading.Lock()        # Lock to ensure thread safety
    
    def allow_request(self, user_id):
        """
        Determines whether a user is allowed to make a request based on the number
        of requests they have made within the defined time window (default is 5 requests per minute).
        """
        current_time = time.time()

        with self.lock:
            if user_id not in self.user_requests:
                # Initialize request tracking for new users
                self.user_requests[user_id] = []
            
            # Remove requests older than the time window
            self.user_requests[user_id] = [
                timestamp for timestamp in self.user_requests[user_id]
                if current_time - timestamp < self.time_window
            ]
            
            # Allow the request if the user hasn't hit the limit, otherwise deny
            if len(self.user_requests[user_id]) < self.max_requests:
                self.user_requests[user_id].append(current_time)
                return True
            else:
                return False

# Example usage:
rate_limiter = RateLimiter()

# Simulating multiple requests for user 'user1'
user_id = "user1"

for i in range(7):
    if rate_limiter.allow_request(user_id):
        print(f"Request {i+1} for {user_id} allowed")
    else:
        print(f"Request {i+1} for {user_id} denied")
