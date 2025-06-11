def create_command_menu():
    return {
        "type": "flex",
        "altText": "⚡ 系統管理選單",
        "contents": {
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [{
                    "type": "text",
                    "text": "⚡ 系統管理面板",
                    "weight": "bold",
                    "size": "xl",
                    "color": "#1DB446"
                }, {
                    "type": "text",
                    "text": "請選擇要執行的操作",
                    "size": "sm",
                    "color": "#666666"
                }]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "md",
                "contents": [{
                    "type": "button",
                    "style": "primary",
                    "color": "#1DB446",
                    "action": {
                        "type": "message",
                        "label": "📊 系統狀態",
                        "text": "/狀態"
                    },
                    "height": "sm"
                }, {
                    "type": "button",
                    "style": "primary",
                    "color": "#4A90E2",
                    "action": {
                        "type": "message",
                        "label": "💾 記憶體使用",
                        "text": "/記憶體"
                    },
                    "height": "sm"
                }, {
                    "type": "button",
                    "style": "primary",
                    "color": "#FF6B6B",
                    "action": {
                        "type": "message",
                        "label": "🔄 重啟系統",
                        "text": "/重啟"
                    },
                    "height": "sm"
                }, {
                    "type": "button",
                    "style": "primary",
                    "color": "#6B7280",
                    "action": {
                        "type": "message",
                        "label": "📝 今日流量",
                        "text": "/流量"
                    },
                    "height": "sm"
                }, {
                    "type": "button",
                    "style": "primary",
                    "color": "#805AD5",
                    "action": {
                        "type": "message",
                        "label": "👥 管理員列表",
                        "text": "/管理員列表"
                    },
                    "height": "sm"
                }]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [{
                    "type": "text",
                    "text": "🔒 系統管理專用",
                    "size": "sm",
                    "color": "#666666",
                    "align": "center"
                }]
            }
        }
    }
