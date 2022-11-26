import kp_table


def run(id: str):
    if topic := kp_table.get_topic(id):
        return topic.to_dict()
    else:
        return None
