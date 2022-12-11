import datetime
from kp_topic import KpTopic


def run(body: dict, topic_id: str, login_user_id: str):
    now = datetime.datetime.now()

    old_topic = KpTopic.db_get_item(topic_id)
    if not old_topic:
        return {
            'status': 'error',
            'result': 'topic is not found'
        }

    new_topic = KpTopic(**body)
    new_topic.id = old_topic.id
    new_topic.created_at = old_topic.created_at
    new_topic.created_by = old_topic.created_by
    new_topic.updated_at = str(now)
    new_topic.updated_by = login_user_id

    KpTopic.db_post(new_topic)

    result = {
        'status': 'success',
        'result': new_topic.id
    }

    return result
