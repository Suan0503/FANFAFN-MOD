import requests
from config import LANGUAGE_MAP

def translate_text(text, target_lang):
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl={target_lang}&dt=t&q={text}"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()[0][0][0]
    else:
        return "翻譯失敗QQ"

def language_selection_message():
    contents = [{
        "type": "button",
        "style": "primary",
        "color": "#0099FF",
        "action": {
            "type": "postback",
            "label": label,
            "data": f"lang:{code}"
        }
    } for label, code in LANGUAGE_MAP.items()]
    contents.append({
        "type": "button",
        "style": "secondary",
        "action": {
            "type": "postback",
            "label": "🔄 重設翻譯設定",
            "data": "reset"
        }
    })
    return {
        "type": "flex",
        "altText": "🌍 請選擇翻譯語言",
        "contents": {
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [{
                    "type": "text",
                    "text": "🌍 翻譯小精靈選單",
                    "weight": "bold",
                    "size": "lg",
                    "color": "#0099FF"
                }, {
                    "type": "text",
                    "text": "請選擇你要翻譯的語言 ✈️",
                    "size": "sm",
                    "color": "#555555"
                }]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": contents
            },
            "footer": {
                "type": "box",
                "layout": "horizontal",
                "contents": [{
                    "type": "text",
                    "text": "🏝️",
                    "align": "end",
                    "size": "lg"
                }]
            }
        }
    }
