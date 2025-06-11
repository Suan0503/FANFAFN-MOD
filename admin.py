def is_group_admin(user_id, group_id, data):
    return data.get('group_admin', {}).get(group_id) == user_id
