import queue  
import random
import time

request_queue = queue.Queue()

request_counter = 1

def generate_request():
    global request_counter
    request_data = f"Заявка з ID {request_counter}"
    request_queue.put(request_data)
    print(f"{request_data} додана до черги.")
    request_counter += 1

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Обробка {request}...")
        
        time.sleep(random.uniform(0.5, 1.5))
        print(f"{request} успішно оброблена.")
    else:
        print("Чергa пуста. Немає заявок для обробки.")

def main():
    try:
        while True:
            if random.choice([True, False]):
                generate_request()
            
            process_request()
            
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nПрограма завершена.")

if __name__ == "__main__":
    main()
