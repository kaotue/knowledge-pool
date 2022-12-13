import os
import uuid
import dataclasses
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get('TABLE_NAME', 'kp-table'))


@dataclasses.dataclass
class NosqlClass:

    def __new__(cls, *args, **kwargs):
        dataclasses.dataclass(cls)
        return super().__new__(cls)

    @classmethod
    def create_new_id(cls) -> str:
        return uuid.uuid4().hex

    @classmethod
    def create_by_items(cls, items: list[dict]):
        d = {x['attr'].removeprefix(cls.prefix): x['data'] for x in items}
        return cls(**d)

    def to_items(self) -> list[dict]:
        ary = []
        for k, v in self.__dict__.items():
            ary.append({
                'id': self.prefix + self.id,
                'attr': self.prefix + k,
                'data': v
            })
        return ary

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)

    @classmethod
    def db_post(cls, data) -> None:
        with table.batch_writer() as batch:
            for item in data.to_items():
                batch.put_item(Item=item)

    @classmethod
    def db_get_item(cls, id: str):
        response = table.query(
            KeyConditionExpression=Key('id').eq(cls.prefix + id)
        )
        if 'Items' not in response.keys():
            return None
        return cls.create_by_items(response['Items'])

    @classmethod
    def db_get_items(cls, ids: list[str]) -> list:
        responses = []
        for id in ids:
            if response := cls.db_get_item(id):
                responses.append(response)
        return responses

    @classmethod
    def db_query(cls, attr: str, data: str) -> list:
        response = table.query(
            IndexName='attr-data-index',
            KeyConditionExpression=Key('attr').eq(cls.prefix + attr) & Key('data').eq(str(data))
        )
        if 'Items' not in response.keys():
            return []
        ids = [x['id'].removeprefix(cls.prefix) for x in response['Items']]
        return cls.db_get_items(ids)
