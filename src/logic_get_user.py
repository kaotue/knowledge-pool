from kp_user import KpUser


def run(id: str):
    if user := KpUser.db_get_item(id):
        return user.to_dict()
    else:
        return None
