'''import requests
from bs4 import BeautifulSoup

# The URL of the website
URL = "http://210.212.217.214/index.php"

# Start a session
session = requests.Session()

# You might need to fetch the login page first to get any necessary cookies
response = session.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

# Set up the payload for the POST request
payload = {
    "username": "R200300",  # Replace with your username
    "password": "VDFNS"   # Replace with your password
}

# Send the POST request
login_response = session.post(URL, data=payload)

# Convert the response to BeautifulSoup object for easier searching
login_soup = BeautifulSoup(login_response.content, 'html.parser')
print(login_response)

# Check if the success message exists in the response
if "Invalid credentials" in login_response.text:
    print("Login failed!")
else:
    print("Login might be successful!")


# From here, you can navigate to other URLs within the site using the session to remain logged in
import requests
from bs4 import BeautifulSoup

LOGIN_URL = 'http://210.212.217.214/index.php'

# Start a session
session = requests.Session()

# Define the payload
payload = {
    'username': 'R200300',
    'password': 'VDFNS',
    'login': 'Login'  # This is the value of the login button
}

# Post request to login
response = session.post(LOGIN_URL, data=payload)
print(response.content)

# Check if login might have been successful
if 1:
    print("Login might be successful.")
    
    # Parse the content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the image URL using the provided CSS path
    img_tag = soup.select_one("html body table tbody tr td img")
    
    if img_tag:
        img_url = img_tag['src']
        print(f"Image URL: {img_url}")
        
        # Optionally, if you want to download the image
        img_response = session.get(img_url, stream=True)
        with open('my_image.jpg', 'wb') as img_file:
            for chunk in img_response.iter_content(chunk_size=8192):
                img_file.write(chunk)
        print("Image saved as my_image.jpg")
    else:
        print("Image not found.")
else:
    print("Login might have failed.")

# Close the session
session.close()
import requests
from bs4 import BeautifulSoup

LOGIN_URL = 'http://210.212.217.214/index.php'
REDIRECT_URL = 'http://210.212.217.214/redirect.php'

headers = {
    'User-Agent': 'Mozilla/5.0',  # Set a user agent
    'Referer': LOGIN_URL  # Indicate that request is coming after visiting the login page
}

# Start a session
session = requests.Session()

# Get the login page first (sometimes necessary to set initial cookies or get CSRF tokens)
session.get(LOGIN_URL, headers=headers)

# Define the payload
payload = {
    'username': 'YOUR_USERNAME',
    'password': 'YOUR_PASSWORD',
    'login': 'Login'  # This is the value of the login button
}

# Post request to login
response = session.post(LOGIN_URL, data=payload, headers=headers, allow_redirects=True)

# Check the final URL or content
if REDIRECT_URL in response.url:
    print("Login might be successful.")

    # Additional steps, like extracting the image, go here.

else:
    print("Login might have failed.")

# Close the session
session.close()

from selenium import webdriver

# Set up the webdriver (for this example, I'm using Chrome)
browser = webdriver.Chrome()

# Open the login page
browser.get("http://210.212.217.214/index.php")

# Enter the username and password
username_elem = browser.find_element_by_name("username")
username_elem.send_keys("R200300")

password_elem = browser.find_element_by_name("password")
password_elem.send_keys("VDFNS")

# Click the login button
login_button = browser.find_element_by_name("login")
login_button.click()

# Check for successful login by checking the URL or some element on the redirected page
if "redirect.php" in browser.current_url:
    print("Login might be successful.")
    # To get the image
    img_elem = browser.find_element_by_css_selector("html body table tbody tr td img")
    img_url = img_elem.get_attribute("src")
    print("Image URL:", img_url)
else:
    print("Login might have failed.")

# Close the browser when done
browser.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

URL = "http://210.212.217.214/"

# Initialize the Firefox browser
browser = webdriver.Firefox(executable_path='/home/rguktrkvalley/Desktop/EXAMS/final_touch/edc/geckodriver-v0.33.0-linux32')
browser.get(URL)

# Find the username and password fields
username_elem = browser.find_element(By.NAME, "username")
password_elem = browser.find_element(By.NAME, "password")

# Fill out the form and submit
username_elem.send_keys("R200300")
password_elem.send_keys("VDFNS")
password_elem.send_keys(Keys.RETURN)  # Pressing the Return/Enter key to submit the form

# Check if login is successful by looking for some element specific to the login success page
# For the sake of this example, I'll assume there's an element with id "success" on successful login
# Modify this as per the actual structure of your website
try:
    success_elem = browser.find_element(By.CSS_SELECTOR, "html body table tbody tr td img")
    if success_elem:
        print("Login successful!")
        # If you want to save the image:
        with open("profile_image.png", "wb") as file:
            file.write(success_elem.screenshot_as_png)
except:
    print("Login might have failed.")

browser.close()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

def automate_login(username, password):
    URL = "http://210.212.217.214/index.php"
    
    # Define the geckodriver service
    #service = Service('/home/rguktrkvalley/Desktop/EXAMS/final_touch/edc/geckodriver-v0.33.0-linux32')
    service = Service('geckodriver')
    # Initialize the Firefox browser with the service
    browser = webdriver.Firefox()
    browser.get(URL)

    # Find the username, password fields and the submit button
    username_elem = browser.find_element(By.NAME, "username")
    password_elem = browser.find_element(By.NAME, "password")
    submit_elem = browser.find_element(By.NAME, "login")

    # Input the username and password
    username_elem.send_keys(username)
    password_elem.send_keys(password)

    # Click the submit button
    submit_elem.click()

    # After this, you should be logged in. Now, you can perform further operations
    # For example, fetching the image from the specified CSS path
    image_elem = browser.find_element(By.CSS_SELECTOR, "html body table tbody tr td img")
    image_url = image_elem.get_attribute("src")

    # If you want to close the browser after fetching the image URL
    browser.close()

    return image_url

# Test the function
image_url = automate_login("R200300", "VDFNS")
print(f"Image URL: {image_url}")


import asyncio
from pyppeteer import launch

async def automate_login(username, password):
    browser = await launch(headless=False)  # headless=False means the browser GUI will be visible
    page = await browser.newPage()
    
    await page.goto('http://210.212.217.214/index.php')
    
    await page.type('input[name="username"]', username)
    await page.type('input[name="password"]', password)
    await page.click('button[name="login"]')
    
    await asyncio.sleep(5)  # wait for 5 seconds to see the browser action, adjust as needed
    
    # Check if successful by examining some property of the page (URL, specific content, etc.)
    current_url = page.url
    if current_url == "http://210.212.217.214/redirect.php":
        print("Login might be successful")
    else:
        print("Login might have failed")
    
    await browser.close()

# Use asyncio to run the function
asyncio.get_event_loop().run_until_complete(automate_login("R200300", "VDFNS"))

import asyncio
from pyppeteer import launch

async def automate_login(username_str, password_str):
    browser = await launch(headless=False)
    page = await browser.newPage()

    await page.goto('http://210.212.217.214/index.php')

    # filling the form
    await page.type('input[name="username"]', username_str)
    await page.type('input[name="password"]', password_str)

    # submitting the form
    await page.click('button[name="login"]')
    
    # Waiting for the redirect to complete
    await page.waitForNavigation()
    
    # Checking the URL
    current_url = page.url
    print(current_url)

    if "redirect.php" in current_url:
        print("Login might have been successful.")
        
        # get image src
        img_elem = await page.querySelector("html body table tbody tr td img")
        img_src = await page.evaluate('(element) => element.src', img_elem)
        
        # download the image
        img_response = await page.goto(img_src)
        with open('downloaded_image.jpg', 'wb') as file:
            file.write(await img_response.buffer())
        print("Image downloaded successfully!")
    else:
        print("Login might have failed.")

    await browser.close()

username = "R200300"
password = "VDFNS"
asyncio.get_event_loop().run_until_complete(automate_login(username, password))



import asyncio
from pyppeteer import launch

async def automate_login(username, password):
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('http://210.212.217.214/index.php')

    # Fill in the login details
    await page.type('input[name="username"]', username)
    await page.type('input[name="password"]', password)
    await page.click('button[name="login"]')

    try:
        await page.waitForNavigation()
    except:
        print("Navigation took too long. Proceeding with current page...")

    current_url = page.url
    
    if 'redirect.php' in current_url:
        print("Login might be successful.")

        # Locate the image using XPath
        img_element = await page.xpath("/html/body/table/tbody/tr[6]/td/img")
        if img_element:
            img_element = img_element[0]
            img_src = await page.evaluate('(element) => element.src', img_element)

            # Downloading the image
            img_data = await page.goto(img_src)
            with open('downloaded_image.jpg', 'wb') as f:
                f.write(await img_data.buffer())
        else:
            print("Could not locate the image.")
    else:
        print("Login might have failed.")
        
    await browser.close()

# Your credentials
username = "R200075"
password = "IVITX"

asyncio.get_event_loop().run_until_complete(automate_login(username, password))
'''
import asyncio
from pyppeteer import launch

async def automate_login(username, password):
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('http://210.212.217.214/index.php')

    # Fill in the login details
    await page.waitForSelector('input[name="username"]', timeout=10000)
    await page.type('input[name="username"]', username)

    await page.type('input[name="password"]', password)
    await page.click('button[name="login"]')

    try:
        await page.waitForNavigation()
    except:
        print("Navigation took too long. Proceeding with current page...")

    current_url = page.url
    
    if 'redirect.php' in current_url:
        print("Login might be successful.")

        # Get the filename for the image
        filename_element = await page.xpath("/html/body/table/tbody/tr[3]/td")
        if not filename_element:
            print("Could not fetch the filename.")
            await browser.close()
            return
        filename = await page.evaluate('(element) => element.textContent', filename_element[0])

        # Locate the image using XPath
        img_element = await page.xpath("/html/body/table/tbody/tr[6]/td/img")
        if img_element:
            img_element = img_element[0]
            img_src = await page.evaluate('(element) => element.src', img_element)

            # Downloading the image
            img_data = await page.goto(img_src)
            with open(f'{filename}.jpg', 'wb') as f:
                f.write(await img_data.buffer())
        else:
            print("Could not locate the image.")
    else:
        print("Login might have failed.")
        
    await browser.close()

# Your credentials
username = "R200300"
password = "VDFNS"

asyncio.get_event_loop().run_until_complete(automate_login(username, password))

