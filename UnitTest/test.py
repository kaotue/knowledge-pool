import unittest
import sys
import datetime

sys.path.append('../../src')
from src import app
from src.models import KpTopic
from src.models import KpUser


def get_base_request():
    return {
        "body": '{ "test": "body"}',
        "resource": "/{proxy+}",
        "requestContext": {
        },
        "queryStringParameters": {"foo": "bar"},
        "headers": {
        },
        "pathParameters": {"proxy": "accounts/self"},
        "httpMethod": "GET",
        "path": "/v1/api/topics/new",
    }


class MyTestCase(unittest.TestCase):
    now: datetime.datetime = datetime.datetime.now()

    def test_post_new(self):
        request = get_base_request()
        topic = KpTopic()
        topic.id = '123'
        topic.type = '1'
        topic.q = 'value_q'
        topic.a = 'value_a'
        topic.is_public = True
        topic.created_at = self.now
        topic.updated_at = self.now
        topic.created_at = 'kaotue'
        topic.updated_at = 'kaotue'

        response = app.lambda_handler(request, "")
        self.assertEqual(response["statusCode"], 200)


if __name__ == '__main__':
    unittest.main()

    # id: str = ''
    # type: str = ''
    # q: str = ''
    # a: str = ''
    # is_public: str = ''
    # tags: list[str] = dataclasses.field(default_factory=list)
    # created_at: datetime.datetime = None
    # updated_at: datetime.datetime = None
    # created_by: str = ''
    # updated_by: str = ''