# Keylogger
"Exploring cybersecurity with an educational keylogger demo. Learn about potential threats responsibly. Misuse is strictly discouraged. Knowledge is power."


---

**Keylogger with Enhanced Features**

This repository contains a Python keylogger script with extended functionalities, designed to provide insights into cybersecurity awareness and help users understand potential threats. Please note that the use of keyloggers for malicious purposes is strongly discouraged and may be illegal. The primary intent of this project is to educate, research, and promote ethical awareness.

**Features:**

1. **Basic Keylogging:** The script captures keystrokes and maintains a log of them.

2. **Webcam Capture:** The keylogger can take snapshots using the webcam.

3. **Screenshot Capture:** It can capture screenshots of a specified region.

4. **Active Window Tracking:** The script logs the titles of active windows.

5. **Website Tracking:** When applicable, it tracks URLs visited in supported browsers.

6. **Webhook Integration:** The captured data, screenshots, and URLs are sent to a Discord webhook for reporting.

7. **Interval Reporting:** The script reports captured data at regular intervals.

8. **Stealth:** The keylogger once executed hides and runs in the backgroud of the computer without its victim knowing about it. 

**Usage Instructions:**

1. Ensure you have the required packages installed. You can do this by running `pip install -r requirements.txt`.

2. The script requires the `dhooks`, `pynput`, `pyautogui`, and `opencv-python` packages to function correctly.

3. Modify the `WEBHOOK_URL` variable with the URL of your Discord webhook.

4. Adjust the `TIME_INTERVAL` to control the reporting frequency.

5. Run the script and let it monitor keystrokes, capture screenshots, and track URLs (if applicable).

6. This project serves as an educational tool to showcase keylogger behavior and its potential ethical use in cybersecurity awareness and research.

**Ethical Considerations:**

- **Use Responsibly:** This keylogger script should be used responsibly, and any form of misuse is discouraged.

- **Respect Legalities:** It is essential to adhere to ethical and legal guidelines while using or experimenting with such tools.

- **Educational Purposes:** The primary goal is to educate about potential security threats and techniques.

- **Privacy Awareness:** Respect the privacy of individuals and systems at all times.

**Disclaimer:**

The creators of this repository do not endorse or encourage the use of keyloggers for malicious purposes. The script is provided for educational and ethical understanding of cybersecurity practices.

Remember, knowledge is a powerful tool when wielded responsibly and ethically. Always use this tool with good intentions and adhere to applicable laws and regulations.

---

Implementing Discord Webhook to get Keystrokes:

Access Your Discord Server:
Log in to your Discord account and navigate to the server where you want to add the webhook.

Server Settings:
Click on the server name to open the drop-down menu, then select "Server Settings."

Integrations:
In the left sidebar, click on "Integrations."

Webhooks:
Scroll down and click on the "Webhooks" section.

Create Webhook:
Click the "Create Webhook" button.

Webhook Setup:

Name: Give your webhook a name. This is the name that will appear as the sender when the webhook posts.
Channel: Choose the text channel where the webhook messages will be sent.
Webhook Avatar: You can set an avatar image for the webhook (optional).
Copy Webhook URL:
After setting up the webhook, a webhook URL will be generated. This URL is unique and acts as the endpoint for sending messages to the webhook.

Linking Webhook to Your Script:

Python Code:
In your Python script, you need to use the dhooks library to send messages to the webhook. Make sure you have the dhooks package installed (you can install it using pip).

Replace Webhook URL:
Locate the WEBHOOK_URL variable in the script and replace it with the URL of the webhook you created.

Run Your Script:
Run your Python script. It should now send messages, screenshots, or other data to the specified Discord channel via the webhook.
