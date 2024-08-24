from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'hello' in incoming_msg:
        response = 'Hello! How can I help you today?'
    else:
        response = 'I am a bot, please say "hello" to start the conversation.'

    msg.body(response)
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)

