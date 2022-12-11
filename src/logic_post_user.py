import datetime
from kp_user import KpUser


def run(body: dict, user_id: str, login_user_id: str):
    now = datetime.datetime.now()

    user = KpUser(**body)
    user.id = KpUser.create_new_id()
    user.created_at = str(now)
    user.updated_at = str(now)
    user.created_by = login_user_id
    user.updated_by = login_user_id

    KpUser.db_post(user)

    result = {
        'status': 'success',
        'result': user.id
    }

    return result
