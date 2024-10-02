# retrieve_sms_example.py
# This script demonstrates how to retrieve SMS messages received on your mobile phone 
# using the smsmobileapi Python module. You can interact with the received messages in real-time.

from smsmobileapi import SMSSender

# Initialize the SMS sender with your API key
sms = SMSSender(api_key='YOUR_API_KEY')

# Retrieve the list of received SMS messages
received_messages = sms.get_received_messages()

# Print the list of received messages
print('Received SMS Messages:', received_messages)

# Notes:
# - Ensure your phone is connected to the mobile app, and the API key is valid.
# - The response will include details such as the sender's number, message content, and timestamp.
# - You can use this data to process replies and interact with contacts in real-time.
