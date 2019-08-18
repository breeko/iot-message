import json

def print_message(_client, _userdata, message):
    payload = json.loads(message.payload)
    msg = payload.get("message")
    print(msg)

subs = {
    "topic": print_message
}
