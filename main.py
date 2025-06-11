from flask import Flask, request, send_from_directory
import threading
import sys
import os
import time

from linebot_api import line_bot_api, handler, reply
from config import LANGUAGE_MAP
from master_user import load_master_users, save_master_users
from data_store import data, load_data, save_data
from command_menu import create_command_menu
from translate import translate_text, language_selection_message
from admin import is_group_admin
from monitor import monitor_memory, keep_alive

import psutil

app = Flask(__name__)
MASTER_USER_IDS = load_master_users()
load_data()

start_time = time.time()
translate_counter = 0
translate_char_counter = 0

@app.route("/webhook", methods=['POST'])
def webhook():
    # ...原 webhook 處理函式內容完整貼上...
    pass # 請將 main.py 的 webhook 內容貼到這裡（記得根據模組import位置微調）

@app.route("/images/<path:filename>")
def serve_image(filename):
    return send_from_directory('images', filename)

@app.route("/")
def home():
    return "🎉 翻譯小精靈啟動成功 ✨"

if __name__ == '__main__':
    max_retries = 3
    retry_count = 0

    while True:
        try:
            keep_alive_thread = threading.Thread(target=keep_alive, args=(save_data,), daemon=True)
            keep_alive_thread.start()
            print("✨ Keep-Alive機制已啟動")
            app.run(host='0.0.0.0', port=5000)
        except Exception as e:
            retry_count += 1
            print(f"❌ 發生錯誤 (重試 {retry_count}/{max_retries}): {str(e)}")
            if retry_count >= max_retries:
                print("🔄 達到最大重試次數,完全重啟程序...")
                os._exit(1)
            print(f"🔄 5秒後重試...")
            time.sleep(5)
            continue
