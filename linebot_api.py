from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage, FlexSendMessage
from config import CHANNEL_ACCESS_TOKEN, CHANNEL_SECRET

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

def reply(token, message_content):
    if isinstance(message_content, dict):
        if message_content.get("type") == "flex":
            message = FlexSendMessage(alt_text=message_content["altText"],
                                      contents=message_content["contents"])
        else:
            message = TextSendMessage(text=message_content["text"])
    elif isinstance(message_content, list):
        message = [
            TextSendMessage(text=m["text"]) if m["type"] == "text" else m
            for m in message_content
        ]
    line_bot_api.reply_message(token, message)
