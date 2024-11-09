from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC  # Import EC for explicit wait

import os
import time

# Constants
PHONE_NUMBER = "+91 94872 15043"  # Recipient's phone number in international format (without +)
MESSAGE = "Happy Birthday to you da ! Hope you have an amazing year ahead!"
VIDEO_PATH = "/path/to/birthday_video.mp4"  # Path to the video file

# Path to Chrome data for storing session
SESSION_DIR = os.path.join(os.path.dirname(__file__), "chrome_data")

# Set Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")
#
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--window-size=1920x1080")

chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")  # Disable sandboxing (often needed for Docker/EC2)
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
chrome_options.add_argument("--remote-debugging-port=9222")  # Use debugging port
chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration (can cause issues on Linux)
chrome_options.add_argument("--single-process")  # Run Chrome in a single process
chrome_options.add_argument("--user-data-dir={}".format(SESSION_DIR))  # Session data path


# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Open WhatsApp Web with the direct phone number URL
    driver.get(f"https://web.whatsapp.com/send?phone={PHONE_NUMBER}")
    wait = WebDriverWait(driver, 30)

    # Wait for QR code scan if first login
    if "--headless" not in chrome_options.arguments:
        print("Please scan the QR code on WhatsApp Web.")
        time.sleep(1)  # Allow time for QR code scanning on the first run

    # Wait for the chat to load
    chat_window = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true" and @aria-placeholder="Type a message"]')))

    # Click on the editable div (optional, depending on the situation)
    chat_window.click()

    # Type content into the editable div
    chat_window.send_keys(MESSAGE)
    chat_window.send_keys(Keys.RETURN)

    chat_window.send_keys("https://google.com")
    chat_window.send_keys(Keys.RETURN)


    time.sleep(3)


    wait.until(EC.presence_of_element_located(
        (By.XPATH, '//div[@contenteditable="true" and @aria-placeholder="Type a message"]')))

    chat_window.click()

    # Send the third message
    chat_window.send_keys("**Ithu automated message da coding vazhiya send aguthu. Morning pesran da**")
    chat_window.send_keys(Keys.RETURN)

    time.sleep(3)

    print("Birthday message sent successfully!")

    print("Birthday message sent successfully!")

finally:
    driver.quit()