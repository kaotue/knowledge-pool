import datetime
import kp_table
from kp_user import KpUser


def run(body: dict, user_id: str, login_user_id: str):
    now = datetime.datetime.now()

    old_user = kp_table.get_user(user_id)
    if not old_user:
        return {
            'status': 'error',
            'result': 'user is not found'
        }

    new_user = KpUser(**body)
    new_user.id = old_user.id
    new_user.created_at = old_user.created_at
    new_user.created_by = old_user.created_by
    new_user.updated_at = str(now)
    new_user.updated_by = login_user_id

    kp_table.post_user(new_user)

    result = {
        'status': 'success',
        'result': new_user.id
    }

    return result
