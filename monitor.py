import psutil
import gc
import os
import time
import requests

def monitor_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_usage_mb = memory_info.rss / 1024 / 1024
    gc.collect()
    process.memory_percent()
    return memory_usage_mb

def keep_alive(save_data_func):
    retry_count = 0
    max_retries = 3
    restart_interval = 10800
    last_restart = time.time()

    while True:
        try:
            current_time = time.time()
            if current_time - last_restart >= restart_interval:
                print("⏰ 執行定時重啟...")
                save_data_func()
                os._exit(0)
            response = requests.get('http://0.0.0.0:5000/', timeout=10)
            if response.status_code == 200:
                print("🔄 Keep-Alive請求成功")
                retry_count = 0
            else:
                raise Exception(f"請求返回狀態碼: {response.status_code}")
        except Exception as e:
            retry_count += 1
            print(f"❌ Keep-Alive請求失敗 (重試 {retry_count}/{max_retries})")
            if retry_count >= max_retries:
                print("🔄 重啟伺服器...")
                os._exit(1)
            time.sleep(30)
            continue
        time.sleep(300)
