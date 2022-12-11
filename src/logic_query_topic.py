from kp_topic import KpTopic


def run(query: dict[str, str]):
    if not query:
        return None
    attr, data = list(query.items())[0]
    if topic := KpTopic.db_query(attr, data):
        return topic.to_dict()
    else:
        return None
