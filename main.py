import requests
import json
import os
import time
import ipaddress
from dotenv import load_dotenv


# Load the environment variables from the .env file
load_dotenv('.env')
api_key = os.getenv('API')


def request(ip):
    time.sleep(1)
    url = f'http://api.ipapi.com/{ip}?access_key={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        data = json.dumps(data, indent=4)
        print(data)
    else:
        print("Error:", response.status_code)


def main():
    while True:
        print('\n'+'-' * 42)
        print('\033[34mExample: 161.185.160.93 (Press q to quit)\033[0m')
        print('-' * 42)
        ip = input("\033[32m" + "\nEnter an IP address: " + "\033[0m").strip().lower()

        if ip == 'q':
            break
        else:
            try:
                ipaddress.ip_address(ip)
                print("Fetching data...\n")
                request(ip)
            except ValueError:
                print(f"\n\033[31mError: {ip} is not a valid IP address.\033[0m")


if __name__ == '__main__':
    main()
