import datetime
import kp_table
from kp_topic import KpTopic


def run(body: dict, user_id: str):
    now = datetime.datetime.now()

    topic = KpTopic(**body)
    topic.id = KpTopic.create_new_id()
    topic.created_at = str(now)
    topic.updated_at = str(now)
    topic.created_by = user_id
    topic.updated_by = user_id

    kp_table.post_topic(topic)

    result = {
        'status': 'success',
        'result': topic.id
    }

    return result
