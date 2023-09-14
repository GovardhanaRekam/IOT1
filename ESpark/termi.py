
import subprocess
import time
import requests
from bs4 import BeautifulSoup

def start_ngrok():
    # Step 1: Open terminal and run ngrok
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'cd ~/Downloads/ngrok-v3-stable-linux-amd64 && ./ngrok http 0.0.0.0:8000'])

    # Step 2: Wait for 5 seconds
    time.sleep(5)

    # Step 3: Scrape the ngrok web interface
    response = requests.get('http://localhost:4040/status')
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extracting the required data from the scraped content
    web_interface = soup.body.get_text().split("Web Interface")[1].split("\n")[1].strip()
    forwarding = soup.body.get_text().split("Forwarding")[1].split("\n")[1].strip()

    return web_interface, forwarding

if __name__ == "__main__":
    web_interface, forwarding = start_ngrok()
    print("Web Interface Link:", web_interface)
    print("Forwarding Link:", forwarding)
'''
import subprocess
import time
import requests
from bs4 import BeautifulSoup

def start_ngrok():
    # Step 1: Open terminal and run ngrok
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'cd ~/Downloads/ngrok-v3-stable-linux-amd64 && ./ngrok http 5000'])

    # Step 2: Wait for 5 seconds
    time.sleep(15)

    # Step 3: Scrape the ngrok web interface
    response = requests.get('http://localhost:4040/status')
    soup = BeautifulSoup(response.content, 'html.parser')
    
    text_content = soup.body.get_text()

    # Extracting the required data from the scraped content
    web_interface = None
    forwarding = None

    if "Web Interface" in text_content:
        web_interface = text_content.split("Web Interface")[1].split("\n")[1].strip()
    
    if "Forwarding" in text_content:
        forwarding = text_content.split("Forwarding")[1].split("\n")[1].strip()

    return web_interface, forwarding

if __name__ == "__main__":
    web_interface, forwarding = start_ngrok()
    
    if web_interface:
        print("Web Interface Link:", web_interface)
    else:
        print("Web Interface Link not found!")

    if forwarding:
        print("Forwarding Link:", forwarding)
    else:
        print("Forwarding Link not found!")

import subprocess
import time
import re

def start_ngrok():
    # Run the ngrok command and capture the output
    output = subprocess.check_output(['./ngrok', 'http', '5000'], cwd='/home/amma/Downloads/ngrok-v3-stable-linux-amd64', text=True)

    # Use regex to extract the Web Interface and Forwarding URLs
    web_interface_match = re.search(r"Web Interface\s+([^\s]+)", output)
    forwarding_match = re.search(r"Forwarding\s+([^\s]+)", output)

    web_interface = web_interface_match.group(1) if web_interface_match else None
    forwarding = forwarding_match.group(1) if forwarding_match else None
    
    return web_interface, forwarding

if __name__ == "__main__":
    web_interface, forwarding = start_ngrok()
    
    if web_interface:
        print("Web Interface Link:", web_interface)
    else:
        print("Web Interface Link not found!")

    if forwarding:
        print("Forwarding Link:", forwarding)
    else:
        print("Forwarding Link not found!")

import subprocess
import time
import re

def start_ngrok():
    # Step 1: Start ngrok and pipe its output
    cmd = ['./ngrok', 'http', '5000']
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='/home/amma/Downloads/ngrok-v3-stable-linux-amd64')

    # Allow ngrok some time to initialize and then read its output
    time.sleep(5)
    output = process.stdout.read().decode('utf-8')

    # Step 2: Use regex to extract the Web Interface and Forwarding URLs
    web_interface_match = re.search(r"Web Interface\s+([^\s]+)", output)
    forwarding_match = re.search(r"Forwarding\s+([^\s]+)", output)

    web_interface = web_interface_match.group(1) if web_interface_match else None
    forwarding = forwarding_match.group(1) if forwarding_match else None
    
    return web_interface, forwarding

if __name__ == "__main__":
    web_interface, forwarding = start_ngrok()
    
    if web_interface:
        print("Web Interface Link:", web_interface)
    else:
        print("Web Interface Link not found!")

    if forwarding:
        print("Forwarding Link:", forwarding)
    else:
        print("Forwarding Link not found!")
'''
