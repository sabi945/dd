from twilio.rest import Client

account_sid = 'AC35d1a67c37cab7c11c2eecb3bde8f2dd'
auth_token = '2394eda2cac2d1f70e6bfb5ed3533124'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='apakah kamu berteman dengan nomor ini 0815-2387-9956? kala ya bilang ke padanya ada pesan dari twilio ',
  to='whatsapp:+6285212282606'
)

#   to='whatsapp:+6282229109779'
print(message.sid)