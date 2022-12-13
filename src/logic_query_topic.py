from kp_topic import KpTopic


def run(query: dict[str, str]):
    if not query:
        return None
    attr, data = list(query.items())[0]
    if topics := KpTopic.db_query(attr, data):
        return [x.to_dict() for x in topics]
    else:
        return None
