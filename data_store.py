import os
import json

data = {
    "user_whitelist": [],
    "user_prefs": {},
    "voice_translation": {},
    "group_admin": {}
}

def load_data():
    global data
    if os.path.exists("data.json"):
        with open("data.json", "r", encoding="utf-8") as f:
            try:
                loaded_data = json.load(f)
                data = {
                    "user_whitelist": loaded_data.get("user_whitelist", []),
                    "user_prefs": {
                        k: set(v) if isinstance(v, list) else v
                        for k, v in loaded_data.get("user_prefs", {}).items()
                    },
                    "voice_translation": loaded_data.get("voice_translation", {}),
                    "group_admin": loaded_data.get("group_admin", {})
                }
                print("✅ 成功讀取資料！")
            except Exception as e:
                print("❌ 讀取 data.json 出錯，使用預設資料")
    else:
        print("🆕 沒找到資料，創建新的 data.json")
        save_data()

def save_data():
    save_data = {
        "user_whitelist": data["user_whitelist"],
        "user_prefs": {
            k: list(v) if isinstance(v, set) else v
            for k, v in data["user_prefs"].items()
        },
        "voice_translation": data["voice_translation"],
        "group_admin": data.get("group_admin", {})
    }
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(save_data, f, ensure_ascii=False, indent=2)
        print("💾 資料已儲存！")
