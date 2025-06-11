import os
import json
from config import MASTER_USER_FILE, DEFAULT_MASTER_USER_IDS

def load_master_users():
    if os.path.exists(MASTER_USER_FILE):
        with open(MASTER_USER_FILE, "r", encoding="utf-8") as f:
            return set(json.load(f))
    else:
        save_master_users(DEFAULT_MASTER_USER_IDS)
        return DEFAULT_MASTER_USER_IDS.copy()

def save_master_users(master_set):
    with open(MASTER_USER_FILE, "w", encoding="utf-8") as f:
        json.dump(list(master_set), f, ensure_ascii=False, indent=2)
        print("💾 主人列表已更新！")
