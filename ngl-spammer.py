import requests

username = input("Enter the username: ")
message = input("Enter the message you want to spam: ")
amount = int(input("Enter the amount of messages you want to spam: "))

for i in range(amount):
    dict = {
            'username': f'{username}',
            'question': f'{message}',
            'deviceId': '0',
            'referrer': '',
        }
    response = requests.post('https://ngl.link/api/submit', data=dict)

    if response.status_code == 200:
        print(f"Message {i+1} sent.")
    else:
        print(f"Error sending message {i+1}.")



