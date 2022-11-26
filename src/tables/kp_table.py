import datetime
import boto3
import os
from boto3.dynamodb.conditions import Key, Attr
from models import KpTopic

TTL_MINUTES_HEART_BEAT: int = int(os.environ.get('TTL_MINUTES_HEART_BEAT', '10'))
table = boto3.resource('dynamodb').Table(os.environ.get('TABLE_NAME', 'kp-table'))


def post_topic(topic: KpTopic) -> None:
    with table.batch_writer() as batch:
        for item in topic.to_items():
            batch.put_item(Item=item)


def get_topic(id: str) -> KpTopic:
    response = table.get_item(Key={'id': id})
    if 'Item' not in response.keys():
        return None
    topic = KpTopic.create_by_table_items()
    return response['Item']
