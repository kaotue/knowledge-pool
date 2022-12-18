from kp_topic import KpTopic
from boto3.dynamodb.conditions import Key, Attr


def run(query: dict[str, str]):
    if not query:
        return None
    keys = []
    for attr, data in query.items():
        if attr == 'tag':
            keys.append(Key('attr').eq(KpTopic.prefix + 'tag_1') & Key('data').eq(str(data)))
            keys.append(Key('attr').eq(KpTopic.prefix + 'tag_2') & Key('data').eq(str(data)))
            keys.append(Key('attr').eq(KpTopic.prefix + 'tag_3') & Key('data').eq(str(data)))
        else:
            keys.append(Key.eq(KpTopic.prefix + attr) & Key.eq(str(data)))
    if topics := KpTopic.db_query_by_keys(keys):
        return [x.to_dict() for x in topics]
    else:
        return None
