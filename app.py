from flask import Flask, request, abort
import base64
import hashlib
import hmac

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('BanLnTCb802Zvxu88pspr3aL6SsOIXG9FLFY3E1drgaLsJCqfJ/X48TLgAIIWEpEz4nbw4u4sohV3ZS5G9Dt4p36kOXQ4ILbf339+C6wrwM/uEMMBA6jWKrrBrXn4dDLWc5MHltB/wdr9eRnVLSmagdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ab4a046624a52e60f5a3ffe253be1729')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    # signature = request.headers['X-LINE-SIGNATURE']
	channel_secret = 'ab4a046624a52e60f5a3ffe253be1729' # Channel secret string
	# Request body string
	print request.headers
	print "BODY==========="
	body = request.get_data(as_text=True)
	print body
	hash = hmac.new(channel_secret.encode('utf-8'), body.encode('utf-8'), hashlib.sha256).digest()
	signature = request.headers['X-Line-Signature']

    # get request body as text
	app.logger.info("Request body: " + body)

    # handle webhook body
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)

	return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()