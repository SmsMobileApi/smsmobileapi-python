# send_sms_example.py
# This script demonstrates how to send an SMS using the smsmobileapi Python module.
# The SMS will be sent from your mobile phone using your phone number, 
# and the recipient can reply directly to your number.

from smsmobileapi import SMSSender

# Initialize the SMS sender with your API key
sms = SMSSender(api_key='YOUR_API_KEY')

# Set the recipient's phone number and the message content
recipient_number = '+123456789'  # Replace with the actual phone number
message_content = 'Hello from Python! This is a test SMS.'

# Send the SMS
response = sms.send_message(to=recipient_number, message=message_content)

# Print the response from the API, which contains details about the SMS status
print('Send SMS Response:', response)

# Notes:
# - Ensure your phone is connected to the mobile app, and the API key is valid.
# - The SMS is sent through your mobile phone, so it's free if covered by your mobile plan.
