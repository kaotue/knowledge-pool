import kp_table


def run(id: str):
    if user := kp_table.get_user(id):
        return user.to_dict()
    else:
        return None
