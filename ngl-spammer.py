import requests
import random
import time

def send_spam_message(username, message, amount):
    for i in range(amount):
        data = {
            'username': f'{username}',
            'question': f'{message}',
            'deviceId': '0',
            'referrer': '',
        }
        try:
            response = requests.post('https://ngl.link/api/submit', data=data)
            if response.status_code == 200:
                print(f"Message {i+1} sent.")
            else:
                print(f"Error sending message {i+1}: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending message {i+1}: {e}")

        # Introduce randomness in time intervals between messages so that i is not detected as a spam instantly 😊
        delay = random.uniform(1, 10) 
        time.sleep(delay)

if __name__ == "__main__":
    username = input("Enter the username: ")
    message = input("Enter the message you want to spam: ")
    while True:
        try:
            amount = int(input("Enter the amount of messages you want to spam: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    send_spam_message(username, message, amount)


