import asyncio
import httpx
import time

# ENDPOINT = "http://127.0.0.1:8000/hello-world" 
# ENDPOINT = "http://127.0.0.1:8000/async-hello-world"
# ENDPOINT = "http://127.0.0.1:8000/non-async"
# ENDPOINT = "http://127.0.0.1:8000/incorrect-async-blocking-request"
# ENDPOINT = "http://127.0.0.1:8000/truely-async"
# ENDPOINT = "http://127.0.0.1:8000/cpu-bound-with-async"  #uvicorn main:app --workers 4 --port 8000
ENDPOINT = "http://127.0.0.1:8000/cpu-bound-without-async" # uvicorn main:app --workers 4 --port 8000

CONCURRENT_USERS = 5
TOTAL_TIME = 0
success_count = 0


async def make_request(user_id):
    """Simulate a single user request."""
    async with httpx.AsyncClient() as client:
        global TOTAL_TIME
        global success_count

        start_time = time.time()
        try:
            response = await client.get(ENDPOINT, timeout=100.0)
            elapsed_time = time.time() - start_time
            TOTAL_TIME += elapsed_time
            success_count += 1
            print(f"User {user_id}: Status Code: {response.status_code}, Time Taken: {elapsed_time:.2f}s")
        except Exception as e:
            print(f"User {user_id}: Failed with error: {type(e).__name__} - {e}")


async def simulate_users():
    """Simulate multiple concurrent users."""
    global success_count

    tasks = [make_request(user_id) for user_id in range(1, CONCURRENT_USERS + 1)]
    await asyncio.gather(*tasks)

    if success_count > 0:
        print(f"Average time taken: {TOTAL_TIME / success_count:.2f}s")
    else:
        print("No successful requests to calculate average time.")



asyncio.run(simulate_users())
