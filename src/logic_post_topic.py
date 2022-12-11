import datetime
from kp_topic import KpTopic


def run(body: dict, login_user_id: str):
    now = datetime.datetime.now()

    topic = KpTopic(**body)
    topic.id = KpTopic.create_new_id()
    topic.created_at = str(now)
    topic.updated_at = str(now)
    topic.created_by = login_user_id
    topic.updated_by = login_user_id

    KpTopic.db_post(topic)

    result = {
        'status': 'success',
        'result': topic.id
    }

    return result
