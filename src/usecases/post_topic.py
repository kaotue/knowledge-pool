import uuid
import datetime
from tables import kp_table
from models import KpTopic


def run(body: dict, user_id: str):
    now = datetime.datetime.now()
    topic = KpTopic(**body)
    topic.created_at = now
    topic.updated_at = now
    topic.created_by = user_id
    topic.updated_at = user_id
    kp_table.post_topic(topic)

    return 'success'

    # topic.q = 'question'
    # topic.a = 'answer'
    # topic.tags = ['test']
    # topic.is_public = True
    # topic.created_at = now
    # topic.updated_at = now
    # topic.created_by = 'admin'
    # topic.updated_by = 'admin'
    #
    # kp_table.put_item(topic)
    # return 'success'
