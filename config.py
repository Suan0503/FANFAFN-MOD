import os

CHANNEL_ACCESS_TOKEN = os.getenv('CHANNEL_ACCESS_TOKEN')
CHANNEL_SECRET = os.getenv('CHANNEL_SECRET')

LANGUAGE_MAP = {
    '🇹🇼 中文': 'zh-TW',
    '🇺🇸 英文': 'en',
    '🇹🇭 泰文': 'th',
    '🇻🇳 越南文': 'vi',
    '🇲🇲 緬甸文': 'my',
    '🇰🇷 韓文': 'ko',
    '🇮🇩 印尼文': 'id',
    '🇯🇵 日語': 'ja',
    '🇷🇺 俄羅斯': 'ru'
}

MASTER_USER_FILE = "master_user_ids.json"
DEFAULT_MASTER_USER_IDS = {
    'U5ce6c382d12eaea28d98f2d48673b4b8', 'U2bcd63000805da076721eb62872bc39f',
    'Uea1646aa1a57861c85270d846aaee0eb', 'U8f3cc921a9dd18d3e257008a34dd07c1'
}
