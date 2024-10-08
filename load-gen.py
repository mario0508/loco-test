import requests
import threading


def send_request():
    try:
        response = requests.get('http://localhost:8000')
        print(f"Response code: {response.status_code}")
    except Exception as e:
        print(f"Request failed: {e}")


num_requests = 1000000 


threads = []
for _ in range(num_requests):
    thread = threading.Thread(target=send_request)
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

print("Finished sending requests.")
