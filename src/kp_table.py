import os
import boto3
from boto3.dynamodb.conditions import Key, Attr
from kp_topic import KpTopic
from kp_user import KpUser

table = boto3.resource('dynamodb').Table(os.environ.get('TABLE_NAME', 'kp-table'))


def post_topic(topic: KpTopic) -> None:
    with table.batch_writer() as batch:
        for item in topic.to_items():
            batch.put_item(Item=item)


def get_topic(id: str) -> KpTopic:
    response = table.query(
        KeyConditionExpression=Key('id').eq(KpTopic.prefix + id)
    )
    if 'Items' not in response.keys():
        return None
    return KpTopic.create_by_items(response['Items'])


def get_topics(ids: list[str]) -> list[KpTopic]:
    pass


def post_user(user: KpUser) -> None:
    with table.batch_writer() as batch:
        for item in user.to_items():
            batch.put_item(Item=item)


def get_user(id: str) -> KpUser:
    response = table.query(
        KeyConditionExpression=Key('id').eq(KpUser.prefix + id)
    )
    if 'Items' not in response.keys():
        return None
    return KpUser.create_by_items(response['Items'])
