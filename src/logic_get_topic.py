from kp_topic import KpTopic


def run(id: str):
    if topic := KpTopic.db_get_item(id):
        return topic.to_dict()
    else:
        return None
