# test message reply
from flask import Flask, request, abort
import requests
import json
Channel_access_token = 'x5wQFRGb2nx1vqs8DfRuaauNMxcWnKI9Z+tGZed3bBMGSAvqDDjWRI+QsnWrGhMGv1o25HYISK83AIDkDVfjxXQC6KITKjMVQJrULoVHMmwwSx1rXKqrW36aPfwqgc0ykTLm5xy2HrmbDSoK4nfrKQdB04t89/1O/w1cDnyilFU='
app = Flask(__name__)


def COVID_TODAY():
    data = requests.get('https://covid19.th-stat.com/api/open/today')
    json_data = json.loads(data.text)
    covid = json_data['Confirmed']

    return covid


def COVID_NEW():
    data = requests.get('https://covid19.th-stat.com/api/open/today')
    json_data = json.loads(data.text)
    covid = json_data['NewConfirmed']

    return covid


@app.route('/', methods=['POST', 'GET'])

def webhook():
    if request.method == 'POST':
        payload = request.json
        Reply_token = payload['events'][0]['replyToken']
        message = payload['events'][0]['message']['text']
        if "new" in message:
            Reply_messasge = 'ผู้ป่วยรายใหม่วันนี้ : {}'.format(COVID_NEW())
            ReplyMessage(Reply_token, Reply_messasge, Channel_access_token)
        elif "โควิด" in message:
            Reply_messasge = 'ผู้ป่วยสะสมวันนี้ของโควิด: {}'.format(COVID_TODAY())
            ReplyMessage(Reply_token, Reply_messasge, Channel_access_token)
            return request.json, 200
        elif request.method == 'GET':
            return 'GET port 80', 200
        else:
            abort(400)


@app.route('/webhook')
def hello():
    return 'Get port 80', 200


def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer {}'.format(Line_Acees_Token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }
    data = {
        "replyToken": Reply_token,
        "messages": [{
            "type": "text",
            "text": TextMessage
        }]
    }
    data = json.dumps(data)
    r = requests.post(LINE_API, headers=headers, data=data)
    return 200
    if __name__ == '__main__':
        app.run(port=80)
